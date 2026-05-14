import fs from 'fs';
import path from 'path';

const resultsPath = path.join(process.cwd(), 'public', 'output', 'results.json');
const results = JSON.parse(fs.readFileSync(resultsPath, 'utf-8'));

console.log('Total files:', results.length);

const complexityCounts: Record<string, number> = { Simple: 0, Medium: 0, Complex: 0 };

const modelsSet = new Set<string>();

results.forEach((file: any) => {
  file.models.forEach((m: any) => modelsSet.add(m.model_name));
});

const models = Array.from(modelsSet);

const overallStats: Record<string, any> = {};

for (const model of models) {
  overallStats[model] = {
    count: 0,
    semantic_match_pct: 0,
    format_match_pct: 0,
    pass_at_1: 0,
    p2c_semantic_match_pct: 0,
    p2c_format_match_pct: 0,
    pylint: 0,
    complexity_reduction: 0,
    loc_ratio: 0,
    mypy_errors: 0,
    exec_time: 0,
    halstead: 0
  };
}

results.forEach((file: any) => {
  file.models.forEach((m: any) => {
    const s = overallStats[m.model_name];
    s.count++;
    
    // soft match
    const ut_total = m.metrics?.unit_tests_total || 1;
    const ut_passed = m.metrics?.unit_tests_passed || 0;
    s.semantic_match_pct += (ut_passed / ut_total) * 100;
    
    // hard match
    const fmt_passed = m.metrics?.format_match_passed || 0;
    s.format_match_pct += (fmt_passed / ut_total) * 100;
    
    // pass@1
    if (m.metrics?.pass_at_1) s.pass_at_1++;
    
    // p2c
    const p2c_total = m.metrics?.python_to_cobol_unit_tests_total || 1;
    const p2c_passed = m.metrics?.python_to_cobol_semantic_match_passed || 0;
    const p2c_fmt = m.metrics?.python_to_cobol_format_match_passed || 0;
    s.p2c_semantic_match_pct += (p2c_passed / p2c_total) * 100;
    s.p2c_format_match_pct += (p2c_fmt / p2c_total) * 100;
    
    s.pylint += m.metrics?.pylint_score || 0;
    s.complexity_reduction += m.metrics?.complexity_reduction_pct || 0;
    s.loc_ratio += m.metrics?.loc_ratio || 0;
    s.mypy_errors += m.metrics?.mypy_error_count || 0;
    s.exec_time += m.metrics?.exec_time_python_avg_ms || 0;
    s.halstead += m.metrics?.halstead_effort || 0;
  });
});

for (const model of models) {
  const s = overallStats[model];
  if (s.count > 0) {
    s.semantic_match_pct = (s.semantic_match_pct / s.count).toFixed(1);
    s.format_match_pct = (s.format_match_pct / s.count).toFixed(1);
    s.pass_at_1 = ((s.pass_at_1 / s.count) * 100).toFixed(1);
    s.p2c_semantic_match_pct = (s.p2c_semantic_match_pct / s.count).toFixed(1);
    s.p2c_format_match_pct = (s.p2c_format_match_pct / s.count).toFixed(1);
    s.pylint = (s.pylint / s.count).toFixed(2);
    s.complexity_reduction = (s.complexity_reduction / s.count).toFixed(1);
    s.loc_ratio = (s.loc_ratio / s.count).toFixed(2);
    s.mypy_errors = (s.mypy_errors / s.count).toFixed(0);
    s.exec_time = (s.exec_time / s.count).toFixed(1);
    s.halstead = (s.halstead / s.count).toFixed(0);
  }
}

fs.writeFileSync(path.join(process.cwd(), 'public', 'output', 'overall_metrics.json'), JSON.stringify(overallStats, null, 2));
console.log('Saved overall_metrics.json');

