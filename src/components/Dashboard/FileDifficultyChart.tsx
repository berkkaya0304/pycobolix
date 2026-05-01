'use client';

import React from 'react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, Legend, ResponsiveContainer, Cell,
} from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './FileDifficultyChart.module.css';

interface Props { data: AnalysisResult[]; }

/** Builds one bar per (file, model) group showing hard match % */
export default function FileDifficultyChart({ data }: Props) {
  const { t } = useTranslation();
  // Unique model names
  const models = [...new Set(data.flatMap(f => f.models.map(m => m.model_name)))];

  const chartData = data.map(file => {
    const entry: Record<string, string | number> = {
      name: file.source_file.replace(/\.(cbl|cob)$/i, ''),
    };
    file.models.forEach(m => {
      const total = m.metrics.unit_tests_total ?? 0;
      entry[m.model_name] = total > 0
        ? Math.round(((m.metrics.format_match_passed ?? 0) / total) * 100)
        : 0;
    });
    return entry;
  });

  const MODEL_COLORS: Record<string, string> = {};
  const PALETTE = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#06b6d4']; // Premium palette
  models.forEach((m, i) => { MODEL_COLORS[m] = PALETTE[i % PALETTE.length]; });

  return (
    <div className={styles.chartContainer}>
      <h3 className={styles.title}>{t('charts.fileDifficultyChart')}</h3>
      <p className={styles.subtitle}>{t('chartLabels.fileDifficulty.subtitle')}</p>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={chartData} margin={{ top: 10, right: 10, left: -20, bottom: 50 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" vertical={false} opacity={0.5} />
          <XAxis
            dataKey="name"
            tick={{ fill: 'var(--text-secondary)', fontSize: 11, fontWeight: 500 }}
            angle={-35}
            textAnchor="end"
            interval={0}
            axisLine={false}
            tickLine={false}
            dy={5}
          />
          <YAxis
            domain={[0, 100]}
            unit="%"
            tick={{ fill: 'var(--text-secondary)', fontSize: 11 }}
            axisLine={false}
            tickLine={false}
          />
          <Tooltip
            contentStyle={{ 
              backgroundColor: 'rgba(15, 23, 42, 0.85)', 
              backdropFilter: 'blur(8px)',
              borderColor: 'var(--border)', 
              color: 'var(--text)',
              borderRadius: '8px',
              boxShadow: '0 8px 20px rgba(0,0,0,0.2)'
            }}
            itemStyle={{ color: '#fff', fontWeight: 500 }}
            labelStyle={{ color: 'var(--text-secondary)', fontWeight: 700, marginBottom: '0.4rem' }}
            cursor={{ fill: 'var(--border)', opacity: 0.1 }}
            formatter={(v: any) => `${v}%`}
          />
          <Legend
            wrapperStyle={{ color: 'var(--text)', fontSize: '0.8rem', paddingTop: '0.75rem' }}
            verticalAlign="top"
          />
          {models.map(model => (
            <Bar key={model} dataKey={model} fill={MODEL_COLORS[model]} radius={[4, 4, 0, 0]} />
          ))}
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
