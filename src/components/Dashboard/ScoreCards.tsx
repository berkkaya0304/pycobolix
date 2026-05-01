import React from 'react';
import {
  Activity, CheckCircle, TrendingDown, FlaskConical,
  Fingerprint, Hash, FileText, Clock, Code2, Layers, ShieldCheck,
} from 'lucide-react';
import styles from './ScoreCards.module.css';
import { AnalysisResult } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';

interface ScoreCardsProps { 
  data: AnalysisResult[]; 
  viewType?: 'directional' | 'additional';
  activeTab?: 'cobol-to-python' | 'python-to-cobol' | 'additional';
}

function safeMean(arr: number[]) {
  return arr.length ? arr.reduce((a, b) => a + b, 0) / arr.length : 0;
}

export default function ScoreCards({ data, viewType = 'directional', activeTab = 'cobol-to-python' }: ScoreCardsProps) {
  const allModels = data.flatMap(d => d.models);
  const totalRuns = allModels.length;
  const { t } = useTranslation();
  if (totalRuns === 0) return null;

  // ─── Core rates ──────────────────────────────────────────────────────────────
  const avgPylint = safeMean(allModels.map(m => m.metrics.pylint_score));
  const avgReduc  = safeMean(allModels.map(m => m.metrics.complexity_reduction_pct));

  // ─── Differential testing ────────────────────────────────────────────────────
  const totalTests      = allModels.reduce((a, m) => a + (m.metrics.unit_tests_total    ?? 0), 0);
  const formatPassed    = allModels.reduce((a, m) => a + (m.metrics.format_match_passed    ?? 0), 0);
  const semanticPassed  = allModels.reduce((a, m) => a + (m.metrics.unit_tests_passed    ?? 0), 0);
  const formatRate      = totalTests > 0 ? (formatPassed    / totalTests) * 100 : 0;
  const semanticRate    = totalTests > 0 ? (semanticPassed  / totalTests) * 100 : 0;

  // ─── New metrics ─────────────────────────────────────────────────────────────
  const locValues  = allModels.map(m => m.metrics.loc_ratio).filter((v): v is number => v != null);
  const avgLocRatio = locValues.length ? safeMean(locValues) : null;

  const execValues = allModels.map(m => m.metrics.exec_time_python_avg_ms).filter((v): v is number => v != null);
  const avgExecMs  = execValues.length ? Math.round(safeMean(execValues)) : null;

  const mypyValues = allModels.map(m => m.metrics.mypy_error_count).filter((v): v is number => v != null);
  const avgMypy    = mypyValues.length ? Math.round(safeMean(mypyValues) * 10) / 10 : null;

  const halsteadValues = allModels.map(m => m.metrics.halstead_effort).filter((v): v is number => v != null);
  const avgHalstead    = halsteadValues.length ? Math.round(safeMean(halsteadValues)) : null;

  const totalFiles = data.length;

  // ─── Error distribution totals ────────────────────────────────────────────────
  const errSign  = allModels.reduce((a, m) => a + (m.metrics.error_sign      ?? 0), 0);
  const errWs    = allModels.reduce((a, m) => a + (m.metrics.error_whitespace ?? 0), 0);
  const errLogic = allModels.reduce((a, m) => a + (m.metrics.error_logic      ?? 0), 0);
  const errCrash = allModels.reduce((a, m) => a + (m.metrics.error_crash      ?? 0), 0);
  const totalErr = errSign + errWs + errLogic + errCrash;

  const directionPrefix = activeTab === 'python-to-cobol' ? 'Py➔CBL' : 'CBL➔Py';

  const cards = [
    {
      title: `${directionPrefix} ${t('scoreCards.semanticMatchRate').split(' ').slice(1).join(' ')}`,
      value: `${semanticRate.toFixed(1)}%`,
      sub:   t('scoreCards.semanticMatchSub'),
      icon:  CheckCircle,
      color: semanticRate >= 80 ? 'var(--success)' : 'var(--warning)',
      internalId: 'semanticMatchRate',
    },
    {
      title: `${directionPrefix} ${t('scoreCards.formatMatchRate').split(' ').slice(1).join(' ')}`,
      value: `${formatRate.toFixed(1)}%`,
      sub:   t('scoreCards.formatMatchSub'),
      icon:  Fingerprint,
      color: formatRate >= 70 ? 'var(--success)' : 'var(--error)',
      internalId: 'formatMatchRate',
    },
    {
      title: t('scoreCards.totalTestCases'),
      value: String(totalTests),
      sub:   t('scoreCards.totalTestCasesSub').replace('{files}', String(totalFiles)).replace('{runs}', String(totalRuns)),
      icon:  FlaskConical,
      color: 'var(--accent)',
      internalId: 'totalTestCases',
    },
    {
      title: t('scoreCards.avgPylintScore'),
      value: avgPylint.toFixed(2),
      sub:   t('scoreCards.avgPylintSub'),
      icon:  Activity,
      color: avgPylint >= 8 ? 'var(--success)' : avgPylint >= 6 ? 'var(--warning)' : 'var(--error)',
    },
    {
      title: t('scoreCards.ccReduction'),
      value: `${avgReduc.toFixed(1)}%`,
      sub:   t('scoreCards.ccReductionSub'),
      icon:  TrendingDown,
      color: avgReduc >= 10 ? 'var(--success)' : 'var(--accent)',
    },
    {
      title: t('scoreCards.avgLocRatio'),
      value: avgLocRatio != null ? avgLocRatio.toFixed(2) : '—',
      sub:   t('scoreCards.avgLocRatioSub'),
      icon:  FileText,
      color: avgLocRatio != null && avgLocRatio < 0.8 ? 'var(--success)' : 'var(--accent)',
    },
    {
      title: t('scoreCards.avgExecTime'),
      value: avgExecMs != null ? `${avgExecMs} ms` : '—',
      sub:   t('scoreCards.avgExecTimeSub'),
      icon:  Clock,
      color: 'var(--accent)',
    },
    {
      title: t('scoreCards.avgMypyErrors'),
      value: avgMypy != null ? String(avgMypy) : '—',
      sub:   t('scoreCards.avgMypyErrorsSub'),
      icon:  ShieldCheck,
      color: avgMypy === 0 ? 'var(--success)' : (avgMypy ?? 1) > 5 ? 'var(--error)' : 'var(--warning)',
    },
    {
      title: t('scoreCards.avgHalsteadEffort'),
      value: avgHalstead != null ? avgHalstead.toLocaleString() : '—',
      sub:   t('scoreCards.avgHalsteadSub'),
      icon:  Code2,
      color: 'var(--accent)',
    },
    {
      title: t('scoreCards.filesAnalyzed'),
      value: String(totalFiles),
      sub:   t('scoreCards.filesAnalyzedSub').replace('{runs}', String(totalRuns)),
      icon:  Layers,
      color: 'var(--accent)',
    },
    {
      title: t('scoreCards.dominantErrorType'),
      value: totalErr === 0 ? '—' :
             errLogic >= Math.max(errSign, errWs, errCrash) ? t('explorer.logic')
               : errWs >= Math.max(errSign, errLogic, errCrash) ? t('explorer.whitespace')
               : errSign >= Math.max(errWs, errLogic, errCrash) ? t('explorer.signError')
               : t('explorer.crash'),
      sub:   totalErr > 0
        ? `logic:${errLogic} ws:${errWs} sign:${errSign} crash:${errCrash}`
        : t('scoreCards.dominantErrorSubEmpty'),
      icon:  Activity,
      color: totalErr === 0 ? 'var(--accent)' :
             errCrash >= Math.max(errSign, errWs, errLogic) ? 'var(--error)' : 'var(--warning)',
      internalId: 'dominantErrorType',
    },
  ];

  const directionalCardsIds = ['semanticMatchRate', 'formatMatchRate', 'totalTestCases', 'dominantErrorType'];
  const filteredCards = cards.filter(c => 
    viewType === 'directional' 
      ? (c.internalId && directionalCardsIds.includes(c.internalId))
      : !(c.internalId && directionalCardsIds.includes(c.internalId))
  );

  return (
    <div className={styles.container}>
      {filteredCards.map(({ title, value, sub, icon: Icon, color }) => (
        <div key={title} className={styles.card} style={{ '--card-accent': color } as React.CSSProperties}>
          <div className={styles.header}>
            <span className={styles.title}>{title}</span>
            <div className={styles.iconWrapper} style={{ backgroundColor: `color-mix(in srgb, ${color} 15%, transparent)`, color }}>
              <Icon size={20} />
            </div>
          </div>
          <div className={styles.value} style={{ color }}>{value}</div>
          <div className={styles.trend}>
            <span className={styles.neutral}>{sub}</span>
          </div>
        </div>
      ))}
    </div>
  );
}
