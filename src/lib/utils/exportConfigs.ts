import { AnalysisResult, LlmUsageEntry } from '@/lib/data/types';

export function getMatchComparisonConfig(data: AnalysisResult[], t: any) {
  const stats: Record<string, { hard: number; soft: number; total: number }> = {};
  data.forEach(file => {
    file.models.forEach(model => {
      if (!stats[model.model_name]) {
        stats[model.model_name] = { hard: 0, soft: 0, total: 0 };
      }
      const s = stats[model.model_name];
      const total = model.metrics.unit_tests_total ?? 0;
      s.total += total;
      s.hard += model.metrics.format_match_passed ?? 0;
      s.soft += model.metrics.unit_tests_passed ?? 0;
    });
  });

  const labels = Object.keys(stats);
  const hardData = labels.map(name => stats[name].total > 0 ? Math.round((stats[name].hard / stats[name].total) * 100) : 0);
  const softData = labels.map(name => stats[name].total > 0 ? (stats[name].soft / stats[name].total) * 100 : 0);

  return {
    type: 'bar',
    xlabel: 'Model',
    ylabel: 'Percentage (%)',
    labels,
    datasets: [
      { label: t ? t('chartLabels.matchComparison.formatMatch') : 'Format Match', data: hardData, color: '#10b981' },
      { label: t ? t('chartLabels.matchComparison.semanticMatch') : 'Semantic Match', data: softData, color: '#f59e0b' }
    ]
  };
}

export function getTestOutcomeConfig(data: AnalysisResult[], t: any) {
  const stats: Record<string, { total: number; perfect: number; equivalent: number; failed: number }> = {};
  data.forEach(file => {
    file.models.forEach(model => {
      if (!stats[model.model_name]) {
        stats[model.model_name] = { total: 0, perfect: 0, equivalent: 0, failed: 0 };
      }
      const s = stats[model.model_name];
      const total = model.metrics.unit_tests_total ?? 0;
      const semantic = model.metrics.unit_tests_passed ?? 0;
      const format = model.metrics.format_match_passed ?? 0;
      
      s.total += total;
      s.perfect += format;
      s.equivalent += Math.max(0, semantic - format);
      s.failed += Math.max(0, total - semantic);
    });
  });

  const labels = Object.keys(stats);
  const perfectData = labels.map(name => stats[name].total > 0 ? (stats[name].perfect / stats[name].total) * 100 : 0);
  const equivData = labels.map(name => stats[name].total > 0 ? (stats[name].equivalent / stats[name].total) * 100 : 0);
  const failData = labels.map(name => stats[name].total > 0 ? (stats[name].failed / stats[name].total) * 100 : 0);

  return {
    type: 'stacked_bar_h',
    xlabel: 'Percentage (%)',
    ylabel: 'Model',
    labels,
    datasets: [
      { label: t ? t('chartLabels.testOutcome.perfectMatch') : 'Perfect Match', data: perfectData, color: '#10b981' },
      { label: t ? t('chartLabels.testOutcome.equivalent') : 'Equivalent', data: equivData, color: '#6366f1' },
      { label: t ? t('chartLabels.testOutcome.failed') : 'Failed', data: failData, color: '#ef4444' }
    ]
  };
}


export function getPylintScatterConfig(data: AnalysisResult[], t: any) {
  const modelPoints: Record<string, any[]> = {};
  const modelColors: Record<string, string> = {};
  const PALETTE = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#06b6d4'];
  let colorIdx = 0;

  data.forEach(file => {
    file.models.forEach(m => {
      if (!modelPoints[m.model_name]) {
        modelPoints[m.model_name] = [];
        modelColors[m.model_name] = PALETTE[colorIdx++ % PALETTE.length];
      }
      const total = m.metrics.unit_tests_total ?? 0;
      const formatPct = total > 0 ? Math.round(((m.metrics.format_match_passed ?? 0) / total) * 100) : 0;
      
      modelPoints[m.model_name].push({
        x: m.metrics.pylint_score,
        y: formatPct
      });
    });
  });

  const datasets = Object.keys(modelPoints).map(name => ({
    label: name,
    color: modelColors[name],
    data: modelPoints[name]
  }));

  return {
    type: 'scatter',
    xlabel: t ? t('chartLabels.pylintScatter.pylintScore') : 'Pylint Score',
    ylabel: t ? t('chartLabels.pylintScatter.formatMatch') : 'Format Match %',
    xlim: [-0.5, 10.5],
    ylim: [-5, 105],
    datasets
  };
}

