'use client';

import React, { useState, useEffect, useCallback, useRef } from 'react';
import styles from './page.module.css';
import { 
  getSettingsAction, 
  saveSettingsAction, 
  listOllamaModelsAction, 
  listOllamaCloudModelsAction,
  getPythonModelDirsAction,
  uploadPythonModelDirAction,
  deletePythonModelDirAction,
  getCobolFilesAction,
  uploadCobolFilesAction,
  deleteCobolFileAction
} from '@/app/actions';
import { Settings, Zap, Check, RotateCw, RefreshCw, Server, Cloud, Key, Cpu, FolderOpen, FileCode2, Trash2, UploadCloud, Bot } from 'lucide-react';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import { toast } from 'sonner';

interface OllamaModel {
  name: string;
  size: number;
  modified_at: string;
}

const DEFAULT_MODEL = 's';

function formatBytes(bytes: number): string {
  if (!bytes) return '';
  const gb = bytes / (1024 ** 3);
  if (gb >= 1) return `${gb.toFixed(1)} GB`;
  const mb = bytes / (1024 ** 2);
  return `${Math.round(mb)} MB`;
}

interface SettingsState {
  llmProvider: 'ollama-local' | 'ollama-cloud' | 'gemini';
  ollamaModel: string;
  geminiApiKey: string;
  geminiModel: string;
  ollamaCloudApiKey: string;
  ollamaCloudBaseUrl: string;
  ollamaCloudModel: string;
  llmRetryCount: number;
}

const DEFAULT_SETTINGS: SettingsState = {
  llmProvider: 'ollama-local',
  ollamaModel: DEFAULT_MODEL,
  geminiApiKey: '',
  geminiModel: 'gemini-2.5-pro',
  ollamaCloudApiKey: '',
  ollamaCloudBaseUrl: '',
  ollamaCloudModel: '',
  llmRetryCount: 3
};

