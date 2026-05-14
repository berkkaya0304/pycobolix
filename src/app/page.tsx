'use client';

import React, { useState, useEffect, useRef } from 'react';
import styles from './page.module.css';
import {
  getSettingsAction,
  saveSettingsAction,
  listOllamaModelsAction,
  listOllamaCloudModelsAction,
  getPythonModelDirsAction,
  uploadPythonModelDirAction,
  getCobolFilesAction,
  uploadCobolFilesAction,
  runAnalysisAction,
  deletePythonModelDirAction,
  deleteCobolFileAction,
} from '@/app/actions';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import { toast } from 'sonner';
import {
  Zap, Server, Cloud, FolderOpen, ArrowRight, Check,
  RotateCw,
  Bot, UploadCloud, RefreshCw, Key, Cpu, FileCode2, Trash2,
} from 'lucide-react';
import { useRouter } from 'next/navigation';

type Provider = 'ollama-local' | 'ollama-cloud' | 'gemini';

export default function LandingPage() {
  const { t } = useTranslation();
  const router = useRouter();
  const pyFolderRef   = useRef<HTMLInputElement>(null);
  const cblFolderRef  = useRef<HTMLInputElement>(null);

  // ─── Test Case AI Provider ───────────────────────────────────────────────
  const [provider, setProvider]                         = useState<Provider>('ollama-local');
  // ollama-local
  const [ollamaModel, setOllamaModel]                   = useState('');
  const [ollamaUrl, setOllamaUrl]                       = useState('http://localhost:11434');
  const [localModels, setLocalModels]                   = useState<any[]>([]);
  const [modelsLoading, setModelsLoading]               = useState(false);
  // ollama-cloud
  const [cloudUrl, setCloudUrl]                         = useState('');
  const [cloudApiKey, setCloudApiKey]                   = useState('');
  const [cloudModel, setCloudModel]                     = useState('');
  const [cloudModels, setCloudModels]                   = useState<any[]>([]);
  const [cloudModelsLoading, setCloudModelsLoading]     = useState(false);
  // gemini
  const [geminiApiKey, setGeminiApiKey]                 = useState('');
  const [geminiModel, setGeminiModel]                   = useState('gemini-2.5-pro');

  // ─── Python Translation Models ───────────────────────────────────────────
  const [pythonModels, setPythonModels]                 = useState<string[]>([]);
  const [newPyModelName, setNewPyModelName]             = useState('');
  const [selectedPyFolder, setSelectedPyFolder]         = useState<FileList | null>(null);
  const [addingPy, setAddingPy]                         = useState(false);
  const [showTranslateAi, setShowTranslateAi]           = useState(false);
  const [translating, setTranslating]                   = useState(false);
  // ─── COBOL Source Files ──────────────────────────────────────────────────
  const [cobolFiles, setCobolFiles]                     = useState<string[]>([]);
  const [selectedCblFiles, setSelectedCblFiles]         = useState<FileList | null>(null);
  const [uploadingCbl, setUploadingCbl]                 = useState(false);
  const [llmRetryCount, setLlmRetryCount]               = useState(3);

  // ─── Page ────────────────────────────────────────────────────────────────
  const [pageLoading, setPageLoading]                   = useState(true);
  const [analyzing, setAnalyzing]                       = useState(false);
  const [progressMessage, setProgressMessage]           = useState('Initializing analysis...');
  const [loadingPercent, setLoadingPercent]             = useState<number | null>(null);
  const [startTime, setStartTime]                       = useState<number | null>(null);
  const [elapsedSeconds, setElapsedSeconds]             = useState(0);

  useEffect(() => {
    let timer: NodeJS.Timeout | undefined;
    if ((analyzing || translating) && startTime) {
      timer = setInterval(() => {
        setElapsedSeconds(Math.floor((Date.now() - startTime) / 1000));
      }, 1000);
    } else {
      setElapsedSeconds(0);
    }
    return () => clearInterval(timer);
  }, [analyzing, translating, startTime]);

  // ─── Load initial ────────────────────────────────────────────────────────
  useEffect(() => {
    async function load() {
      const [st, ollList, pyDirs, cblList] = await Promise.all([
        getSettingsAction(),
        listOllamaModelsAction(),
        getPythonModelDirsAction(),
        getCobolFilesAction(),
      ]);
      if (st.success && st.data) {
        setProvider(st.data.llmProvider || 'ollama-local');
        setOllamaModel(st.data.ollamaModel || '');
        setOllamaUrl(st.data.ollamaBaseUrl || 'http://localhost:11434');
        setGeminiApiKey(st.data.geminiApiKey || '');
        setGeminiModel(st.data.geminiModel || 'gemini-2.5-pro');
        setCloudUrl(st.data.ollamaCloudBaseUrl || '');
        setCloudApiKey(st.data.ollamaCloudApiKey || '');
        setCloudModel(st.data.ollamaCloudModel || '');
        setLlmRetryCount(st.data.llmRetryCount || 3);
      }
      if (ollList.success && ollList.data) setLocalModels(ollList.data);
      if (pyDirs.success && pyDirs.data)   setPythonModels(pyDirs.data);
      if (cblList.success && cblList.data) setCobolFiles(cblList.data);
      setPageLoading(false);
    }
    load();
  }, []);

  // ─── Helpers ────────────────────────────────────────────────────────────
  const save = (patch: Record<string, any>) => saveSettingsAction(patch as any);

  const handleSelectProvider = async (p: Provider) => {
    setProvider(p);
    await save({ llmProvider: p });
  };

  const refreshLocalModels = async () => {
    setModelsLoading(true);
    const res = await listOllamaModelsAction();
    if (res.success && res.data) setLocalModels(res.data);
    setModelsLoading(false);
  };

  const fetchCloudModels = async () => {
    if (!cloudUrl.trim()) return;
    setCloudModelsLoading(true);
    const res = await listOllamaCloudModelsAction(cloudUrl, cloudApiKey);
    if (res.success && res.data) setCloudModels(res.data);
    else { setCloudModels([]); toast.error('Could not fetch cloud models'); }
    setCloudModelsLoading(false);
  };

  // ─── Add Python model ────────────────────────────────────────────────────
  const handleAddPyModel = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newPyModelName.trim() || !selectedPyFolder || selectedPyFolder.length === 0) return;
    setAddingPy(true);
    const fd = new FormData();
    fd.append('modelName', newPyModelName);
    let count = 0;
    Array.from(selectedPyFolder).forEach(f => {
      if (f.name.endsWith('.py')) { fd.append('files', f); count++; }
    });
    if (count === 0) { toast.error('No .py files in selected folder'); setAddingPy(false); return; }
    const res = await uploadPythonModelDirAction(fd);
    if (res.success && res.data) {
      toast.success(`Model added — ${res.data.count} file(s)`);
      setPythonModels(prev => [...prev, res.data.name]);
      setNewPyModelName('');
      setSelectedPyFolder(null);
      if (pyFolderRef.current) pyFolderRef.current.value = '';
    } else {
      toast.error('Error: ' + res.error);
    }
    setAddingPy(false);
  };

  // ─── Upload COBOL files ──────────────────────────────────────────────────
  const handleUploadCbl = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!selectedCblFiles || selectedCblFiles.length === 0) return;
    setUploadingCbl(true);
    const fd = new FormData();
    Array.from(selectedCblFiles).forEach(f => fd.append('files', f));
    const res = await uploadCobolFilesAction(fd);
    if (res.success && res.data) {
      toast.success(`Uploaded ${res.data.count} COBOL file(s)`);
      // Reload list
      const list = await getCobolFilesAction();
      if (list.success && list.data) setCobolFiles(list.data);
      setSelectedCblFiles(null);
      if (cblFolderRef.current) cblFolderRef.current.value = '';
    } else {
      toast.error('Error: ' + res.error);
    }
    setUploadingCbl(false);
  };

  // ─── Delete Actions ──────────────────────────────────────────────────────
  const handleDeletePyModel = async (name: string) => {
    if (!confirm(`Are you sure you want to delete the model "${name}"?`)) return;
    const res = await deletePythonModelDirAction(name);
    if (res.success) {
      toast.success(`Deleted model "${name}"`);
      setPythonModels(prev => prev.filter(m => m !== name));
    } else {
      toast.error('Error: ' + res.error);
    }
  };

  const handleDeleteCobolFile = async (filename: string) => {
    if (!confirm(`Are you sure you want to delete "${filename}"?`)) return;
    const res = await deleteCobolFileAction(filename);
    if (res.success) {
      toast.success(`Deleted file "${filename}"`);
      setCobolFiles(prev => prev.filter(f => f !== filename));
    } else {
      toast.error('Error: ' + res.error);
    }
  };

  // ─── AI Translation Action ───────────────────────────────────────────────
  const handleTranslateAll = async () => {
    if (!newPyModelName.trim() || cobolFiles.length === 0) return;
    setTranslating(true);
    setStartTime(Date.now());
    setProgressMessage('Starting AI translation...');
    await saveSettingsAction({
      llmProvider:       provider,
      ollamaModel,
      ollamaBaseUrl:     ollamaUrl,
      geminiApiKey,
      geminiModel,
      ollamaCloudBaseUrl:  cloudUrl,
      ollamaCloudApiKey:   cloudApiKey,
      ollamaCloudModel:    cloudModel,
    });
    
    const eventSource = new EventSource(`/api/translate?modelName=${encodeURIComponent(newPyModelName)}`);
    eventSource.onmessage = (e) => {
      try {
        const data = JSON.parse(e.data);
        if (data.type === 'progress') {
          setProgressMessage(data.message);
          const match = data.message.match(/File (\d+) of (\d+)/);
          if (match) {
             const current = parseInt(match[1], 10);
             const total = parseInt(match[2], 10);
             if (total > 0) setLoadingPercent(Math.round((current / total) * 100));
          }
        } else if (data.type === 'complete') {
          eventSource.close();
          setLoadingPercent(null);
          setTranslating(false);
          toast.success(`Translation complete! Model "${newPyModelName}" added.`);
          setPythonModels(prev => [...prev, newPyModelName]);
          setNewPyModelName('');
          setShowTranslateAi(false);
        } else if (data.type === 'error') {
          eventSource.close();
          setTranslating(false);
          setLoadingPercent(null);
          toast.error('Translation failed: ' + data.message);
        }
      } catch (err) {
        console.error('Failed to parse SSE', err);
      }
    };
    eventSource.onerror = (e) => {
      console.error('SSE connection error', e);
      eventSource.close();
      setTranslating(false);
      setLoadingPercent(null);
      toast.error('Lost connection to the translation server.');
    };
  };

  // ─── Continue — save all, run analysis, redirect ─────────────────────────
  const handleContinue = async () => {
    setAnalyzing(true);
    setStartTime(Date.now());
    setProgressMessage('Initializing analysis environment...');
    // Save all settings atomically before running
    await saveSettingsAction({
      llmProvider:       provider,
      ollamaModel,
      ollamaBaseUrl:     ollamaUrl,
      geminiApiKey,
      geminiModel,
      ollamaCloudBaseUrl:  cloudUrl,
      ollamaCloudApiKey:   cloudApiKey,
      ollamaCloudModel:    cloudModel,
    });
    
    const eventSource = new EventSource('/api/analyze');
    
    eventSource.onmessage = (e) => {
      try {
        const data = JSON.parse(e.data);
        if (data.type === 'progress') {
          setProgressMessage(data.message);
          const match = data.message.match(/\(File (\d+) of (\d+)\)/);
          if (match) {
             const current = parseInt(match[1], 10);
             const total = parseInt(match[2], 10);
             if (total > 0) {
               setLoadingPercent(Math.round((current / total) * 100));
             }
          }
        } else if (data.type === 'complete') {
          eventSource.close();
          setLoadingPercent(null);
          router.push('/dashboard');
        } else if (data.type === 'error') {
          eventSource.close();
          setAnalyzing(false);
          setLoadingPercent(null);
          toast.error('Analysis failed: ' + data.message);
        }
      } catch (err) {
        console.error('Failed to parse SSE data', err);
      }
    };

    eventSource.onerror = (e) => {
      console.error('SSE connection error', e);
      eventSource.close();
      setAnalyzing(false);
      setLoadingPercent(null);
      toast.error('Lost connection to the analysis server.');
    };
  };

  // ─── Shared sub-components ───────────────────────────────────────────────
  function RadioList({ items, active, onSelect }: {
    items: { name: string }[];
    active: string;
    onSelect: (name: string) => void;
  }) {
    if (items.length === 0) return <div className={styles.emptyState}>No models found.</div>;
    return (
      <div className={styles.modelScroll}>
        {items.map(m => (
          <button
            key={m.name}
            className={`${styles.modelRadioItem} ${m.name === active ? styles.modelRadioItemActive : ''}`}
            onClick={() => onSelect(m.name)}
          >
            <span className={`${styles.radioCircle} ${m.name === active ? styles.radioCircleFilled : ''}`} />
            {m.name}
          </button>
        ))}
      </div>
    );
  }

  // ─── Loading overlays ────────────────────────────────────────────────────
  if (analyzing || translating) {
    return (
      <div className={styles.loadingOverlay}>
        <div className={styles.spinnerRing} />
        <div className={styles.loadingTitle}>
          {translating ? 'Translating COBOL...' : 'Running Analysis'}{loadingPercent !== null ? ` (${loadingPercent}%)` : '…'}
        </div>
        
        <div className={styles.loadingSubtitle} style={{ fontWeight: 500, color: 'var(--accent-color)', minHeight: '1.5rem' }}>
          {progressMessage}
        </div>
        
        <div className={styles.loadingSubtitle} style={{ marginTop: '0.5rem', fontSize: '1.1rem', fontWeight: 'bold' }}>
          Time Elapsed: {Math.floor(elapsedSeconds / 60)}m {String(elapsedSeconds % 60).padStart(2, '0')}s
        </div>

        <div className={styles.loadingSubtitle} style={{ marginTop: '1rem', fontSize: '0.9rem', opacity: 0.8 }}>
          {translating 
            ? 'Translating COBOL source files into Python using AI.' 
            : 'Generating test cases, executing COBOL & Python programs, and computing metrics. Please wait.'}
        </div>
      </div>
    );
  }
  if (pageLoading) return <div className={styles.loadingOverlay}><div className={styles.spinnerRing} /></div>;

  return (
    <main className={styles.main}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', width: '100%', maxWidth: '1000px', margin: '0 auto', paddingBottom: '1rem' }}>
        <div>
          <h1 className={styles.title} style={{ textAlign: 'left' }}>{t('landing.title')}</h1>
          <p className={styles.subtitle} style={{ textAlign: 'left', marginBottom: '0' }}>{t('landing.subtitle')}</p>
        </div>
        <button 
          onClick={() => router.push('/dashboard')} 
          disabled={analyzing || translating}
          style={{
            display: 'flex',
            alignItems: 'center',
            gap: '0.5rem',
            padding: '0.6rem 1.2rem',
            borderRadius: '6px',
            fontSize: '0.9rem',
            fontWeight: 600,
            cursor: 'pointer',
            backgroundColor: 'transparent',
            color: 'var(--text, #f8fafc)',
            border: '1px solid var(--border-color, rgba(148,163,184,0.4))',
            transition: 'all 0.2s ease',
            whiteSpace: 'nowrap'
          }}
          onMouseEnter={e => { e.currentTarget.style.backgroundColor = 'rgba(255,255,255,0.05)'; }}
          onMouseLeave={e => { e.currentTarget.style.backgroundColor = 'transparent'; }}
        >
          Directly to Dashboard without Any Testing <ArrowRight size={16} />
        </button>
      </div>

      <div className={styles.grid}>

        {/* ── Card 1: Test Case AI ─────────────────────────────────────── */}
        <div className={styles.card} id="tutorial-provider">
          <div className={styles.cardTitle}><Zap size={18} />{t('landing.testAiConfig')}</div>
          <p className={styles.cardDesc}>{t('landing.testAiDesc')}</p>

          <div className={styles.providerTabs}>
            {(['ollama-local', 'ollama-cloud', 'gemini'] as Provider[]).map(p => (
              <button
                key={p}
                className={`${styles.providerTab} ${provider === p ? styles.providerTabActive : ''}`}
                onClick={() => handleSelectProvider(p)}
              >
                {p === 'ollama-local' && <Server size={18} />}
                {p === 'ollama-cloud' && <Cloud size={18} />}
                {p === 'gemini'       && <Zap size={18} />}
                {p === 'ollama-local' ? 'Local' : p === 'ollama-cloud' ? 'Cloud' : 'Gemini'}
                {provider === p && <Check size={12} />}
              </button>
            ))}
          </div>

          {/* Local */}
          {provider === 'ollama-local' && (
            <div className={styles.configSection}>
              <div className={styles.configLabel}>Base URL</div>
              <input className={styles.input} value={ollamaUrl}
                onChange={e => setOllamaUrl(e.target.value)}
                onBlur={() => save({ ollamaBaseUrl: ollamaUrl })}
                placeholder="http://localhost:11434"
              />
              <div style={{ display:'flex', alignItems:'center', justifyContent:'space-between' }}>
                <div className={styles.configLabel} style={{ display:'flex', alignItems:'center', gap:'0.35rem' }}>
                  <Cpu size={13} /> Select Model
                </div>
                <button onClick={refreshLocalModels}
                  style={{ background:'none', border:'none', cursor:'pointer', color:'var(--text-secondary)', display:'flex', alignItems:'center', gap:'0.3rem', fontSize:'0.8rem' }}>
                  <RefreshCw size={13} className={modelsLoading ? 'spin' : ''} /> Refresh
                </button>
              </div>
              {localModels.length === 0
                ? <div className={styles.emptyState}>No local models — make sure Ollama is running.</div>
                : <RadioList items={localModels} active={ollamaModel}
                    onSelect={n => { setOllamaModel(n); save({ ollamaModel: n }); }} />
              }
            </div>
          )}

          {/* Cloud */}
          {provider === 'ollama-cloud' && (
            <div className={styles.configSection}>
              <div className={styles.configLabel}>Base URL</div>
              <input className={styles.input} value={cloudUrl}
                onChange={e => setCloudUrl(e.target.value)}
                onBlur={() => save({ ollamaCloudBaseUrl: cloudUrl })}
                placeholder="https://my-ollama.example.com"
              />
              <div className={styles.configLabel} style={{ display:'flex', alignItems:'center', gap:'0.35rem' }}>
                <Key size={13} /> API Key (optional)
              </div>
              <input className={styles.input} type="password" value={cloudApiKey}
                onChange={e => setCloudApiKey(e.target.value)}
                onBlur={() => save({ ollamaCloudApiKey: cloudApiKey })}
                placeholder="Enter API key…"
              />
              <div style={{ display:'flex', alignItems:'center', justifyContent:'space-between' }}>
                <div className={styles.configLabel} style={{ display:'flex', alignItems:'center', gap:'0.35rem' }}>
                  <Cpu size={13} /> Select Model
                </div>
                <button onClick={fetchCloudModels} disabled={!cloudUrl.trim() || cloudModelsLoading}
                  style={{ background:'none', border:'none', cursor:'pointer', color:'var(--text-secondary)', display:'flex', alignItems:'center', gap:'0.3rem', fontSize:'0.8rem', opacity: !cloudUrl.trim() ? 0.5 : 1 }}>
                  <RefreshCw size={13} className={cloudModelsLoading ? 'spin' : ''} /> Fetch
                </button>
              </div>
              {cloudModels.length === 0
                ? <div className={styles.emptyState}>
                    {cloudUrl.trim() ? 'Click "Fetch" to load models.' : 'Enter a Base URL first.'}
                  </div>
                : <RadioList items={cloudModels} active={cloudModel}
                    onSelect={n => { setCloudModel(n); save({ ollamaCloudModel: n }); }} />
              }
            </div>
          )}

          {/* Gemini */}
          {provider === 'gemini' && (
            <div className={styles.configSection}>
              <div className={styles.configLabel} style={{ display:'flex', alignItems:'center', gap:'0.35rem' }}>
                <Key size={13} /> API Key
              </div>
              <input className={styles.input} type="password" value={geminiApiKey}
                onChange={e => setGeminiApiKey(e.target.value)}
                onBlur={() => save({ geminiApiKey })}
                placeholder="Enter your Gemini API key…"
              />
              <div className={styles.configLabel}>Model</div>
              <input className={styles.input} value={geminiModel}
                onChange={e => setGeminiModel(e.target.value)}
                onBlur={() => save({ geminiModel })}
                placeholder="e.g. gemini-2.5-pro"
              />
            </div>
          )}

          <div style={{ marginTop: '1.5rem', paddingTop: '1.25rem', borderTop: '1px solid var(--border-color)' }}>
            <div className={styles.configLabel} style={{ display: 'flex', alignItems: 'center', gap: '0.35rem', justifyContent: 'space-between' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.35rem' }}>
                <RotateCw size={13} /> {t('landing.maxRetries')}
              </div>
              <span style={{ fontWeight: 'bold', color: 'var(--accent-color)' }}>{llmRetryCount}</span>
            </div>
            <input 
              type="range" 
              min="1" 
              max="10" 
              step="1" 
              value={llmRetryCount} 
              onChange={e => setLlmRetryCount(parseInt(e.target.value, 10))}
              style={{ width: '100%', marginTop: '0.5rem' }}
            />
          </div>
        </div>

        {/* ── Card 2: Python Translation Models ────────────────────────── */}
        <div className={styles.card} id="tutorial-models">
          <div className={styles.cardTitle}><Bot size={18} />{t('landing.pythonAiConfig')}</div>
          <p className={styles.cardDesc}>{t('landing.pythonAiDesc')}</p>

          <div className={styles.configLabel}>{t('landing.existingModels')}</div>
          {pythonModels.length === 0
            ? <div className={styles.emptyState}>{t('landing.noModels')}</div>
            : (
              <div className={styles.modelList}>
                {pythonModels.map(m => (
                  <div key={m} className={styles.modelItem} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                      <FolderOpen size={14} />
                      <span className={styles.modelName}>{m}</span>
                    </div>
                    <button 
                      onClick={() => handleDeletePyModel(m)}
                      title="Delete model"
                      style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--error-color, #ef4444)', padding: '2px', display: 'flex' }}
                    >
                      <Trash2 size={14} />
                    </button>
                  </div>
                ))}
              </div>
            )
          }

          <div className={styles.uploadArea}>
            <div className={styles.providerTabs} style={{ marginTop: '0', marginBottom: '1rem' }}>
              <button
                className={`${styles.providerTab} ${!showTranslateAi ? styles.providerTabActive : ''}`}
                onClick={() => setShowTranslateAi(false)}
              >
                <UploadCloud size={16} /> Upload Folder
                {!showTranslateAi && <Check size={12} />}
              </button>
              <button
                className={`${styles.providerTab} ${showTranslateAi ? styles.providerTabActive : ''}`}
                onClick={() => setShowTranslateAi(true)}
              >
                <Zap size={16} /> Translate using AI
                {showTranslateAi && <Check size={12} />}
              </button>
            </div>

            <div className={styles.uploadLabel}>
              {showTranslateAi ? 'Target Model Name' : t('landing.addNewModel')}
            </div>
            <input className={styles.input}
              placeholder={showTranslateAi ? 'e.g. translated_model_1' : String(t('landing.newModelPlaceholder') || 'Model name…')}
              value={newPyModelName}
              onChange={e => setNewPyModelName(e.target.value)}
              disabled={addingPy || translating}
            />
            
            {!showTranslateAi ? (
              <div className={styles.uploadRow}>
                <div className={styles.fileInputWrapper}>
                  <input id="pyFolderInput" ref={pyFolderRef} type="file"
                    className={styles.fileInputHidden}
                    // @ts-ignore
                    webkitdirectory="" directory="" multiple
                    onChange={e => setSelectedPyFolder(e.target.files)}
                    disabled={addingPy}
                  />
                  <label htmlFor="pyFolderInput"
                    className={`${styles.fileInputTrigger} ${selectedPyFolder ? styles.fileInputTriggerActive : ''}`}>
                    <FolderOpen size={14} />
                    {selectedPyFolder ? `${selectedPyFolder.length} file(s) selected` : 'Select Python folder…'}
                  </label>
                </div>
                <form onSubmit={handleAddPyModel}>
                  <button type="submit" className={styles.btnPrimary}
                    disabled={addingPy || !newPyModelName.trim() || !selectedPyFolder}>
                    {addingPy ? <RefreshCw size={14} className="spin" /> : <UploadCloud size={14} />}
                    {t('landing.addModelBtn')}
                  </button>
                </form>
              </div>
            ) : (
              <div style={{ marginTop: '0.5rem' }}>
                <button 
                  className={styles.btnPrimary} 
                  style={{ width: '100%', justifyContent: 'center' }}
                  onClick={handleTranslateAll}
                  disabled={translating || !newPyModelName.trim() || cobolFiles.length === 0}
                >
                  {translating ? <RefreshCw size={14} className="spin" /> : <Bot size={14} />}
                  Translate {cobolFiles.length} COBOL file(s)
                </button>
                {cobolFiles.length === 0 && (
                  <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', marginTop: '0.5rem', textAlign: 'center' }}>
                    Please upload COBOL files below first.
                  </div>
                )}
              </div>
            )}
          </div>
        </div>

        {/* ── Card 3: COBOL Source Files ────────────────────────────────── */}
        <div className={styles.card} style={{ gridColumn: '1 / -1' }} id="tutorial-cobol">
          <div className={styles.cardTitle}><FileCode2 size={18} />COBOL Source Files</div>
          <p className={styles.cardDesc}>
            Upload the COBOL source files (.cbl / .cob) you want to analyse.
            They will be saved to <code>public/cobol/</code>.
          </p>

          {cobolFiles.length === 0 ? (
            <div className={styles.emptyState}>No COBOL files found. Upload files below.</div>
          ) : (
            <div className={styles.modelList} style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))' }}>
              {cobolFiles.map(f => (
                <div key={f} className={styles.modelItem} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', overflow: 'hidden' }}>
                    <FileCode2 size={14} style={{ flexShrink: 0 }} />
                    <span className={styles.modelName} style={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{f}</span>
                  </div>
                  <button 
                    onClick={() => handleDeleteCobolFile(f)}
                    title="Delete file"
                    style={{ background: 'none', border: 'none', cursor: 'pointer', color: 'var(--error-color, #ef4444)', padding: '2px', display: 'flex', flexShrink: 0 }}
                  >
                    <Trash2 size={14} />
                  </button>
                </div>
              ))}
            </div>
          )}

          <form className={styles.uploadRow} onSubmit={handleUploadCbl}>
            <div className={styles.fileInputWrapper}>
              <input id="cblInput" ref={cblFolderRef} type="file"
                className={styles.fileInputHidden}
                accept=".cbl,.cob,.CBL,.COB" multiple
                onChange={e => setSelectedCblFiles(e.target.files)}
                disabled={uploadingCbl}
              />
              <label htmlFor="cblInput"
                className={`${styles.fileInputTrigger} ${selectedCblFiles ? styles.fileInputTriggerActive : ''}`}>
                <FileCode2 size={14} />
                {selectedCblFiles
                  ? `${selectedCblFiles.length} COBOL file(s) selected`
                  : 'Select COBOL files (.cbl / .cob)…'}
              </label>
            </div>
            <button type="submit" className={styles.btnPrimary}
              disabled={uploadingCbl || !selectedCblFiles}>
              {uploadingCbl ? <RefreshCw size={14} className="spin" /> : <UploadCloud size={14} />}
              Upload Files
            </button>
          </form>
        </div>

      </div>{/* /grid */}

      {/* ── Continue ─────────────────────────────────────────────────────── */}
      <div className={styles.continueWrap} id="tutorial-continue">
        <button className={styles.continueBtn} onClick={handleContinue} disabled={analyzing || translating}>
          {t('landing.continueBtn')} <ArrowRight size={20} />
        </button>
      </div>
    </main>
  );
}