export function getComplexityConfig(data: AnalysisResult[], t: any) {
  const modelStats: Record<string, { complexity: number; count: number }> = {};
  data.forEach(file => {
    file.models.forEach(model => {
      if (!modelStats[model.model_name]) {
        modelStats[model.model_name] = { complexity: 0, count: 0 };
      }
      modelStats[model.model_name].complexity += model.metrics.complexity_reduction_pct;
      modelStats[model.model_name].count += 1;
    });
  });

  const labels = Object.keys(modelStats);
  const values = labels.map(name => (modelStats[name].complexity / modelStats[name].count));
  const PALETTE = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#06b6d4'];
  const colors = labels.map((_, i) => PALETTE[i % PALETTE.length]);

  return {
    type: 'bar',
    xlabel: 'Model',
    ylabel: t ? t('chartLabels.complexity.reduction') : 'Reduction %',
    labels,
    datasets: [{ label: 'Complexity Reduction', data: values, colors }],
    showLegend: false
  };
}

export function getMaintainabilityConfig(data: AnalysisResult[], t: any) {
  const stats: Record<string, { halsteadSum: number; ccRedSum: number; count: number }> = {};
  data.forEach(file => {
    file.models.forEach(model => {
      if (!stats[model.model_name]) {
        stats[model.model_name] = { halsteadSum: 0, ccRedSum: 0, count: 0 };
      }
      stats[model.model_name].halsteadSum += model.metrics.halstead_effort ?? 0;
      stats[model.model_name].ccRedSum += model.metrics.complexity_reduction_pct ?? 0;
      stats[model.model_name].count++;
    });
  });

  const labels = Object.keys(stats);
  const halsteadData = labels.map(name => stats[name].count > 0 ? Math.round(stats[name].halsteadSum / stats[name].count) : 0);
  // Note: Python script doesn't support multiple Y-axes easily in this generic way yet, 
  // but we can export the primary metric (Halstead) or just export as multiple series.
  return {
    type: 'bar',
    xlabel: 'Model',
    ylabel: 'Value',
    labels,
    datasets: [
      { label: t ? t('chartLabels.maintainability.avgHalstead') : 'Avg Halstead Effort', data: halsteadData, color: '#6366f1' }
    ]
  };
}

export function getExecutionVsSizeConfig(data: AnalysisResult[], t: any) {
  const modelPoints: Record<string, any[]> = {};
  const PALETTE = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#06b6d4'];
  let colorIdx = 0;

  data.forEach(file => {
    file.models.forEach(m => {
      if (!modelPoints[m.model_name]) {
        modelPoints[m.model_name] = [];
      }
      const loc = m.metrics.loc_ratio ?? null;
      const exec = m.metrics.exec_time_python_avg_ms ?? null;
      if (loc !== null && exec !== null) {
        modelPoints[m.model_name].push({ x: loc, y: exec });
      }
    });
  });

  const datasets = Object.keys(modelPoints).map((name, i) => ({
    label: name,
    color: PALETTE[i % PALETTE.length],
    data: modelPoints[name]
  }));

  return {
    type: 'scatter',
    xlabel: t ? t('chartLabels.execVsSize.locRatio') : 'LoC Ratio',
    ylabel: t ? t('chartLabels.execVsSize.execTime') : 'Exec Time (ms)',
    datasets
  };
}

export function getErrorPatternConfig(data: AnalysisResult[], t: any) {
  const buckets: Record<string, number> = {
    [t('chartLabels.errorPattern.signError')]: 0,
    [t('chartLabels.errorPattern.whitespace')]: 0,
    [t('chartLabels.errorPattern.logicError')]: 0,
    [t('chartLabels.errorPattern.crash')]: 0,
  };

  data.forEach(file => {
    file.models.forEach(m => {
      m.test_results?.forEach(test => {
        if (!test.semantic_match) {
          const type = test.failure_category;
          if (type === 'sign_error') buckets[t('chartLabels.errorPattern.signError')]++;
          else if (type === 'whitespace') buckets[t('chartLabels.errorPattern.whitespace')]++;
          else if (type === 'logic') buckets[t('chartLabels.errorPattern.logicError')]++;
          else if (type === 'crash') buckets[t('chartLabels.errorPattern.crash')]++;
        }
      });
    });
  });

  const labels = Object.keys(buckets);
  const values = labels.map(l => buckets[l]);
  const colors = ['#f59e0b', '#6366f1', '#ec4899', '#ef4444']; // matching CATEGORY_META order

  return {
    type: 'pie',
    labels,
    datasets: [{ label: 'Error Patterns', data: values, colors }],
    showLegend: false
  };
}

