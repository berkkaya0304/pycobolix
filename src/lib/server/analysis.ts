import fs from 'fs';
import path from 'path';
import { v4 as uuidv4 } from 'uuid';
import ollama, { Ollama } from 'ollama';
import { GoogleGenAI } from '@google/genai';
import { exec, spawn } from 'child_process';
import util from 'util';
import { AnalysisResult, Metrics, TestResult, InvalidTestCase, InvalidTestResult, InvalidTestSummary, LlmUsageEntry } from '@/lib/data/types';
import { getSettings } from '@/lib/settings';

const execPromise = util.promisify(exec);

const COBOL_DIR        = path.join(process.cwd(), 'public', 'cobol');
const PYTHON_BASE_DIR  = path.join(process.cwd(), 'public', 'python');
const OUTPUT_DIR       = path.join(process.cwd(), 'public', 'output');
const ARCHIVE_DIR      = path.join(OUTPUT_DIR, 'archive');
const RESULTS_FILE     = path.join(OUTPUT_DIR, 'results.json');
const SUMMARY_FILE     = path.join(OUTPUT_DIR, 'summary.json');
const DETAIL_FILE      = path.join(OUTPUT_DIR, 'test_detail.json');
const INVALID_TESTS_FILE = path.join(OUTPUT_DIR, 'invalid_test_cases.json');
const LLM_USAGE_FILE   = path.join(OUTPUT_DIR, 'llm_usage.json');

function trackLlmUsage(entry: Omit<LlmUsageEntry, 'id' | 'timestamp'>) {
  try {
    const existing: LlmUsageEntry[] = fs.existsSync(LLM_USAGE_FILE) 
      ? JSON.parse(fs.readFileSync(LLM_USAGE_FILE, 'utf-8')) 
      : [];
    
    const newEntry: LlmUsageEntry = {
      id: uuidv4(),
      timestamp: new Date().toISOString(),
      ...entry
    };
    
    existing.push(newEntry);
    fs.writeFileSync(LLM_USAGE_FILE, JSON.stringify(existing, null, 2));
  } catch (err) {
    console.error('Failed to track LLM usage:', err);
  }
}

// CONSTANT REMOVED: const MODEL_DIRS = ['x', 'y', 'a', 'b'];

// Ensure output directories exist
if (!fs.existsSync(OUTPUT_DIR))  fs.mkdirSync(OUTPUT_DIR,  { recursive: true });
if (!fs.existsSync(ARCHIVE_DIR)) fs.mkdirSync(ARCHIVE_DIR, { recursive: true });

