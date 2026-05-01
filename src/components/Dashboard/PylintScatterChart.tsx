'use client';

import React from 'react';
import {
  ScatterChart, Scatter, XAxis, YAxis, CartesianGrid,
  Tooltip, ResponsiveContainer, Label, ZAxis,
} from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './FileDifficultyChart.module.css'; // reuse container styles

interface Props { data: AnalysisResult[]; }

const MODEL_COLORS: Record<string, string> = {};
const PALETTE = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#06b6d4']; // Premium palette

export default function PylintScatterChart({ data }: Props) {
  const { t } = useTranslation();
  let colorIdx = 0;

  const points = data.flatMap(file =>
    file.models.map(m => {
      const total = m.metrics.unit_tests_total ?? 0;
      const formatPct = total > 0 ? Math.round(((m.metrics.format_match_passed ?? 0) / total) * 100) : 0;
      if (!MODEL_COLORS[m.model_name]) {
        MODEL_COLORS[m.model_name] = PALETTE[colorIdx++ % PALETTE.length];
      }
      return {
        model:    m.model_name,
        x:        m.metrics.pylint_score,
        y:        formatPct,
        file:     file.source_file,
        color:    MODEL_COLORS[m.model_name],
      };
    })
  );

  const models = [...new Set(points.map(p => p.model))];

  const CustomDot = (props: any) => {
    const { cx, cy, payload } = props;
    return <circle cx={cx} cy={cy} r={6} fill={payload.color} fillOpacity={0.85} stroke="none" />;
  };

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
        <div>Pylint: <b style={{ color: '#fff' }}>{d.x.toFixed(1)}</b></div>
        <div>{t('chartLabels.pylintScatter.formatMatch')}: <b style={{ color: '#fff' }}>{d.y}%</b></div>
      </div>
    );
  };

  return (
    <div className={styles.chartContainer}>
      <h3 className={styles.title}>{t('charts.pylintScatterChart')}</h3>
      <p className={styles.subtitle}>{t('chartLabels.pylintScatter.subtitle')}</p>
      {/* Legend */}
      <div style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap', marginBottom: '0.5rem' }}>
        {models.map(m => (
          <span key={m} style={{ fontSize: '0.75rem', color: MODEL_COLORS[m], display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
            <span style={{ display: 'inline-block', width: 10, height: 10, borderRadius: '50%', background: MODEL_COLORS[m] }} />
            {m}
          </span>
        ))}
      </div>
      <ResponsiveContainer width="100%" height="85%">
        <ScatterChart margin={{ top: 10, right: 20, left: 10, bottom: 30 }}>
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" />
          <XAxis type="number" dataKey="x" domain={[0, 10]} tick={{ fill: 'var(--text-secondary)', fontSize: 11 }}>
            <Label value={t('chartLabels.pylintScatter.pylintScore')} offset={-10} position="insideBottom" fill="var(--text-secondary)" fontSize={11} />
          </XAxis>
          <YAxis type="number" dataKey="y" domain={[0, 100]} unit="%" tick={{ fill: 'var(--text-secondary)', fontSize: 11 }}>
            <Label value={t('chartLabels.pylintScatter.formatMatch')} angle={-90} position="insideLeft" fill="var(--text-secondary)" fontSize={11} />
          </YAxis>
          <ZAxis range={[60, 60]} />
          <Tooltip content={<CustomTooltip />} />
          <Scatter data={points} shape={<CustomDot />} />
        </ScatterChart>
      </ResponsiveContainer>
    </div>
  );
}