export function getConsensusFailureConfig(data: AnalysisResult[], t: any) {
  const modelCount = new Set(data.flatMap(f => f.models.map(m => m.model_name))).size;
  const buckets: Record<string, number> = { 
    [t('chartLabels.consensusFailure.allPass')]: 0, 
    [t('chartLabels.consensusFailure.oneModel')]: 0, 
    [t('chartLabels.consensusFailure.twoThreeModels')]: 0, 
    [t('chartLabels.consensusFailure.allModels')]: 0 
  };

  data.forEach(file => {
    const maxTests = Math.max(...file.models.map(m => m.test_results?.length ?? 0));
    for (let i = 0; i < maxTests; i++) {
      let failCount = 0;
      file.models.forEach(m => {
        const tr = m.test_results?.[i];
        if (tr && !tr.semantic_match) failCount++;
      });
      if (failCount === 0)             buckets[t('chartLabels.consensusFailure.allPass')]++;
      else if (failCount === 1)        buckets[t('chartLabels.consensusFailure.oneModel')]++;
      else if (failCount < modelCount) buckets[t('chartLabels.consensusFailure.twoThreeModels')]++;
      else                             buckets[t('chartLabels.consensusFailure.allModels')]++;
    }
  });

  const labels = Object.keys(buckets);
  const values = labels.map(l => buckets[l]);
  const colors = ['#10b981', '#f59e0b', '#f97316', '#ef4444'];

  return {
    type: 'bar',
    xlabel: 'Failure Level',
    ylabel: 'Count',
    labels,
    datasets: [{ label: 'Consensus Failures', data: values, colors }],
    showLegend: false
  };
}

export function getHardSoftDeltaConfig(data: AnalysisResult[], t: any) {
  const stats: Record<string, { hard: number; soft: number; total: number }> = {};
  data.forEach(file => {
    file.models.forEach(model => {
      if (!stats[model.model_name]) {
        stats[model.model_name] = { hard: 0, soft: 0, total: 0 };
      }
      const s = stats[model.model_name];
      const total = model.metrics.unit_tests_total ?? 0;
      s.total += total;
      s.hard += model.metrics.format_match_passed ?? 0;
      s.soft += model.metrics.unit_tests_passed ?? 0;
    });
  });

  const labels = Object.keys(stats);
  const hardData = labels.map(name => stats[name].total > 0 ? (stats[name].hard / stats[name].total) * 100 : 0);
  const softData = labels.map(name => stats[name].total > 0 ? (stats[name].soft / stats[name].total) * 100 : 0);
  const gapData = labels.map((_, i) => softData[i] - hardData[i]);

  return {
    type: 'bar',
    xlabel: 'Model',
    ylabel: 'Percentage (%)',
    labels,
    datasets: [
      { label: 'Format Match', data: hardData, color: '#10b981' },
      { label: 'Semantic Match', data: softData, color: '#f59e0b' },
      { label: 'Gap', data: gapData, color: '#6366f1' }
    ]
  };
}

export function getRadarConfig(data: AnalysisResult[], t: any) {
  const modelStats: Record<string, { pylint: number; complexity: number; pass: number; count: number }> = {};
  const PALETTE = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#06b6d4'];

  data.forEach(file => {
    file.models.forEach(model => {
      if (!modelStats[model.model_name]) {
        modelStats[model.model_name] = { pylint: 0, complexity: 0, pass: 0, count: 0 };
      }
      const stats = modelStats[model.model_name];
      stats.pylint += model.metrics.pylint_score;
      stats.complexity += model.metrics.complexity_reduction_pct;
      const passed = model.metrics.unit_tests_passed ?? (model.metrics.pass_at_1 ? 1 : 0);
      const total = model.metrics.unit_tests_total ?? 1;
      stats.pass += total > 0 ? passed / total : 0;
      stats.count += 1;
    });
  });

  const labels = [
    t ? t('modelComparison.pylint') : 'Pylint',
    t ? t('modelComparison.complexity') : 'Complexity',
    t ? t('modelComparison.passRate') : 'Pass Rate'
  ];

  const modelKeys = Object.keys(modelStats);
  const datasets = modelKeys.map((model, i) => {
    const stats = modelStats[model];
    const pylintVal = (stats.pylint / stats.count) * 10;
    const complexityVal = stats.complexity / stats.count;
    const passVal = (stats.pass / stats.count) * 100;
    return {
      label: model,
      color: PALETTE[i % PALETTE.length],
      data: [pylintVal, complexityVal, passVal]
    };
  });

  return {
    type: 'radar',
    labels,
    datasets
  };
}