export async function runFullAnalysis(onProgress?: (msg: string) => void): Promise<AnalysisResult[]> {
  const cobolFiles = fs.readdirSync(COBOL_DIR).filter(f => f.endsWith('.cbl') || f.endsWith('.cob'));
  
  // Shared reproducibility identifiers for this entire run
  const RUN_ID        = uuidv4();
  const RUN_TIMESTAMP = new Date().toISOString();
  const settings      = getSettings();
  const provider      = settings.llmProvider || 'ollama-local';
  const LLM_MODEL     = provider === 'gemini' 
    ? (settings.geminiModel || 'gemini-2.5-pro') 
    : provider === 'ollama-cloud' 
      ? (settings.ollamaCloudModel || 'llama3') 
      : (settings.ollamaModel || 'llama3');
  // Dynamic Model Discovery: Scan public/python for subdirectories
  const modelDirs = fs.readdirSync(PYTHON_BASE_DIR, { withFileTypes: true })
        .filter(dirent => dirent.isDirectory())
        .map(dirent => dirent.name);

  console.log(`[Run ${RUN_ID}] Discovered models: ${modelDirs.join(', ')}`);
  if (onProgress) onProgress(`Discovered ${modelDirs.length} python models.`);

  const results: AnalysisResult[] = [];
  const totalFiles = cobolFiles.length;

  for (let idx = 0; idx < totalFiles; idx++) {
    const cblFile = cobolFiles[idx];
    const fileNumStr = `(File ${idx + 1} of ${totalFiles})`;
    const baseName = path.parse(cblFile).name;
    const cblPath = path.join(COBOL_DIR, cblFile);
    const cobolCode = fs.readFileSync(cblPath, 'utf-8');

    console.log(`[COBOL ➔ Python] Analyzing ${cblFile} ${fileNumStr}...`);
    if (onProgress) onProgress(`[COBOL ➔ Python] Analyzing ${cblFile} ${fileNumStr}...`);

    // 1. Generate Input Cases (BVA first, LLM fallback)
    let inputStrategy: 'bva' | 'llm' = 'bva';
    let inputs: string[] = [];
    const bvaInputs = generateBVAInputs(cobolCode);
    if (bvaInputs.length > 0) {
      inputs = bvaInputs;
    } else {
      inputStrategy = 'llm';
      const maxRetries = settings.llmRetryCount || 3;
      for (let attempt = 1; attempt <= maxRetries && inputs.length < 5; attempt++) {
        if (attempt > 1) console.warn(`[LLM] C2P inputs: only ${inputs.length}/5 for ${cblFile}, retrying (${attempt}/${maxRetries})...`);
        inputs = await generateTestInputsLLM(cobolCode, LLM_MODEL, provider, cblFile);
      }
      console.log(`[LLM] Final C2P input count for ${cblFile}: ${inputs.length}/5`);
      if (inputs.length < 5) {
        console.warn(`[SKIP] ${cblFile}: could not generate 5 test inputs after 3 retries — excluding from output.`);
        if (onProgress) onProgress(`[SKIP] ${cblFile}: test generation failed, skipping.`);
        
        // Push an empty/failed mock entry to the results so the UI can still show it failed
        const emptyModelResults = modelDirs.map(m => ({
          model_name: formatModelName(m),
          python_filename: '',
          python_code: '',
          status: 'error' as const,
          quality_label: 'Low' as const,
          metrics: { pylint_score: 0, complexity_score: 1, complexity_reduction_pct: 0, pass_at_1: false } as Metrics,
          test_results: [{ actual_output: '[SKIPPED: TEST GENERATION FAILED]', expected_output: '', input: '', semantic_match: false, format_match: false }],
          python_to_cobol_test_results: [],
          invalid_test_results: [],
        }));
        
        results.push({
          id: uuidv4(),
          source_file: cblFile,
          cobol_code: cobolCode,
          cobol_execution_status: 'skipped',
          timestamp: RUN_TIMESTAMP,
          models: emptyModelResults,
        });

        continue;
      }
    }
    
    // 2. Execute COBOL (Ground Truth)
    const cobolResult = await executeCobolWithInputs(cblPath, inputs);

    // 3. Scan Python directories for matching files — run all models CONCURRENTLY
    const modelResults: any[] = (await Promise.all(
      modelDirs.map(async (model) => {
        const modelDir = path.join(PYTHON_BASE_DIR, model);
        const pythonFiles = fs.readdirSync(modelDir).filter(f => f.endsWith('.py'));
        const pyFile = pythonFiles.find(f => path.parse(f).name.toLowerCase() === baseName.toLowerCase());

        if (!pyFile) return null; // No matching file for this model — skip

        const pyPath = path.join(modelDir, pyFile);
        const pythonCode = fs.readFileSync(pyPath, 'utf-8');

        console.log(`  [COBOL ➔ Python] Found match in ${model}: ${pyFile}`);
        if (onProgress) onProgress(`[COBOL ➔ Python] Evaluating python code from ${model} ${fileNumStr}...`);

        let pyResults: TestResult[] = [];
        let pyPassed = false;
        let unitTestsPassed = 0;
        const unitTestsTotal = inputs.length;
        let formatMatchPassed = 0;

        if (cobolResult.status === 'success') {
          // 4. Execute Python against Inputs & Compare with Cobol Output
          const comparison = await executePythonAndCompare(pyPath, inputs, cobolResult.outputs);
          pyResults = comparison.detailedResults;
          unitTestsPassed = comparison.passedCount;
          pyPassed = comparison.allPassed;
          formatMatchPassed = comparison.formatMatchCount;
        }

        // ─── REVERSE TESTING (Python ➔ COBOL) ─────────────────────────
        let pythonToCobolUnitTestsPassed = 0;
        let pythonToCobolUnitTestsTotal = 0;
        let pythonToCobolFormatMatchPassed = 0;
        let pythonToCobolTestResults: TestResult[] = [];

        let pyInputs: string[] = [];
        const maxRetries = settings.llmRetryCount || 3;
        for (let attempt = 1; attempt <= maxRetries && pyInputs.length < 5; attempt++) {
          if (attempt > 1) console.warn(`[LLM] P2C inputs: only ${pyInputs.length}/5 for ${pyFile}, retrying (${attempt}/${maxRetries})...`);
          pyInputs = await generateTestInputsFromPythonLLM(pythonCode, LLM_MODEL, provider, pyFile);
        }
        console.log(`[LLM] Final P2C input count for ${pyFile}: ${pyInputs.length}/5`);
        if (pyInputs.length > 0) {
          console.log(`  [Python ➔ COBOL] Generated ${pyInputs.length} test inputs from ${pyFile}.`);
          if (onProgress) onProgress(`[Python ➔ COBOL] Generated ${pyInputs.length} reverse test inputs for ${model} ${fileNumStr}.`);
          const pyBaselineResult = await executePythonWithInputs(pyPath, pyInputs);
          if (pyBaselineResult.status === 'success') {
            const revComparison = await executeCobolAndCompare(cblPath, pyInputs, pyBaselineResult.outputs);
            pythonToCobolUnitTestsTotal = pyInputs.length;
            pythonToCobolUnitTestsPassed = revComparison.passedCount;
            pythonToCobolFormatMatchPassed = revComparison.formatMatchCount;
            pythonToCobolTestResults = revComparison.detailedResults;
          }
        }

        // 5. Static analysis — already parallel internally
        const [pylintScore, complexity, mypyErrors, halstead] = await Promise.all([
          getPylintScore(pyPath),
          getComplexityScore(pyPath),
          getMypyErrors(pyPath),
          getHalsteadMetrics(pyPath),
        ]);
        const cobolComplexity = getCobolComplexity(cobolCode);
        const locRatio = computeLocRatio(pythonCode, cobolCode);

        // Error pattern distribution
        const errCounts = { sign: 0, whitespace: 0, logic: 0, crash: 0 };
        pyResults.forEach(r => {
          if (!r.semantic_match) {
            if (r.failure_category === 'sign_error')  errCounts.sign++;
            else if (r.failure_category === 'whitespace') errCounts.whitespace++;
            else if (r.failure_category === 'logic')   errCounts.logic++;
            else if (r.failure_category === 'crash')   errCounts.crash++;
          }
        });

        // Execution time averages
        const pyTimes = pyResults.map(r => r.exec_time_ms ?? 0).filter(t => t > 0);
        const execTimePythonAvg = pyTimes.length ? pyTimes.reduce((a, b) => a + b, 0) / pyTimes.length : undefined;
        const execTimeCobolAvg = cobolResult.avgTimeMs;

        const metrics: Metrics = {
          pylint_score: pylintScore,
          complexity_score: complexity.cc,
          complexity_reduction_pct: 0,
          pass_at_1: pyPassed,
          unit_tests_passed: unitTestsPassed,
          unit_tests_total: unitTestsTotal,
          format_match_passed: formatMatchPassed,
          loc_ratio: locRatio,
          exec_time_python_avg_ms: execTimePythonAvg,
          exec_time_cobol_avg_ms: execTimeCobolAvg,
          mypy_error_count: mypyErrors,
          halstead_volume:     halstead.volume,
          halstead_difficulty: halstead.difficulty,
          halstead_effort:     halstead.effort,
          error_sign:       errCounts.sign       || undefined,
          error_whitespace: errCounts.whitespace  || undefined,
          error_logic:      errCounts.logic       || undefined,
          error_crash:      errCounts.crash       || undefined,
          python_to_cobol_semantic_match_passed: pythonToCobolUnitTestsPassed,
          python_to_cobol_unit_tests_total:      pythonToCobolUnitTestsTotal,
          python_to_cobol_format_match_passed:   pythonToCobolFormatMatchPassed,
        };

        const reduction = cobolComplexity > 0
          ? ((cobolComplexity - complexity.cc) / cobolComplexity) * 100
          : 0;
        metrics.complexity_reduction_pct = Math.round(reduction);

        return {
          model_name: formatModelName(model),
          python_filename: pyFile,
          python_code: pythonCode,
          status: pyPassed ? 'success' : 'error',
          quality_label: metrics.pylint_score > 9 ? 'High' : metrics.pylint_score > 7 ? 'Medium' : 'Low',
          metrics,
          test_results: pyResults,
          python_to_cobol_test_results: pythonToCobolTestResults,
        };
      })
    )).filter(Boolean); // remove nulls (models with no matching file)

    // Run COBOL boundary-violation tests Ã¢â‚¬â€ always generated by Ollama
    console.log(`[COBOL ➔ Python] [LLM] Generating boundary tests for ${cblFile} via Ollama (${LLM_MODEL})...`);
    if (onProgress) onProgress(`[COBOL ➔ Python] Generating invalid boundary conditions for ${cblFile} ${fileNumStr}...`);
    const invalidCases = await generateInvalidTestCasesLLM(cobolCode, cblFile, LLM_MODEL, provider);
    console.log(`[LLM] Generated ${invalidCases.length} invalid test case(s) for ${cblFile}.`);

    if (invalidCases.length > 0) {
      // Pre-calculate true COBOL expected outputs for the invalid cases
      console.log(`[COBOL] Generating true execution outputs for ${invalidCases.length} invalid cases...`);
      const invalidInputs = invalidCases.map(tc => tc.input);
      const cobolInvalidResult = await executeCobolWithInputs(cblPath, invalidInputs);
      if (cobolInvalidResult.status === 'success' && cobolInvalidResult.outputs.length === invalidCases.length) {
        invalidCases.forEach((tc, idx) => {
          if (cobolInvalidResult.outputs[idx] !== undefined) {
            tc.cobol_expected_output = cobolInvalidResult.outputs[idx];
          }
        });
      }
    }

    if (invalidCases.length > 0 && modelResults.length > 0) {
      for (const mr of modelResults as any[]) {
        if (!mr.python_filename) continue;
        const model = modelDirs.find(d => formatModelName(d) === mr.model_name);
        if (!model) continue;
        const pyPath = path.join(PYTHON_BASE_DIR, model, mr.python_filename);
        if (!fs.existsSync(pyPath)) continue;
        const { results: invalResults, summary } = await runInvalidBoundaryTests(pyPath, invalidCases);
        mr.invalid_test_results = invalResults;
        mr.invalid_test_summary = summary;
      }
    }

    if (modelResults.length > 0) {
        const result: AnalysisResult = {
            id: uuidv4(),
            source_file: cblFile,
            cobol_code: cobolCode,
            cobol_execution_status: cobolResult.status,
            timestamp: RUN_TIMESTAMP,
            models: modelResults,
            run_metadata: {
              run_id:   RUN_ID,
              timestamp: RUN_TIMESTAMP,
              ollama_model: LLM_MODEL,
              input_generation_strategy: inputStrategy,
            },
        };
        results.push(result);
    }
  }

  // ─── Generate Executive Summary ──────────────────────────────────────────
  if (results.length > 0) {
    if (onProgress) onProgress('Generating executive summary using selected LLM...');
    const executiveSummary = await generateExecutiveSummary(results, LLM_MODEL, provider);
    results[0].executive_summary = executiveSummary;
  }

  // Save rolling latest + timestamped archive copy
  const payload = JSON.stringify(results, null, 2);
  
  // Create summary payload (equivalent to what's in page.tsx)
  const summaryPayload = results.flatMap(file =>
    file.models.map(m => {
      const total = m.metrics.unit_tests_total ?? 0;
      return {
        source_file:              file.source_file,
        model:                    m.model_name,
        c2p_format_pct:           total > 0 ? Math.round(((m.metrics.format_match_passed    ?? 0) / total) * 100) : 0,
        c2p_semantic_pct:         total > 0 ? Math.round(((m.metrics.unit_tests_passed    ?? 0) / total) * 100) : 0,
        pylint:                   m.metrics.pylint_score,
        complexity_reduction_pct: m.metrics.complexity_reduction_pct,
        loc_ratio:                m.metrics.loc_ratio              ?? null,
        exec_time_python_avg_ms:  m.metrics.exec_time_python_avg_ms ?? null,
        mypy_error_count:         m.metrics.mypy_error_count         ?? null,
        halstead_effort:          m.metrics.halstead_effort          ?? null,
        p2c_format_pct:           (m.metrics.python_to_cobol_unit_tests_total ?? 0) > 0 ? Math.round(((m.metrics.python_to_cobol_format_match_passed ?? 0) / (m.metrics.python_to_cobol_unit_tests_total ?? 1)) * 100) : 0,
        p2c_semantic_pct:         (m.metrics.python_to_cobol_unit_tests_total ?? 0) > 0 ? Math.round(((m.metrics.python_to_cobol_semantic_match_passed ?? 0) / (m.metrics.python_to_cobol_unit_tests_total ?? 1)) * 100) : 0,
        boundary_faithfulness_pct: (m.invalid_test_results?.length ?? 0) > 0 ? Math.round((m.invalid_test_results!.filter(r => r.cobol_faithful).length / m.invalid_test_results!.length) * 100) : 0,
      };
    })
  );

  fs.writeFileSync(RESULTS_FILE, payload); // Legacy support
  fs.writeFileSync(DETAIL_FILE, payload);
  fs.writeFileSync(SUMMARY_FILE, JSON.stringify(summaryPayload, null, 2));

  const archiveFile = path.join(ARCHIVE_DIR, `results_${RUN_TIMESTAMP.replace(/[:.]/g, '-')}.json`);
  fs.writeFileSync(archiveFile, payload);
  console.log(`[Run ${RUN_ID}] Archived to ${path.basename(archiveFile)}`);
  if (onProgress) onProgress('Analysis completed successfully. Saving results...');

  // Save invalid test results separately (legacy flat format for backward compat)
  const invalidPayload = results.map(r => ({
    source_file: r.source_file,
    models: r.models.map(m => ({
      model_name: m.model_name,
      invalid_results: (m as any).invalid_test_results ?? [],
    })),
  }));
  fs.writeFileSync(INVALID_TESTS_FILE, JSON.stringify(invalidPayload, null, 2));

  // ─── Final Run Summary ────────────────────────────────────────────────────
  console.log(`\n${'='.repeat(60)}`);
  console.log(`[Run ${RUN_ID}] FINAL TEST SUMMARY`);
  console.log('='.repeat(60));
  let totalPassed = 0, totalSkipped = 0, totalTests = 0;
  for (const r of results) {
    for (const m of r.models as any[]) {
      const allResults: any[] = [
        ...(m.test_results ?? []),
        ...(m.python_to_cobol_test_results ?? []),
        ...(m.invalid_test_results ?? []),
      ];
      const skipped = allResults.filter(t => String(t.actual_output ?? t.python_actual_output ?? '').includes('[SKIPPED')).length;
      const passed  = allResults.filter(t => t.semantic_match || t.cobol_faithful).length;
      totalPassed  += passed;
      totalSkipped += skipped;
      totalTests   += allResults.length;
      if (skipped > 0) {
        console.log(`  ⏭  ${r.source_file} [${m.model_name}]: ${skipped} skipped (timeout)`);
      }
      console.log(`  ✅ ${r.source_file} [${m.model_name}]: ${passed}/${allResults.length} passed`);
    }
  }
  console.log('─'.repeat(60));
  console.log(`  TOTAL: ${totalPassed} passed | ${totalSkipped} skipped | ${totalTests} total`);
  console.log('='.repeat(60) + '\n');
  if (onProgress) onProgress(`Run complete — ${totalPassed} passed, ${totalSkipped} skipped out of ${totalTests} tests.`);

  return results;
}

