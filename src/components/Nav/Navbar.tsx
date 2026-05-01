'use client';

import React, { useEffect, useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { useTheme } from 'next-themes';
import styles from './Navbar.module.css';
import { LayoutDashboard, Code2, BarChart3, Settings, Sun, Moon, Languages, Coins } from 'lucide-react';
import { useTranslation, Language } from '@/lib/i18n/LanguageContext';

export default function Navbar() {
  const pathname = usePathname();
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);
  const { t, language, setLanguage } = useTranslation();

  const navItems = [
    { href: '/dashboard',    label: t('nav.dashboard'),     icon: LayoutDashboard },
    { href: '/explorer',     label: t('nav.codeExplorer'),  icon: Code2 },
    { href: '/analysis',     label: t('nav.analysis'),      icon: BarChart3 },
    { href: '/token',        label: t('nav.tokenUsage'),    icon: Coins },
    { href: '/settings',     label: t('nav.settings'),      icon: Settings },
  ];

  // Avoid hydration mismatch by waiting for mount
  useEffect(() => {
    setMounted(true);
  }, []);

  const toggleLanguage = () => {
    setLanguage(language === 'en' ? 'tr' : 'en');
  };

  return (
    <nav className={styles.navbar}>
      <Link href="/" className={styles.brand}>
        <div className={styles.logoWrapper}>
          <LayoutDashboard className={styles.logoIcon} size={24} />
          <div className={styles.logoGlow} />
        </div>
        <div className={styles.brandText}>
          <span className={styles.brandPy}>Py</span>
          <span className={styles.brandCobol}>cobol</span>
          <span className={styles.brandIx}>ix</span>
        </div>
      </Link>

      <div className={styles.links} id="tutorial-nav">
        {navItems.map(({ href, label, icon: Icon }) => {
          const active = pathname === href;
          return (
            <Link
              key={href}
              href={href}
              className={`${styles.link} ${active ? styles.active : ''}`}
            >
              <Icon size={16} />
              {label}
              {active && <span className={styles.activeDot} />}
            </Link>
          );
        })}
        
        {/* Toggle Actions */}
        <div className={styles.actions}>
          {mounted && (
            <>
              <button
                onClick={toggleLanguage}
                className={styles.iconButton}
                aria-label={t('language.toggle')}
                title={language === 'en' ? 'Switch to Turkish' : 'İngilizceye geç'}
              >
                <Languages size={18} />
                <span style={{ fontSize: '0.75rem', fontWeight: 600, marginLeft: '4px', textTransform: 'uppercase' }}>
                  {language}
                </span>
              </button>

              <button
                onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
                className={styles.iconButton}
                aria-label={t('theme.toggle')}
              >
                {theme === 'dark' ? <Moon size={18} /> : <Sun size={18} />}
              </button>
            </>
          )}
        </div>
      </div>
    </nav>
  );
}