export function getBoundaryFaithfulnessConfig(data: AnalysisResult[], t: any) {
  const modelStats: Record<string, { faithful: number; unfaithful: number; crashed: number; total: number }> = {};
  
  data.forEach(file => {
    file.models.forEach(model => {
      const invalids = (model as any).invalid_test_results as any[] | undefined;
      if (!invalids || invalids.length === 0) return;

      if (!modelStats[model.model_name]) {
        modelStats[model.model_name] = { faithful: 0, unfaithful: 0, crashed: 0, total: 0 };
      }
      const ms = modelStats[model.model_name];
      invalids.forEach((r: any) => {
        ms.total++;
        if (r.cobol_faithful) ms.faithful++;
        else if (r.python_crashed) ms.crashed++;
        else ms.unfaithful++;
      });
    });
  });

  const labels = Object.keys(modelStats);
  const faithfulData = labels.map(n => modelStats[n].total > 0 ? (modelStats[n].faithful / modelStats[n].total) * 100 : 0);
  const unfaithfulData = labels.map(n => modelStats[n].total > 0 ? (modelStats[n].unfaithful / modelStats[n].total) * 100 : 0);
  const crashedData = labels.map(n => modelStats[n].total > 0 ? (modelStats[n].crashed / modelStats[n].total) * 100 : 0);

  return {
    type: 'stacked_bar_h',
    xlabel: 'Percentage (%)',
    ylabel: 'Model',
    labels,
    datasets: [
      { label: t ? t('chartLabels.boundaryFaithfulness.faithful') : 'Faithful', data: faithfulData, color: '#10b981' },
      { label: t ? t('chartLabels.boundaryFaithfulness.unfaithful') : 'Unfaithful', data: unfaithfulData, color: '#f59e0b' },
      { label: t ? t('chartLabels.boundaryFaithfulness.crashed') : 'Crashed', data: crashedData, color: '#ef4444' }
    ]
  };
}

export function getTokenUsageConfig(usage: LlmUsageEntry[], t?: (key: string) => string) {
  const taskLabels: Record<string, string> = {
    translation: 'Translation',
    python_to_cobol_inputs: 'Python-to-COBOL Inputs',
    boundary_test_generation: 'Boundary Tests',
    input_generation: 'Forward Inputs',
    executive_summary: 'Executive Summary'
  };

  const order = [
    'translation',
    'python_to_cobol_inputs',
    'boundary_test_generation',
    'input_generation',
    'executive_summary'
  ];

  const stats: Record<string, { prompt: number; completion: number }> = {};
  usage.forEach(entry => {
    if (!stats[entry.type]) {
      stats[entry.type] = { prompt: 0, completion: 0 };
    }
    stats[entry.type].prompt += entry.prompt_tokens ?? 0;
    stats[entry.type].completion += entry.completion_tokens ?? 0;
  });

  const labels = order.filter(type => stats[type]).map(type => taskLabels[type] ?? type);
  const promptData = order.filter(type => stats[type]).map(type => stats[type].prompt / 1000);
  const completionData = order.filter(type => stats[type]).map(type => stats[type].completion / 1000);

  return {
    type: 'stacked_bar_h',
    xlabel: t ? t('chartLabels.tokenCost.tokensThousands') : 'Tokens (thousands)',
    ylabel: 'Pipeline Task',
    labels,
    datasets: [
      { label: t ? t('chartLabels.tokenCost.promptTokens') : 'Prompt Tokens', data: promptData, color: '#6366f1' },
      { label: t ? t('chartLabels.tokenCost.completionTokens') : 'Completion Tokens', data: completionData, color: '#ec4899' }
    ],
    valueFormat: 'number',
    valueSuffix: 'k'
  };
}
