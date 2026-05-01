'use client';

import React from 'react';
import {
  ScatterChart, Scatter, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, Legend
} from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './ModelComparison.module.css';

interface Props { data: AnalysisResult[]; }

const MODEL_COLORS: Record<string, string> = {};
const PALETTE = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#06b6d4']; // Premium palette

export default function ExecutionVsSizeChart({ data }: Props) {
  const { t } = useTranslation();
  let colorIdx = 0;

  // Flatten and filter: we need points that have both loc_ratio and exec_time
  const scatterData = data.flatMap(file => 
    file.models.map(m => {
      const loc = m.metrics.loc_ratio ?? null;
      const exec = m.metrics.exec_time_python_avg_ms ?? null;
      if (loc === null || exec === null) return null;

      if (!MODEL_COLORS[m.model_name]) {
        MODEL_COLORS[m.model_name] = PALETTE[colorIdx % PALETTE.length];
        colorIdx++;
      }

      return {
        model: m.model_name,
        file: file.source_file.replace(/\.(cbl|cob)$/i, ''),
        x: loc,     // LoC Ratio
        y: exec,    // Execution Time
        color: MODEL_COLORS[m.model_name],
      };
    }).filter(d => d !== null)
  );

  // Group by model for the Legend to work with multiple Scatters
  const groupedByModel = scatterData.reduce((acc, curr) => {
    if (!acc[curr!.model]) acc[curr!.model] = [];
    acc[curr!.model].push(curr);
    return acc;
  }, {} as Record<string, any[]>);

  const CustomTooltip = ({ active, payload }: any) => {
    if (!active || !payload?.length) return null;
    const d = payload[0].payload;
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
        <div style={{ fontWeight: 700, color: d.color, marginBottom: '0.25rem' }}>{d.model}</div>
        <div style={{ color: 'var(--text-secondary)', marginBottom: '0.5rem', fontSize: '0.78rem' }}>{d.file}</div>
        <div>{t('chartLabels.execVsSize.locRatio')}: <b style={{ color: '#fff' }}>{d.x.toFixed(2)}x</b></div>
        <div>{t('chartLabels.execVsSize.execTime')}: <b style={{ color: '#fff' }}>{d.y.toFixed(0)} ms</b></div>
      </div>
    );
  };

  return (
    <div className={styles.chartContainer}>
      <h3 className={styles.title}>{t('charts.executionVsSizeChart')}</h3>
      <p className={styles.subtitle}>{t('chartLabels.execVsSize.subtitle')}</p>
      <ResponsiveContainer width="100%" height="85%">
        <ScatterChart margin={{ top: 10, right: 30, bottom: 5, left: -20 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" opacity={0.5} />
          <XAxis 
            type="number" 
            dataKey="x" 
            name={t('chartLabels.execVsSize.locRatio')} 
            tick={{ fill: 'var(--text-secondary)', fontSize: 11 }}
            axisLine={false}
            tickLine={false}
            dy={5}
            domain={['auto', 'auto']}
            tickFormatter={(v) => `${v.toFixed(1)}x`}
          />
          <YAxis 
            type="number" 
            dataKey="y" 
            name={t('chartLabels.execVsSize.execTime')} 
            tick={{ fill: 'var(--text-secondary)', fontSize: 11 }}
            axisLine={false}
            tickLine={false}
            dx={-5}
            tickFormatter={(v) => `${v}ms`}
          />
          <Tooltip content={<CustomTooltip />} cursor={{ strokeDasharray: '3 3', stroke: 'var(--text-secondary)', opacity: 0.5 }} />
          <Legend wrapperStyle={{ color: 'var(--text)', fontSize: '0.8rem', paddingTop: '0.5rem' }} verticalAlign="top"/>
          {Object.keys(groupedByModel).map(modelName => (
            <Scatter 
              key={modelName}
              name={modelName} 
              data={groupedByModel[modelName]} 
              fill={MODEL_COLORS[modelName]} 
              opacity={0.8}
            />
          ))}
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
}
