'use client';

import React, { useState } from 'react';
import { AnalysisResult } from '@/lib/data/types';
import styles from './ModelStatsTable.module.css';
import { useTranslation } from '@/lib/i18n/LanguageContext';

interface Props { 
  data: AnalysisResult[]; 
  viewType?: 'directional' | 'additional';
}

type SortKey = 'model' | 'files' | 'tests' | 'formatPct' | 'semanticPct' |
               'pylintAvg' | 'complexAvg' | 'locRatioAvg' | 'execPyAvg' | 'mypyAvg' | 'halsteadEffort';

interface ModelStat {
  model:          string;
  files:          number;
  tests:          number;
  formatPct:        number;
  semanticPct:        number;
  pylintAvg:      number;
  pylintMin:      number;
  pylintMax:      number;
  complexAvg:     number;
  locRatioAvg:    number | null;
  execPyAvg:      number | null;
  execCblAvg:     number | null;
  mypyAvg:        number | null;
  halsteadEffort: number | null;
}

function pct(n: number, d: number) { return d > 0 ? Math.round((n / d) * 100) : 0; }
function avg(arr: number[]) { return arr.length ? arr.reduce((a, b) => a + b, 0) / arr.length : 0; }
function minOf(arr: number[]) { return arr.length ? Math.min(...arr) : 0; }
function maxOf(arr: number[]) { return arr.length ? Math.max(...arr) : 0; }