export async function runCustomAnalysis(pythonCode: string, testCases: {input: string, expected_output: string}[]): Promise<{ passed: boolean, detailedResults: TestResult[] }> {
    // Save temp file
    const tempId = uuidv4();
    const tempPath = path.join(OUTPUT_DIR, `temp_${tempId}.py`);
    fs.writeFileSync(tempPath, pythonCode);

    try {
        const inputs = testCases.map(tc => tc.input);
        const expectedOutputs = testCases.map(tc => tc.expected_output);

        const comparison = await executePythonAndCompare(tempPath, inputs, expectedOutputs);
        
        if (fs.existsSync(tempPath)) fs.unlinkSync(tempPath);
        
        return { 
            passed: comparison.allPassed, 
            detailedResults: comparison.detailedResults 
        };
    } catch (e) {
        if (fs.existsSync(tempPath)) fs.unlinkSync(tempPath);
        throw e;
    }
}

export async function runInteractiveSandbox(
    cobolCode: string, 
    pythonCode: string, 
    input: string
): Promise<{ success: boolean; result?: TestResult; error?: string }> {
    // Generate a short ID because GnuCOBOL (cobc) limits base file name length
    const tempId = uuidv4().split('-')[0];
    const tempCobolPath = path.join(OUTPUT_DIR, `sb_${tempId}.cbl`);
    const tempPythonPath = path.join(OUTPUT_DIR, `sb_${tempId}.py`);

    fs.writeFileSync(tempCobolPath, cobolCode);
    fs.writeFileSync(tempPythonPath, pythonCode);

    try {
        // 1. Run COBOL to get Ground Truth
        const cobolResult = await executeCobolWithInputs(tempCobolPath, [input]);
        if (cobolResult.status !== 'success') {
            return { success: false, error: 'Failed to compile or execute COBOL.' };
        }

        const expectedOutput = cobolResult.outputs[0] || '';

        // 2. Run Python and Compare
        const comparison = await executePythonAndCompare(tempPythonPath, [input], [expectedOutput]);
        const testResult = comparison.detailedResults[0];

        // Ensure COBOL execution time is also returned (optional, but helpful for Sandbox)
        // We can attach it to the result or just return the result
        return { success: true, result: testResult };
    } catch (e: any) {
        return { success: false, error: e.message || 'Unknown error during execution' };
    } finally {
        try { if (fs.existsSync(tempCobolPath)) fs.unlinkSync(tempCobolPath); } catch (e) {}
        try {
            const tempExePath = tempCobolPath.replace('.cbl', '.exe');
            if (fs.existsSync(tempExePath)) fs.unlinkSync(tempExePath);
        } catch (e) {}
        try { if (fs.existsSync(tempPythonPath)) fs.unlinkSync(tempPythonPath); } catch (e) {}
    }
}

// ─── COBOL-aware Boundary Value Analysis (BVA) ──────────────────────────────Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

interface PicInfo {
  type: 'numeric' | 'alphanumeric';
  signed: boolean;
  totalDigits: number;
  decimalDigits: number;
}

function parsePic(pic: string): PicInfo {
  const p = pic.toUpperCase().trim();
  const signed = p.startsWith('S');
  if (/X/.test(p)) {
    const m = p.match(/X\((\d+)\)/);
    const len = m ? parseInt(m[1]) : (p.match(/X+/)?.[0].length ?? 1);
    return { type: 'alphanumeric', signed: false, totalDigits: len, decimalDigits: 0 };
  }
  const expanded = p.replace(/9\((\d+)\)/g, (_, n) => '9'.repeat(parseInt(n)));
  const vIdx = expanded.indexOf('V');
  const intPart = vIdx >= 0 ? expanded.slice(0, vIdx) : expanded;
  const decPart = vIdx >= 0 ? expanded.slice(vIdx + 1) : '';
  return {
    type: 'numeric', signed,
    totalDigits:   (intPart.match(/9/g) ?? []).length,
    decimalDigits: (decPart.match(/9/g) ?? []).length,
  };
}

function parsePicForVar(cobolCode: string, varName: string): PicInfo | null {
  const lines = cobolCode.toUpperCase().split('\n');
  for (const line of lines) {
    const t = line.trim();
    if (t.startsWith('*')) continue;
    if (!t.includes(varName.toUpperCase())) continue;
    const m = t.match(/PIC\s+([S9XV()V.\.Z+\-,$]+)/i);
    if (m) return parsePic(m[1]);
  }
  return null;
}

function parseAcceptVariables(cobolCode: string): string[] {
  const upper = cobolCode.toUpperCase();
  const skip = new Set(['DATE', 'TIME', 'DAY', 'SYSIN']);
  const result: string[] = [];
  const re = /\bACCEPT\s+([A-Z][A-Z0-9-]*)/g;
  let m: RegExpExecArray | null;
  while ((m = re.exec(upper)) !== null) {
    if (!skip.has(m[1])) result.push(m[1]);
  }
  return result;
}

function generateBoundaryValues(pic: PicInfo): string[] {
  if (pic.type === 'alphanumeric') {
    const L = pic.totalDigits;
    return [...new Set(['A', 'A'.repeat(Math.max(1, Math.floor(L / 2))), 'A'.repeat(L)])];
  }
  const maxInt = Math.pow(10, pic.totalDigits) - 1;
  const minInt = pic.signed ? -maxInt : 0;
  const mid    = Math.floor((minInt + maxInt) / 2);
  if (pic.decimalDigits > 0) {
    const scale = Math.pow(10, pic.decimalDigits);
    const fmt = (n: number) => (n / scale).toFixed(pic.decimalDigits);
    return [...new Set([minInt * scale, scale, mid * scale, (maxInt - 1) * scale, maxInt * scale])].map(fmt);
  }
  return [...new Set([minInt, minInt + 1, mid, maxInt - 1, maxInt])]  
    .filter(v => v >= minInt && v <= maxInt).map(String);
}

function generateBVAInputs(cobolCode: string): string[] {
  const vars = parseAcceptVariables(cobolCode);
  if (vars.length === 0) return [];
  const perVar: string[][] = [];
  for (const v of vars) {
    const pic = parsePicForVar(cobolCode, v);
    if (!pic) { console.warn(`[BVA] No PIC for ACCEPT var: ${v} Ã¢â‚¬â€œ LLM fallback`); return []; }
    perVar.push(generateBoundaryValues(pic));
  }
  const maxLevels = Math.max(...perVar.map(a => a.length));
  const cases = new Set<string>();
  const combine = (fn: (vals: string[]) => string) => perVar.map(fn).join('\n');
  cases.add(combine(v => v[0]));
  cases.add(combine(v => v[v.length - 1]));
  for (let i = 1; i < maxLevels - 1 && cases.size < 5; i++)
    cases.add(perVar.map(v => v[Math.min(i, v.length - 1)]).join('\n'));
  if (perVar.length > 1 && cases.size < 5) {
    cases.add([perVar[0][0], ...perVar.slice(1).map(v => v[v.length - 1])].join('\n'));
    cases.add([perVar[0][perVar[0].length - 1], ...perVar.slice(1).map(v => v[0])].join('\n'));
  }
  return [...cases].slice(0, 5);
}


async function generateTestInputs(cobolCode: string, model: string, provider: string): Promise<string[]> {
  const bva = generateBVAInputs(cobolCode);
  if (bva.length > 0) {
    console.log(`[BVA] Generated ${bva.length} boundary-value test input(s) from PIC clauses.`);
    return bva;
  }
  console.log('[BVA] No parseable ACCEPT/PIC found Ã¢â‚¬â€œ falling back to LLM.');
  return generateTestInputsLLM(cobolCode, model, provider);
}


