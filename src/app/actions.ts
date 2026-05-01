'use server';

import fs from 'fs';
import path from 'path';
import { runFullAnalysis, getAnalysisResults, runCustomAnalysis, runInteractiveSandbox } from '@/lib/server/analysis';
import { getSettings, saveSettings, AppSettings } from '@/lib/settings';
import ollama, { Ollama } from 'ollama';
import { GoogleGenAI } from '@google/genai';
import { revalidatePath } from 'next/cache';

export async function runInteractiveSandboxAction(
    cobolCode: string, 
    pythonCode: string, 
    input: string
) {
    try {
        const result = await runInteractiveSandbox(cobolCode, pythonCode, input);
        return result;
    } catch (error: any) {
        return { success: false, error: error.message };
    }
}

export async function runAnalysisAction() {
  try {
    const settings = getSettings();
    const provider = settings.llmProvider || 'ollama-local';
    
    if (provider === 'gemini') {
      if (!settings.geminiApiKey?.trim()) return { success: false, error: 'GEMINI_API_KEY_MISSING' };
      if (!settings.geminiModel?.trim()) return { success: false, error: 'NO_MODEL_SELECTED' };
    } else if (provider === 'ollama-cloud') {
      if (!settings.ollamaCloudBaseUrl?.trim()) return { success: false, error: 'CLOUD_URL_MISSING' };
      if (!settings.ollamaCloudModel?.trim()) return { success: false, error: 'NO_MODEL_SELECTED' };
    } else {
      // Local Ollama
      const modelStr = settings.ollamaModel?.trim();
      if (!modelStr) return { success: false, error: 'NO_MODEL_SELECTED' };
      try {
        const response = await ollama.list();
        const isInstalled = response.models.some((m: any) => m.name === modelStr || m.name.startsWith(modelStr + ':'));
        if (!isInstalled) return { success: false, error: 'MODEL_NOT_INSTALLED' };
      } catch {
         return { success: false, error: 'OLLAMA_NOT_REACHABLE' };
      }
    }

    const results = await runFullAnalysis();
    return { success: true, data: results };
  } catch (error) {
    console.error('Analysis failed:', error);
    return { success: false, error: 'Failed to run analysis' };
  }
}

export async function getAnalysisResultsAction() {
  try {
    revalidatePath('/', 'layout');
    const results = getAnalysisResults();
    return { success: true, data: results };
  } catch (error) {
     console.error('Failed to fetch results:', error);
     return { success: false, error: 'Failed to fetch results' };
  }
}

// Ensure the type matches what generateTestCases returns or stores
// For simplicity, we assume we re-use test cases from a stored result since we don't store them separately yet.
// In a real DB app, we'd fetch test cases by ID.
// Here, we'll ask the client to pass the original test cases or we re-generate (expensive).
// OPTION: The client sends the test cases found in the `AnalysisResult`.
// But `AnalysisResult` now has `test_results`. We need the *inputs/expected*.
// Let's assume the client sends back the `inputs` and `expected` from the `test_results` it has.

export async function runCustomCodeAction(pythonCode: string, testCases: {input: string, expected_output: string}[]) {
    try {
        const result = await runCustomAnalysis(pythonCode, testCases);
        return { success: true, ...result };
    } catch (error: any) {
        return { success: false, error: error.message };
    }
}

// ─── Settings Actions ──────────────────────────────────────────────────────────

export async function getSettingsAction() {
  try {
    const settings = getSettings();
    return { success: true, data: settings };
  } catch {
    return { success: false, error: 'Failed to load settings' };
  }
}

export async function saveSettingsAction(settings: Partial<AppSettings>) {
  try {
    const saved = saveSettings(settings);
    return { success: true, data: saved };
  } catch {
    return { success: false, error: 'Failed to save settings' };
  }
}

export async function listOllamaModelsAction() {
  try {
    const response = await ollama.list();
    const models = response.models.map((m: any) => ({
      name: m.name,
      size: m.size,
      modified_at: m.modified_at,
    }));
    return { success: true, data: models };
  } catch {
    return { success: false, error: 'Ollama not reachable. Make sure it is running on localhost:11434.' };
  }
}

