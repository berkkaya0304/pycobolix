'use client';

import React from 'react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, Legend, ResponsiveContainer, Cell
} from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './ModelComparison.module.css';

interface Props { data: AnalysisResult[]; }

export default function TestOutcomeDistributionChart({ data }: Props) {
  const { t } = useTranslation();
  // Aggregate outcomes per model
  const stats: Record<string, { total: number; perfect: number; equivalent: number; failed: number }> = {};

  data.forEach(file => {
    file.models.forEach(model => {
      if (!stats[model.model_name]) {
        stats[model.model_name] = { total: 0, perfect: 0, equivalent: 0, failed: 0 };
      }
      const s = stats[model.model_name];
      const t = model.metrics.unit_tests_total ?? 0;
      const semantic = model.metrics.unit_tests_passed ?? 0;
      const format = model.metrics.format_match_passed ?? 0;
      
      s.total += t;
      s.perfect += format;
      s.equivalent += Math.max(0, semantic - format);
      s.failed += Math.max(0, t - semantic);
    });
  });

  const chartData = Object.entries(stats).map(([name, s]) => {
    return {
      name,
      [t('chartLabels.testOutcome.perfectMatch')]: s.total > 0 ? (s.perfect / s.total) * 100 : 0,
      [t('chartLabels.testOutcome.equivalent')]: s.total > 0 ? (s.equivalent / s.total) * 100 : 0,
      [t('chartLabels.testOutcome.failed')]: s.total > 0 ? (s.failed / s.total) * 100 : 0,
    };
  });

  const CustomTooltip = ({ active, payload, label }: any) => {
    if (!active || !payload?.length) return null;
    return (
      <div style={{ 
        background: 'rgba(15, 23, 42, 0.85)', 
        backdropFilter: 'blur(8px)',
        border: '1px solid var(--border)', 
        borderRadius: 8, 
        padding: '0.75rem 1rem', 
        fontSize: '0.85rem', 
        color: 'var(--text)',
        boxShadow: '0 8px 20px rgba(0,0,0,0.2)'
      }}>
        <div style={{ fontWeight: 700, marginBottom: '0.4rem', color: 'var(--text-secondary)' }}>{label}</div>
        {payload.map((p: any) => (
          <div key={p.name} style={{ color: p.color, fontWeight: 500, marginBottom: '0.2rem' }}>
            {p.name}: <b style={{ color: '#fff' }}>{p.value.toFixed(1)}%</b>
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className={styles.chartContainer}>
      <h3 className={styles.title}>{t('charts.testOutcomeDistributionChart')}</h3>
      <p className={styles.subtitle}>{t('chartLabels.testOutcome.subtitle')}</p>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart 
          data={chartData} 
          layout="vertical"
          margin={{ top: 10, right: 30, left: 10, bottom: 5 }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" horizontal={false} opacity={0.5} />
          <XAxis 
            type="number" 
            domain={[0, 100]} 
            tick={{ fill: 'var(--text-secondary)', fontSize: 11 }}
            axisLine={false} 
            tickLine={false} 
            tickFormatter={(v) => `${v}%`}
          />
          <YAxis 
            type="category" 
            dataKey="name" 
            tick={{ fill: 'var(--text-secondary)', fontSize: 11, fontWeight: 500 }} 
            axisLine={false} 
            tickLine={false} 
            width={100}
          />
          <Tooltip content={<CustomTooltip />} cursor={{ fill: 'var(--border)', opacity: 0.1 }} />
          <Legend wrapperStyle={{ color: 'var(--text)', fontSize: '0.8rem', paddingTop: '0.5rem' }} />
          
          <Bar dataKey={t('chartLabels.testOutcome.perfectMatch')} stackId="a" fill="#10b981" radius={[0, 0, 0, 0]} />
          <Bar dataKey={t('chartLabels.testOutcome.equivalent')} stackId="a" fill="#6366f1" radius={[0, 0, 0, 0]} />
          <Bar dataKey={t('chartLabels.testOutcome.failed')} stackId="a" fill="#ef4444" radius={[0, 4, 4, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
