export interface Metrics {
  pylint_score: number;                  // 0-10 (Pylint)
  complexity_score: number;              // Radon Cyclomatic Complexity
  complexity_reduction_pct: number;      // (COBOL_CC - Python_CC) / COBOL_CC * 100
  pass_at_1: boolean;
  unit_tests_passed?: number;
  unit_tests_total?: number;

  // Differential Testing
  format_match_passed?: number;            // Exact char-for-char matches

  // Code Size
  loc_ratio?: number;                    // Python LoC / COBOL LoC

  // Reverse Differential Testing (Python -> COBOL)
  python_to_cobol_semantic_match_passed?: number;
  python_to_cobol_unit_tests_total?: number;
  python_to_cobol_format_match_passed?: number;

  // Execution Performance
  exec_time_python_avg_ms?: number;      // Mean Python execution time per test (ms)
  exec_time_cobol_avg_ms?: number;       // Mean COBOL execution time per test (ms)

  // Static Analysis
  mypy_error_count?: number;             // Number of mypy type errors
  halstead_volume?: number;              // Halstead Volume (H)
  halstead_difficulty?: number;          // Halstead Difficulty (D)
  halstead_effort?: number;              // Halstead Effort (E) — proxy for dev effort to comprehend
  maintainability_index?: number;        // Maintainability Index

  // COBOL Boundary Test Rates
  cobol_boundary_tests_total?: number;
  cobol_boundary_tests_passed?: number;

  // Error Pattern Distribution (counts per category)
  error_sign?: number;
  error_whitespace?: number;
  error_logic?: number;
  error_crash?: number;
}

export type QualityLabel = 'High' | 'Medium' | 'Low';

export interface TestResult {
  input: string;
  expected_output: string;               // From COBOL (ground truth)
  actual_output: string;                 // From Python (LLM translation)
  semantic_match: boolean;               // Soft match
  format_match: boolean;                 // Exact char-for-char
  failure_category?: 'sign_error' | 'whitespace' | 'logic' | 'crash' | null;
  exec_time_ms?: number;                 // Single test execution time
}

/**
 * A single COBOL-boundary-violation test case definition.
 * Describes an input that COBOL handles with overflow/truncation/sign-stripping,
 * and the COBOL-correct expected output (e.g. PIC 99 receiving 100 → outputs "10").
 */
export interface InvalidTestCase {
  id: string;                            // Unique identifier, e.g. "tc_overflow_age"
  category: 'overflow' | 'sign_error' | 'alpha_to_numeric' | 'boundary_valid';
  description: string;                   // Human-readable description
  input: string;                         // Raw stdin (newline-separated if multiple ACCEPTs)
  cobol_expected_output: string;         // What COBOL actually produces
  cobol_constraint: string;              // PIC clause / COBOL rule that causes this
}

/**
 * Result of running an InvalidTestCase against a Python model.
 * `should_fail` = true means Python SHOULD NOT produce output (or should produce
 * the same truncated/sign-stripped output as COBOL). If Python produces something
 * different, that is a faithfulness violation.
 */
export interface InvalidTestResult {
  test_id: string;
  category: InvalidTestCase['category'];
  description: string;
  input: string;
  cobol_expected_output: string;
  python_actual_output: string;
  cobol_faithful: boolean;               // true = Python output matches COBOL (good)
  python_crashed: boolean;               // true = Python raised an exception
  exec_time_ms: number;
}

export interface InvalidTestSummary {
  total: number;
  faithful: number;                      // Python matched COBOL boundary behavior
  unfaithful: number;                    // Python produced wrong output for boundary input
  crashed: number;                       // Python crashed instead of handling gracefully
}

export interface ModelResult {
  model_name: string;
  python_code: string;
  python_filename: string;
  status: 'success' | 'error';
  quality_label: QualityLabel;
  metrics: Metrics;
  test_results?: TestResult[];
  /** Results from running Python-generated test cases against COBOL */
  python_to_cobol_test_results?: TestResult[];
  /** Results from running COBOL boundary-violation inputs against this Python model */
  invalid_test_results?: InvalidTestResult[];
  invalid_test_summary?: InvalidTestSummary;
}

export interface AnalysisResult {
  id: string;
  source_file: string;
  cobol_code: string;
  cobol_execution_status?: 'success' | 'failed' | 'skipped';
  timestamp: string;
  models: ModelResult[];
  /** AI-generated executive summary of the overall analysis findings */
  executive_summary?: string;
  /** Reproducibility metadata recorded at analysis run time */
  run_metadata?: {
    run_id: string;                              // UUID shared by all files in a single run
    timestamp: string;                           // ISO-8601 run start time
    ollama_model: string;                        // Model used for LLM fallback
    input_generation_strategy: 'bva' | 'llm';   // How test inputs were produced
  };
}

export interface LlmUsageEntry {
  id: string;
  timestamp: string;
  model: string;
  provider: string;
  type: 'input_generation' | 'boundary_test_generation' | 'executive_summary' | 'translation' | 'python_to_cobol_inputs';
  prompt_tokens: number;
  completion_tokens: number;
  total_tokens: number;
  duration_ms: number;
  file_name?: string;
}
