import fs from 'fs';
import path from 'path';
import { spawnSync } from 'child_process';
import {
  getMatchComparisonConfig,
  getTestOutcomeConfig,
  getPylintScatterConfig,
  getComplexityConfig,
  getMaintainabilityConfig,
  getExecutionVsSizeConfig,
  getErrorPatternConfig,
  getConsensusFailureConfig,
  getHardSoftDeltaConfig,
  getRadarConfig,
  getBoundaryFaithfulnessConfig,
  getTokenUsageConfig
} from '../src/lib/utils/exportConfigs';
import { AnalysisResult, LlmUsageEntry } from '../src/lib/data/types';

const resultsPath = path.join(process.cwd(), 'public', 'output', 'results.json');
const results: AnalysisResult[] = JSON.parse(fs.readFileSync(resultsPath, 'utf-8'));
const usagePath = path.join(process.cwd(), 'public', 'output', 'llm_usage.json');
const usage: LlmUsageEntry[] = fs.existsSync(usagePath)
  ? JSON.parse(fs.readFileSync(usagePath, 'utf-8'))
  : [];

const dummyT = (k: string) => k.split('.').pop() || k;

const configs = {
  'match_comparison': getMatchComparisonConfig(results, dummyT),
  'test_outcome': getTestOutcomeConfig(results, dummyT),
  'pylint_scatter': getPylintScatterConfig(results, dummyT),
  'complexity': getComplexityConfig(results, dummyT),
  'maintainability': getMaintainabilityConfig(results, dummyT),
  'exec_vs_size': getExecutionVsSizeConfig(results, dummyT),
  'error_pattern': getErrorPatternConfig(results, dummyT),
  'consensus_failure': getConsensusFailureConfig(results, dummyT),
  'hard_soft_delta': getHardSoftDeltaConfig(results, dummyT),
  'radar_quality': getRadarConfig(results, dummyT),
  'boundary_faithfulness': getBoundaryFaithfulnessConfig(results, dummyT),
  'token_usage': getTokenUsageConfig(usage, dummyT)
};

const outputDir = path.join(process.cwd(), 'article', 'pycobolix_last_converted');
const pythonScript = path.join(process.cwd(), 'scripts', 'export_generic_chart.py');

for (const [name, config] of Object.entries(configs)) {
  const payload = {
    ...config,
    format: 'pdf',
    title: ''
  };
  
  const res = spawnSync('python', [pythonScript], {
    input: JSON.stringify(payload),
    maxBuffer: 10 * 1024 * 1024
  });
  
  if (res.status !== 0) {
    console.error(`Failed to export ${name}:`, res.stderr?.toString());
  } else {
    fs.writeFileSync(path.join(outputDir, `fig_new_${name}.pdf`), res.stdout);
    console.log(`Exported fig_new_${name}.pdf`);
  }
}