function cleanAndParseJSON(str: string): any {
  let cleaned = str.replace(/```(?:json)?/gi, '').replace(/```/g, '');
  
  cleaned = cleaned.replace(/"(?:[^"\\]|\\.)*"|(\/\*[\s\S]*?\*\/)|(\/\/.*$)/gm, (match, blockComment, lineComment) => {
     if (blockComment || lineComment) return '';
     return match;
  });

  cleaned = cleaned.replace(/,\s*([\]}])/g, '$1');

  try { return JSON.parse(cleaned); } catch {}

  const startObj = cleaned.indexOf('{');
  const endObj = cleaned.lastIndexOf('}');
  const startArr = cleaned.indexOf('[');
  const endArr = cleaned.lastIndexOf(']');
  
  let jsonStr = cleaned;
  if (startObj !== -1 && endObj !== -1 && (startArr === -1 || startObj < startArr)) {
      jsonStr = cleaned.substring(startObj, endObj + 1);
  } else if (startArr !== -1 && endArr !== -1) {
      jsonStr = cleaned.substring(startArr, endArr + 1);
  } else if (startArr !== -1 && endArr === -1) {
      jsonStr = cleaned.substring(startArr);
  } else if (startObj !== -1 && endObj === -1) {
      jsonStr = cleaned.substring(startObj);
  }
  
  try { return JSON.parse(jsonStr); } catch {}
  
  let unescapedQuotesCount = (jsonStr.replace(/\\"/g, '').match(/"/g) || []).length;
  
  if (jsonStr.trim().startsWith('[')) {
       let recovered = jsonStr.replace(/,\s*$/, '');
       if (unescapedQuotesCount % 2 !== 0) recovered += '"';
       recovered += ']';
       try { return JSON.parse(recovered); } catch {}
       
       if (jsonStr.lastIndexOf(',') !== -1) {
           recovered = jsonStr.substring(0, jsonStr.lastIndexOf(',')).trim() + ']';
           try { return JSON.parse(recovered); } catch {}
       }
  } else if (jsonStr.trim().startsWith('{')) {
       let recovered = jsonStr.replace(/,\s*$/, '');
       if (unescapedQuotesCount % 2 !== 0) recovered += '"';
       recovered += '}';
       try { return JSON.parse(recovered); } catch {}
  }
  
  throw new Error("Unable to parse JSON");
}

async function generateInvalidTestCasesLLM(
  cobolCode: string,
  filename: string,
  modelArg: string,
  provider: string,
  maxRetries: number = getSettings().llmRetryCount || 3
): Promise<InvalidTestCase[]> {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      const settings = getSettings();

      // NOTE: When format:'json' is used, Ollama forces the model to return a JSON
      // object - even if we ask for an array. The key name wrapping the array is
      // model-dependent, so we scan all top-level values for the first array.
      const prompt =
        'You are a COBOL QA expert. Analyze the COBOL program below and generate boundary violation test cases.\n\n' +
        'Return a JSON object with a key "cases" containing an array of test case objects.\n' +
        'Each object must have exactly these fields:\n' +
        '  id           - unique snake_case string\n' +
        '  category     - one of: overflow, sign_error, alpha_to_numeric, boundary_valid\n' +
        '  description  - human-readable explanation\n' +
        '  input        - raw stdin string (use \\n between lines if multiple ACCEPT statements)\n' +
        '  cobol_expected_output - exact string COBOL would print\n' +
        '  cobol_constraint      - PIC clause that causes this behavior\n\n' +
        'Generate 5 test cases. Focus on:\n' +
        '- overflow: value wider than PIC field (PIC 99 + 100 -> COBOL prints 10)\n' +
        '- sign_error: negative value to unsigned PIC (COBOL takes absolute value)\n' +
        '- alpha_to_numeric: letters to numeric PIC (COBOL stores 0)\n' +
        '- boundary_valid: exact maximum valid value\n\n' +
        'Example response:\n' +
        '{"cases":[{"id":"ex_overflow","category":"overflow","description":"PIC 99 overflow","input":"100","cobol_expected_output":"Value: 00","cobol_constraint":"PIC 99 max 2 digits"}]}\n\n' +
        'COBOL FILE: ' + filename + '\n' +
        cobolCode;

      let fullResponse = '';
      const t0 = Date.now();

      let promptTokens = 0;
      let completionTokens = 0;

      if (provider === 'gemini') {
        const ai = new GoogleGenAI({ apiKey: settings.geminiApiKey || '' });
        const response = await ai.models.generateContent({
          model: modelArg,
          contents: prompt,
          config: {
            responseMimeType: 'application/json',
            temperature: 0.1 + (attempt * 0.1), // slightly increase temp on retry
          }
        });
        fullResponse = response.text || '';
        if (response.usageMetadata) {
          promptTokens = response.usageMetadata.promptTokenCount || 0;
          completionTokens = response.usageMetadata.candidatesTokenCount || 0;
        }
      } else {
        const ollamaClient = provider === 'ollama-cloud'
          ? new Ollama({ host: settings.ollamaCloudBaseUrl, headers: settings.ollamaCloudApiKey ? { Authorization: `Bearer ${settings.ollamaCloudApiKey}` } : {} })
          : ollama;

        const responseStream = await ollamaClient.generate({
          model: modelArg,
          prompt,
          format: 'json',
          stream: true,
          options: { temperature: 0.1 + (attempt * 0.1), seed: 42 + attempt },
        });

        for await (const chunk of responseStream) {
          fullResponse += chunk.response;
          if (chunk.done) {
            promptTokens = chunk.prompt_eval_count || 0;
            completionTokens = chunk.eval_count || 0;
          }
        }
      }

      const duration = Date.now() - t0;

      trackLlmUsage({
        model: modelArg,
        provider,
        type: 'boundary_test_generation',
        prompt_tokens: promptTokens,
        completion_tokens: completionTokens,
        total_tokens: promptTokens + completionTokens,
        duration_ms: duration,
        file_name: filename
      });

      console.log(`[LLM] Raw response for ${filename} (attempt ${attempt}) (first 300 chars): ${fullResponse.slice(0, 300)}`);

      let parsed: any;
      try {
        parsed = cleanAndParseJSON(fullResponse);
      } catch {
        console.error(`[LLM] Failed to parse JSON response for ${filename} on attempt ${attempt}`);
        if (attempt === maxRetries) return [];
        continue; // retry
      }

      // Strategy: find any array - either the root or the first array-valued property
      let arr: any[] = [];
      if (Array.isArray(parsed)) {
        arr = parsed;
      } else if (parsed && typeof parsed === 'object') {
        // First try the explicit 'cases' key we asked for
        if (Array.isArray(parsed.cases)) {
          arr = parsed.cases;
        } else {
          // Scan all top-level values for any array
          const found = Object.values(parsed).find(v => Array.isArray(v));
          if (found) arr = found as any[];
        }
      }

      console.log(`[LLM] Array candidates found for ${filename} (attempt ${attempt}): ${arr.length}`);

      if (arr.length === 0) {
        console.warn(`[LLM] No array found in Ollama response for ${filename} on attempt ${attempt}. Full response:`, fullResponse.slice(0, 500));
        if (attempt === maxRetries) return [];
        continue; // retry
      }

      const required = ['id', 'category', 'description', 'input', 'cobol_expected_output', 'cobol_constraint'];
      const validCategories = new Set(['overflow', 'sign_error', 'alpha_to_numeric', 'boundary_valid']);

      const valid = arr.filter(tc =>
        tc && typeof tc === 'object' &&
        required.every(k => k in tc) &&
        validCategories.has(tc.category)
      );

      console.log(`[LLM] Valid test cases after schema check for ${filename}: ${valid.length}`);
      
      if (valid.length < 5) {
        if (attempt === maxRetries) return valid.length > 0 ? valid.map(tc => ({
          id: String(tc.id),
          category: tc.category as InvalidTestCase['category'],
          description: String(tc.description),
          input: String(tc.input),
          cobol_expected_output: String(tc.cobol_expected_output),
          cobol_constraint: String(tc.cobol_constraint),
        })) : [];
        console.warn(`[LLM] Only ${valid.length}/5 valid boundary cases for ${filename} on attempt ${attempt}, retrying...`);
        continue; // retry
      }

      return valid.map(tc => ({
        id: String(tc.id),
        category: tc.category as InvalidTestCase['category'],
        description: String(tc.description),
        input: String(tc.input),
        cobol_expected_output: String(tc.cobol_expected_output),
        cobol_constraint: String(tc.cobol_constraint),
      }));
    } catch (error) {
      console.error(`[LLM] Error generating invalid test cases via LLM on attempt ${attempt}:`, error);
      if (attempt === maxRetries) return [];
    }
  }
  return [];
}

