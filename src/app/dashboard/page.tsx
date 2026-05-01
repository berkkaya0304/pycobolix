'use client';

import React, { useState, useEffect } from 'react';
import styles from './page.module.css';
import { MOCK_DATA } from '@/lib/data/mockData';
import ScoreCards from '@/components/Dashboard/ScoreCards';
import ModelComparison from '@/components/Dashboard/ModelComparison';
import ComplexityChart from '@/components/Dashboard/ComplexityChart';
import MatchComparisonChart from '@/components/Dashboard/MatchComparisonChart';
import TestOutcomeDistributionChart from '@/components/Dashboard/TestOutcomeDistributionChart';
import MaintainabilityChart from '@/components/Dashboard/MaintainabilityChart';
import ModelStatsTable from '@/components/Dashboard/ModelStatsTable';
import HardSoftDeltaChart from '@/components/Dashboard/HardSoftDeltaChart';
import ConsensusFailureChart from '@/components/Dashboard/ConsensusFailureChart';
import ErrorPatternChart from '@/components/Dashboard/ErrorPatternChart';
import MetricLegend from '@/components/Dashboard/MetricLegend';
import BoundaryFaithfulnessChart from '@/components/Dashboard/BoundaryFaithfulnessChart';
import { AnalysisResult } from '@/lib/data/types';
import { runAnalysisAction, getAnalysisResultsAction, generateAnalysisExplanationAction } from '@/app/actions';
import { Play, RotateCw, Download, BarChart3, Activity, PieChart, Target, FileText } from 'lucide-react';
import { pdf } from '@react-pdf/renderer';
import { ReactPDFReport } from '@/lib/report/ReactPDFReport';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import { en } from '@/lib/i18n/dictionaries/en';
import { tr } from '@/lib/i18n/dictionaries/tr';
import { toast } from 'sonner';
import { deepSanitize } from '@/lib/utils/pdfSanitizer';