export default function ModelStatsTable({ data, viewType = 'directional' }: Props) {
  const [sortKey, setSortKey]   = useState<SortKey>('formatPct');
  const [sortAsc, setSortAsc]   = useState(false);
  const { t } = useTranslation();

  type Acc = {
    pylints: number[];
    complexities: number[];
    tests: number;
    format: number;
    semantic: number;
    files: number;
    locRatios: number[];
    execPyMs: number[];
    execCblMs: number[];
    mypyErrors: number[];
    halsteadEfforts: number[];
  };

  const byModel: Record<string, Acc> = {};

  data.forEach(file => {
    file.models.forEach(m => {
      if (!byModel[m.model_name]) {
        byModel[m.model_name] = {
          pylints: [], complexities: [], tests: 0, format: 0, semantic: 0, 
          files: 0,
          locRatios: [], execPyMs: [], execCblMs: [], mypyErrors: [], halsteadEfforts: [],
        };
      }
      const s = byModel[m.model_name];
      s.files += 1;
      s.pylints.push(m.metrics.pylint_score);
      s.complexities.push(m.metrics.complexity_reduction_pct);
      s.tests   += m.metrics.unit_tests_total    ?? 0;
      s.format    += m.metrics.format_match_passed    ?? 0;
      s.semantic    += m.metrics.unit_tests_passed    ?? 0;

      if (m.metrics.loc_ratio               != null) s.locRatios.push(m.metrics.loc_ratio);
      if (m.metrics.exec_time_python_avg_ms != null) s.execPyMs.push(m.metrics.exec_time_python_avg_ms);
      if (m.metrics.exec_time_cobol_avg_ms  != null) s.execCblMs.push(m.metrics.exec_time_cobol_avg_ms);
      if (m.metrics.mypy_error_count        != null) s.mypyErrors.push(m.metrics.mypy_error_count);
      if (m.metrics.halstead_effort         != null) s.halsteadEfforts.push(m.metrics.halstead_effort);
    });
  });

  const stats: ModelStat[] = Object.entries(byModel).map(([model, s]) => ({
    model,
    files:      s.files,
    tests:      s.tests,
    formatPct:    pct(s.format,    s.tests),
    semanticPct:    pct(s.semantic,    s.tests),
    pylintAvg:  avg(s.pylints),
    pylintMin:  minOf(s.pylints),
    pylintMax:  maxOf(s.pylints),
    complexAvg: avg(s.complexities),
    locRatioAvg:    s.locRatios.length      ? Math.round(avg(s.locRatios) * 100) / 100  : null,
    execPyAvg:      s.execPyMs.length       ? Math.round(avg(s.execPyMs))               : null,
    execCblAvg:     s.execCblMs.length      ? Math.round(avg(s.execCblMs))              : null,
    mypyAvg:        s.mypyErrors.length     ? Math.round(avg(s.mypyErrors) * 10) / 10  : null,
    halsteadEffort: s.halsteadEfforts.length ? Math.round(avg(s.halsteadEfforts))        : null,
  })).sort((a, b) => {
    const va = a[sortKey] ?? -Infinity;
    const vb = b[sortKey] ?? -Infinity;
    if (typeof va === 'string' && typeof vb === 'string')
      return sortAsc ? va.localeCompare(vb) : vb.localeCompare(va);
    return sortAsc ? (va as number) - (vb as number) : (vb as number) - (va as number);
  });

  if (stats.length === 0) return null;

  function handleSort(key: SortKey) {
    if (sortKey === key) setSortAsc(p => !p);
    else { setSortKey(key); setSortAsc(false); }
  }

  function Th({ k, label }: { k: SortKey; label: string }) {
    return (
      <th className={styles.th} onClick={() => handleSort(k)} style={{ cursor: 'pointer', userSelect: 'none' }}>
        {label} {sortKey === k ? (sortAsc ? '▲' : '▼') : ''}
      </th>
    );
  }

  function Cell({ v, good, bad }: { v: string; good?: boolean; bad?: boolean }) {
    const color = good ? '#22c55e' : bad ? '#ef4444' : undefined;
    return <td className={styles.td} style={{ color }}>{v}</td>;
  }

  return (
    <div className={styles.wrap}>
      <div className={styles.header}>
        <p className={styles.title}>{t('statsTable.title')}</p>
        <p className={styles.sub}>{t('statsTable.subtitle')}</p>
      </div>
      <div className={styles.scroll}>
        <table className={styles.table}>
          <thead>
            <tr>
              <Th k="model"          label={t('statsTable.colModel')} />
              <Th k="files"          label={t('statsTable.colFiles')} />
              {viewType === 'directional' && (
                <>
                  <Th k="tests"          label={t('statsTable.colTests')} />
                  <Th k="formatPct"        label={t('statsTable.colFormatPct')} />
                  <Th k="semanticPct"        label={t('statsTable.colSemanticPct')} />
                </>
              )}
              {viewType === 'additional' && (
                <>
                  <Th k="pylintAvg"      label={t('statsTable.colPylintAvg')} />
                  <Th k="complexAvg"     label={t('statsTable.colComplexAvg')} />
                  <Th k="locRatioAvg"    label={t('statsTable.colLocRatio')} />
                  <Th k="execPyAvg"      label={t('statsTable.colExecPy')} />
                  <Th k="mypyAvg"        label={t('statsTable.colMypy')} />
                  <Th k="halsteadEffort" label={t('statsTable.colHalstead')} />
                </>
              )}
            </tr>
          </thead>
          <tbody>
            {stats.map((s, i) => (
              <tr key={s.model} className={`${styles.tr} ${i % 2 === 1 ? styles.even : ''}`}>
                <td className={`${styles.td} ${styles.modelCell}`}>{s.model}</td>
                <td className={styles.td}>{s.files}</td>
                {viewType === 'directional' && (
                  <>
                    <td className={styles.td}>{s.tests}</td>
                    <Cell v={`${s.formatPct}%`}    good={s.formatPct    >= 70} bad={s.formatPct    < 40} />
                    <Cell v={`${s.semanticPct}%`}    good={s.semanticPct    >= 80} bad={s.semanticPct    < 50} />
                  </>
                )}
                {viewType === 'additional' && (
                  <>
                    <td className={styles.td}>
                      <span style={{ color: s.pylintAvg >= 8 ? '#22c55e' : s.pylintAvg >= 6 ? '#f59e0b' : '#ef4444' }}>
                        {s.pylintAvg.toFixed(1)}
                      </span>
                      <span className={styles.minmax}>
                        &nbsp;({s.pylintMin.toFixed(1)} – {s.pylintMax.toFixed(1)})
                      </span>
                    </td>
                    <td className={styles.td}>{s.complexAvg.toFixed(1)}%</td>
                    <td className={styles.td}
                        style={{ color: s.locRatioAvg != null && s.locRatioAvg < 0.8 ? '#22c55e' : undefined }}>
                      {s.locRatioAvg != null ? s.locRatioAvg : '—'}
                    </td>
                    <td className={styles.td}>{s.execPyAvg != null ? `${s.execPyAvg} ms` : '—'}</td>
                    <td className={styles.td}
                        style={{ color: s.mypyAvg === 0 ? '#22c55e' : (s.mypyAvg ?? 0) > 5 ? '#ef4444' : undefined }}>
                      {s.mypyAvg != null ? s.mypyAvg : '—'}
                    </td>
                    <td className={styles.td}>{s.halsteadEffort != null ? s.halsteadEffort.toLocaleString() : '—'}</td>
                  </>
                )}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
