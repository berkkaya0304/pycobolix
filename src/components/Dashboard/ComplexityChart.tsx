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
  Cell
} from 'recharts';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './ComplexityChart.module.css';

interface ComplexityChartProps {
  data: AnalysisResult[];
}

export default function ComplexityChart({ data }: ComplexityChartProps) {
  const { t } = useTranslation();
  // Aggregate data by model
  const modelStats: Record<string, { complexity: number; count: number }> = {};

  data.forEach(file => {
      file.models.forEach(model => {
        if (!modelStats[model.model_name]) {
            modelStats[model.model_name] = { complexity: 0, count: 0 };
        }
        modelStats[model.model_name].complexity += model.metrics.complexity_reduction_pct;
        modelStats[model.model_name].count += 1;
      });
  });

  const chartData = Object.keys(modelStats).map(model => ({
    name: model,
    [t('chartLabels.complexity.reduction')]: Math.round(modelStats[model].complexity / modelStats[model].count),
  }));
  
  const COLORS = ['#6366f1', '#10b981', '#f59e0b', '#ec4899', '#06b6d4']; // Premium palette

  return (
    <div className={styles.chartContainer}>
      <h3 className={styles.title}>{t('charts.complexityChart')}</h3>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart
          data={chartData}
          margin={{
            top: 5,
            right: 30,
            left: 20,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" vertical={false} opacity={0.5} />
          <XAxis dataKey="name" tick={{ fill: 'var(--text-secondary)', fontSize: 12, fontWeight: 500 }} axisLine={false} tickLine={false} dy={10} />
          <YAxis tick={{ fill: 'var(--text-secondary)', fontSize: 12 }} axisLine={false} tickLine={false} dx={-10} />
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
            cursor={{fill: 'var(--border)', opacity: 0.1}}
          />
          <Legend wrapperStyle={{ color: 'var(--text)', paddingTop: '1rem', fontSize: '0.85rem' }} />
          <Bar dataKey={t('chartLabels.complexity.reduction')} radius={[6, 6, 0, 0]}>
            {chartData.map((entry, index) => (
              <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
            ))}
          </Bar>
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