export async function listOllamaCloudModelsAction(baseUrl: string, apiKey?: string) {
  try {
    if (!baseUrl?.trim()) {
      return { success: false, error: 'Base URL is required' };
    }
    const headers: Record<string, string> = { 'Content-Type': 'application/json' };
    if (apiKey?.trim()) headers['Authorization'] = `Bearer ${apiKey.trim()}`;

    const cloudClient = new Ollama({ host: baseUrl.trim(), headers });
    const response = await cloudClient.list();
    const models = response.models.map((m: any) => ({
      name: m.name,
      size: m.size ?? 0,
      modified_at: m.modified_at ?? '',
    }));
    return { success: true, data: models };
  } catch (e: any) {
    return { success: false, error: 'Could not reach Ollama Cloud: ' + (e.message ?? 'Unknown error') };
  }
}

// ─── Python Model Directories ────────────────────────────────────────────────

export async function getPythonModelDirsAction() {
  try {
    const pythonBaseDir = path.join(process.cwd(), 'public', 'python');
    if (!fs.existsSync(pythonBaseDir)) {
      fs.mkdirSync(pythonBaseDir, { recursive: true });
      return { success: true, data: [] };
    }
    const dirs = fs.readdirSync(pythonBaseDir, { withFileTypes: true })
      .filter(dirent => dirent.isDirectory())
      .map(dirent => dirent.name);
    return { success: true, data: dirs };
  } catch (error: any) {
    return { success: false, error: 'Failed to read Python directories: ' + error.message };
  }
}

export async function createPythonModelDirAction(name: string) {
  try {
    if (!name || name.trim() === '') {
      return { success: false, error: 'Name cannot be empty' };
    }
    const safeName = name.trim().replace(/[^a-zA-Z0-9_\-]/g, '');
    if (!safeName) {
      return { success: false, error: 'Name must contain valid characters' };
    }
    const pythonBaseDir = path.join(process.cwd(), 'public', 'python');
    const newDir = path.join(pythonBaseDir, safeName);
    
    if (fs.existsSync(newDir)) {
      return { success: false, error: 'Provider directory already exists' };
    }
    
    fs.mkdirSync(newDir, { recursive: true });
    return { success: true, data: safeName };
  } catch (error: any) {
    return { success: false, error: 'Failed to create Python directory: ' + error.message };
  }
}

export async function uploadPythonModelDirAction(formData: FormData) {
  try {
    const name = formData.get('modelName') as string;
    if (!name || name.trim() === '') {
      return { success: false, error: 'Model name cannot be empty' };
    }
    const safeName = name.trim().replace(/[^a-zA-Z0-9_\-]/g, '');
    if (!safeName) {
      return { success: false, error: 'Model name must contain valid characters' };
    }
    
    // Check if directory already exists
    const pythonBaseDir = path.join(process.cwd(), 'public', 'python');
    const newDir = path.join(pythonBaseDir, safeName);
    if (fs.existsSync(newDir)) {
      return { success: false, error: 'Provider directory already exists' };
    }

    // Get all files
    const files = formData.getAll('files') as File[];
    if (!files || files.length === 0) {
      return { success: false, error: 'No files uploaded' };
    }

    // Create directory
    fs.mkdirSync(newDir, { recursive: true });

    // Write files
    let savedCount = 0;
    for (const file of files) {
      // Basic validation to only accept python files
      if (file.name.endsWith('.py')) {
        const buffer = Buffer.from(await file.arrayBuffer());
        // Webkit relative path is not consistently available on the server-side File object
        // So we just use the base filename
        const filePath = path.join(newDir, file.name);
        fs.writeFileSync(filePath, buffer);
        savedCount++;
      }
    }

    return { success: true, data: { name: safeName, count: savedCount } };
  } catch (error: any) {
    return { success: false, error: 'Failed to upload Python directory: ' + error.message };
  }
}

// ─── COBOL Source Files ───────────────────────────────────────────────────────