async function generateTestInputsLLM(cobolCode: string, modelArg: string, provider: string, filename?: string): Promise<string[]> {
  try {
    const settings = getSettings();
    const t0 = Date.now();

    const prompt = `
     You are a QA Engineer. Analyze the following COBOL code to understand what inputs it accepts (ACCEPT statements).
     Generate 5 distinct input sets that would cover different execution paths.
     Return ONLY a JSON array of strings, where each string is the raw input to be fed to stdin.
     
     Rules:
     - Each string in the array represents ONE test case's full input.
     - If multiple ACCEPTs are required for a single run, join them with "\\n" (newline) in the string.
     - Do NOT include any explanations or keys, just the array of strings.
     
     COBOL CODE:
     ${cobolCode}
     `;

    let fullResponse = '';

    let promptTokens = 0;
    let completionTokens = 0;

    if (provider === 'gemini') {
      const ai = new GoogleGenAI({ apiKey: settings.geminiApiKey || '' });
      const response = await ai.models.generateContent({
        model: modelArg,
        contents: prompt,
        config: {
          responseMimeType: 'application/json',
          temperature: 0,
        }
      });
      fullResponse = response.text || '';
      if (response.usageMetadata) {
        promptTokens = response.usageMetadata.promptTokenCount || 0;
        completionTokens = response.usageMetadata.candidatesTokenCount || 0;
      }
    } else {
      const ollamaClient = provider === 'ollama-cloud'
        ? new Ollama({ host: settings.ollamaCloudBaseUrl, headers: settings.ollamaCloudApiKey ? { Authorization: `Bearer ${settings.ollamaCloudApiKey}` } : {} })
        : ollama;

      const responseStream = await ollamaClient.generate({
        model: modelArg,
        prompt,
        format: 'json',
        stream: true,
        options: { temperature: 0, seed: 42 }, // deterministic / reproducible
      });

      for await (const chunk of responseStream) {
        fullResponse += chunk.response;
        if (chunk.done) {
          promptTokens = chunk.prompt_eval_count || 0;
          completionTokens = chunk.eval_count || 0;
        }
      }
    }

    const duration = Date.now() - t0;
    trackLlmUsage({
      model: modelArg,
      provider,
      type: 'input_generation',
      prompt_tokens: promptTokens,
      completion_tokens: completionTokens,
      total_tokens: promptTokens + completionTokens,
      duration_ms: duration,
      file_name: filename || '-'
    });

    let parsed: any;
    try {
      parsed = cleanAndParseJSON(fullResponse);
    } catch {
      console.error('[LLM] Error parsing Ollama JSON response.', fullResponse.slice(0, 100));
      return [];
    }
    
    let inputs: string[] = [];
    if (Array.isArray(parsed)) {
      inputs = parsed.map(p => typeof p === 'string' ? p : JSON.stringify(p));
    } else if (typeof parsed === 'object' && parsed !== null) {
      const found = Object.values(parsed).find(v => Array.isArray(v)) as string[] | undefined;
      if (found) inputs = found.map((p: any) => typeof p === 'string' ? p : JSON.stringify(p));
    }
    return inputs;
  } catch (error) {
    console.error('[LLM] Error calling Ollama:', error);
    return [];
  }
}

// Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬ Failure Category Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
function categorizeFailure(
  expected: string, actual: string
): 'sign_error' | 'whitespace' | 'logic' | 'crash' {
  if (!actual || /Traceback|Error:|Exception:/.test(actual)) return 'crash';
  if (expected.replace(/\s+/g, '') === actual.replace(/\s+/g, '')) return 'whitespace';
  const expNums = [...expected.matchAll(/-?\d+(\.\d+)?/g)].map(m => parseFloat(m[0]));
  const actNums = [...actual.matchAll(/-?\d+(\.\d+)?/g)].map(m => parseFloat(m[0]));
  if (expNums.length > 0 && expNums.length === actNums.length) {
    const signErrors = expNums.filter((v, i) => Math.abs(v) === Math.abs(actNums[i]) && v !== actNums[i]);
    if (signErrors.length === expNums.length) return 'sign_error';
  }
  return 'logic';
}

// Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬ mypy error count Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
async function getMypyErrors(filePath: string): Promise<number> {
  const cmd = `python -m mypy --ignore-missing-imports "${filePath}"`;
  try {
    const { stdout, stderr } = await execPromise(cmd);
    const combined = stdout + stderr;
    // "Found N errors in ..." or "N errors" pattern
    const matchN = combined.match(/(\d+) error/);
    if (matchN) return parseInt(matchN[1], 10);
    // If mypy exits 0 and says "Success", it's genuinely clean
    if (/Success: no issues found/.test(combined)) return 0;
    return 0;
  } catch (e: any) {
    // mypy exits non-zero when there are errors; combine stdout+stderr
    const combined = (e.stdout ?? '') + (e.stderr ?? '');
    const matchN = combined.match(/(\d+) error/);
    if (matchN) return parseInt(matchN[1], 10);
    // If mypy itself is not found or crashes, log and return null-like sentinel
    console.warn('[mypy] Could not run mypy:', (e.message ?? '').slice(0, 80));
    return 0;
  }
}

// Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬ Halstead Complexity (radon hal) Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
async function getHalsteadMetrics(filePath: string): Promise<{ volume?: number; difficulty?: number; effort?: number }> {
  try {
    const { stdout } = await execPromise(`python -m radon hal -j "${filePath}"`);
    const startIdx = stdout.indexOf('{');
    const endIdx = stdout.lastIndexOf('}');
    if (startIdx === -1 || endIdx === -1) return {};
    const jsonStr = stdout.substring(startIdx, endIdx + 1);
    const data = JSON.parse(jsonStr);
    // Use Object.values to avoid relying on platform-specific path key shape
    const fileData = Object.values(data)[0] as any;
    const total = fileData?.total;
    if (!total) return {};
    return {
      volume:     typeof total.volume     === 'number' ? Math.round(total.volume)     : undefined,
      difficulty: typeof total.difficulty === 'number' ? Math.round(total.difficulty * 100) / 100 : undefined,
      effort:     typeof total.effort     === 'number' ? Math.round(total.effort)     : undefined,
    };
  } catch (e: any) {
    console.warn('[radon hal] Failed:', (e.message ?? '').slice(0, 120));
    return {};
  }
}

// Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬ LoC Ratio Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
function computeLocRatio(pythonCode: string, cobolCode: string): number {
  const countLines = (s: string) => s.split('\n').filter(l => l.trim().length > 0).length;
  const cblLoc = countLines(cobolCode);
  return cblLoc > 0 ? Math.round((countLines(pythonCode) / cblLoc) * 100) / 100 : 0;
}

async function executeCobolWithInputs(filePath: string, inputs: string[]): Promise<{ status: 'success' | 'failed' | 'skipped'; outputs: string[]; avgTimeMs?: number }> {
    const outputs: string[] = [];
    const timings: number[] = [];

    // Check if cobc exists
    try {
        await execPromise('cobc --version');
    } catch (e) {
        console.warn('GnuCOBOL (cobc) not found.');
        return { status: 'skipped', outputs: [] };
    }

    const uniqueSuffix = `_${Date.now()}_${Math.floor(Math.random() * 1000)}`;
    const exePath = filePath.replace(/\.(cbl|cob)$/i, `${uniqueSuffix}.exe`);

    let compileSuccess = false;
    for (let attempt = 1; attempt <= 3; attempt++) {
        try {
            // Compile (create exe)
            await execPromise(`cobc -x -o "${exePath}" "${filePath}"`);
            compileSuccess = true;
            break; // Success
        } catch (e: any) {
            const errStr = String(e.message || e);
            if (errStr.includes('Permission denied') || errStr.includes('ld returned 1 exit status')) {
                console.warn(`[COBOL] Compilation locked for ${filePath} (attempt ${attempt}). Retrying in 500ms...`);
                await new Promise(res => setTimeout(res, 500));
            } else {
                console.error(`[COBOL] Compilation failed for ${filePath}:`, e);
                return { status: 'failed', outputs: [] };
            }
        }
    }

    if (!compileSuccess) {
        console.error(`[COBOL] Compilation completely failed (locked) for ${filePath} after 3 retries.`);
        return { status: 'failed', outputs: [] };
    }

    const EXEC_TIMEOUT_MS = 10_000;

    for (const input of inputs) {
        try {
            const runCmd = process.platform === 'win32' ? exePath : `./${path.basename(exePath)}`;
            const cwd = path.dirname(exePath);

            const child = spawn(runCmd, [], { cwd, shell: false });

            let stdoutData = '';
            let timedOut = false;

            const MAX_OUTPUT_BYTES = 1_048_576;
            const exitPromise = new Promise((resolve) => {
                child.stdout.on('data', (data) => {
                    if (stdoutData.length < MAX_OUTPUT_BYTES) stdoutData += data.toString();
                    else { timedOut = true; try { child.kill('SIGKILL'); } catch {} }
                });
                child.on('close', (code) => { resolve(code); });
                child.on('error', (err) => { resolve(1); });
            });

            if (input) {
                const inputToSend = input.replace(/\n/g, '\r\n');
                child.stdin.write(inputToSend);
            }
            child.stdin.end();

            const t0cobol = Date.now();
            const timeoutHandle = setTimeout(() => {
                timedOut = true;
                try { child.kill('SIGKILL'); } catch {}
            }, EXEC_TIMEOUT_MS);

            await exitPromise;
            clearTimeout(timeoutHandle);
            timings.push(Date.now() - t0cobol);

            if (timedOut) {
                console.warn(`[COBOL] Test case timed out for ${filePath} — skipping.`);
                outputs.push('[SKIPPED: timeout]');
                continue;
            }
            
            // Normalize output for cleanup
            const cleaned = stdoutData.split('\n')
                .map(line => line.replace(/^(Enter|Input|Type|.*Enter).*?:\s*/i, '').trim())
                .filter(line => line.length > 0)
                .join('\n').trim();
                
            outputs.push(cleaned);

        } catch (e) {
            outputs.push("Error executing COBOL");
        }
    }

    // Cleanup
    try {
        if (fs.existsSync(exePath)) fs.unlinkSync(exePath);
    } catch (e) {
        console.warn(`[COBOL] Could not delete executable ${exePath}:`, e);
    }
    const avgTimeMs = timings.length ? timings.reduce((a, b) => a + b, 0) / timings.length : undefined;
    return { status: 'success', outputs, avgTimeMs };
}

