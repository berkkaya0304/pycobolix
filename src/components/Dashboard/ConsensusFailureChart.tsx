'use client';

import React from 'react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, Cell,
} from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './FileDifficultyChart.module.css';

interface Props { data: AnalysisResult[]; }

/**
 * Consensus Failure Analysis:
 * For each COBOL file + test-case index, count how many models failed it.
 * Bucket into: nobody failed, 1 model failed, 2+ failed, all failed.
 */
export default function ConsensusFailureChart({ data }: Props) {
  const { t } = useTranslation();
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
        const t = m.test_results?.[i];
        if (t && !t.semantic_match) failCount++;
      });
      if (failCount === 0)             buckets[t('chartLabels.consensusFailure.allPass')]++;
      else if (failCount === 1)        buckets[t('chartLabels.consensusFailure.oneModel')]++;
      else if (failCount < modelCount) buckets[t('chartLabels.consensusFailure.twoThreeModels')]++;
      else                             buckets[t('chartLabels.consensusFailure.allModels')]++;
    }
  });

  const chartData = Object.entries(buckets).map(([name, count]) => ({ name, count }));
  const COLORS = ['#10b981', '#f59e0b', '#f97316', '#ef4444']; // emerald, amber, orange, red for severity

  const total = chartData.reduce((a, b) => a + b.count, 0);

  return (
    <div className={styles.chartContainer}>
      <h3 className={styles.title}>{t('charts.consensusFailureChart')}</h3>
      <p className={styles.subtitle}>{t('chartLabels.consensusFailure.subtitle')}</p>
      <ResponsiveContainer width="100%" height="85%">
        <BarChart data={chartData} margin={{ top: 10, right: 10, left: -20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" vertical={false} opacity={0.5} />
          <XAxis dataKey="name" tick={{ fill: 'var(--text-secondary)', fontSize: 11, fontWeight: 500 }} axisLine={false} tickLine={false} dy={5} />
          <YAxis tick={{ fill: 'var(--text-secondary)', fontSize: 11 }} axisLine={false} tickLine={false} />
          <Tooltip
            contentStyle={{ 
              backgroundColor: 'rgba(15, 23, 42, 0.85)', 
              backdropFilter: 'blur(8px)',
              borderColor: 'var(--border)', 
              color: 'var(--text)',
              borderRadius: '8px',
              boxShadow: '0 8px 20px rgba(0,0,0,0.2)'
            }}
            itemStyle={{ color: '#fff', fontWeight: 600 }}
            cursor={{ fill: 'var(--border)', opacity: 0.1 }}
            formatter={(v: any) => [`${v} ${t('chartLabels.errorPattern.tests')} (${total > 0 ? Math.round((v / total) * 100) : 0}%)`, t('chartLabels.consensusFailure.count')]}
          />
          <Bar dataKey="count" radius={[6, 6, 0, 0]}>
            {chartData.map((_, i) => (
              <Cell key={i} fill={COLORS[i % COLORS.length]} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
