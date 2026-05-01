'use client';

import React from 'react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, Legend, ResponsiveContainer, ReferenceLine,
} from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './FileDifficultyChart.module.css';

interface Props { data: AnalysisResult[]; }

export default function HardSoftDeltaChart({ data }: Props) {
  const { t } = useTranslation();
  const allModels = [...new Set(data.flatMap(f => f.models.map(m => m.model_name)))];

  const byModel: Record<string, { hard: number[]; soft: number[] }> = {};
  data.forEach(file => {
    file.models.forEach(m => {
      const total = m.metrics.unit_tests_total ?? 0;
      if (!byModel[m.model_name]) byModel[m.model_name] = { hard: [], soft: [] };
      byModel[m.model_name].hard.push(total > 0 ? Math.round(((m.metrics.format_match_passed ?? 0) / total) * 100) : 0);
      byModel[m.model_name].soft.push(total > 0 ? Math.round(((m.metrics.unit_tests_passed ?? 0) / total) * 100) : 0);
    });
  });

  const avg = (arr: number[]) => arr.length ? Math.round(arr.reduce((a, b) => a + b, 0) / arr.length) : 0;

  const chartData = allModels.map(model => {
    const s = byModel[model];
    const hardAvg = avg(s.hard);
    const softAvg = avg(s.soft);
    return {
      model,
      [t('chartLabels.hardSoftDelta.formatMatch')]:  hardAvg,
      [t('chartLabels.hardSoftDelta.semanticMatch')]:  softAvg,
      [t('chartLabels.hardSoftDelta.formatGap')]:  softAvg - hardAvg,   // positive = soft >> hard → formatting issues
    };
  });

  const CustomTooltip = ({ active, payload, label }: any) => {
    if (!active || !payload?.length) return null;
    return (
      <div style={{ background: 'var(--surface)', border: '1px solid var(--border)', borderRadius: 8, padding: '0.5rem 0.75rem', fontSize: '0.8rem', color: 'var(--text)' }}>
        <div style={{ fontWeight: 700, marginBottom: '0.25rem' }}>{label}</div>
        {payload.map((p: any) => (
          <div key={p.name} style={{ color: p.color }}>{p.name}: <b>{p.value}%</b></div>
        ))}
      </div>
    );
  };

  return (
    <div className={styles.chartContainer}>
      <h3 className={styles.title}>{t('charts.hardSoftDeltaChart')}</h3>
      <p className={styles.subtitle}>{t('chartLabels.hardSoftDelta.subtitle')}</p>
      <ResponsiveContainer width="100%" height="85%">
        <BarChart data={chartData} margin={{ top: 10, right: 30, left: 0, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
          <XAxis dataKey="model" tick={{ fill: 'var(--text-secondary)', fontSize: 11 }} />
          <YAxis domain={[0, 100]} unit="%" tick={{ fill: 'var(--text-secondary)', fontSize: 11 }} />
          <Tooltip content={<CustomTooltip />} />
          <Legend wrapperStyle={{ color: 'var(--text)', fontSize: '0.78rem' }} verticalAlign="top" />
          <Bar dataKey={t('chartLabels.hardSoftDelta.formatMatch')}  fill="#22c55e" radius={[3, 3, 0, 0]} />
          <Bar dataKey={t('chartLabels.hardSoftDelta.semanticMatch')}  fill="#f59e0b" radius={[3, 3, 0, 0]} />
          <Bar dataKey={t('chartLabels.hardSoftDelta.formatGap')}  fill="#3b82f6" radius={[3, 3, 0, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