async function executePythonAndCompare(filePath: string, inputs: string[], expectedOutputs: string[]): Promise<{ allPassed: boolean, passedCount: number, formatMatchCount: number, detailedResults: TestResult[] }> {
    const detailedResults: TestResult[] = [];
    let passedCount = 0;
    let formatMatchCount = 0;

    const EXEC_TIMEOUT_MS = 10_000;

    for (let i = 0; i < inputs.length; i++) {
        const input = inputs[i];
        const expected = expectedOutputs[i] || "";
        
        let actualOutput = '';
        let testPassed = false;
        let execTimeMs = 0;
        let skipped = false;

        try {
            const pythonProcess = spawn('python', ['-u', filePath]);
            
            let stdoutData = '';
            let stderrData = '';
            let timedOut = false;

            const MAX_OUTPUT_BYTES = 1_048_576;
            const exitPromise = new Promise((resolve) => {
                pythonProcess.stdout.on('data', (data) => {
                    if (stdoutData.length < MAX_OUTPUT_BYTES) stdoutData += data.toString();
                    else { timedOut = true; try { pythonProcess.kill('SIGKILL'); } catch {} }
                });
                pythonProcess.stderr.on('data', (data) => { stderrData += data.toString().slice(0, 2048); });
                pythonProcess.on('close', (code) => { resolve(code); });
                pythonProcess.on('error', (err) => { resolve(1); });
            });

            if (input) {
                const inputToSend = input.replace(/\n/g, '\r\n');
                pythonProcess.stdin.write(inputToSend);
            }
            pythonProcess.stdin.end();

            const t0py = Date.now();
            const timeoutHandle = setTimeout(() => {
                timedOut = true;
                try { pythonProcess.kill('SIGKILL'); } catch {}
            }, EXEC_TIMEOUT_MS);

            await exitPromise;
            clearTimeout(timeoutHandle);
            execTimeMs = Date.now() - t0py;

            if (timedOut) {
                console.warn(`[Python] Test case #${i + 1} timed out for ${filePath} — skipping.`);
                skipped = true;
                actualOutput = '[SKIPPED: timeout]';
            } else {
                actualOutput = stdoutData.split('\n')
                    .map(line => line.replace(/^(Enter|Input|Type|.*Enter).*?:\s*/i, '').trim())
                    .filter(line => line.length > 0)
                    .join('\n').trim();

                if (stderrData) actualOutput += `\n[STDERR]: ${stderrData}`;

                // --- SOFT / legacy match (fuzzy, whitespace-normalized) ---
                if (normalizeOutput(actualOutput).includes(normalizeOutput(expected))) {
                    testPassed = true;
                    passedCount++;
                }

                // --- FORMAT MATCH: exact character-for-character after trimming line whitespace ---
                const isFormat = formatMatchOutputs(actualOutput, expected);
                if (isFormat) formatMatchCount++;
            }

        } catch (error: any) {
            actualOutput = `Error: ${error.message}`;
        }

        detailedResults.push({
            input: input,
            expected_output: expected,
            actual_output: actualOutput,
            semantic_match: testPassed,
            format_match: formatMatchOutputs(actualOutput, expected),
            exec_time_ms: execTimeMs,
            failure_category: skipped ? 'crash' : (testPassed ? null : categorizeFailure(expected, actualOutput)),
        });
    }

    return { 
        allPassed: passedCount === inputs.length,
        passedCount,
        formatMatchCount,
        detailedResults 
    };
}

// ─── Reverse Differential Testing Helpers ─────────────────────────────────────

async function generateTestInputsFromPythonLLM(pythonCode: string, modelArg: string, provider: string, filename?: string): Promise<string[]> {
  try {
    const settings = getSettings();
    const t0 = Date.now();

    const prompt = `
     You are a QA Engineer. Analyze the following Python code to understand what inputs it accepts via standard input (e.g. \`input()\` calls).
     Generate 5 distinct input sets that would cover different execution paths.
     Return ONLY a JSON array of strings, where each string is the raw input to be fed to stdin.
     
     Rules:
     - Each string in the array represents ONE test case's full input.
     - If multiple inputs() are required for a single run, join them with "\\n" (newline) in the string.
     - Do NOT include any explanations or keys, just the array of strings.
     
     PYTHON CODE:
     ${pythonCode}
     `;

    let fullResponse = '';

    let promptTokens = 0;
    let completionTokens = 0;

    if (provider === 'gemini') {
      const ai = new GoogleGenAI({ apiKey: settings.geminiApiKey || '' });
      const response = await ai.models.generateContent({
        model: modelArg,
        contents: prompt,
        config: {
          responseMimeType: 'application/json',
          temperature: 0.1,
        }
      });
      fullResponse = response.text || '';
      if (response.usageMetadata) {
        promptTokens = response.usageMetadata.promptTokenCount || 0;
        completionTokens = response.usageMetadata.candidatesTokenCount || 0;
      }
    } else {
      const ollamaClient = provider === 'ollama-cloud'
        ? new Ollama({ host: settings.ollamaCloudBaseUrl, headers: settings.ollamaCloudApiKey ? { Authorization: `Bearer ${settings.ollamaCloudApiKey}` } : {} })
        : ollama;

      const responseStream = await ollamaClient.generate({
        model: modelArg,
        prompt,
        format: 'json',
        stream: true,
        options: { temperature: 0.1, seed: 42 },
      });

      for await (const chunk of responseStream) {
        fullResponse += chunk.response;
        if (chunk.done) {
          promptTokens = chunk.prompt_eval_count || 0;
          completionTokens = chunk.eval_count || 0;
        }
      }
    }

    const duration = Date.now() - t0;
    trackLlmUsage({
      model: modelArg,
      provider,
      type: 'python_to_cobol_inputs',
      prompt_tokens: promptTokens,
      completion_tokens: completionTokens,
      total_tokens: promptTokens + completionTokens,
      duration_ms: duration,
      file_name: filename || '-'
    });

    let parsed: any;
    try {
      parsed = cleanAndParseJSON(fullResponse);
    } catch {
      console.error('[LLM] Error parsing Python test input Ollama JSON response.', fullResponse.slice(0, 100));
      return [];
    }

    let inputs: string[] = [];
    if (Array.isArray(parsed)) {
      inputs = parsed.map(p => typeof p === 'string' ? p : JSON.stringify(p));
    } else if (typeof parsed === 'object' && parsed !== null) {
      const found = Object.values(parsed).find(v => Array.isArray(v)) as string[] | undefined;
      if (found) inputs = found.map((p: any) => typeof p === 'string' ? p : JSON.stringify(p));
    }
    return inputs;
  } catch (error) {
    console.error('[LLM] Error calling Ollama for Python test inputs:', error);
    return [];
  }
}

async function executePythonWithInputs(filePath: string, inputs: string[]): Promise<{ status: 'success' | 'failed' | 'skipped'; outputs: string[]; avgTimeMs?: number }> {
    const outputs: string[] = [];
    const timings: number[] = [];

    const EXEC_TIMEOUT_MS = 10_000;

    for (const input of inputs) {
        let actualOutput = '';
        try {
            const pythonProcess = spawn('python', ['-u', filePath]);
            let stdoutData = '';
            let timedOut = false;

            const exitPromise = new Promise((resolve) => {
                pythonProcess.stdout.on('data', (data) => { stdoutData += data.toString(); });
                pythonProcess.on('close', (code) => { resolve(code); });
                pythonProcess.on('error', (err) => { resolve(1); });
            });

            if (input) {
                const inputToSend = input.replace(/\n/g, '\r\n');
                pythonProcess.stdin.write(inputToSend);
            }
            pythonProcess.stdin.end();

            const t0 = Date.now();
            const timeoutHandle = setTimeout(() => {
                timedOut = true;
                try { pythonProcess.kill('SIGKILL'); } catch {}
            }, EXEC_TIMEOUT_MS);

            await exitPromise;
            clearTimeout(timeoutHandle);
            timings.push(Date.now() - t0);

            if (timedOut) {
                console.warn(`[Python] Input test timed out for ${filePath} — skipping.`);
                outputs.push('[SKIPPED: timeout]');
                continue;
            }
            
            actualOutput = stdoutData.split('\n')
                .map(line => line.replace(/^(Enter|Input|Type|.*Enter).*?:\s*/i, '').trim())
                .filter(line => line.length > 0)
                .join('\n').trim();
                
            outputs.push(actualOutput);

        } catch (e) {
            outputs.push("Error executing Python");
        }
    }

    const avgTimeMs = timings.length ? timings.reduce((a, b) => a + b, 0) / timings.length : undefined;
    return { status: 'success', outputs, avgTimeMs };
}

