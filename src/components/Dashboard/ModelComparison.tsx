'use client';

import React from 'react';
import {
  Radar,
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  PolarRadiusAxis,
  ResponsiveContainer,
  Legend,
  Tooltip
} from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import styles from './ModelComparison.module.css';
import { useTranslation } from '@/lib/i18n/LanguageContext';

interface ModelComparisonProps {
  data: AnalysisResult[];
}

export default function ModelComparison({ data }: ModelComparisonProps) {
  const { t } = useTranslation();
  // Aggregate data by model
  const modelStats: Record<string, { pylint: number; complexity: number; pass: number; count: number }> = {};

  // Flatten all model results
  data.forEach(file => {
      file.models.forEach(model => {
        if (!modelStats[model.model_name]) {
            modelStats[model.model_name] = { pylint: 0, complexity: 0, pass: 0, count: 0 };
        }
        
        const stats = modelStats[model.model_name];
        stats.pylint += model.metrics.pylint_score;
        stats.complexity += model.metrics.complexity_reduction_pct;
        
        // Calculate pass rate ratio (0.0 to 1.0)
        // If pass_at_1 is boolean, we treat it as 1 or 0? 
        // Previously it was: const passed = item.metrics.unit_tests_passed || 0;
        // The mock data now has unit_tests_passed.
        
        const passed = model.metrics.unit_tests_passed ?? (model.metrics.pass_at_1 ? 1 : 0);
        const total = model.metrics.unit_tests_total ?? 1;
        const ratio = total > 0 ? passed / total : 0;
        
        stats.pass += ratio;
        stats.count += 1;
      });
  });

  const COLORS = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#06b6d4']; // Premium indigo, emerald, amber, pink, cyan

  // TRANSPOSE DATA: Axis = Metric, Series = Model
  // We want 3 axes: Pylint, Complexity, Pass Rate
  const metrics = [
    { name: t('modelComparison.pylint'), key: 'pylint' },
    { name: t('modelComparison.complexity'), key: 'complexity' },
    { name: t('modelComparison.passRate'), key: 'pass' }
  ];

  const modelKeys = Object.keys(modelStats);

  const chartData = metrics.map(metric => {
    const row: any = { subject: metric.name, fullMark: 100 };
    modelKeys.forEach(model => {
       const stats = modelStats[model];
       let value = 0;
       if (metric.key === 'pylint') value = (stats.pylint / stats.count) * 10;
       if (metric.key === 'complexity') value = stats.complexity / stats.count;
       if (metric.key === 'pass') value = (stats.pass / stats.count) * 100;
       row[model] = Math.round(value);
    });
    return row;
  });

  return (
    <div className={styles.chartContainer}>
      <h3 className={styles.title}>{t('modelComparison.title')}</h3>
      <div style={{ flex: 1, minHeight: 0, width: '100%' }}>
        <ResponsiveContainer width="100%" height="100%">
          <RadarChart cx="50%" cy="50%" outerRadius="75%" data={chartData}>
            <PolarGrid stroke="var(--border)" strokeOpacity={0.5} />
            <PolarAngleAxis dataKey="subject" tick={{ fill: 'var(--text-secondary)', fontSize: 12, fontWeight: 600 }} />
            <PolarRadiusAxis angle={30} domain={[0, 100]} tick={{ fill: 'var(--text-secondary)', fontSize: 10 }} axisLine={false} />
            {modelKeys.map((model, index) => (
              <Radar
                key={model}
                name={model}
                dataKey={model}
                stroke={COLORS[index % COLORS.length]}
                strokeWidth={2.5}
                fill={COLORS[index % COLORS.length]}
                fillOpacity={0.35}
              />
            ))}
            <Legend wrapperStyle={{ color: 'var(--text)', paddingTop: '1rem', fontSize: '0.85rem' }} />
            <Tooltip 
              contentStyle={{ 
                backgroundColor: 'rgba(15, 23, 42, 0.85)', 
                backdropFilter: 'blur(8px)',
                borderColor: 'var(--border)', 
                color: 'var(--text)',
                borderRadius: '8px',
                boxShadow: '0 8px 20px rgba(0,0,0,0.2)'
              }}
              itemStyle={{ color: 'var(--text)', fontWeight: 500 }}
              labelStyle={{ color: 'var(--text-secondary)', fontWeight: 700, marginBottom: '0.5rem' }}
            />
          </RadarChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
}