export async function getCobolFilesAction() {
  try {
    const cobolDir = path.join(process.cwd(), 'public', 'cobol');
    if (!fs.existsSync(cobolDir)) {
      fs.mkdirSync(cobolDir, { recursive: true });
      return { success: true, data: [] as string[] };
    }
    const files = fs.readdirSync(cobolDir)
      .filter(f => f.endsWith('.cbl') || f.endsWith('.cob') || f.endsWith('.CBL') || f.endsWith('.COB'));
    return { success: true, data: files };
  } catch (error: any) {
    return { success: false, error: 'Failed to read COBOL files: ' + error.message };
  }
}

export async function uploadCobolFilesAction(formData: FormData) {
  try {
    const files = formData.getAll('files') as File[];
    if (!files || files.length === 0) {
      return { success: false, error: 'No files uploaded' };
    }

    const cobolDir = path.join(process.cwd(), 'public', 'cobol');
    if (!fs.existsSync(cobolDir)) fs.mkdirSync(cobolDir, { recursive: true });

    let savedCount = 0;
    for (const file of files) {
      const lower = file.name.toLowerCase();
      if (lower.endsWith('.cbl') || lower.endsWith('.cob')) {
        const buffer = Buffer.from(await file.arrayBuffer());
        fs.writeFileSync(path.join(cobolDir, file.name), buffer);
        savedCount++;
      }
    }

    return { success: true, data: { count: savedCount } };
  } catch (error: any) {
    return { success: false, error: 'Failed to upload COBOL files: ' + error.message };
  }
}

export async function deletePythonModelDirAction(name: string) {
  try {
    if (!name || name.trim() === '') {
      return { success: false, error: 'Model name cannot be empty' };
    }
    const safeName = name.trim().replace(/[^a-zA-Z0-9_\-]/g, '');
    const pythonBaseDir = path.join(process.cwd(), 'public', 'python');
    const dirToDelete = path.join(pythonBaseDir, safeName);
    
    if (fs.existsSync(dirToDelete)) {
      fs.rmSync(dirToDelete, { recursive: true, force: true });
      return { success: true };
    }
    return { success: false, error: 'Directory not found' };
  } catch (error: any) {
    return { success: false, error: 'Failed to delete Python directory: ' + error.message };
  }
}

export async function deleteCobolFileAction(filename: string) {
  try {
    if (!filename || filename.trim() === '') {
      return { success: false, error: 'Filename cannot be empty' };
    }
    const cobolDir = path.join(process.cwd(), 'public', 'cobol');
    const fileToDelete = path.join(cobolDir, filename);
    
    // Basic security check to prevent directory traversal
    if (!fileToDelete.startsWith(cobolDir)) {
      return { success: false, error: 'Invalid filename' };
    }

    if (fs.existsSync(fileToDelete)) {
      fs.unlinkSync(fileToDelete);
      return { success: true };
    }
    return { success: false, error: 'File not found' };
  } catch (error: any) {
    return { success: false, error: 'Failed to delete COBOL file: ' + error.message };
  }
}