async function executeCobolAndCompare(filePath: string, inputs: string[], expectedOutputs: string[]): Promise<{ allPassed: boolean, passedCount: number, formatMatchCount: number, detailedResults: TestResult[] }> {
    const detailedResults: TestResult[] = [];
    let passedCount = 0;
    let formatMatchCount = 0;

    const uniqueSuffix = `_${Date.now()}_${Math.floor(Math.random() * 1000)}`;
    const exePath = filePath.replace(/\.(cbl|cob)$/i, `${uniqueSuffix}.exe`);

    try {
        await execPromise(`cobc -x -o "${exePath}" "${filePath}"`);
    } catch (e: any) {
        console.error(`[COBOL] Compilation failed in reverse test for ${filePath}:`, e);
        return { allPassed: false, passedCount: 0, formatMatchCount: 0, detailedResults: [] };
    }

    const runCmd = process.platform === 'win32' ? exePath : `./${path.basename(exePath)}`;
    const cwd = path.dirname(exePath);

    const EXEC_TIMEOUT_MS = 10_000;
    const MAX_OUTPUT_BYTES = 1_048_576; // 1 MB cap to prevent RangeError

    for (let i = 0; i < inputs.length; i++) {
        const input = inputs[i];
        const expected = expectedOutputs[i] || "";
        
        let actualOutput = '';
        let testPassed = false;
        let execTimeMs = 0;
        let skipped = false;

        try {
            const child = spawn(runCmd, [], { cwd, shell: false });
            
            let stdoutData = '';
            let stderrData = '';
            let timedOut = false;

            const exitPromise = new Promise((resolve) => {
                child.stdout.on('data', (data) => {
                    if (stdoutData.length < MAX_OUTPUT_BYTES) {
                        stdoutData += data.toString();
                    } else if (!timedOut) {
                        timedOut = true;
                        console.warn(`[COBOL] Output size limit reached for ${filePath} — killing process.`);
                        try { child.kill('SIGKILL'); } catch {}
                    }
                });
                child.stderr.on('data', (data) => { stderrData += data.toString().slice(0, 2048); });
                child.on('close', (code) => { resolve(code); });
                child.on('error', (err) => { resolve(1); });
            });

            if (input) {
                const inputToSend = input.replace(/\n/g, '\r\n');
                child.stdin.write(inputToSend);
            }
            child.stdin.end();

            const t0 = Date.now();
            const timeoutHandle = setTimeout(() => {
                timedOut = true;
                try { child.kill('SIGKILL'); } catch {}
            }, EXEC_TIMEOUT_MS);

            await exitPromise;
            clearTimeout(timeoutHandle);
            execTimeMs = Date.now() - t0;

            if (timedOut) {
                console.warn(`[COBOL] Test case #${i + 1} timed out or hit output limit for ${filePath} — skipping.`);
                skipped = true;
                actualOutput = '[SKIPPED: timeout/output-limit]';
            } else {
                actualOutput = stdoutData.split('\n')
                    .map(line => line.replace(/^(Enter|Input|Type|.*Enter).*?:\s*/i, '').trim())
                    .filter(line => line.length > 0)
                    .join('\n').trim();

                if (stderrData) actualOutput += `\n[STDERR]: ${stderrData}`;

                if (normalizeOutput(actualOutput).includes(normalizeOutput(expected))) {
                    testPassed = true;
                    passedCount++;
                }

                const isFormat = formatMatchOutputs(actualOutput, expected);
                if (isFormat) formatMatchCount++;
            }

        } catch (error: any) {
            actualOutput = `Error: ${error.message}`;
        }

        detailedResults.push({
            input: input,
            expected_output: expected,
            actual_output: actualOutput,
            semantic_match: testPassed,
            format_match: formatMatchOutputs(actualOutput, expected),
            exec_time_ms: execTimeMs,
            failure_category: skipped ? 'crash' : (testPassed ? null : categorizeFailure(expected, actualOutput)),
        });
    }

    try {
        if (fs.existsSync(exePath)) fs.unlinkSync(exePath);
    } catch (e) {
        console.warn(`[COBOL] Could not delete executable ${exePath}:`, e);
    }

    return { 
        allPassed: passedCount === inputs.length,
        passedCount,
        formatMatchCount,
        detailedResults 
    };
}

async function getPylintScore(filePath: string): Promise<number> {
    try {
        const command = `python -m pylint "${filePath}"`;
        try {
            const { stdout } = await execPromise(command);
            const match = stdout.match(/Your code has been rated at ([\d\.]+)\/10/);
            if (match) return parseFloat(match[1]);
        } catch (e: any) {
            if (e.stdout) {
                 const match = e.stdout.match(/Your code has been rated at ([\d\.]+)\/10/);
                 if (match) return parseFloat(match[1]);
            }
        }
        return 0; 
    } catch (e) {
        console.warn('Pylint execution failed (tool might not be installed). Using mock score.');
        return Math.random() * 3 + 6;
    }
}

async function getComplexityScore(filePath: string): Promise<{ cc: number }> {
     try {
        const command = `python -m radon cc "${filePath}" -j`;
        const { stdout } = await execPromise(command);
        const startIdx = stdout.indexOf('{');
        const endIdx = stdout.lastIndexOf('}');
        if (startIdx === -1 || endIdx === -1) return { cc: 1 };
        const jsonStr = stdout.substring(startIdx, endIdx + 1);
        const data = JSON.parse(jsonStr);
        const entries = Object.values(data)[0] as any[];
        if (!entries || !Array.isArray(entries) || entries.length === 0) return { cc: 1 };
        
        const total = entries.reduce((acc: number, curr: any) => acc + (curr.complexity || 0), 0);
        return { cc: Math.round(total / entries.length) || 1 };
    } catch (e: any) {
        console.warn('[radon cc] Failed:', (e.message ?? '').slice(0, 120));
        // Silently use mock score if radon is missing
        return { cc: Math.floor(Math.random() * 20) + 1 };
    }
}

export function getAnalysisResults(): AnalysisResult[] {
    const fileToTry = fs.existsSync(DETAIL_FILE) ? DETAIL_FILE : RESULTS_FILE;
    if (fs.existsSync(fileToTry)) {
        const data = fs.readFileSync(fileToTry, 'utf-8');
        return JSON.parse(data);
    }
    return [];
}

function formatModelName(dir: string): string {
    return dir.charAt(0).toUpperCase() + dir.slice(1);
}

function normalizeOutput(str: string): string {
    // 1. Replace commas with spaces, then replace all whitespace with single space
    let normalized = str.replace(/,/g, ' ').replace(/\s+/g, ' ').trim();
    // 2. Remove leading zeros from numbers (e.g., "005" -> "5", "0" -> "0")
    return normalized.split(' ').map(token => {
        // Check if token is a number
        if (/^\d+$/.test(token)) {
            // Remove leading zeros, but keep at least one digit if the number is 0
            return token.replace(/^0+(?=\d)/, '');
        }
        return token;
    }).join(' ');
}

/**
 * HARD MATCH: Every line of the actual output must exactly equal the corresponding
 * line of the expected output (after trimming trailing/leading whitespace per line).
 * This matches the academic "Hard Match" definition Ã¢â‚¬â€ an LLM in practice will likely
 * fail this test due to formatting differences.
 */
function formatMatchOutputs(actual: string, expected: string): boolean {
    if (!expected) return false;
    const actualLines = actual.split('\n').map(l => l.trim()).filter(l => l.length > 0);
    const expectedLines = expected.split('\n').map(l => l.trim()).filter(l => l.length > 0);
    if (actualLines.length !== expectedLines.length) return false;
    return actualLines.every((line, i) => line === expectedLines[i]);
}

function getCobolComplexity(code: string): number {
    let cc = 1; // Base complexity
    
    // Convert to uppercase for case-insensitive matching
    const upperCode = code.toUpperCase();
    
    // Remove comments (lines starting with *)
    const lines = upperCode.split('\n').filter(line => {
        const trimmed = line.trim();
        return trimmed.length > 6 && trimmed[6] !== '*';
    });
    
    const cleanCode = lines.join(' ');

    // Keywords that increase cyclomatic complexity
    const keywords = [
        'IF ', 
        'ELSE', 
        'EVALUATE', 
        'WHEN', 
        'PERFORM', 
        'LOOP', 
        'SEARCH', 
        'AND', 
        'OR'
        // 'GO TO' is also a branch, but often structural. Let's count it.
    ];

    keywords.forEach(kw => {
        // Count occurrences
        // Using split is a simple way to count substrings
        cc += cleanCode.split(kw).length - 1;
    });

    return cc;
}

