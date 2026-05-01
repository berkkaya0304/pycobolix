import React, { useState } from 'react';
import { Play, RotateCw } from 'lucide-react';
import styles from './SandboxPanel.module.css';
import { TestResult } from '@/lib/data/types';
import { runInteractiveSandboxAction } from '@/app/actions';
import { useTranslation } from '@/lib/i18n/LanguageContext';

interface SandboxPanelProps {
  cobolCode: string;
  pythonCode: string;
}

export default function SandboxPanel({ cobolCode, pythonCode }: SandboxPanelProps) {
  const [input, setInput] = useState<string>('');
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState<TestResult | null>(null);
  const [error, setError] = useState<string | null>(null);
  const { t } = useTranslation();

  const handleRun = async () => {
    if (!cobolCode || !pythonCode) {
      setError(t('sandbox.bothRequired'));
      return;
    }
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const res = await runInteractiveSandboxAction(cobolCode, pythonCode, input);
      if (res.success && 'result' in res && res.result) {
        setResult(res.result as TestResult);
      } else {
        setError(res.error || t('sandbox.executionFailed'));
      }
    } catch (e: any) {
      setError(t('sandbox.unexpectedError') + e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.sandboxContainer}>
      <div className={styles.inputSection}>
        <label className={styles.label}>{t('sandbox.customStdin')}</label>
        <textarea
          className={styles.textarea}
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder={t('sandbox.placeholder')}
          spellCheck={false}
        />
        <div className={styles.actionRow}>
          <button
            className={styles.runButton}
            onClick={handleRun}
            disabled={loading || !cobolCode || !pythonCode}
          >
            {loading ? <RotateCw className="spin" size={16} /> : <Play size={16} />}
            {loading ? t('sandbox.running') : t('sandbox.runInSandbox')}
          </button>
          {error && <div className={styles.errorMsg}>{error}</div>}
        </div>
      </div>

      {result && (
        <div className={styles.resultsSection}>
          <div className={styles.badgeRow}>
            <span className={`${styles.badge} ${result.format_match ? styles.badgeGreenOn : styles.badgeOff}`}>
              {t('analysis.format')} {result.format_match ? '✓' : '✗'}
            </span>
            <span className={`${styles.badge} ${result.semantic_match ? styles.badgeAmberOn : styles.badgeOff}`}>
              {t('analysis.semantic')} {result.semantic_match ? '✓' : '✗'}
            </span>
          </div>

          <div className={styles.splitOutputs}>
            <div className={styles.outputBox}>
              <div className={styles.outputHeader}>
                <span>{t('sandbox.cobolOutput')}</span>
              </div>
              <pre className={styles.outputPre}>{result.expected_output || t('sandbox.noOutput')}</pre>
            </div>
            <div className={styles.outputBox}>
              <div className={styles.outputHeader}>
                <span>{t('sandbox.pythonOutput')}</span>
                {result.exec_time_ms !== undefined && (
                  <span>{result.exec_time_ms} ms</span>
                )}
              </div>
              <pre className={styles.outputPre}>{result.actual_output || t('sandbox.noOutput')}</pre>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