export async function generateAnalysisExplanationAction(results: any[], lang: string = 'en') {
  try {
    const settings = getSettings();
    const provider = settings.llmProvider || 'ollama-local';
    const modelArg = provider === 'gemini' 
      ? (settings.geminiModel || 'gemini-1.5-pro') 
      : provider === 'ollama-cloud' 
        ? (settings.ollamaCloudModel || 'llama3') 
        : (settings.ollamaModel || 'llama3');

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
      Analyze the following analysis report data and provide concise, professional, and distinct insights for each section of a PDF report.
      
      Response Format: You MUST reply with ONLY a valid, flat JSON object. Do NOT use nested objects. The values MUST be simple strings containing a single paragraph.
      {
        "executiveSummary": "A single paragraph string summarizing overall success rate, best model, and a concluding recommendation.",
        "matchRates": "A single paragraph string focused on the Format vs Semantic match rates.",
        "pylintAndComplexity": "A single paragraph string analyzing pylint scores and cyclomatic complexity reduction.",
        "errorPatterns": "A single paragraph string focused on the distribution of Sign, Whitespace, Logic, and Crash errors.",
        "pythonToCobol": "A single paragraph string focused exclusively on the Python to COBOL (Reverse) metrics, if available."
      }
      
      Response Language: ${lang === 'tr' ? 'Turkish' : 'English'}
      
      DATA: 
      ${JSON.stringify(summaryData, null, 2)}
    `;

    let explanationTxt = '';

    if (provider === 'gemini') {
      if (!settings.geminiApiKey) throw new Error('GEMINI_API_KEY_MISSING');
      const ai = new GoogleGenAI({ apiKey: settings.geminiApiKey });
      const response = await ai.models.generateContent({
        model: modelArg,
        contents: prompt,
        config: {
          temperature: 0.2,
        }
      });
      explanationTxt = response.text || '';
    } else {
      const ollamaClient = provider === 'ollama-cloud'
        ? new Ollama({ host: settings.ollamaCloudBaseUrl, headers: settings.ollamaCloudApiKey ? { Authorization: `Bearer ${settings.ollamaCloudApiKey}` } : {} })
        : ollama;

      const response = await ollamaClient.generate({
        model: modelArg,
        prompt: prompt,
        stream: false,
        format: 'json',
      });
      explanationTxt = response.response;
    }

    let parsedExplanation;
    try {
        // Find the first { and the last } to extract just the JSON part
        const startIdx = explanationTxt.indexOf('{');
        const endIdx = explanationTxt.lastIndexOf('}');
        
        if (startIdx !== -1 && endIdx !== -1 && endIdx > startIdx) {
            const jsonStr = explanationTxt.substring(startIdx, endIdx + 1);
            parsedExplanation = JSON.parse(jsonStr);
            
            // Safety Check: The AI might still send nested objects despite instructions.
            // If any value is a nested object, stringify it so React-PDF doesn't crash or print [object Object].
            const keys = ['executiveSummary', 'matchRates', 'pylintAndComplexity', 'errorPatterns', 'pythonToCobol'];
            for (const k of keys) {
                if (parsedExplanation[k] && typeof parsedExplanation[k] === 'object') {
                    // Try to extract a string if it's deeply nested, or just format it cleanly
                    const vals = Object.values(parsedExplanation[k]);
                    if (vals.length > 0 && typeof vals[0] === 'string') {
                         parsedExplanation[k] = vals.join(' ');
                    } else {
                         parsedExplanation[k] = JSON.stringify(parsedExplanation[k]);
                    }
                }
            }
        } else {
             throw new Error("Could not find JSON object bounds");
        }
    } catch (e) {
        console.error("Failed to parse AI JSON:", e, explanationTxt);
        // Fallback: Just strip the code blocks and use the raw text
        const cleanFallback = explanationTxt.replace(/```json/gi, '').replace(/```/g, '').trim();
        parsedExplanation = {
            executiveSummary: cleanFallback.substring(0, 800) + (cleanFallback.length > 800 ? '...' : ''),
            matchRates: '',
            pylintAndComplexity: '',
            errorPatterns: '',
            pythonToCobol: ''
        };
    }

    // Persist the explanation back to the files (just keeping executive summary for backward compatibility in standard JSON files)
    if (parsedExplanation && parsedExplanation.executiveSummary) {
      const RESULTS_FILE = path.join(process.cwd(), 'public', 'output', 'results.json');
      const DETAIL_FILE = path.join(process.cwd(), 'public', 'output', 'test_detail.json');
      
      const allResults = getAnalysisResults();
      if (allResults && allResults.length > 0) {
        allResults[0].executive_summary = parsedExplanation.executiveSummary;
        const payload = JSON.stringify(allResults, null, 2);
        fs.writeFileSync(RESULTS_FILE, payload);
        fs.writeFileSync(DETAIL_FILE, payload);
      }
    }

    return { success: true, data: parsedExplanation };
  } catch (error: any) {
    console.error('Explanation generation failed:', error);
    return { success: false, error: error.message || 'Failed to generate explanation' };
  }
}