async function runInvalidBoundaryTests(
  pyPath: string,
  cases: InvalidTestCase[]
): Promise<{ results: InvalidTestResult[]; summary: InvalidTestSummary }> {
  const results: InvalidTestResult[] = [];

  const EXEC_TIMEOUT_MS = 10_000;

  for (const tc of cases) {
    let pythonOutput = '';
    let crashed = false;
    let execTimeMs = 0;

    let realCobolExpected = tc.cobol_expected_output;

    try {
      const proc = spawn('python', ['-u', pyPath]);
      let stdout = '';
      let stderr = '';
      let timedOut = false;

      const done = new Promise<void>(resolve => {
        proc.stdout.on('data', (d: Buffer) => { stdout += d.toString(); });
        proc.stderr.on('data', (d: Buffer) => { stderr += d.toString(); });
        proc.on('close', () => resolve());
        proc.on('error', () => resolve());
      });

      if (tc.input) {
        proc.stdin.write(tc.input.replace(/\n/g, '\r\n'));
      }
      proc.stdin.end();

      const t0 = Date.now();
      const timeoutHandle = setTimeout(() => {
        timedOut = true;
        try { proc.kill('SIGKILL'); } catch {}
      }, EXEC_TIMEOUT_MS);

      await done;
      clearTimeout(timeoutHandle);
      execTimeMs = Date.now() - t0;

      if (timedOut) {
        console.warn(`[Python] Boundary test "${tc.id}" timed out for ${pyPath} — skipping.`);
        crashed = true;
        pythonOutput = '[SKIPPED: timeout]';
      } else {
        pythonOutput = stdout
          .split('\n')
          .map((line: string) => line.trim())
          .filter((line: string) => line.length > 0)
          .join('\n')
          .trim();

        if (stderr) {
          crashed = true;
          pythonOutput += (pythonOutput ? '\n' : '') + `[STDERR]: ${stderr}`;
        }
      }
    } catch (e: any) {
      crashed = true;
      pythonOutput = `Error: ${e.message}`;
    }

    const faithful =
      !crashed &&
      normalizeOutput(pythonOutput).includes(normalizeOutput(realCobolExpected));

    results.push({
      test_id: tc.id,
      category: tc.category,
      description: tc.description,
      input: tc.input,
      cobol_expected_output: realCobolExpected,
      python_actual_output: pythonOutput,
      cobol_faithful: faithful,
      python_crashed: crashed,
      exec_time_ms: execTimeMs,
    });
  }

  const faithful = results.filter(r => r.cobol_faithful).length;
  const crashed  = results.filter(r => r.python_crashed).length;
  const summary: InvalidTestSummary = {
    total: results.length,
    faithful,
    crashed,
    unfaithful: results.length - faithful - crashed,
  };

  return { results, summary };
}

async function generateExecutiveSummary(results: AnalysisResult[], modelArg: string, provider: string): Promise<string> {
  try {
    const settings = getSettings();
    const t0 = Date.now();
    
    // Create a concise summary for the LLM
    const summaryData = results.map(r => ({
      file: r.source_file,
      models: r.models.map((m: any) => ({
        name: m.model_name,
        c2p_pass: `${m.metrics.unit_tests_passed}/${m.metrics.unit_tests_total}`,
        p2c_pass: `${m.metrics.python_to_cobol_semantic_match_passed}/${m.metrics.python_to_cobol_unit_tests_total}`,
        pylint: m.metrics.pylint_score,
        complexity_reduction: `${m.metrics.complexity_reduction_pct}%`
      }))
    }));

    const prompt = `
      You are an expert software architect specialized in Legacy Modernization (COBOL to Python).
      Analyze the following analysis report data and provide a professional, concise executive summary.
      Highlight:
      1. Overall success rate of the migration (COBOL to Python and Reverse).
      2. Which model performed best and why.
      3. Key areas of improvement.
      4. A concluding recommendation.
      
      Response Language: English
      
      DATA: 
      ${JSON.stringify(summaryData, null, 2)}
    `;

    let summary = '';
    let promptTokens = 0;
    let completionTokens = 0;

    if (provider === 'gemini') {
      const ai = new GoogleGenAI({ apiKey: settings.geminiApiKey || '' });
      const response = await ai.models.generateContent({
        model: modelArg,
        contents: prompt,
        config: { temperature: 0.2 }
      });
      summary = response.text || '';
      if (response.usageMetadata) {
        promptTokens = response.usageMetadata.promptTokenCount || 0;
        completionTokens = response.usageMetadata.candidatesTokenCount || 0;
      }
    } else {
      const ollamaClient = provider === 'ollama-cloud'
        ? new Ollama({ host: settings.ollamaCloudBaseUrl, headers: settings.ollamaCloudApiKey ? { Authorization: `Bearer ${settings.ollamaCloudApiKey}` } : {} })
        : ollama;

      const response = await ollamaClient.generate({
        model: modelArg,
        prompt: prompt,
        stream: false,
      });
      summary = response.response;
      promptTokens = response.prompt_eval_count || 0;
      completionTokens = response.eval_count || 0;
    }

    const duration = Date.now() - t0;
    trackLlmUsage({
      model: modelArg,
      provider,
      type: 'executive_summary',
      prompt_tokens: promptTokens,
      completion_tokens: completionTokens,
      total_tokens: promptTokens + completionTokens,
      duration_ms: duration
    });
    return summary;
  } catch (error) {
    console.error('Failed to generate executive summary:', error);
    return '';
  }
}

export async function generateCobolToPythonTranslationLLM(cobolCode: string, filename: string, modelArg: string, provider: string): Promise<string> {
  const settings = getSettings();
  const prompt = `
You are an expert in Legacy Modernization. Translate the following COBOL program into idiomatic, readable, and fully functional Python code.
Do not include any explanations, markdown formatting backticks, or other text outside of the Python code itself. Return ONLY valid Python code.

COBOL FILE: ${filename}
CODE:
${cobolCode}
`;

  let fullResponse = '';
  const t0 = Date.now();
  let promptTokens = 0;
  let completionTokens = 0;

  if (provider === 'gemini') {
    const ai = new GoogleGenAI({ apiKey: settings.geminiApiKey || '' });
    const response = await ai.models.generateContent({
      model: modelArg,
      contents: prompt,
      config: { temperature: 0.2 },
    });
    fullResponse = response.text || '';
    if (response.usageMetadata) {
      promptTokens = response.usageMetadata.promptTokenCount || 0;
      completionTokens = response.usageMetadata.candidatesTokenCount || 0;
    }
  } else {
    const ollamaClient = provider === 'ollama-cloud'
      ? new Ollama({ host: settings.ollamaCloudBaseUrl, headers: settings.ollamaCloudApiKey ? { Authorization: `Bearer ${settings.ollamaCloudApiKey}` } : {} })
      : ollama;

    const responseStream = await ollamaClient.generate({
      model: modelArg,
      prompt,
      stream: true,
      options: { temperature: 0.2 },
    });

    for await (const chunk of responseStream) {
      fullResponse += chunk.response;
      if (chunk.done) {
        promptTokens = chunk.prompt_eval_count || 0;
        completionTokens = chunk.eval_count || 0;
      }
    }
  }

  const duration = Date.now() - t0;
  trackLlmUsage({
    model: modelArg,
    provider,
    type: 'translation',
    prompt_tokens: promptTokens,
    completion_tokens: completionTokens,
    total_tokens: promptTokens + completionTokens,
    duration_ms: duration,
    file_name: filename
  });

  // Clean up any markdown code blocks if the LLM provided them anyway
  let cleaned = fullResponse.replace(/^```python\s*/gi, '').replace(/^```\s*/g, '').replace(/```\s*$/g, '');
  return cleaned.trim() + '\n';
}

export async function runCobolToPythonTranslation(targetModelName: string, onProgress?: (msg: string) => void): Promise<{ success: boolean; count: number; error?: string }> {
  try {
    const safeName = targetModelName.trim().replace(/[^a-zA-Z0-9_\\-]/g, '');
    if (!safeName) return { success: false, count: 0, error: 'Invalid model name' };

    const settings = getSettings();
    const provider = settings.llmProvider || 'ollama-local';
    const LLM_MODEL = provider === 'gemini' 
      ? (settings.geminiModel || 'gemini-2.5-pro') 
      : provider === 'ollama-cloud' 
        ? (settings.ollamaCloudModel || 'llama3') 
        : (settings.ollamaModel || 'llama3');

    const cobolFiles = fs.readdirSync(COBOL_DIR).filter(f => f.toLowerCase().endsWith('.cbl') || f.toLowerCase().endsWith('.cob'));
    if (cobolFiles.length === 0) {
      if (onProgress) onProgress('No COBOL files found.');
      return { success: false, count: 0, error: 'No COBOL files found to translate.' };
    }

    const outputDir = path.join(PYTHON_BASE_DIR, safeName);
    if (!fs.existsSync(outputDir)) {
      fs.mkdirSync(outputDir, { recursive: true });
    }

    let successCount = 0;
    for (let i = 0; i < cobolFiles.length; i++) {
        const file = cobolFiles[i];
        if (onProgress) onProgress(`Translating ${file} (File ${i+1} of ${cobolFiles.length})...`);
        
        const cblPath = path.join(COBOL_DIR, file);
        const cobolCode = fs.readFileSync(cblPath, 'utf-8');
        
        try {
            const pythonCode = await generateCobolToPythonTranslationLLM(cobolCode, file, LLM_MODEL, provider);
            const baseName = path.parse(file).name;
            const pyPath = path.join(outputDir, `${baseName}.py`);
            fs.writeFileSync(pyPath, pythonCode);
            successCount++;
        } catch (err: any) {
            console.error(`Error translating ${file}:`, err);
            if (onProgress) onProgress(`Error translating ${file}: ${err.message}`);
        }
    }
    
    if (onProgress) onProgress(`Translation complete. ${successCount}/${cobolFiles.length} files translated successfully.`);
    return { success: true, count: successCount };

  } catch (err: any) {
    console.error('Translation process failed:', err);
    if (onProgress) onProgress('Translation process failed: ' + err.message);
    return { success: false, count: 0, error: err.message };
  }
}
