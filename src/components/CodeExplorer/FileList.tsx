import React from 'react';
import styles from './FileList.module.css';
import { AnalysisResult } from '@/lib/data/types';
import { FileText, CheckCircle, AlertTriangle } from 'lucide-react';
import { useTranslation } from '@/lib/i18n/LanguageContext';

interface FileListProps {
  files: AnalysisResult[];
  selectedFileId: string | null;
  onSelectFile: (id: string) => void;
}

export default function FileList({ files, selectedFileId, onSelectFile }: FileListProps) {
  const { t } = useTranslation();

  return (
    <div className={styles.fileList}>
      <h3 className={styles.panelTitle}>{t('explorer.analysedFiles')}</h3>
      <div className={styles.listContainer}>
        {files.map((file) => {
            // Determine overall status based on models
            const anySuccess = file.models.some(m => m.status === 'success');
            const modelsCount = file.models.length;
            
            return (
              <div 
                key={file.id} 
                className={`${styles.fileItem} ${selectedFileId === file.id ? styles.selected : ''}`}
                onClick={() => onSelectFile(file.id)}
              >
                <div style={{display: 'flex', alignItems: 'center', gap: '0.75rem'}}>
                  <FileText size={18} className={styles.fileIcon} />
                  <div>
                    <div className={styles.fileName}>{file.source_file}</div>
                    <div className={styles.fileMeta}>
                        {t('explorer.modelsCount').replace('{count}', modelsCount.toString())}
                    </div>
                  </div>
                </div>
                
                {anySuccess ? (
                    <CheckCircle size={16} className={styles.statusSuccess} /> 
                ) : (
                    <AlertTriangle size={16} className={styles.statusError} />
                )}
              </div>
            );
        })}
      </div>
    </div>
  );
}
