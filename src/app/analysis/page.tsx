'use client';

import React, { useState, useEffect } from 'react';
import styles from './page.module.css';
import { MOCK_DATA } from '@/lib/data/mockData';
import { AnalysisResult, TestResult } from '@/lib/data/types';
import { getAnalysisResultsAction, generateAnalysisExplanationAction } from '@/app/actions';
import { ChevronDown, ChevronRight, Download, Sparkles } from 'lucide-react';
import ExportWrapper from '@/components/Dashboard/ExportWrapper';
import { useTranslation } from '@/lib/i18n/LanguageContext';

// ─── JSON Export Helpers ────────────────────────────────────────────────────
function triggerDownload(content: string, filename: string, mime = 'application/json') {
  const blob = new Blob([content], { type: mime });
  const url  = URL.createObjectURL(blob);
  const a    = document.createElement('a');
  a.href = url;  a.download = filename;  a.click();
  URL.revokeObjectURL(url);
}

function pct(num: number | undefined, total: number | undefined): string {
  if (!total || total === 0) return '—';
  return `${Math.round(((num ?? 0) / total) * 100)}%`;
}

function MatchBar({ value, color }: { value: number; color: string }) {
  return (
    <div className={styles.barWrap}>
      <div
        className={styles.bar}
        style={{ width: `${Math.max(0, Math.min(100, value))}%`, background: color }}
      />
      <span className={styles.barLabel}>{value}%</span>
    </div>
  );
}

// ─── Markdown Parser Helper ─────────────────────────────────────────────────
function parseMarkdown(text: string) {
  if (!text) return null;
  const parts = text.split(/(\*\*.*?\*\*)/g);
  return parts.map((part, i) => {
    if (part.startsWith('**') && part.endsWith('**')) {
      return <strong key={i}>{part.slice(2, -2)}</strong>;
    }
    return <React.Fragment key={i}>{part}</React.Fragment>;
  });
}

// ─── Failure category badge ─────────────────────────────────────────────────
const CAT_COLORS: Record<string, string> = {
  sign_error: '#f59e0b',
  whitespace: '#3b82f6',
  logic:      '#ef4444',
  crash:      '#6b7280',
};
function FailureBadge({ category }: { category?: string | null }) {
  if (!category) return null;
  const label = category.replace('_', ' ').toUpperCase();
  return (
    <span style={{
      display: 'inline-block', fontSize: '0.65rem', fontWeight: 700,
      padding: '1px 6px', borderRadius: 4,
      background: CAT_COLORS[category] ?? '#888', color: '#fff',
      marginLeft: 4,
    }}>
      {label}
    </span>
  );
}

