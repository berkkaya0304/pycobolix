import React from 'react';
import { ModelResult } from '@/lib/data/types';

interface ModelSelectorProps {
  models: ModelResult[];
  activeModel: string;
  onModelChange: (model: string) => void;
}

export default function ModelSelector({ models, activeModel, onModelChange }: ModelSelectorProps) {
  return (
    <div style={{
      display: 'flex', 
      gap: '0.5rem', 
      padding: '0.5rem 1rem', 
      borderBottom: '1px solid var(--border)', 
      background: 'var(--surface)'
    }}>
      {models.map(model => (
        <button
          key={model.model_name}
          onClick={() => onModelChange(model.model_name)}
          style={{
            padding: '0.25rem 0.75rem',
            borderRadius: '4px',
            border: 'none',
            background: activeModel === model.model_name ? 'var(--accent)' : 'transparent',
            color: activeModel === model.model_name ? 'white' : 'var(--text)',
            cursor: 'pointer',
            fontWeight: 500,
            fontSize: '0.9rem'
          }}
        >
          {model.model_name}
        </button>
      ))}
    </div>
  );
}
