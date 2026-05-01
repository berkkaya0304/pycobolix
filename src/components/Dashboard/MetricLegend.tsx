'use client';

import React, { useState } from 'react';
import styles from './MetricLegend.module.css';
import { ChevronDown, ChevronUp } from 'lucide-react';
import { useTranslation } from '@/lib/i18n/LanguageContext';

interface MetricDef {
  key: string;
  categoryKey: string;
  hasFormula?: boolean;
  hasRange?: boolean;
  hasGood?: boolean;
  tabRelevance: Array<'cobol-to-python' | 'python-to-cobol' | 'additional' | 'directional'>;
}

const METRICS: MetricDef[] = [
  { key: 'semanticMatch', categoryKey: 'match', hasFormula: true, hasRange: true, hasGood: true, tabRelevance: ['directional'] },
  { key: 'formatMatch', categoryKey: 'match', hasFormula: true, hasRange: true, hasGood: true, tabRelevance: ['directional'] },
  { key: 'totalTestCases', categoryKey: 'test', hasRange: true, tabRelevance: ['directional'] },
  { key: 'filesAnalyzed', categoryKey: 'test', tabRelevance: ['cobol-to-python', 'python-to-cobol', 'additional'] },
  { key: 'pylintScore', categoryKey: 'quality', hasFormula: true, hasRange: true, hasGood: true, tabRelevance: ['additional'] },
  { key: 'complexityReduction', categoryKey: 'quality', hasFormula: true, hasRange: true, hasGood: true, tabRelevance: ['additional'] },
  { key: 'locRatio', categoryKey: 'size', hasFormula: true, hasRange: true, hasGood: true, tabRelevance: ['additional'] },
  { key: 'avgExecTime', categoryKey: 'performance', hasFormula: true, hasRange: true, hasGood: true, tabRelevance: ['additional'] },
  { key: 'mypyErrorCount', categoryKey: 'typeSafety', hasFormula: true, hasRange: true, hasGood: true, tabRelevance: ['additional'] },
  { key: 'halsteadVolume', categoryKey: 'halstead', hasFormula: true, hasRange: true, hasGood: true, tabRelevance: ['additional'] },
  { key: 'halsteadDifficulty', categoryKey: 'halstead', hasFormula: true, hasRange: true, hasGood: true, tabRelevance: ['additional'] },
  { key: 'halsteadEffort', categoryKey: 'halstead', hasFormula: true, hasRange: true, hasGood: true, tabRelevance: ['additional'] },
  { key: 'errorSign', categoryKey: 'errorCat', hasGood: true, tabRelevance: ['directional'] },
  { key: 'errorWhitespace', categoryKey: 'errorCat', hasGood: true, tabRelevance: ['directional'] },
  { key: 'errorLogic', categoryKey: 'errorCat', hasGood: true, tabRelevance: ['directional'] },
  { key: 'errorCrash', categoryKey: 'errorCat', hasGood: true, tabRelevance: ['directional'] },
  { key: 'consensusFailure', categoryKey: 'consensus', tabRelevance: ['directional'] }
];

interface Props {
  activeTab?: 'cobol-to-python' | 'python-to-cobol' | 'additional';
}

export default function MetricLegend({ activeTab = 'cobol-to-python' }: Props) {
  const [open, setOpen] = useState(false);
  const [activeCatKey, setActiveCatKey] = useState<string | null>(null);
  const { t } = useTranslation();

  const isDirectional = activeTab === 'cobol-to-python' || activeTab === 'python-to-cobol';

  const tabFilteredMetrics = METRICS.filter(m => 
    m.tabRelevance.includes(activeTab) || 
    (isDirectional && m.tabRelevance.includes('directional'))
  );

  const CATEGORY_KEYS = [...new Set(tabFilteredMetrics.map(m => m.categoryKey))];

  const filtered = activeCatKey 
    ? tabFilteredMetrics.filter(m => m.categoryKey === activeCatKey) 
    : tabFilteredMetrics;

  return (
    <div className={styles.wrap}>
      <button 
        className={`${styles.toggleBtn} ${open ? styles.toggleBtnOpen : ''}`} 
        onClick={() => setOpen(p => !p)}
      >
        <div className={styles.toggleContent}>
          <span className={styles.toggleIcon}>📖</span>
          <span className={styles.toggleText}>
            {t('metricLegend.title')} <span className={styles.toggleSub}>{t('metricLegend.subtitle')}</span>
          </span>
        </div>
        <div className={styles.chevron}>
          {open ? <ChevronUp size={20} /> : <ChevronDown size={20} />}
        </div>
      </button>

      {open && (
        <div className={styles.body}>
          {/* Category filter */}
          <div className={styles.catRow}>
            <button
              className={`${styles.catBtn} ${activeCatKey === null ? styles.catActive : ''}`}
              onClick={() => setActiveCatKey(null)}
            >
              {t('metricLegend.all')}
            </button>
            {CATEGORY_KEYS.map(catKey => (
              <button
                key={catKey}
                className={`${styles.catBtn} ${activeCatKey === catKey ? styles.catActive : ''}`}
                onClick={() => setActiveCatKey(c => c === catKey ? null : catKey)}
              >
                {t(`metricLegend.categories.${catKey}`)}
              </button>
            ))}
          </div>

          {/* Metric cards */}
          <div className={styles.grid}>
            {filtered.map(m => (
              <div key={m.key} className={styles.card}>
                <div className={styles.cardHeader}>
                  <span className={styles.catTag}>{t(`metricLegend.categories.${m.categoryKey}`)}</span>
                  <span className={styles.metricName}>{t(`metricLegend.metrics.${m.key}.name`)}</span>
                </div>
                {m.hasFormula && (
                  <code className={styles.formula}>{t(`metricLegend.metrics.${m.key}.formula`)}</code>
                )}
                <p className={styles.desc}>{t(`metricLegend.metrics.${m.key}.desc`)}</p>
                {m.hasRange && <div className={styles.metaRow}><b>{t('metricLegend.range')}</b> {t(`metricLegend.metrics.${m.key}.range`)}</div>}
                {m.hasGood  && <div className={styles.metaRow}><b>{t('metricLegend.goodValue')}</b> <span style={{ color: '#22c55e' }}>{t(`metricLegend.metrics.${m.key}.good`)}</span></div>}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
