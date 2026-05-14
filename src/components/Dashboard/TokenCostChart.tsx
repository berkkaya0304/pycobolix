'use client';

import React, { useState, useEffect, useMemo } from 'react';
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
  Cell,
  LabelList
} from 'recharts';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import styles from './TokenCostChart.module.css';
import { LlmUsageEntry } from '@/lib/data/types';
import { Coins, Zap, Activity, ArrowUpRight } from 'lucide-react';

export default function TokenCostChart() {
  const { t } = useTranslation();
  const [usage, setUsage] = useState<LlmUsageEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const [activeCategory, setActiveCategory] = useState<'All' | 'Translation' | 'Test Gen'>('All');

  useEffect(() => {
    async function fetchUsage() {
      try {
        const res = await fetch('/api/llm-usage');
        const data = await res.json();
        setUsage(Array.isArray(data) ? data : []);
      } catch (err) {
        console.error('Failed to fetch LLM usage:', err);
      } finally {
        setLoading(false);
      }
    }
    fetchUsage();
  }, []);

  // Always compute per-category totals from full data (unfiltered)
  const categoryTotals = useMemo(() => {
    let translationTokens = 0;
    let testGenTokens = 0;

    usage.forEach(entry => {
      const total = entry.prompt_tokens + entry.completion_tokens;
      if (entry.type === 'translation') {
        translationTokens += total;
      } else {
        testGenTokens += total;
      }
    });

    return { translation: translationTokens, testGen: testGenTokens, total: translationTokens + testGenTokens };
  }, [usage]);

  const { chartData, totals } = useMemo(() => {
    const stats: Record<string, { prompt: number; completion: number; category: string; rawModel: string }> = {};
    let totalPrompt = 0;
    let totalCompletion = 0;

    usage.forEach(entry => {
      const category = entry.type === 'translation' ? 'Translation' : 'Test Gen';
      
      if (activeCategory !== 'All' && category !== activeCategory) return;

      const key = `${entry.model} (${category})`;

      if (!stats[key]) {
        stats[key] = { prompt: 0, completion: 0, category, rawModel: entry.model };
      }
      stats[key].prompt += entry.prompt_tokens;
      stats[key].completion += entry.completion_tokens;
      totalPrompt += entry.prompt_tokens;
      totalCompletion += entry.completion_tokens;
    });

    const data = Object.entries(stats).map(([name, s]) => {
      const displayName = name
        .replace(/-202\d{5}/g, '')
        .replace(/-00\d/g, '')
        .replace('(Translation)', '')
        .replace('(Test Gen)', '');

      return {
        name: displayName,
        label: activeCategory === 'All' ? `${displayName} (${s.category})` : displayName,
        category: s.category,
        Prompt: s.prompt,
        Completion: s.completion,
        Total: s.prompt + s.completion,
        fullName: name,
        rawModel: s.rawModel
      };
    });

    data.sort((a, b) => b.Total - a.Total);

    return { 
      chartData: data, 
      totals: { prompt: totalPrompt, completion: totalCompletion, total: totalPrompt + totalCompletion } 
    };
  }, [usage, activeCategory]);

  const formatNumber = (num: number) => {
    if (num >= 1000000) return `${(num / 1000000).toFixed(1)}M`;
    if (num >= 1000) return `${(num / 1000).toFixed(1)}k`;
    return num.toString();
  };

  const pct = (part: number, whole: number) => whole > 0 ? `${((part / whole) * 100).toFixed(0)}%` : '0%';

  const CustomTooltip = ({ active, payload }: any) => {
    if (!active || !payload?.length) return null;
    const d = payload[0].payload;
    return (
      <div className={styles.customTooltip}>
        <div className={styles.tooltipHeader}>
          <Activity size={14} className={styles.tooltipIcon} />
          <span>{d.fullName}</span>
        </div>
        <div className={styles.tooltipBody}>
          <div className={styles.tooltipRow}>
            <span className={styles.tooltipLabel}>Prompt:</span>
            <span className={styles.tooltipValue}>{d.Prompt.toLocaleString()}</span>
          </div>
          <div className={styles.tooltipRow}>
            <span className={styles.tooltipLabel}>Completion:</span>
            <span className={styles.tooltipValue}>{d.Completion.toLocaleString()}</span>
          </div>
          <div className={styles.tooltipDivider} />
          <div className={styles.tooltipRow}>
            <span className={styles.tooltipLabelTotal}>Total Tokens:</span>
            <span className={styles.tooltipValueTotal}>{d.Total.toLocaleString()}</span>
          </div>
        </div>
      </div>
    );
  };

  const CustomYAxisTick = (props: any) => {
    const { x, y, payload } = props;
    const value = payload.value;
    const match = value.match(/(.+) \((.+)\)$/);
    
    if (match) {
      const [_, name, category] = match;
      return (
        <g transform={`translate(${x},${y})`}>
          <text x={-10} y={-4} textAnchor="end" className={styles.axisLabel} fontSize={10} fontWeight={700}>
            {name}
          </text>
          <text x={-10} y={10} textAnchor="end" className={styles.axisLabelSmall} fontSize={9} fontWeight={500}>
            {category}
          </text>
        </g>
      );
    }
    
    return (
      <g transform={`translate(${x},${y})`}>
        <text x={-10} y={4} textAnchor="end" className={styles.axisLabel} fontSize={10} fontWeight={700}>
          {value}
        </text>
      </g>
    );
  };

  return (
    <div className={styles.chartContainer}>
      <div className={styles.header}>
        <div className={styles.headerTitleArea}>
          <h3 className={styles.title}>{t('charts.tokenCostChart')}</h3>
          <p className={styles.subtitle}>{t('chartLabels.tokenCost.subtitle')}</p>
          
          <div className={styles.categoryTabs} data-no-export>
            {(['All', 'Translation', 'Test Gen'] as const).map(cat => (
              <button
                key={cat}
                className={`${styles.tabBtn} ${activeCategory === cat ? styles.tabActive : ''}`}
                onClick={() => setActiveCategory(cat)}
              >
                {cat === 'All' ? t('common.all') : (cat === 'Translation' ? 'Translation' : 'Test Gen')}
              </button>
            ))}
          </div>
        </div>

        <div className={styles.statsPanel}>
          <div className={styles.statCardMain}>
            <div className={styles.statCardMainIcon}>
              <Coins size={20} />
            </div>
            <div className={styles.statText}>
              <span className={styles.statValLarge}>{formatNumber(categoryTotals.total)}</span>
              <span className={styles.statLabel}>{t('chartLabels.tokenCost.totalTokens')}</span>
            </div>
          </div>
          <div className={styles.statDivider} />
          <div className={styles.statCardsSub}>
            <div className={styles.statCardCategory}>
              <span className={styles.catDotTranslation} />
              <div className={styles.statText}>
                <span className={styles.statVal}>{formatNumber(categoryTotals.translation)}</span>
                <span className={styles.statLabelSm}>Translation</span>
              </div>
              <span className={styles.statPct}>{pct(categoryTotals.translation, categoryTotals.total)}</span>
            </div>
            <div className={styles.statCardCategory}>
              <span className={styles.catDotTestGen} />
              <div className={styles.statText}>
                <span className={styles.statVal}>{formatNumber(categoryTotals.testGen)}</span>
                <span className={styles.statLabelSm}>Test Gen</span>
              </div>
              <span className={styles.statPct}>{pct(categoryTotals.testGen, categoryTotals.total)}</span>
            </div>
          </div>
        </div>
      </div>

      {loading ? (
        <div className={styles.loading}>
           <div className={styles.spinner} />
           <span>{t('chartLabels.tokenCost.loading')}</span>
        </div>
      ) : chartData.length > 0 ? (
        <div className={styles.chartWrapper}>
          <ResponsiveContainer width="100%" height="100%">
            <BarChart 
              data={chartData} 
              layout="vertical" 
              margin={{ top: 5, right: 90, left: 20, bottom: 5 }}
              barGap={0}
            >
              <defs>
                <linearGradient id="promptGradient" x1="0" y1="0" x2="1" y2="0">
                  <stop offset="0%" stopColor="#6366f1" stopOpacity={0.8} />
                  <stop offset="100%" stopColor="#818cf8" stopOpacity={0.9} />
                </linearGradient>
                <linearGradient id="completionGradient" x1="0" y1="0" x2="1" y2="0">
                  <stop offset="0%" stopColor="#ec4899" stopOpacity={0.8} />
                  <stop offset="100%" stopColor="#f472b6" stopOpacity={0.9} />
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" stroke="var(--border)" horizontal={false} opacity={0.3} />
              <XAxis type="number" hide />
              <YAxis 
                type="category" 
                dataKey="label" 
                width={200}
                tick={<CustomYAxisTick />}
                axisLine={false} 
                tickLine={false} 
              />
              <Tooltip content={<CustomTooltip />} cursor={{ fill: 'rgba(255,255,255,0.05)' }} />
              
              <Bar 
                dataKey="Prompt" 
                stackId="a" 
                fill="url(#promptGradient)" 
                radius={[0, 0, 0, 0]}
                barSize={24}
                isAnimationActive={false}
              />
              <Bar 
                dataKey="Completion" 
                stackId="a" 
                fill="url(#completionGradient)" 
                radius={[0, 4, 4, 0]}
                barSize={24}
                isAnimationActive={false}
              >
                <LabelList 
                  dataKey="Total" 
                  position="right" 
                  formatter={formatNumber}
                  className={styles.barLabel}
                  style={{ fontSize: '10px', fontWeight: 700 }}
                  offset={10}
                />
              </Bar>
            </BarChart>
          </ResponsiveContainer>
          
          <div className={styles.legend}>
             <div className={styles.legendItem}>
               <span className={styles.legendDotPrompt} />
               <span>{t('chartLabels.tokenCost.promptTokens')}</span>
             </div>
             <div className={styles.legendItem}>
               <span className={styles.legendDotComp} />
               <span>{t('chartLabels.tokenCost.completionTokens')}</span>
             </div>
          </div>
        </div>
      ) : (
        <div className={styles.empty}>{t('chartLabels.tokenCost.empty')}</div>
      )}
    </div>
  );
}
