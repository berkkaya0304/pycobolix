'use client';

import React, { useEffect, useState, useRef } from 'react';
import styles from './SplitView.module.css';
import { AnalysisResult, ModelResult } from '@/lib/data/types';
import Editor from '@monaco-editor/react';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus, prism } from 'react-syntax-highlighter/dist/esm/styles/prism';
import ModelSelector from './ModelSelector';
import { useTheme } from 'next-themes';
import { useTranslation } from '@/lib/i18n/LanguageContext';

interface SplitViewProps {
  selectedFile: AnalysisResult | null;
  activeModel: string;
  onModelChange: (model: string) => void;
  customCode: string;
  onCodeChange: (code: string) => void;
  editable: boolean;
}

const customStyle = {
  lineHeight: '1.5',
  fontSize: '0.9rem',
  borderRadius: '4px',
  margin: 0,
  padding: '1rem',
  background: 'transparent', // Let container background show
};

export default function SplitView({ selectedFile, activeModel, onModelChange, customCode, onCodeChange, editable }: SplitViewProps) {
  const editorRef = useRef<any>(null);
  const { resolvedTheme } = useTheme();
  const [mounted, setMounted] = useState(false);
  const { t } = useTranslation();

  useEffect(() => {
    setMounted(true);
  }, []);

  useEffect(() => {
      if (selectedFile && !selectedFile.models.some(m => m.model_name === activeModel)) {
          if (selectedFile.models.length > 0) {
              onModelChange(selectedFile.models[0].model_name);
          }
      }
  }, [selectedFile, activeModel, onModelChange]);

  if (!selectedFile) {
    return (
      <div className={styles.placeholderState}>
        {t('explorer.selectFileMessage')}
      </div>
    );
  }

  // Find the currently active model result
  const activeModelResult = selectedFile.models.find(m => m.model_name === activeModel) || selectedFile.models[0];
  
  // Decide what Python code to show: custom/edited code > active model code > empty
  const pythonCodeToDisplay = customCode || activeModelResult?.python_code || '';

  function handleEditorDidMount(editor: any, monaco: any) {
    editorRef.current = editor;
  }

  const isDarkMode = mounted && resolvedTheme === 'dark';

  return (
    <div className={styles.container}>
      {/* Model Selector Tabs */}
      <ModelSelector 
        models={selectedFile.models}
        activeModel={activeModel}
        onModelChange={onModelChange}
      />

      <div className={styles.editorsContainer}>
        {/* Left Pane: COBOL */}
        <div className={styles.editorPane}>
          <div className={styles.paneHeader}>
            <span>{t('explorer.cobolSource')}</span>
            <span className={styles.badge}>{t('explorer.legacyBadge')}</span>
          </div>
          <Editor
            height="100%"
            defaultLanguage="cobol" // Monaco might verify this, usually plain text or registered
            value={selectedFile.cobol_code}
            theme={isDarkMode ? 'vs-dark' : 'vs-light'}
            onMount={handleEditorDidMount}
            options={{ readOnly: true, minimap: { enabled: false } }}
          />
        </div>

        {/* Right Pane: Python */}
        <div className={styles.editorPane}>
          <div className={styles.paneHeader}>
             <div style={{display: 'flex', alignItems: 'center', gap: '0.5rem'}}>
                <span>{t('explorer.pythonModernization')}</span>
                {activeModelResult?.metrics.pass_at_1 ? (
                    <span className={styles.badgeSuccess}>{t('explorer.verifiedBadge')}</span>
                ) : (
                    <span className={styles.badgeError}>{t('explorer.unverifiedBadge')}</span>
                )}
             </div>
             {editable && onCodeChange ? (
                 <textarea 
                    value={pythonCodeToDisplay}
                    onChange={(e) => onCodeChange(e.target.value)}
                    style={{
                        position: 'absolute',
                        top: 0, left: 0, width: '100%', height: '100%',
                        background: 'transparent',
                        color: 'transparent', 
                        caretColor: isDarkMode ? 'white' : 'black',
                        border: 'none',
                        resize: 'none',
                        outline: 'none',
                        fontFamily: 'Consolas, Monaco, "Andale Mono", "Ubuntu Mono", monospace',
                        fontSize: '0.9rem',
                        lineHeight: '1.5',
                        padding: '1rem',
                        zIndex: 10,
                        whiteSpace: 'pre'
                    }}
                    spellCheck={false}
                 />
             ) : null}
             <SyntaxHighlighter
              language="python"
              style={isDarkMode ? vscDarkPlus : prism}
              customStyle={customStyle}
              showLineNumbers
            >
              {pythonCodeToDisplay}
            </SyntaxHighlighter>
          </div>
        </div>
      </div>
    </div>
  );
}
