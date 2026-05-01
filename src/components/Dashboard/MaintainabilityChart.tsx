'use client';

import React from 'react';
import {
  ComposedChart, Bar, Line, XAxis, YAxis, CartesianGrid,
  Tooltip, Legend, ResponsiveContainer, Cell
} from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './ModelComparison.module.css';

interface Props { data: AnalysisResult[]; }

export default function MaintainabilityChart({ data }: Props) {
  const { t } = useTranslation();
  // Aggregate averages per model
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

  const chartData = Object.entries(stats).map(([name, s]) => ({
    name,
    [t('chartLabels.maintainability.avgHalstead')]: s.count > 0 ? Math.round(s.halsteadSum / s.count) : 0,
    [t('chartLabels.maintainability.ccReduction')]: s.count > 0 ? Math.round(s.ccRedSum / s.count) : 0,
  }));

  const COLORS = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#06b6d4']; // Premium palette

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
        {payload.map((p: any) => {
          const isPct = p.dataKey === t('chartLabels.maintainability.ccReduction');
          return (
            <div key={p.name} style={{ color: p.color, fontWeight: 500, marginBottom: '0.2rem' }}>
              {p.name}: <b style={{ color: '#fff' }}>{isPct ? `${p.value}%` : p.value.toLocaleString()}</b>
            </div>
          );
        })}
      </div>
    );
  };

  return (
    <div className={styles.chartContainer}>
      <h3 className={styles.title}>{t('charts.maintainabilityChart')}</h3>
      <p className={styles.subtitle}>{t('chartLabels.maintainability.subtitle')}</p>
      <ResponsiveContainer width="100%" height="100%">
        <ComposedChart data={chartData} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" vertical={false} opacity={0.5} />
          <XAxis dataKey="name" tick={{ fill: 'var(--text-secondary)', fontSize: 12, fontWeight: 500 }} axisLine={false} tickLine={false} dy={10} />
          
          {/* Left Y Axis for Halstead Effort (numbers in thousands) */}
          <YAxis 
            yAxisId="left" 
            tick={{ fill: 'var(--text-secondary)', fontSize: 11 }} 
            axisLine={false} 
            tickLine={false} 
            dx={-5}
            tickFormatter={(v) => v >= 1000 ? `${(v/1000).toFixed(1)}k` : v}
          />
          {/* Right Y Axis for CC Reduction % */}
          <YAxis 
            yAxisId="right" 
            orientation="right" 
            tick={{ fill: 'var(--text-secondary)', fontSize: 11 }} 
            axisLine={false} 
            tickLine={false} 
            dx={5}
            tickFormatter={(v) => `${v}%`}
          />

          <Tooltip content={<CustomTooltip />} cursor={{ fill: 'var(--border)', opacity: 0.1 }} />
          <Legend wrapperStyle={{ color: 'var(--text)', fontSize: '0.8rem', paddingTop: '1rem' }} />
          
          <Bar yAxisId="left" dataKey={t('chartLabels.maintainability.avgHalstead')} radius={[6, 6, 0, 0]} maxBarSize={60}>
            {chartData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Bar>
          
          <Line 
            yAxisId="right" 
            type="monotone" 
            dataKey={t('chartLabels.maintainability.ccReduction')} 
            stroke="#f59e0b" /* amber */
            strokeWidth={3}
            dot={{ r: 6, fill: '#f59e0b', strokeWidth: 2, stroke: 'var(--surface)' }}
            activeDot={{ r: 8, strokeWidth: 0 }}
          />
        </ComposedChart>
      </ResponsiveContainer>
    </div>
  );
}
