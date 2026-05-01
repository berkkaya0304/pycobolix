'use client';

import React, { useState } from 'react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid,
  Tooltip, Legend, ResponsiveContainer,
} from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './ModelComparison.module.css';

interface Props { data: AnalysisResult[]; }

type Category = 'overflow' | 'sign_error' | 'alpha_to_numeric' | 'boundary_valid';

const CATEGORY_LABELS: Record<Category, any> = {
  overflow:          'chartLabels.boundaryFaithfulness.overflow',
  sign_error:        'chartLabels.boundaryFaithfulness.signError',
  alpha_to_numeric:  'chartLabels.boundaryFaithfulness.alphaNumeric',
  boundary_valid:    'chartLabels.boundaryFaithfulness.boundaryValid',
};

const CATEGORY_COLORS: Record<Category, string> = {
  overflow:         '#f59e0b',
  sign_error:       '#ef4444',
  alpha_to_numeric: '#8b5cf6',
  boundary_valid:   '#10b981',
};

export default function BoundaryFaithfulnessChart({ data }: Props) {
  const { t } = useTranslation();
  const [view, setView] = useState<'model' | 'category'>('model');

  // Aggregate: per-model totals
  const modelStats: Record<string, { faithful: number; unfaithful: number; crashed: number; total: number }> = {};
  // Aggregate: per-category totals
  const catStats: Record<string, { faithful: number; unfaithful: number; crashed: number; total: number }> = {};

  data.forEach(file => {
    file.models.forEach(model => {
      const invalids = (model as any).invalid_test_results as any[] | undefined;
      if (!invalids || invalids.length === 0) return;

      if (!modelStats[model.model_name]) {
        modelStats[model.model_name] = { faithful: 0, unfaithful: 0, crashed: 0, total: 0 };
      }
      const ms = modelStats[model.model_name];

      invalids.forEach((r: any) => {
        ms.total++;
        if (r.cobol_faithful)   ms.faithful++;
        else if (r.python_crashed) ms.crashed++;
        else                    ms.unfaithful++;

        const cat = r.category as Category;
        if (!catStats[cat]) catStats[cat] = { faithful: 0, unfaithful: 0, crashed: 0, total: 0 };
        const cs = catStats[cat];
        cs.total++;
        if (r.cobol_faithful)   cs.faithful++;
        else if (r.python_crashed) cs.crashed++;
        else                    cs.unfaithful++;
      });
    });
  });

  const modelChartData = Object.entries(modelStats).map(([name, s]) => ({
    name,
    [t('chartLabels.boundaryFaithfulness.faithful')]:   s.total > 0 ? Math.round((s.faithful   / s.total) * 100) : 0,
    [t('chartLabels.boundaryFaithfulness.unfaithful')]: s.total > 0 ? Math.round((s.unfaithful / s.total) * 100) : 0,
    [t('chartLabels.boundaryFaithfulness.crashed')]:   s.total > 0 ? Math.round((s.crashed    / s.total) * 100) : 0,
    _total: s.total,
  }));

  const catChartData = Object.entries(catStats).map(([cat, s]) => ({
    name: t(CATEGORY_LABELS[cat as Category]) ?? cat,
    [t('chartLabels.boundaryFaithfulness.faithful')]:   s.total > 0 ? Math.round((s.faithful   / s.total) * 100) : 0,
    [t('chartLabels.boundaryFaithfulness.unfaithful')]: s.total > 0 ? Math.round((s.unfaithful / s.total) * 100) : 0,
    [t('chartLabels.boundaryFaithfulness.crashed')]:   s.total > 0 ? Math.round((s.crashed    / s.total) * 100) : 0,
    _total: s.total,
    _color: CATEGORY_COLORS[cat as Category] ?? '#6366f1',
  }));

  const hasData = modelChartData.some(d => d._total > 0) || catChartData.some(d => d._total > 0);

  const CustomTooltip = ({ active, payload, label }: any) => {
    if (!active || !payload?.length) return null;
    const total = payload[0]?.payload?._total ?? 0;
    return (
      <div style={{
        background: 'rgba(15,23,42,0.9)',
        backdropFilter: 'blur(8px)',
        border: '1px solid var(--border)',
        borderRadius: 8,
        padding: '0.75rem 1rem',
        fontSize: '0.82rem',
        color: 'var(--text)',
        boxShadow: '0 8px 20px rgba(0,0,0,0.25)',
        minWidth: 180,
      }}>
        <div style={{ fontWeight: 700, marginBottom: '0.4rem', color: 'var(--text-secondary)' }}>
          {label} <span style={{ opacity: 0.6, fontWeight: 400 }}>({total} {t('chartLabels.errorPattern.tests')})</span>
        </div>
        {payload.map((p: any) => (
          <div key={p.name} style={{ color: p.fill, fontWeight: 500, marginBottom: '0.2rem', display: 'flex', justifyContent: 'space-between', gap: '1rem' }}>
            <span>{p.name}</span>
            <b style={{ color: '#fff' }}>{p.value}%</b>
          </div>
        ))}
      </div>
    );
  };

  if (!hasData) {
    return (
      <div className={styles.chartContainer}>
        <h3 className={styles.title}>{t('charts.boundaryFaithfulnessChart')}</h3>
        <p className={styles.subtitle} style={{ marginTop: '0.5rem', opacity: 0.6 }}>
          {t('chartLabels.boundaryFaithfulness.noData')}
        </p>
      </div>
    );
  }

  const chartData = view === 'model' ? modelChartData : catChartData;

  return (
    <div className={styles.chartContainer}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', flexWrap: 'wrap', gap: '0.5rem', marginBottom: '0.75rem' }}>
        <div>
          <h3 className={styles.title} style={{ marginBottom: '0.15rem' }}>{t('charts.boundaryFaithfulnessChart')}</h3>
          <p className={styles.subtitle}>
            {t('chartLabels.boundaryFaithfulness.subtitle')}
          </p>
        </div>
        {/* Toggle */}
        <div style={{
          display: 'flex',
          gap: 2,
          background: 'rgba(255,255,255,0.05)',
          borderRadius: 8,
          padding: 3,
          border: '1px solid var(--border)',
          flexShrink: 0,
        }}>
          {(['model', 'category'] as const).map(v => (
            <button
              key={v}
              onClick={() => setView(v)}
              style={{
                padding: '0.3rem 0.75rem',
                borderRadius: 6,
                border: 'none',
                fontSize: '0.78rem',
                fontWeight: 600,
                cursor: 'pointer',
                background: view === v ? 'var(--accent, #6366f1)' : 'transparent',
                color: view === v ? '#fff' : 'var(--text-secondary)',
                transition: 'all 0.2s',
              }}
            >
              {v === 'model' ? t('chartLabels.boundaryFaithfulness.byModel') : t('chartLabels.boundaryFaithfulness.byCategory')}
            </button>
          ))}
        </div>
      </div>

      {/* Summary pills */}
      <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap', marginBottom: '0.75rem' }}>
        {([
          { label: t('chartLabels.boundaryFaithfulness.faithful'), color: '#10b981', key: 'faithful' as const },
          { label: t('chartLabels.boundaryFaithfulness.unfaithful'), color: '#f59e0b', key: 'unfaithful' as const },
          { label: t('chartLabels.boundaryFaithfulness.crashed'), color: '#ef4444', key: 'crashed' as const },
        ]).map(({ label, color, key }) => {
          const total = Object.values(modelStats).reduce((s, m) => s + m.total, 0);
          const count = Object.values(modelStats).reduce((s, m) => s + m[key], 0);
          return (
            <span key={key} style={{
              display: 'inline-flex', alignItems: 'center', gap: '0.35rem',
              padding: '0.25rem 0.6rem',
              borderRadius: 20,
              fontSize: '0.75rem',
              fontWeight: 600,
              background: `${color}22`,
              color,
              border: `1px solid ${color}44`,
            }}>
              <span style={{ width: 7, height: 7, borderRadius: '50%', background: color, display: 'inline-block' }} />
              {label}: {total > 0 ? Math.round((count / total) * 100) : 0}%
            </span>
          );
        })}
      </div>

      <ResponsiveContainer width="100%" height={220}>
        <BarChart
          data={chartData}
          layout="vertical"
          margin={{ top: 4, right: 30, left: 10, bottom: 4 }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" horizontal={false} opacity={0.4} />
          <XAxis
            type="number"
            domain={[0, 100]}
            tick={{ fill: 'var(--text-secondary)', fontSize: 11 }}
            axisLine={false}
            tickLine={false}
            tickFormatter={v => `${v}%`}
          />
          <YAxis
            type="category"
            dataKey="name"
            tick={{ fill: 'var(--text-secondary)', fontSize: 11, fontWeight: 500 }}
            axisLine={false}
            tickLine={false}
            width={110}
          />
          <Tooltip content={<CustomTooltip />} cursor={{ fill: 'var(--border)', opacity: 0.08 }} />
          <Legend wrapperStyle={{ color: 'var(--text)', fontSize: '0.78rem', paddingTop: '0.5rem' }} />

          <Bar dataKey={t('chartLabels.boundaryFaithfulness.faithful')}   stackId="a" fill="#10b981" radius={[0, 0, 0, 0]} />
          <Bar dataKey={t('chartLabels.boundaryFaithfulness.unfaithful')} stackId="a" fill="#f59e0b" radius={[0, 0, 0, 0]} />
          <Bar dataKey={t('chartLabels.boundaryFaithfulness.crashed')}   stackId="a" fill="#ef4444" radius={[0, 4, 4, 0]} />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