export default function AnalysisPage() {
  const [data, setData] = useState<AnalysisResult[]>(MOCK_DATA);
  const { t, language } = useTranslation() as any; // Destructure `language` from useTranslation
  const [activeTab, setActiveTab] = useState<'c2p' | 'p2c' | 'boundary'>('c2p');
  const [expanded, setExpanded] = useState<Record<string, boolean>>({});
  const [sortKey, setSortKey] = useState<string>('format');
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('desc');
  
  // AI Explanation State
  const [aiExplanation, setAiExplanation] = useState<string>('');
  const [isGenerating, setIsGenerating] = useState<boolean>(false);

  useEffect(() => {
    async function load() {
      const res = await getAnalysisResultsAction();
      if (res?.success && res.data && res.data.length > 0) {
        setData(res.data);
        if (res.data[0].executive_summary) {
          setAiExplanation(res.data[0].executive_summary);
        }
      }
    }
    load();
  }, []);

  function toggleExpand(key: string) {
    setExpanded(prev => ({ ...prev, [key]: !prev[key] }));
  }

  function handleSort(key: string) {
    if (sortKey === key) setSortDir(d => d === 'asc' ? 'desc' : 'asc');
    else { setSortKey(key); setSortDir('desc'); }
  }

  async function handleGenerateExplanation() {
    if (isGenerating || data.length === 0) return;
    setIsGenerating(true);
    try {
      const res = await generateAnalysisExplanationAction(data, language || 'en');
      if (res.success && res.data) {
        let text = '';
        if (typeof res.data === 'string') {
          text = res.data;
        } else if (typeof res.data === 'object' && res.data !== null) {
          const t_titles = {
            en: {
              executiveSummary: '**Executive Summary**',
              matchRates: '**Match Rates**',
              pylintAndComplexity: '**Quality & Complexity**',
              errorPatterns: '**Error Patterns**',
              pythonToCobol: '**Reverse Translation (Python -> COBOL)**'
            },
            tr: {
              executiveSummary: '**Yönetici Özeti**',
              matchRates: '**Eşleşme Oranları**',
              pylintAndComplexity: '**Kod Kalitesi ve Karmaşıklık**',
              errorPatterns: '**Hata Dağılımı**',
              pythonToCobol: '**Ters Çeviri (Python -> COBOL)**'
            }
          };
          
          const currentLang = (language === 'tr' ? 'tr' : 'en') as 'en' | 'tr';
          const titles = t_titles[currentLang];
          
          const parts = [];
          
          if (res.data.executiveSummary) parts.push(`${titles.executiveSummary}\n${res.data.executiveSummary}`);
          if (res.data.matchRates) parts.push(`${titles.matchRates}\n${res.data.matchRates}`);
          if (res.data.pylintAndComplexity) parts.push(`${titles.pylintAndComplexity}\n${res.data.pylintAndComplexity}`);
          if (res.data.errorPatterns) parts.push(`${titles.errorPatterns}\n${res.data.errorPatterns}`);
          if (res.data.pythonToCobol) parts.push(`${titles.pythonToCobol}\n${res.data.pythonToCobol}`);
          
          text = parts.join('\n\n');
        }
        setAiExplanation(text);
      }
    } catch (err) {
      console.error(err);
    } finally {
      setIsGenerating(false);
    }
  }

  // ─── Row type ───────────────────────────────────────────────────────────────
  interface Row {
    file:           string;
    model:          string;
    // C2P
    format:         number;
    semantic:       number;
    pylint:         number;
    complexity:     number;
    locRatio:       number | null;
    execPyMs:       number | null;
    execCblMs:      number | null;
    mypyErrors:     number | null;
    halsteadEffort: number | null;
    tests:          TestResult[];
    // P2C
    revFormat:      number;
    revSemantic:    number;
    revTests:       TestResult[];
    // Boundary
    invFaithful:    number;
    invTotal:       number;
    invResults:     any[];
    // Metadata
    rowKey:         string;
  }

  const rows: Row[] = [];
  data.forEach(file => {
    file.models.forEach(model => {
      const total = model.metrics.unit_tests_total ?? 0;
      const revTotal = model.metrics.python_to_cobol_unit_tests_total ?? 0;
      const invTotal = model.invalid_test_results?.length ?? 0;
      const invFaithful = model.invalid_test_results?.filter(r => r.cobol_faithful).length ?? 0;

      rows.push({
        file:     file.source_file,
        model:    model.model_name,
        // C2P
        format:     total > 0 ? Math.round(((model.metrics.format_match_passed    ?? 0) / total) * 100) : 0,
        semantic:     total > 0 ? Math.round(((model.metrics.unit_tests_passed    ?? 0) / total) * 100) : 0,
        pylint:   model.metrics.pylint_score,
        complexity: model.metrics.complexity_reduction_pct,
        locRatio:   model.metrics.loc_ratio       ?? null,
        execPyMs:   model.metrics.exec_time_python_avg_ms ?? null,
        execCblMs:  model.metrics.exec_time_cobol_avg_ms  ?? null,
        mypyErrors: model.metrics.mypy_error_count ?? null,
        halsteadEffort: model.metrics.halstead_effort     ?? null,
        tests:  model.test_results ?? [],
        // P2C
        revFormat:   revTotal > 0 ? Math.round(((model.metrics.python_to_cobol_format_match_passed ?? 0) / revTotal) * 100) : 0,
        revSemantic: revTotal > 0 ? Math.round(((model.metrics.python_to_cobol_semantic_match_passed ?? 0) / revTotal) * 100) : 0,
        revTests:    model.python_to_cobol_test_results ?? [],
        // Boundary
        invFaithful: invTotal > 0 ? Math.round((invFaithful / invTotal) * 100) : 0,
        invTotal:    invTotal,
        invResults:  model.invalid_test_results ?? [],
        // Key
        rowKey: `${file.id}-${model.model_name}`,
      });
    });
  });

  // ─── Sorting ─────────────────────────────────────────────────────────────────
  rows.sort((a, b) => {
    const dir = sortDir === 'desc' ? -1 : 1;
    if (sortKey === 'file')    return dir * a.file.localeCompare(b.file);
    if (sortKey === 'model')   return dir * a.model.localeCompare(b.model);
    const numKey = sortKey as keyof Row;
    const av = (a[numKey] as number) ?? -Infinity;
    const bv = (b[numKey] as number) ?? -Infinity;
    return (av - bv) * dir;
  });

  function SortIcon({ col }: { col: string }) {
    if (sortKey !== col) return <span className={styles.sortIdle}>↕</span>;
    return <span className={styles.sortActive}>{sortDir === 'desc' ? '↓' : '↑'}</span>;
  }

  // ─── JSON Downloads ──────────────────────────────────────────────────────────
  function downloadSummaryJSON() {
    const summary = data[0]?.executive_summary || aiExplanation;
    const payload = {
      executive_summary: summary,
      results: data.flatMap(file =>
        file.models.map(m => {
          const total = m.metrics.unit_tests_total ?? 0;
          return {
            source_file:              file.source_file,
            model:                    m.model_name,
            c2p_format_pct:           total > 0 ? Math.round(((m.metrics.format_match_passed    ?? 0) / total) * 100) : 0,
            c2p_semantic_pct:         total > 0 ? Math.round(((m.metrics.unit_tests_passed    ?? 0) / total) * 100) : 0,
            pylint:                   m.metrics.pylint_score,
            complexity_reduction_pct: m.metrics.complexity_reduction_pct,
            loc_ratio:                m.metrics.loc_ratio              ?? null,
            exec_time_python_avg_ms:  m.metrics.exec_time_python_avg_ms ?? null,
            mypy_error_count:         m.metrics.mypy_error_count         ?? null,
            halstead_effort:          m.metrics.halstead_effort          ?? null,
            p2c_format_pct:           (m.metrics.python_to_cobol_unit_tests_total ?? 0) > 0 ? Math.round(((m.metrics.python_to_cobol_format_match_passed ?? 0) / (m.metrics.python_to_cobol_unit_tests_total ?? 1)) * 100) : 0,
            p2c_semantic_pct:         (m.metrics.python_to_cobol_unit_tests_total ?? 0) > 0 ? Math.round(((m.metrics.python_to_cobol_semantic_match_passed ?? 0) / (m.metrics.python_to_cobol_unit_tests_total ?? 1)) * 100) : 0,
            boundary_faithfulness_pct: (m.invalid_test_results?.length ?? 0) > 0 ? Math.round((m.invalid_test_results!.filter(r => r.cobol_faithful).length / m.invalid_test_results!.length) * 100) : 0,
          };
        })
      )
    };
    triggerDownload(
      JSON.stringify(payload, null, 2),
      `analysis_summary_${new Date().toISOString().replace(/[:.]/g, '-')}.json`
    );
  }

  function downloadDetailJSON() {
    const summary = data[0]?.executive_summary || aiExplanation;
    const payload = {
      executive_summary: summary,
      detail_results: data
    };
    triggerDownload(
      JSON.stringify(payload, null, 2),
      `analysis_full_detail_${new Date().toISOString().replace(/[:.]/g, '-')}.json`
    );
  }

  // ─── Columns configuration ──────────────────────────────────────────────────
  const getColCount = () => {
    return 13; // file, model, [res1, res2, tests], pylint, complexity, loc, pyMs, mypy, halstead, chevron
  };

  const getActiveTests = (row: Row) => {
    if (activeTab === 'c2p') return row.tests;
    if (activeTab === 'p2c') return row.revTests;
    if (activeTab === 'boundary') return row.invResults;
    return [];
  };

  return (
    <main className={styles.main}>
      <div className={styles.pageHeader}>
        <div>
          <h1 className={styles.headerTitle}>{t('analysis.title')}</h1>
          <p className={styles.headerSub}>{t('analysis.subtitle')}</p>
        </div>
        <div className={styles.csvButtons}>
          <button className={styles.csvBtn} onClick={downloadSummaryJSON}>
            <Download size={14} /> {t('analysis.summaryJson')}
          </button>
          <button className={`${styles.csvBtn} ${styles.csvBtnDetail}`} onClick={downloadDetailJSON}>
            <Download size={14} /> {t('analysis.testDetailJson')}
          </button>
        </div>
      </div>

      <div className={styles.tabs}>
        <button className={`${styles.tabBtn} ${activeTab === 'c2p' ? styles.active : ''}`} onClick={() => { setActiveTab('c2p'); setSortKey('format'); }}>
          {t('dashboard.cobolToPython')}
        </button>
        <button className={`${styles.tabBtn} ${activeTab === 'p2c' ? styles.active : ''}`} onClick={() => { setActiveTab('p2c'); setSortKey('revFormat'); }}>
          {t('dashboard.pythonToCobol')}
        </button>
        <button className={`${styles.tabBtn} ${activeTab === 'boundary' ? styles.active : ''}`} onClick={() => { setActiveTab('boundary'); setSortKey('invFaithful'); }}>
          {t('dashboard.additionalData')}
        </button>
      </div>

      <ExportWrapper filename="analysis_detail_table" title="Table: Detailed Per-File Analysis Results" paperStyle={true}>
        <div className={styles.tableWrap}>
        <table className={styles.table}>
          <thead>
            <tr>
              <th className={`${styles.th} ${styles.sortable} ${styles.stickyCol} ${styles.stickyHeader}`} onClick={() => handleSort('file')}>
                {t('analysis.file')} <SortIcon col="file" />
              </th>
              <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('model')}>
                {t('analysis.model')} <SortIcon col="model" />
              </th>

              {activeTab === 'c2p' ? (
                <>
                  <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('format')}>
                    {t('analysis.formatPct')} <SortIcon col="format" />
                  </th>
                  <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('semantic')}>
                    {t('analysis.semanticPct')} <SortIcon col="semantic" />
                  </th>
                  <th className={styles.th}>Tests</th>
                </>
              ) : activeTab === 'p2c' ? (
                <>
                  <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('revFormat')}>
                    {t('analysis.formatPct')} <SortIcon col="revFormat" />
                  </th>
                  <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('revSemantic')}>
                    {t('analysis.semanticPct')} <SortIcon col="revSemantic" />
                  </th>
                  <th className={styles.th}>Tests</th>
                </>
              ) : (
                <>
                  <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('invFaithful')}>
                    {t('analysis.faithful')} % <SortIcon col="invFaithful" />
                  </th>
                  <th className={styles.th}>Faithful</th>
                  <th className={styles.th}>Cases</th>
                </>
              )}

              {/* Common Quality Metrics */}
              <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('pylint')}>
                {t('analysis.pylint')} <SortIcon col="pylint" />
              </th>
              <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('complexity')}>
                {t('analysis.ccReduction')} <SortIcon col="complexity" />
              </th>
              <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('locRatio')}>
                {t('analysis.locRatio')} <SortIcon col="locRatio" />
              </th>
              <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('execPyMs')}>
                {t('analysis.execMs')} <SortIcon col="execPyMs" />
              </th>
              <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('mypyErrors')}>
                {t('analysis.mypy')} <SortIcon col="mypyErrors" />
              </th>
              <th className={`${styles.th} ${styles.sortable}`} onClick={() => handleSort('halsteadEffort')}>
                {t('analysis.halsteadE')} <SortIcon col="halsteadEffort" />
              </th>

              <th className={`${styles.th} ${styles.stickyEndCol} ${styles.stickyHeader}`} />
            </tr>
          </thead>
          <tbody>
            {rows.map(row => {
              const tests = getActiveTests(row);
              return (
                <React.Fragment key={row.rowKey}>
                  <tr
                    className={styles.tr}
                    onClick={() => tests.length > 0 && toggleExpand(row.rowKey)}
                    style={{ cursor: tests.length > 0 ? 'pointer' : 'default' }}
                  >
                    <td className={`${styles.td} ${styles.stickyCol}`}>
                      <span className={styles.fileName}>{row.file}</span>
                    </td>
                    <td className={styles.td}>
                      <span className={styles.modelBadge}>{row.model}</span>
                    </td>

                    {activeTab === 'c2p' ? (
                      <>
                        <td className={styles.td}><MatchBar value={row.format} color="#22c55e" /></td>
                        <td className={styles.td}><MatchBar value={row.semantic} color="#f59e0b" /></td>
                        <td className={styles.td} style={{ fontSize: '0.8rem' }}>{row.tests.length} tests</td>
                      </>
                    ) : activeTab === 'p2c' ? (
                      <>
                        <td className={styles.td}><MatchBar value={row.revFormat} color="#22c55e" /></td>
                        <td className={styles.td}><MatchBar value={row.revSemantic} color="#f59e0b" /></td>
                        <td className={styles.td} style={{ fontSize: '0.8rem' }}>{row.revTests.length} tests</td>
                      </>
                    ) : (
                      <>
                        <td className={styles.td}><MatchBar value={row.invFaithful} color="#8b5cf6" /></td>
                        <td className={styles.td} style={{ fontSize: '0.8rem', fontWeight: 600, color: '#22c55e' }}>
                           {row.invResults.filter(r => r.cobol_faithful).length} / {row.invTotal}
                        </td>
                        <td className={styles.td} style={{ fontSize: '0.8rem' }}>{row.invTotal} cases</td>
                      </>
                    )}

                    {/* Common Quality Metrics */}
                    <td className={styles.td}>
                      <span className={styles.pylint} style={{ color: row.pylint >= 8 ? '#22c55e' : row.pylint >= 6 ? '#f59e0b' : '#ef4444' }}>
                        {row.pylint.toFixed(1)} / 10
                      </span>
                    </td>
                    <td className={styles.td}><span className={styles.reduction}>{row.complexity}%</span></td>
                    <td className={styles.td} style={{ color: (row.locRatio ?? 1) < 0.8 ? '#22c55e' : undefined }}>
                      {row.locRatio != null ? row.locRatio : '—'}
                    </td>
                    <td className={styles.td} style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                      {row.execPyMs != null ? `${row.execPyMs} ms` : '—'}
                    </td>
                    <td className={styles.td} style={{ color: row.mypyErrors === 0 ? '#22c55e' : (row.mypyErrors ?? 0) > 5 ? '#ef4444' : undefined }}>
                      {row.mypyErrors != null ? row.mypyErrors : '—'}
                    </td>
                    <td className={styles.td} style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                      {row.halsteadEffort != null ? row.halsteadEffort.toLocaleString() : '—'}
                    </td>

                    <td className={`${styles.td} ${styles.stickyEndCol}`}>
                      {tests.length > 0 && (
                        expanded[row.rowKey]
                          ? <ChevronDown size={16} className={styles.chevron} />
                          : <ChevronRight size={16} className={styles.chevron} />
                      )}
                    </td>
                  </tr>

                  {expanded[row.rowKey] && tests.map((test: any, i) => (
                    <tr key={`${row.rowKey}-t${i}`} className={styles.expandedRow}>
                      <td colSpan={getColCount()} className={styles.expandedCell}>
                        <div className={styles.testRow}>
                          <div className={styles.testMeta}>
                            <span className={styles.testIdx}>#{i + 1}</span>
                            {activeTab !== 'boundary' ? (
                              <>
                                <span className={`${styles.badge} ${test.format_match ? styles.badgeGreenOn : styles.badgeOff}`}>{t('analysis.format')} {test.format_match ? '✓' : '✗'}</span>
                                <span className={`${styles.badge} ${test.semantic_match ? styles.badgeAmberOn : styles.badgeOff}`}>{t('analysis.semantic')} {test.semantic_match ? '✓' : '✗'}</span>
                                {!test.semantic_match && <FailureBadge category={test.failure_category} />}
                                {test.exec_time_ms != null && <span style={{ fontSize: '0.72rem', color: 'var(--text-secondary)', marginLeft: 8 }}>⏱ {test.exec_time_ms} ms</span>}
                              </>
                            ) : (
                              <>
                                <span className={`${styles.badge} ${test.cobol_faithful ? styles.badgeGreenOn : styles.badgeOff}`}>Faithful: {test.cobol_faithful ? 'Yes' : 'No'}</span>
                                {test.python_crashed && <span className={styles.badge} style={{ background: '#ef4444', color: '#fff' }}>Crashed</span>}
                                <span className={styles.badge} style={{ background: '#3b82f622', color: '#3b82f6' }}>{test.category}</span>
                                <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', marginLeft: 8 }}>{test.description}</span>
                              </>
                            )}
                          </div>
                          <div className={styles.testIo}>
                            <div>
                              <div className={styles.ioLabel}>{t('common.input')}</div>
                              <pre className={styles.ioPre}>{test.input || t('common.none')}</pre>
                            </div>
                            <div>
                              <div className={styles.ioLabel}>{activeTab === 'boundary' ? 'COBOL Rule/Constraint' : (activeTab === 'p2c' ? 'Python Output' : t('common.expectedCobol'))}</div>
                              <pre className={styles.ioPre}>{activeTab === 'boundary' ? test.cobol_expected_output : test.expected_output}</pre>
                            </div>
                            <div>
                              <div className={styles.ioLabel}>{activeTab === 'boundary' ? 'Python Result' : (activeTab === 'p2c' ? 'COBOL Result' : t('common.actualPython'))}</div>
                              <pre className={styles.ioPre}>{activeTab === 'boundary' ? test.python_actual_output : test.actual_output}</pre>
                            </div>
                          </div>
                        </div>
                      </td>
                    </tr>
                  ))}
                </React.Fragment>
              );
            })}

            {rows.length === 0 && (
              <tr>
                <td colSpan={getColCount()} className={styles.emptyState}>{t('analysis.noAnalysisResults')}</td>
              </tr>
            )}
          </tbody>
        </table>
        </div>
      </ExportWrapper>

      <div className={styles.aiReportContainer}>
        <div className={styles.aiReportContainerContentBorder} />
        <div className={styles.aiReportHeader}>
          <h2 className={styles.aiReportTitle}>
            <Sparkles size={20} className={styles.sparkleIcon} />
            {language === 'tr' ? 'AI Analiz Özeti' : 'AI Analysis Summary'}
          </h2>
          <button 
            className={styles.generateBtn} 
            onClick={handleGenerateExplanation}
            disabled={isGenerating}
          >
            {isGenerating ? (
              <span className={styles.spinner}></span>
            ) : (
              <>
                <Sparkles size={14} />
                {aiExplanation ? (language === 'tr' ? 'Tekrar Oluştur' : 'Regenerate') : (language === 'tr' ? 'Özet Oluştur' : 'Generate Summary')}
              </>
            )}
          </button>
        </div>
        
        {isGenerating ? (
          <div className={styles.loadingWrapper}>
            <div className={styles.spinner}></div>
            <p>{language === 'tr' ? 'AI raporu analiz ediyor...' : 'AI is analyzing the report...'}</p>
          </div>
        ) : aiExplanation ? (
          <div className={styles.aiReportContent}>
            {aiExplanation.split('\n').map((line, i) => {
              if (!line.trim()) return null; // skip empty lines
              // Simple markdown parser for **text**
              const parts = line.split(/(\*\*.*?\*\*)/g);
              return (
                <p key={i}>
                  {parts.map((part, j) => {
                    if (part.startsWith('**') && part.endsWith('**')) {
                      return <strong key={j}>{part.slice(2, -2)}</strong>;
                    }
                    return <span key={j}>{part}</span>;
                  })}
                </p>
              );
            })}
          </div>
        ) : (
          <div className={styles.aiReportContent} style={{ textAlign: 'center', opacity: 0.6 }}>
            <p>{language === 'tr' ? 'Raporun genel bir özetini ve tavsiyeleri almak için özet oluştur butonuna tıklayın.' : 'Click the button above to generate a high-level summary and recommendations based on the analysis results.'}</p>
          </div>
        )}
      </div>
    </main>
  );
}
