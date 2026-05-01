'use client';

import React, { useState, useEffect } from 'react';
import styles from './page.module.css';
import { MOCK_DATA } from '@/lib/data/mockData';
import FileList from '@/components/CodeExplorer/FileList';
import SplitView from '@/components/CodeExplorer/SplitView';
import ModelSelector from '@/components/CodeExplorer/ModelSelector';
import SandboxPanel from '@/components/CodeExplorer/SandboxPanel';
import { AnalysisResult, TestResult, InvalidTestResult } from '@/lib/data/types';
import { getAnalysisResultsAction, runCustomCodeAction } from '@/app/actions';
import { Play, RotateCw } from 'lucide-react';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import { toast } from 'sonner';

export default function ExplorerPage() {
  const [data, setData] = useState<AnalysisResult[]>(MOCK_DATA);
  const [selectedFileId, setSelectedFileId] = useState<string | null>(null);
  const [activeModel, setActiveModel] = useState<string>('');
  const [customCode, setCustomCode] = useState<string>('');
  const [testResults, setTestResults] = useState<TestResult[] | null>(null);
  const [reverseTestResults, setReverseTestResults] = useState<TestResult[] | null>(null);
  const [invalidTestResults, setInvalidTestResults] = useState<InvalidTestResult[] | null>(null);
  const [activeTab, setActiveTab] = useState<'code' | 'tests' | 'tests_reverse' | 'invalid_tests' | 'sandbox'>('code');
  const [loading, setLoading] = useState(false);
  const { t } = useTranslation();

  // Filtering states
  const [testFilterStatus, setTestFilterStatus] = useState<string>('all'); // 'all' | 'passed' | 'failed'
  const [testFilterCategory, setTestFilterCategory] = useState<string>('all'); // 'all' | 'sign_error' | 'whitespace' | 'logic' | 'crash'
  
  const [reverseTestFilterStatus, setReverseTestFilterStatus] = useState<string>('all'); // 'all' | 'passed' | 'failed'
  const [reverseTestFilterCategory, setReverseTestFilterCategory] = useState<string>('all'); // 'all' | 'sign_error' | 'whitespace' | 'logic' | 'crash'

  const [invalidFilterStatus, setInvalidFilterStatus] = useState<string>('all'); // 'all' | 'faithful' | 'unfaithful' | 'crashed'
  const [invalidFilterCategory, setInvalidFilterCategory] = useState<string>('all'); // 'all' | 'overflow' | 'sign_error' | 'alpha_to_numeric' | 'boundary_valid'

  const displayedTestResults = React.useMemo(() => {
    if (!testResults) return null;
    return testResults.filter(t => {
      const statusMatch = testFilterStatus === 'all' || 
                        (testFilterStatus === 'passed' && t.semantic_match) || 
                        (testFilterStatus === 'failed' && !t.semantic_match);
      const catMatch = testFilterCategory === 'all' || t.failure_category === testFilterCategory;
      return statusMatch && catMatch;
    });
  }, [testResults, testFilterStatus, testFilterCategory]);

  const displayedReverseTestResults = React.useMemo(() => {
    if (!reverseTestResults) return null;
    return reverseTestResults.filter(t => {
      const statusMatch = reverseTestFilterStatus === 'all' || 
                        (reverseTestFilterStatus === 'passed' && t.semantic_match) || 
                        (reverseTestFilterStatus === 'failed' && !t.semantic_match);
      const catMatch = reverseTestFilterCategory === 'all' || t.failure_category === reverseTestFilterCategory;
      return statusMatch && catMatch;
    });
  }, [reverseTestResults, reverseTestFilterStatus, reverseTestFilterCategory]);

  const displayedInvalidResults = React.useMemo(() => {
    if (!invalidTestResults) return null;
    return invalidTestResults.filter(t => {
      const statusMatch = invalidFilterStatus === 'all' ||
                        (invalidFilterStatus === 'faithful' && t.cobol_faithful) ||
                        (invalidFilterStatus === 'unfaithful' && !t.cobol_faithful && !t.python_crashed) ||
                        (invalidFilterStatus === 'crashed' && t.python_crashed);
      const catMatch = invalidFilterCategory === 'all' || t.category === invalidFilterCategory;
      return statusMatch && catMatch;
    });
  }, [invalidTestResults, invalidFilterStatus, invalidFilterCategory]);

  // Load existing results on mount
  useEffect(() => {
    async function load() {
      const res = await getAnalysisResultsAction();
      if (res?.success && res.data && res.data.length > 0) {
        setData(res.data);
        setSelectedFileId(res.data[0].id);
        setActiveModel(res.data[0].models[0]?.model_name ?? '');
      } else if (MOCK_DATA.length > 0) {
        setSelectedFileId(MOCK_DATA[0].id);
        setActiveModel(MOCK_DATA[0].models[0]?.model_name ?? '');
      }
    }
    load();
  }, []);

  const selectedFile = data.find(f => f.id === selectedFileId) ?? null;
  const activeModelResult = selectedFile?.models.find(m => m.model_name === activeModel) ?? selectedFile?.models[0];

  // Sync code & test results when file/model selection changes
  // NOTE: We intentionally do NOT change activeTab here — user stays on whichever tab they're viewing
  useEffect(() => {
    const file = data.find(f => f.id === selectedFileId) ?? null;
    const modelResult = file?.models.find(m => m.model_name === activeModel) ?? file?.models[0];
    if (modelResult) {
      setCustomCode(modelResult.python_code);
      setTestResults((modelResult.test_results ?? null) as TestResult[] | null);
      setReverseTestResults((modelResult.python_to_cobol_test_results ?? null) as TestResult[] | null);
      setInvalidTestResults((modelResult.invalid_test_results ?? null) as InvalidTestResult[] | null);
    }
  }, [selectedFileId, activeModel, data]);

  async function handleRunCode() {
    if (!activeModelResult) return;
    setLoading(true);
    try {
      const inputs = activeModelResult.test_results?.map(tr => ({
        input: tr.input,
        expected_output: tr.expected_output,
      })) ?? [];
      const res = await runCustomCodeAction(customCode, inputs);
      if (res.success) {
        // @ts-ignore
        setTestResults(res.detailedResults);
        setActiveTab('tests');
        toast.success(t('common.passed'));
      } else {
        toast.error(t('explorer.executionFailed') + res.error);
      }
    } catch {
      toast.error(t('explorer.unexpectedError'));
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className={styles.main}>
      {/* Header */}
      <div className={styles.pageHeader}>
        <div>
          <h1 className={styles.headerTitle}>{t('explorer.title')}</h1>
          <p className={styles.headerSub}>
            {t('explorer.subtitle')}
          </p>
        </div>
        <button onClick={handleRunCode} disabled={loading || !selectedFile} className={styles.primaryButton}>
          {loading ? <RotateCw className="spin" size={16} /> : <Play size={16} />}
          {loading ? t('explorer.running') : t('explorer.runAndTest')}
        </button>
      </div>

      {/* Tab bar */}
      <div className={styles.tabBar}>
        <button
          className={`${styles.tab} ${activeTab === 'code' ? styles.tabActive : ''}`}
          onClick={() => setActiveTab('code')}
        >
          {t('explorer.codeView')}
        </button>
        <button
          className={`${styles.tab} ${activeTab === 'tests' ? styles.tabActive : ''}`}
          onClick={() => setActiveTab('tests')}
        >
          {t('explorer.testResults')}
          {testResults && testResults.length > 0 && (
            <span className={styles.tabBadge}>{testResults.length}</span>
          )}
        </button>
        <button
          className={`${styles.tab} ${activeTab === 'tests_reverse' ? styles.tabActive : ''}`}
          onClick={() => setActiveTab('tests_reverse')}
        >
          {t('explorer.reverseTestResults')}
          {reverseTestResults && reverseTestResults.length > 0 && (
            <span className={styles.tabBadge}>{reverseTestResults.length}</span>
          )}
        </button>
        <button
          className={`${styles.tab} ${activeTab === 'invalid_tests' ? styles.tabActive : ''}`}
          onClick={() => setActiveTab('invalid_tests')}
        >
          {t('explorer.invalidTests')}
          {invalidTestResults && invalidTestResults.length > 0 && (
            <span className={styles.tabBadge}>{invalidTestResults.length}</span>
          )}
        </button>
        <button
          className={`${styles.tab} ${activeTab === 'sandbox' ? styles.tabActive : ''}`}
          onClick={() => setActiveTab('sandbox')}
          id="tutorial-sandbox-tab"
        >
          {t('explorer.sandbox')}
        </button>
      </div>

      {/* Explorer grid: FileList | Content */}
      <div className={styles.explorerGrid}>
        <FileList
          files={data}
          selectedFileId={selectedFileId}
          onSelectFile={setSelectedFileId}
        />

        <div className={styles.contentArea}>
          {activeTab === 'code' ? (
            <div id="tutorial-split-view" style={{ flex: 1, display: 'flex' }}>
              <SplitView
                selectedFile={selectedFile}
                activeModel={activeModel}
                onModelChange={setActiveModel}
                customCode={customCode}
                onCodeChange={setCustomCode}
                editable={false}
              />
            </div>
          ) : activeTab === 'tests' ? (
            <div className={styles.testPanel} id="tutorial-tests">
              {selectedFile && (
                <ModelSelector
                  models={selectedFile.models}
                  activeModel={activeModel}
                  onModelChange={setActiveModel}
                />
              )}

              {/* Filtering Toolbar for Test Results */}
              <div className={styles.matchLegend} style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <span style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>{t('common.status')}:</span>
                  <select 
                    style={{ background: 'var(--background)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '4px', padding: '0.2rem' }}
                    value={testFilterStatus} 
                    onChange={e => setTestFilterStatus(e.target.value)}
                  >
                    <option value="all">{t('common.all')}</option>
                    <option value="passed">{t('common.passed')}</option>
                    <option value="failed">{t('common.failed')}</option>
                  </select>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <span style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>{t('common.category')}:</span>
                  <select 
                    style={{ background: 'var(--background)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '4px', padding: '0.2rem' }}
                    value={testFilterCategory} 
                    onChange={e => setTestFilterCategory(e.target.value)}
                  >
                    <option value="all">{t('common.all')}</option>
                    <option value="sign_error">{t('explorer.signError')}</option>
                    <option value="whitespace">{t('explorer.whitespace')}</option>
                    <option value="logic">{t('explorer.logic')}</option>
                    <option value="crash">{t('explorer.crash')}</option>
                  </select>
                </div>
              </div>

              <div className={styles.testScroll}>
                {/* Legend */}
                {testResults && testResults.length > 0 && (
                  <div className={styles.matchLegend}>
                    <span style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>{t('explorer.matchStrategies')}</span>
                    <span><span className={styles.badgeHard}>{t('analysis.format')}</span> {t('explorer.formatMatchDesc')}</span>
                    <span><span className={styles.badgeSoft}>{t('analysis.semantic')}</span> {t('explorer.semanticMatchDesc')}</span>
                  </div>
                )}

                {displayedTestResults?.map((test, idx) => (
                  <div
                    key={idx}
                    className={styles.testCard}
                    style={{
                      borderLeftColor: test.format_match
                        ? '#22c55e'
                        : test.semantic_match
                        ? '#f59e0b'
                        : '#ef4444',
                    }}
                  >
                    {/* Card header with badges */}
                    <div className={styles.testCardHeader}>
                      <span className={styles.testCaseLabel}>{t('analysis.testCase')} #{idx + 1}</span>
                      <div className={styles.badgeRow}>
                        <span className={`${styles.badge} ${test.format_match ? styles.badgeGreenOn : styles.badgeOff}`}>
                          {t('analysis.format')} {test.format_match ? '✓' : '✗'}
                        </span>
                        <span className={`${styles.badge} ${test.semantic_match ? styles.badgeAmberOn : styles.badgeOff}`}>
                          {t('analysis.semantic')} {test.semantic_match ? '✓' : '✗'}
                        </span>
                      </div>
                    </div>

                    {/* IO columns */}
                    <div className={styles.testIoGrid}>
                      <div>
                        <div className={styles.ioLabel}>{t('common.input')}</div>
                        <pre className={styles.ioPre}>{test.input || t('common.none')}</pre>
                      </div>
                      <div>
                        <div className={styles.ioLabel}>{t('common.expectedCobol')}</div>
                        <pre className={styles.ioPre}>{test.expected_output}</pre>
                      </div>
                      <div>
                        <div className={styles.ioLabel}>{t('common.actualPython')}</div>
                        <pre className={styles.ioPre}>{test.actual_output}</pre>
                      </div>
                    </div>
                  </div>
                ))}

                {(!testResults || testResults.length === 0) && (
                  <div className={styles.emptyState}>
                    {t('explorer.noTestResults')}
                  </div>
                )}
              </div>
            </div>
          ) : activeTab === 'tests_reverse' ? (
            <div className={styles.testPanel}>
              {selectedFile && (
                <ModelSelector
                  models={selectedFile.models}
                  activeModel={activeModel}
                  onModelChange={setActiveModel}
                />
              )}

              {/* Filtering Toolbar for Reverse Test Results */}
              <div className={styles.matchLegend} style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <span style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>{t('common.status')}:</span>
                  <select 
                    style={{ background: 'var(--background)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '4px', padding: '0.2rem' }}
                    value={reverseTestFilterStatus} 
                    onChange={e => setReverseTestFilterStatus(e.target.value)}
                  >
                    <option value="all">{t('common.all')}</option>
                    <option value="passed">{t('common.passed')}</option>
                    <option value="failed">{t('common.failed')}</option>
                  </select>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <span style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>{t('common.category')}:</span>
                  <select 
                    style={{ background: 'var(--background)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '4px', padding: '0.2rem' }}
                    value={reverseTestFilterCategory} 
                    onChange={e => setReverseTestFilterCategory(e.target.value)}
                  >
                    <option value="all">{t('common.all')}</option>
                    <option value="sign_error">{t('explorer.signError')}</option>
                    <option value="whitespace">{t('explorer.whitespace')}</option>
                    <option value="logic">{t('explorer.logic')}</option>
                    <option value="crash">{t('explorer.crash')}</option>
                  </select>
                </div>
              </div>

              <div className={styles.testScroll}>
                {/* Legend */}
                {reverseTestResults && reverseTestResults.length > 0 && (
                  <div className={styles.matchLegend}>
                    <span style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>{t('explorer.matchStrategies')}</span>
                    <span><span className={styles.badgeHard}>{t('analysis.format')}</span> {t('explorer.formatMatchDesc')}</span>
                    <span><span className={styles.badgeSoft}>{t('analysis.semantic')}</span> {t('explorer.semanticMatchDesc')}</span>
                  </div>
                )}

                {displayedReverseTestResults?.map((test, idx) => (
                  <div
                    key={idx}
                    className={styles.testCard}
                    style={{
                      borderLeftColor: test.format_match
                        ? '#22c55e'
                        : test.semantic_match
                        ? '#f59e0b'
                        : '#ef4444',
                    }}
                  >
                    {/* Card header with badges */}
                    <div className={styles.testCardHeader}>
                      <span className={styles.testCaseLabel}>{t('analysis.testCase')} #{idx + 1}</span>
                      <div className={styles.badgeRow}>
                        <span className={`${styles.badge} ${test.format_match ? styles.badgeGreenOn : styles.badgeOff}`}>
                          {t('analysis.format')} {test.format_match ? '✓' : '✗'}
                        </span>
                        <span className={`${styles.badge} ${test.semantic_match ? styles.badgeAmberOn : styles.badgeOff}`}>
                          {t('analysis.semantic')} {test.semantic_match ? '✓' : '✗'}
                        </span>
                      </div>
                    </div>

                    {/* IO columns */}
                    <div className={styles.testIoGrid}>
                      <div>
                        <div className={styles.ioLabel}>{t('common.input')} (Generated by Python LLM)</div>
                        <pre className={styles.ioPre}>{test.input || t('common.none')}</pre>
                      </div>
                      <div>
                        <div className={styles.ioLabel}>{t('common.expectedCobol')} (Python Baseline)</div>
                        <pre className={styles.ioPre}>{test.expected_output}</pre>
                      </div>
                      <div>
                        <div className={styles.ioLabel}>{t('common.actualPython')} (COBOL Output)</div>
                        <pre className={styles.ioPre}>{test.actual_output}</pre>
                      </div>
                    </div>
                  </div>
                ))}

                {(!reverseTestResults || reverseTestResults.length === 0) && (
                  <div className={styles.emptyState}>
                    {t('explorer.noTestResults')}
                  </div>
                )}
              </div>
            </div>
          ) : activeTab === 'invalid_tests' ? (
            <div className={styles.testPanel}>
              {selectedFile && (
                <ModelSelector
                  models={selectedFile.models}
                  activeModel={activeModel}
                  onModelChange={setActiveModel}
                />
              )}

              {/* Filtering Toolbar for Invalid Tests */}
              <div className={styles.matchLegend} style={{ display: 'flex', gap: '1rem', flexWrap: 'wrap' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <span style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>{t('common.status')}:</span>
                  <select 
                    style={{ background: 'var(--background)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '4px', padding: '0.2rem' }}
                    value={invalidFilterStatus} 
                    onChange={e => setInvalidFilterStatus(e.target.value)}
                  >
                    <option value="all">{t('common.all')}</option>
                    <option value="faithful">{t('dashboard.faithful')}</option>
                    <option value="unfaithful">{t('dashboard.unfaithful')}</option>
                    <option value="crashed">{t('analysis.crashed')}</option>
                  </select>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <span style={{ color: 'var(--text-secondary)', fontWeight: 600 }}>{t('common.category')}:</span>
                  <select 
                    style={{ background: 'var(--background)', color: 'var(--text)', border: '1px solid var(--border)', borderRadius: '4px', padding: '0.2rem' }}
                    value={invalidFilterCategory} 
                    onChange={e => setInvalidFilterCategory(e.target.value)}
                  >
                    <option value="all">{t('common.all')}</option>
                    <option value="overflow">{t('explorer.overflow')}</option>
                    <option value="sign_error">{t('explorer.signError')}</option>
                    <option value="alpha_to_numeric">{t('explorer.alphaToNumeric')}</option>
                    <option value="boundary_valid">{t('explorer.boundaryValid')}</option>
                  </select>
                </div>
              </div>

              <div className={styles.testScroll}>
                {displayedInvalidResults?.map((test, idx) => (
                  <div
                    key={idx}
                    className={styles.testCard}
                    style={{
                      borderLeftColor: test.cobol_faithful ? '#22c55e' : test.python_crashed ? '#ef4444' : '#f59e0b',
                    }}
                  >
                    <div className={styles.testCardHeader}>
                      <span className={styles.testCaseLabel}>{t('analysis.invalidCase')} #{idx + 1} ({test.category})</span>
                      <div className={styles.badgeRow}>
                        <span className={`${styles.badge} ${test.cobol_faithful ? styles.badgeGreenOn : styles.badgeOff}`}>
                          {t('analysis.faithful')} {test.cobol_faithful ? '✓' : '✗'}
                        </span>
                        {test.python_crashed && (
                          <span className={`${styles.badge} ${styles.badgeOff}`}>
                            {t('analysis.crashed')}
                          </span>
                        )}
                      </div>
                    </div>
                    
                    <div style={{ marginBottom: '0.75rem', fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                      <strong>{t('common.desc')}:</strong> {test.description}
                    </div>

                    <div className={styles.testIoGrid}>
                      <div>
                        <div className={styles.ioLabel}>{t('common.input')}</div>
                        <pre className={styles.ioPre}>{test.input || t('common.none')}</pre>
                      </div>
                      <div>
                        <div className={styles.ioLabel}>{t('common.expectedCobol')}</div>
                        <pre className={styles.ioPre}>{test.cobol_expected_output}</pre>
                      </div>
                      <div>
                        <div className={styles.ioLabel}>{t('common.actualPython')}</div>
                        <pre className={styles.ioPre}>{test.python_actual_output}</pre>
                      </div>
                    </div>
                  </div>
                ))}

                {(!invalidTestResults || invalidTestResults.length === 0) && (
                  <div className={styles.emptyState}>
                    {t('explorer.noInvalidTestCases')}
                  </div>
                )}
              </div>
            </div>
          ) : activeTab === 'sandbox' ? (
            <div className={styles.testPanel}>
              {selectedFile && (
                <ModelSelector
                  models={selectedFile.models}
                  activeModel={activeModel}
                  onModelChange={setActiveModel}
                />
              )}
              <SandboxPanel 
                cobolCode={selectedFile?.cobol_code || ''}
                pythonCode={customCode}
              />
            </div>
          ) : null}
        </div>
      </div>
    </main>
  );
}
