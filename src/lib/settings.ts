import fs from 'fs';
import path from 'path';

const SETTINGS_FILE = path.join(process.cwd(), 'public', 'output', 'settings.json');

export interface AppSettings {
  llmProvider?: 'ollama-local' | 'ollama-cloud' | 'gemini';
  ollamaModel: string;
  ollamaBaseUrl: string;
  geminiApiKey?: string;
  geminiModel?: string;
  ollamaCloudApiKey?: string;
  ollamaCloudBaseUrl?: string;
  ollamaCloudModel?: string;
  llmRetryCount: number;
}

const DEFAULT_SETTINGS: AppSettings = {
  llmProvider: 'ollama-local',
  ollamaModel: 's',
  ollamaBaseUrl: 'http://localhost:11434',
  geminiApiKey: '',
  geminiModel: 'gemini-2.5-pro',
  ollamaCloudApiKey: '',
  ollamaCloudBaseUrl: '',
  ollamaCloudModel: '',
  llmRetryCount: 3,
};

export function getSettings(): AppSettings {
  try {
    if (fs.existsSync(SETTINGS_FILE)) {
      const raw = fs.readFileSync(SETTINGS_FILE, 'utf-8');
      const parsed = JSON.parse(raw);
      return { ...DEFAULT_SETTINGS, ...parsed };
    }
  } catch {}
  return { ...DEFAULT_SETTINGS };
}

export function saveSettings(settings: Partial<AppSettings>): AppSettings {
  const current = getSettings();
  const merged: AppSettings = { ...current, ...settings };
  // Ensure the output dir exists
  const dir = path.dirname(SETTINGS_FILE);
  if (!fs.existsSync(dir)) fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(SETTINGS_FILE, JSON.stringify(merged, null, 2));
  return merged;
}
