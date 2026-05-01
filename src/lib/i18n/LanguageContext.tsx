'use client';

import React, { createContext, useContext, useState, useEffect } from 'react';
import { en } from './dictionaries/en';
import { tr } from './dictionaries/tr';

export type Language = 'en' | 'tr';

interface LanguageContextProps {
  language: Language;
  setLanguage: (lang: Language) => void;
  t: (keyPath: string) => string;
}

const LanguageContext = createContext<LanguageContextProps | undefined>(undefined);

export function LanguageProvider({ children }: { children: React.ReactNode }) {
  const [language, setLanguageState] = useState<Language>('en');
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
    const storedLang = localStorage.getItem('app-language') as Language;
    if (storedLang && (storedLang === 'en' || storedLang === 'tr')) {
      setLanguageState(storedLang);
    }
  }, []);

  const setLanguage = (lang: Language) => {
    setLanguageState(lang);
    localStorage.setItem('app-language', lang);
  };

  // Helper to get nested values like: t('nav.dashboard')
  const t = (keyPath: string): string => {
    const keys = keyPath.split('.');
    const dictionary: any = language === 'tr' ? tr : en;

    let value = dictionary;
    for (const key of keys) {
      if (value[key] === undefined) {
        console.warn(`Translation missing for key: ${keyPath} in language: ${language}`);
        return keyPath;
      }
      value = value[key];
    }
    return value;
  };

  // Prevent hydration mismatch
  if (!mounted) {
    return null;
  }

  return (
    <LanguageContext.Provider value={{ language, setLanguage, t }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useTranslation() {
  const context = useContext(LanguageContext);
  if (context === undefined) {
    throw new Error('useTranslation must be used within a LanguageProvider');
  }
  return context;
}
