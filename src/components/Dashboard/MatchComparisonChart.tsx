'use client';

import React from 'react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './MatchComparisonChart.module.css';

interface Props {
  data: AnalysisResult[];
}

export default function MatchComparisonChart({ data }: Props) {
  const { t } = useTranslation();
  // Aggregate per-model: hard / numeric / soft match pass rates
  const stats: Record<string, { hard: number; soft: number; total: number }> = {};

  data.forEach(file => {
    file.models.forEach(model => {
      if (!stats[model.model_name]) {
        stats[model.model_name] = { hard: 0, soft: 0, total: 0 };
      }
      const s = stats[model.model_name];
      const total = model.metrics.unit_tests_total ?? 0;
      s.total += total;
      s.hard    += model.metrics.format_match_passed    ?? 0;
      s.soft    += model.metrics.unit_tests_passed    ?? 0;
    });
  });

  const chartData = Object.entries(stats).map(([name, s]) => ({
    name,
    [t('chartLabels.matchComparison.formatMatch')]:    s.total > 0 ? Math.round((s.hard    / s.total) * 100) : 0,
    [t('chartLabels.matchComparison.semanticMatch')]:    s.total > 0 ? Math.round((s.soft    / s.total) * 100) : 0,
  }));

  const tooltipStyle = {
    contentStyle: { 
      backgroundColor: 'rgba(15, 23, 42, 0.85)', 
      backdropFilter: 'blur(8px)',
      borderColor: 'var(--border)', 
      color: 'var(--text)',
      borderRadius: '8px',
      boxShadow: '0 8px 20px rgba(0,0,0,0.2)'
    },
    itemStyle: { color: '#fff', fontWeight: 500 },
    labelStyle: { color: 'var(--text-secondary)', fontWeight: 700, marginBottom: '0.4rem' },
    cursor: { fill: 'var(--border)', opacity: 0.1 },
  };

  return (
    <div className={styles.chartContainer}>
      <h3 className={styles.title}>{t('charts.matchComparisonChart')}</h3>
      <div className={styles.legend}>
        <span className={styles.legendHard}>{t('chartLabels.matchComparison.hardDesc')}</span>
        <span className={styles.legendSoft}>{t('chartLabels.matchComparison.softDesc')}</span>
      </div>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={chartData} margin={{ top: 10, right: 10, left: -20, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" vertical={false} opacity={0.5} />
          <XAxis dataKey="name" tick={{ fill: 'var(--text-secondary)', fontSize: 12, fontWeight: 500 }} axisLine={false} tickLine={false} dy={10} />
          <YAxis domain={[0, 100]} unit="%" tick={{ fill: 'var(--text-secondary)', fontSize: 11 }} axisLine={false} tickLine={false} />
          <Tooltip {...tooltipStyle} />
          <Legend wrapperStyle={{ color: 'var(--text)', fontSize: '0.8rem', paddingTop: '1rem' }} />
          <Bar dataKey={t('chartLabels.matchComparison.formatMatch')}    fill="#10b981" radius={[6,6,0,0]} />
          <Bar dataKey={t('chartLabels.matchComparison.semanticMatch')}    fill="#f59e0b" radius={[6,6,0,0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
