'use client';

import React from 'react';
import { PieChart, Pie, Cell, Tooltip, Legend, ResponsiveContainer } from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './FileDifficultyChart.module.css';

interface Props { data: AnalysisResult[]; }

const CATEGORY_META: Record<string, { labelKey: any; color: string }> = {
  sign_error: { labelKey: 'chartLabels.errorPattern.signError',  color: '#f59e0b' }, /* amber */
  whitespace: { labelKey: 'chartLabels.errorPattern.whitespace',  color: '#6366f1' }, /* indigo */
  logic:      { labelKey: 'chartLabels.errorPattern.logicError', color: '#ec4899' }, /* pink */
  crash:      { labelKey: 'chartLabels.errorPattern.crash',       color: '#ef4444' }, /* red */
};

export default function ErrorPatternChart({ data }: Props) {
  const { t } = useTranslation();
  const counts: Record<string, number> = { sign_error: 0, whitespace: 0, logic: 0, crash: 0 };

  data.forEach(file => {
    file.models.forEach(m => {
      counts.sign_error  += m.metrics.error_sign      ?? 0;
      counts.whitespace  += m.metrics.error_whitespace ?? 0;
      counts.logic       += m.metrics.error_logic      ?? 0;
      counts.crash       += m.metrics.error_crash      ?? 0;
    });
  });

  const chartData = Object.entries(counts)
    .filter(([, v]) => v > 0)
    .map(([key, value]) => ({
      name:  CATEGORY_META[key] ? t(CATEGORY_META[key].labelKey) : key,
      value,
      color: CATEGORY_META[key]?.color ?? '#888',
    }));

  const total = chartData.reduce((a, b) => a + b.value, 0);

  if (total === 0) {
    return (
      <div className={styles.chartContainer}>
        <h3 className={styles.title}>{t('charts.errorPatternChart')}</h3>
        <p className={styles.subtitle}>{t('chartLabels.errorPattern.noFailures')}</p>
      </div>
    );
  }

  return (
    <div className={styles.chartContainer}>
      <h3 className={styles.title}>{t('charts.errorPatternChart')}</h3>
      <p className={styles.subtitle}>{t('chartLabels.errorPattern.subtitle')}</p>
      <ResponsiveContainer width="100%" height="85%">
        <PieChart>
          <Pie
            data={chartData}
            cx="50%"
            cy="50%"
            innerRadius="50%"
            outerRadius="80%"
            paddingAngle={4}
            dataKey="value"
            label={({ name, percent }) => `${name} ${((percent ?? 0) * 100).toFixed(0)}%`}
            labelLine={false}
            stroke="none"
          >
            {chartData.map((entry, i) => (
              <Cell key={i} fill={entry.color} />
            ))}
          </Pie>
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
            formatter={(v: any) => [`${v} ${t('chartLabels.errorPattern.tests')} (${Math.round((v / total) * 100)}%)`, '']}
          />
          <Legend
            wrapperStyle={{ color: 'var(--text)', fontSize: '0.8rem' }}
            formatter={(value) => value}
          />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}