export default function DashboardPage() {
  const [data, setData]             = useState<AnalysisResult[]>(MOCK_DATA);
  const [loading, setLoading]       = useState(false);
  const [loadingProgress, setLoadingProgress] = useState('');
  const [loadingPercent, setLoadingPercent] = useState<number | null>(null);
  const [pdfLoading, setPdfLoading] = useState(false);
  const [activeTab, setActiveTab]   = useState<'cobol-to-python' | 'python-to-cobol' | 'additional'>('cobol-to-python');
  const { t, language } = useTranslation();

  useEffect(() => {
    async function loadInitial() {
      const res = await getAnalysisResultsAction();
      if (res && res.success && res.data && res.data.length > 0) {
        setData(res.data);
      }
    }
    loadInitial();
  }, []);

  const handleRunAnalysis = async () => {
    setLoading(true);
    setLoadingProgress(t('dashboard.analyzing') || 'Starting analysis...');
    setLoadingPercent(0);
    
    try {
      const eventSource = new EventSource('/api/analyze');

      eventSource.onmessage = async (e) => {
        try {
          const payload = JSON.parse(e.data);
          if (payload.type === 'progress') {
            setLoadingProgress(payload.message);
            // Attempt to parse "(File X of Y)" from the message to compute percentage
            const match = payload.message.match(/\(File (\d+) of (\d+)\)/);
            if (match) {
               const current = parseInt(match[1], 10);
               const total = parseInt(match[2], 10);
               if (total > 0) {
                 setLoadingPercent(Math.round((current / total) * 100));
               }
            }
          } else if (payload.type === 'complete') {
            eventSource.close();
            // Fetch the final results since the SSE doesn't return the full dataset directly
            const res = await getAnalysisResultsAction();
            if (res && res.success && res.data) {
              setData(res.data);
              toast.success("Analysis completed successfully");
            } else {
              toast.error("Analysis finished, but failed to load results.");
            }
            setLoading(false);
            setLoadingPercent(null);
          } else if (payload.type === 'error') {
            eventSource.close();
            setLoading(false);
            setLoadingPercent(null);
            
            if (payload.message === 'NO_MODEL_SELECTED' || payload.message === 'MODEL_NOT_INSTALLED') {
              toast.error(t('dashboard.modelNotSelectedError'));
            } else if (payload.message === 'OLLAMA_NOT_REACHABLE') {
              toast.error(t('dashboard.ollamaNotReachableError'));
            } else {
              toast.error(t('dashboard.analysisFailed') + payload.message);
            }
          }
        } catch (err) {
          console.error('Failed to parse SSE data', err);
        }
      };

      eventSource.onerror = (e) => {
        console.error('SSE connection error', e);
        eventSource.close();
        setLoading(false);
        setLoadingPercent(null);
        toast.error('Lost connection to the analysis server.');
      };
      
    } catch {
      toast.error(t('dashboard.unexpectedError'));
      setLoading(false);
      setLoadingPercent(null);
    }
  };

  const displayData = React.useMemo(() => {
    if (activeTab === 'cobol-to-python' || activeTab === 'additional') return data;
    // Remap python-to-cobol metrics onto the standard ones so charts reuse them cleanly
    return data.map(file => ({
      ...file,
      models: file.models.map(model => ({
        ...model,
        metrics: {
          ...model.metrics,
          unit_tests_total: model.metrics.python_to_cobol_unit_tests_total ?? 0,
          unit_tests_passed: model.metrics.python_to_cobol_semantic_match_passed ?? 0,
          format_match_passed: model.metrics.python_to_cobol_format_match_passed ?? 0,
        },
        test_results: model.python_to_cobol_test_results ?? []
      }))
    }));
  }, [data, activeTab]);

  const allModelResults = displayData.flatMap(r => r.models);

  const downloadPDF = async () => {
    setPdfLoading(true);
    try {
      const lang = document.documentElement.lang || 'en';
      const explRes = await generateAnalysisExplanationAction(data, lang);
      const explanation = explRes.success ? explRes.data : undefined;
      const dict = language === 'tr' ? tr : en;
      
      console.log('[PDF Debug] Pre-sanitization check in page.tsx...');
      const sData = deepSanitize(data, 'data');
      const sExpl = deepSanitize(explanation, 'explanation');
      const sDict = deepSanitize(dict, 'dict');
      
      console.log('[PDF Debug] Sanitized data ready for ReactPDFReport', { sData, sExpl });
      
      const blob = await pdf(<ReactPDFReport data={sData} aiComments={sExpl} dict={sDict} />).toBlob();
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `modernization_report_${new Date().toISOString().slice(0, 10)}.pdf`;
      link.click();
      URL.revokeObjectURL(url);
    } catch (err) {
      console.error('Failed to generate PDF:', err);
      toast.error('Failed to generate PDF');
    } finally {
      setPdfLoading(false);
    }
  };

  return (
    <main className={styles.main}>
      {/* Header */}
      <div className={styles.pageHeader}>
        <div>
          <h1 className={styles.headerTitle}>{t('dashboard.title')}</h1>
          <p className={styles.headerSub}>
            {t('dashboard.subtitle')}
          </p>
        </div>
        <div style={{ display: 'flex', gap: '0.75rem' }}>
          <button onClick={downloadPDF} disabled={pdfLoading} className={styles.secondaryButton}>
            {pdfLoading ? <RotateCw className="spin" size={16} /> : <Download size={16} />}
            {pdfLoading ? t('dashboard.generatingPdf') : t('dashboard.report')}
          </button>
          <button onClick={handleRunAnalysis} disabled={loading} className={styles.primaryButton}>
            {loading ? <RotateCw className="spin" size={16} /> : <Play size={16} />}
            {loading ? (loadingPercent !== null ? `${loadingPercent}%` : t('dashboard.analyzing')) : t('dashboard.runAnalysis')}
          </button>
        </div>
      </div>

      {/* Tab Toggle */}
      <div className={styles.directionToggleContainer} id="tutorial-tabs">
        <div className={styles.toggleGroup}>
          <button
            className={`${styles.toggleBtn} ${activeTab === 'cobol-to-python' ? styles.active : ''}`}
            onClick={() => setActiveTab('cobol-to-python')}
          >
            {t('dashboard.cobolToPython')}
          </button>
          <button
            className={`${styles.toggleBtn} ${activeTab === 'python-to-cobol' ? styles.active : ''}`}
            onClick={() => setActiveTab('python-to-cobol')}
          >
            {t('dashboard.pythonToCobol')}
          </button>
          <button
            className={`${styles.toggleBtn} ${activeTab === 'additional' ? styles.active : ''}`}
            onClick={() => setActiveTab('additional')}
          >
            {t('dashboard.additionalData')}
          </button>
        </div>
      </div>

      {/* Metric Legend (collapsible Turkish glossary) */}
      <div id="tutorial-glossary">
        <MetricLegend activeTab={activeTab} />
      </div>

      {/* Score Cards */}
      <section id="tutorial-score-cards">
        <ScoreCards data={displayData} viewType={activeTab === 'additional' ? 'additional' : 'directional'} activeTab={activeTab} />
      </section>

      {/* Charts — responsive grid */}
      {(activeTab === 'cobol-to-python' || activeTab === 'python-to-cobol') && (
        <>
          <section className={styles.sectionContainer}>
            <div className={styles.sectionHeader}>
              <div className={styles.sectionIcon}><BarChart3 size={20} /></div>
              <div className={styles.sectionTitleGroup}>
                <h2 className={styles.sectionTitle}>{t('dashboard.modelMetrics')}</h2>
                <p className={styles.sectionSubtitle}>{t('dashboard.modelMetricsSub')}</p>
              </div>
            </div>
            <div className={styles.chartsGrid}>
              <ModelComparison data={displayData} />
              <MatchComparisonChart data={displayData} />
            </div>
          </section>

          <section className={styles.sectionContainer}>
            <div className={styles.sectionHeader}>
              <div className={styles.sectionIcon}><Activity size={20} /></div>
              <div className={styles.sectionTitleGroup}>
                <h2 className={styles.sectionTitle}>{t('dashboard.differentialAnalysis')}</h2>
                <p className={styles.sectionSubtitle}>{t('dashboard.differentialAnalysisSub')}</p>
              </div>
            </div>
            <div className={styles.chartsGrid}>
              <TestOutcomeDistributionChart data={displayData} />
              <HardSoftDeltaChart data={displayData} />
              <ConsensusFailureChart data={displayData} />
              <ErrorPatternChart data={displayData} />
            </div>
          </section>
        </>
      )}

      {activeTab === 'additional' && (
        <>
          <section className={styles.sectionContainer}>
            <div className={styles.sectionHeader}>
              <div className={styles.sectionIcon}><PieChart size={20} /></div>
              <div className={styles.sectionTitleGroup}>
                <h2 className={styles.sectionTitle}>{t('dashboard.modelMetrics')}</h2>
                <p className={styles.sectionSubtitle}>{t('dashboard.modelMetricsSub')}</p>
              </div>
            </div>
            <div className={styles.chartsGrid}>
              <ComplexityChart data={displayData} />
              <MaintainabilityChart data={displayData} />
            </div>
          </section>

          <section className={styles.sectionContainer}>
            <div className={styles.sectionHeader}>
              <div className={styles.sectionIcon}><Target size={20} /></div>
              <div className={styles.sectionTitleGroup}>
                <h2 className={styles.sectionTitle}>{t('dashboard.cobolBoundaryFaithfulness')}</h2>
                <p className={styles.sectionSubtitle}>{t('dashboard.cobolBoundaryDesc')}</p>
              </div>
            </div>
            <BoundaryFaithfulnessChart data={displayData} />
          </section>
        </>
      )}

      {/* Research Summary Table */}
      <section className={styles.sectionContainer}>
        <div className={styles.sectionHeader}>
          <div className={styles.sectionIcon}><FileText size={20} /></div>
          <div className={styles.sectionTitleGroup}>
            <h2 className={styles.sectionTitle}>{t('dashboard.researchSummary')}</h2>
            <p className={styles.sectionSubtitle}>{t('dashboard.researchSummarySub')}</p>
          </div>
        </div>
        <ModelStatsTable data={displayData} viewType={activeTab === 'additional' ? 'additional' : 'directional'} />
      </section>
    </main>
  );
}