export default function SettingsPage() {
  const [currentSettings, setCurrentSettings] = useState<SettingsState>(DEFAULT_SETTINGS);
  const [form, setForm] = useState<SettingsState>(DEFAULT_SETTINGS);
  
  // ─── Python Translation Models ───────────────────────────────────────────
  const [pythonModels, setPythonModels]                 = useState<string[]>([]);
  const [newPyModelName, setNewPyModelName]             = useState('');
  const [selectedPyFolder, setSelectedPyFolder]         = useState<FileList | null>(null);
  const [addingPy, setAddingPy]                         = useState(false);
  const pyFolderRef   = useRef<HTMLInputElement>(null);

  // ─── COBOL Source Files ──────────────────────────────────────────────────
  const [cobolFiles, setCobolFiles]                     = useState<string[]>([]);
  const [selectedCblFiles, setSelectedCblFiles]         = useState<FileList | null>(null);
  const [uploadingCbl, setUploadingCbl]                 = useState(false);
  const cblFolderRef  = useRef<HTMLInputElement>(null);

  const [models, setModels] = useState<OllamaModel[]>([]);
  const [cloudModels, setCloudModels] = useState<OllamaModel[]>([]);
  const [ollamaStatus, setOllamaStatus] = useState<'checking' | 'ok' | 'error'>('checking');
  const [modelsLoading, setModelsLoading] = useState(true);
  const [cloudModelsLoading, setCloudModelsLoading] = useState(false);
  const [saving, setSaving] = useState(false);
  const { t } = useTranslation();

  const loadSettings = useCallback(async () => {
    const res = await getSettingsAction();
    if (res.success && res.data) {
      const loaded: SettingsState = {
        llmProvider: res.data.llmProvider || 'ollama-local',
        ollamaModel: res.data.ollamaModel || DEFAULT_MODEL,
        geminiApiKey: res.data.geminiApiKey || '',
        geminiModel: res.data.geminiModel || 'gemini-2.5-pro',
        ollamaCloudApiKey: res.data.ollamaCloudApiKey || '',
        ollamaCloudBaseUrl: res.data.ollamaCloudBaseUrl || '',
        ollamaCloudModel: res.data.ollamaCloudModel || '',
        llmRetryCount: res.data.llmRetryCount || 3
      };
      setCurrentSettings(loaded);
      setForm(loaded);
    }
  }, []);

  const loadModels = useCallback(async () => {
    setModelsLoading(true);
    setOllamaStatus('checking');
    const res = await listOllamaModelsAction();
    if (res.success && res.data) {
      setModels(res.data as OllamaModel[]);
      setOllamaStatus('ok');
    } else {
      setModels([]);
      setOllamaStatus('error');
    }
    setModelsLoading(false);
  }, []);

  const fetchCloudModels = async () => {
    if (!form.ollamaCloudBaseUrl.trim()) return;
    setCloudModelsLoading(true);
    const res = await listOllamaCloudModelsAction(form.ollamaCloudBaseUrl, form.ollamaCloudApiKey);
    if (res.success && res.data) {
      setCloudModels(res.data as OllamaModel[]);
      toast.success('Fetched cloud models');
    } else {
      setCloudModels([]);
      toast.error(res.error || 'Could not fetch cloud models');
    }
    setCloudModelsLoading(false);
  };

  const loadFiles = useCallback(async () => {
    const [pyDirs, cblList] = await Promise.all([
      getPythonModelDirsAction(),
      getCobolFilesAction(),
    ]);
    if (pyDirs.success && pyDirs.data)   setPythonModels(pyDirs.data);
    if (cblList.success && cblList.data) setCobolFiles(cblList.data);
  }, []);

  useEffect(() => {
    loadSettings();
    loadModels();
    loadFiles();
  }, [loadSettings, loadModels, loadFiles]);

  const handleSave = async () => {
    setSaving(true);
    const res = await saveSettingsAction(form);
    if (res.success && res.data) {
      setCurrentSettings(form);
      toast.success(t('common.saved'));
    } else {
      toast.error(t('common.error'));
    }
    setSaving(false);
  };

  const handleReset = async () => {
    setForm(DEFAULT_SETTINGS);
    setSaving(true);
    const res = await saveSettingsAction(DEFAULT_SETTINGS);
    if (res.success && res.data) {
      setCurrentSettings(DEFAULT_SETTINGS);
      toast.success(t('common.saved'));
    } else {
      toast.error(t('common.error'));
    }
    setSaving(false);
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
      const list = await getCobolFilesAction();
      if (list.success && list.data) setCobolFiles(list.data);
      setSelectedCblFiles(null);
      if (cblFolderRef.current) cblFolderRef.current.value = '';
    } else {
      toast.error('Error: ' + res.error);
    }
    setUploadingCbl(false);
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

  const isDirty = JSON.stringify(form) !== JSON.stringify(currentSettings);

  const updateField = (field: keyof SettingsState, value: string) => {
    setForm(prev => ({ ...prev, [field]: value }));
  };

  const RadioList = ({ items, active, onSelect }: { items: { name: string }[], active: string, onSelect: (name: string) => void }) => {
    if (items.length === 0) return null;
    return (
      <div className={styles.modelList} style={{ marginTop: '0.5rem', maxHeight: '200px', overflowY: 'auto' }}>
        {items.map(m => (
          <button
            key={m.name}
            className={`${styles.modelItem} ${m.name === active ? styles.modelItemActive : ''}`}
            onClick={() => onSelect(m.name)}
            style={{ padding: '0.6rem 0.75rem', display: 'flex', alignItems: 'center', gap: '0.75rem', justifyContent: 'flex-start' }}
          >
            <div className={`${styles.modelRadio} ${m.name === active ? styles.modelRadioFilled : ''}`} style={{ flexShrink: 0 }} />
            <span className={styles.modelName} style={{ margin: 0 }}>{m.name}</span>
          </button>
        ))}
      </div>
    );
  };

  return (
    <main className={styles.main}>
      {/* Header */}
      <div className={styles.pageHeader}>
        <div>
          <h1 className={styles.headerTitle}>{t('settings.title')}</h1>
          <p className={styles.headerSub}>
            {t('settings.subtitle')}
          </p>
        </div>
      </div>

      {/* Provider Selection */}
      <div className={styles.card}>
        <div className={styles.cardTitle}>
          <Settings size={16} />
          {t('settings.llmProvider')}
        </div>
        <div className={styles.providerOptions} style={{ display: 'flex', gap: '1rem', marginTop: '1rem' }}>
          <button
            className={`${styles.modelItem} ${form.llmProvider === 'ollama-local' ? styles.modelItemActive : ''}`}
            onClick={() => updateField('llmProvider', 'ollama-local')}
            style={{ flex: 1, flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '1.5rem', gap: '0.5rem' }}
          >
            <Server size={24} />
            <span style={{ fontWeight: 600 }}>{t('settings.providerLocal')}</span>
          </button>
          
          <button
            className={`${styles.modelItem} ${form.llmProvider === 'ollama-cloud' ? styles.modelItemActive : ''}`}
            onClick={() => updateField('llmProvider', 'ollama-cloud')}
            style={{ flex: 1, flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '1.5rem', gap: '0.5rem' }}
          >
            <Cloud size={24} />
            <span style={{ fontWeight: 600 }}>{t('settings.providerCloud')}</span>
          </button>
          
          <button
            className={`${styles.modelItem} ${form.llmProvider === 'gemini' ? styles.modelItemActive : ''}`}
            onClick={() => updateField('llmProvider', 'gemini')}
            style={{ flex: 1, flexDirection: 'column', alignItems: 'center', justifyContent: 'center', padding: '1.5rem', gap: '0.5rem' }}
          >
            <Zap size={24} />
            <span style={{ fontWeight: 600 }}>{t('settings.providerGemini')}</span>
          </button>
        </div>
      </div>

      {/* Ollama Local Settings */}
      {form.llmProvider === 'ollama-local' && (
      <div className={styles.card}>
        <div className={styles.cardTitle}>
          <Server size={16} />
          {t('settings.ollamaConnection')}
        </div>
        <p className={styles.cardDesc}>
          {t('settings.ollamaDesc')}
        </p>

        <div className={styles.statusRow}>
          <div
            className={`${styles.statusDot} ${
              ollamaStatus === 'ok'
                ? styles.statusDotGreen
                : ollamaStatus === 'error'
                ? styles.statusDotRed
                : styles.statusDotAmber
            }`}
          />
          <span className={styles.statusText}>
            {ollamaStatus === 'checking'
              ? t('settings.checkingConnection')
              : ollamaStatus === 'ok'
              ? t('settings.connectedModels').replace('{count}', models.length.toString())
              : t('settings.ollamaNotReachable')}
          </span>
        </div>

        <div className={styles.infoBox} style={{ marginBottom: '1.5rem' }}>
          {t('settings.ollamaMakeSure')}
        </div>

        <div className={styles.cardTitle} style={{ borderTop: '1px solid var(--border-color)', paddingTop: '1.5rem' }}>
          <Cpu size={16} />
          {t('settings.activeModel')}
        </div>
        <p className={styles.cardDesc}>
          {t('settings.activeModelDesc')} <strong>{form.ollamaModel}</strong>
        </p>

        {modelsLoading ? (
          <div className={styles.emptyState}>
            <RotateCw size={16} style={{ display: 'inline', marginRight: 6 }} className="spin" />
            {t('settings.loadingModels')}
          </div>
        ) : ollamaStatus === 'error' ? (
          <div className={styles.emptyState}>
            {t('settings.noModelsFound')}
            <br />
            <button onClick={loadModels} className={styles.secondaryButton} style={{ marginTop: '0.75rem' }}>
              <RefreshCw size={14} /> {t('settings.retry')}
            </button>
          </div>
        ) : models.length === 0 ? (
          <div className={styles.emptyState}>
            {t('settings.noModelsInstalled')}
          </div>
        ) : (
          <div className={styles.modelList}>
            {models.map((m) => {
              const isActive = m.name === form.ollamaModel;
              return (
                <button
                  key={m.name}
                  className={`${styles.modelItem} ${isActive ? styles.modelItemActive : ''}`}
                  onClick={() => updateField('ollamaModel', m.name)}
                >
                  <div className={`${styles.modelRadio} ${isActive ? styles.modelRadioFilled : ''}`} />
                  <span className={styles.modelName}>{m.name}</span>
                  {m.size > 0 && <span className={styles.modelMeta}>{formatBytes(m.size)}</span>}
                  {m.name === currentSettings.ollamaModel && (
                    <span className={styles.modelCurrentBadge}>{t('settings.current')}</span>
                  )}
                </button>
              );
            })}
          </div>
        )}
      </div>
      )}

      {/* Ollama Cloud Settings */}
      {form.llmProvider === 'ollama-cloud' && (
      <div className={styles.card}>
        <div className={styles.cardTitle}>
          <Cloud size={16} />
          {t('settings.ollamaCloudConnection')}
        </div>
        <p className={styles.cardDesc}>
          {t('settings.ollamaCloudDesc')}
        </p>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', marginTop: '1.5rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, marginBottom: '0.4rem', color: 'var(--text-primary)' }}>
              {t('settings.ollamaCloudBaseUrl')}
            </label>
            <input
              type="text"
              value={form.ollamaCloudBaseUrl}
              onChange={(e) => updateField('ollamaCloudBaseUrl', e.target.value)}
              placeholder={t('settings.ollamaCloudBaseUrlPlaceholder')}
              style={{ width: '100%', padding: '0.6rem 0.75rem', borderRadius: '6px', border: '1px solid var(--border-color)', background: 'var(--bg-secondary)', color: 'var(--text-primary)' }}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, marginBottom: '0.4rem', color: 'var(--text-primary)' }}>
              {t('settings.ollamaCloudApiKey')}
            </label>
            <input
              type="password"
              value={form.ollamaCloudApiKey}
              onChange={(e) => updateField('ollamaCloudApiKey', e.target.value)}
              placeholder={t('settings.ollamaCloudApiKeyPlaceholder')}
              style={{ width: '100%', padding: '0.6rem 0.75rem', borderRadius: '6px', border: '1px solid var(--border-color)', background: 'var(--bg-secondary)', color: 'var(--text-primary)' }}
            />
          </div>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.4rem' }}>
              <label style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-primary)' }}>
                {t('settings.ollamaCloudModel')}
              </label>
              <button 
                onClick={fetchCloudModels} 
                disabled={!form.ollamaCloudBaseUrl.trim() || cloudModelsLoading}
                style={{ background:'none', border:'none', cursor:'pointer', color:'var(--text-secondary)', display:'flex', alignItems:'center', gap:'0.3rem', fontSize:'0.8rem', opacity: !form.ollamaCloudBaseUrl.trim() ? 0.5 : 1 }}
              >
                <RefreshCw size={13} className={cloudModelsLoading ? 'spin' : ''} /> {t('common.refresh') || 'Fetch'}
              </button>
            </div>
            
            {cloudModels.length === 0 ? (
              <input
                type="text"
                value={form.ollamaCloudModel}
                onChange={(e) => updateField('ollamaCloudModel', e.target.value)}
                placeholder={t('settings.ollamaCloudModelPlaceholder')}
                style={{ width: '100%', padding: '0.6rem 0.75rem', borderRadius: '6px', border: '1px solid var(--border-color)', background: 'var(--bg-secondary)', color: 'var(--text-primary)' }}
              />
            ) : (
              <RadioList 
                items={cloudModels} 
                active={form.ollamaCloudModel} 
                onSelect={(n) => updateField('ollamaCloudModel', n)} 
              />
            )}
          </div>
        </div>
      </div>
      )}

      {/* Gemini Settings */}
      {form.llmProvider === 'gemini' && (
      <div className={styles.card}>
        <div className={styles.cardTitle}>
          <Zap size={16} />
          {t('settings.geminiConnection')}
        </div>
        <p className={styles.cardDesc}>
          {t('settings.geminiDesc')}
        </p>

        <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem', marginTop: '1.5rem' }}>
          <div>
            <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, marginBottom: '0.4rem', color: 'var(--text-primary)' }}>
              {t('settings.geminiApiKey')}
            </label>
            <input
              type="password"
              value={form.geminiApiKey}
              onChange={(e) => updateField('geminiApiKey', e.target.value)}
              placeholder={t('settings.geminiApiKeyPlaceholder')}
              style={{ width: '100%', padding: '0.6rem 0.75rem', borderRadius: '6px', border: '1px solid var(--border-color)', background: 'var(--bg-secondary)', color: 'var(--text-primary)' }}
            />
          </div>
          <div>
            <label style={{ display: 'block', fontSize: '0.85rem', fontWeight: 600, marginBottom: '0.4rem', color: 'var(--text-primary)' }}>
              {t('settings.geminiModel')}
            </label>
            <input
              type="text"
              value={form.geminiModel}
              onChange={(e) => updateField('geminiModel', e.target.value)}
              placeholder={t('settings.geminiModelPlaceholder')}
              style={{ width: '100%', padding: '0.6rem 0.75rem', borderRadius: '6px', border: '1px solid var(--border-color)', background: 'var(--bg-secondary)', color: 'var(--text-primary)' }}
            />
          </div>
        </div>
      </div>
      )}

      {/* LLM Advanced Settings */}
      <div className={styles.card}>
        <div className={styles.cardTitle}>
          <RotateCw size={16} />
          {t('settings.maxRetries')}
        </div>
        <p className={styles.cardDesc}>
          {t('settings.maxRetriesDesc')}
        </p>
        <div style={{ marginTop: '1rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
            <input
              type="range"
              min="1"
              max="10"
              step="1"
              value={form.llmRetryCount}
              onChange={(e) => setForm(prev => ({ ...prev, llmRetryCount: parseInt(e.target.value, 10) }))}
              style={{ flex: 1 }}
            />
            <div style={{ 
              width: '3rem', 
              height: '3rem', 
              display: 'flex', 
              alignItems: 'center', 
              justifyContent: 'center', 
              background: 'var(--bg-secondary)', 
              borderRadius: '8px', 
              border: '1px solid var(--border-color)',
              fontWeight: 'bold',
              fontSize: '1.2rem'
            }}>
              {form.llmRetryCount}
            </div>
          </div>
        </div>
      </div>

      {/* Python Translation Models */}
      <div className={styles.card}>
        <div className={styles.cardTitle}><Bot size={16} />{t('landing.pythonAiConfig')}</div>
        <p className={styles.cardDesc}>{t('landing.pythonAiDesc')}</p>

        <div style={{ fontSize: '0.85rem', fontWeight: 600, color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.04em', marginBottom: '0.5rem' }}>{t('landing.existingModels')}</div>
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
          <div className={styles.uploadLabel}>{t('landing.addNewModel')}</div>
          <input className={styles.input}
            placeholder={String(t('landing.newModelPlaceholder') || 'Model name…')}
            value={newPyModelName}
            onChange={e => setNewPyModelName(e.target.value)}
            disabled={addingPy}
          />
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
        </div>
      </div>

      {/* COBOL Source Files */}
      <div className={styles.card}>
        <div className={styles.cardTitle}><FileCode2 size={16} />COBOL Source Files</div>
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

        <form className={styles.uploadRow} onSubmit={handleUploadCbl} style={{ marginTop: '0.5rem' }}>
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

      {/* Actions */}
      <div className={styles.card}>
        <div className={styles.buttonRow}>
          <button
            className={styles.primaryButton}
            onClick={handleSave}
            disabled={saving || !isDirty}
          >
            {saving ? <RotateCw size={14} className="spin" /> : <Check size={14} />}
            {saving ? t('common.saving') : t('common.save')}
          </button>
          <button
            className={styles.secondaryButton}
            onClick={handleReset}
            disabled={saving || JSON.stringify(form) === JSON.stringify(DEFAULT_SETTINGS)}
          >
            {t('common.reset')}
          </button>
          {form.llmProvider === 'ollama-local' && (
            <button
              className={styles.secondaryButton}
              onClick={loadModels}
              disabled={modelsLoading}
              title={t('common.refresh')}
            >
              <RefreshCw size={14} />
              {t('common.refresh')}
            </button>
          )}
        </div>
      </div>

      {/* LLM Usage Info */}
      <div className={styles.card}>
        <div className={styles.cardTitle}>{t('settings.howLlmWorks')}</div>
        <p className={styles.cardDesc}>{t('settings.howLlmWorksDesc')}</p>
        <div className={styles.infoBox}>
          <strong>{t('settings.testInputGenTitle')}</strong> {t('settings.testInputGenDesc')}
          <br /><br />
          <strong>{t('settings.invalidTestGenTitle')}</strong> {t('settings.invalidTestGenDesc')}
          <br /><br />
          {t('settings.modelSelectionDesc')}
        </div>
      </div>
    </main>
  );
}
