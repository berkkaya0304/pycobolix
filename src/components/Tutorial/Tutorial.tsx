'use client';

import React, { useState, useEffect, useRef } from 'react';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import { useRouter, usePathname } from 'next/navigation';
import { useTheme } from 'next-themes';
import styles from './Tutorial.module.css';
import { X, ChevronRight, ChevronLeft, HelpCircle, Languages, Sun, Moon } from 'lucide-react';

interface Step {
  title: string;
  description: string;
  targetId?: string;
  path?: string;
}

export default function Tutorial() {
  const { t, language, setLanguage } = useTranslation();
  const { theme, setTheme } = useTheme();
  const router = useRouter();
  const pathname = usePathname();
  const [isOpen, setIsOpen] = useState(false);
  const [currentStep, setCurrentStep] = useState(0);
  const [targetRect, setTargetRect] = useState<DOMRect | null>(null);
  const requestRef = useRef<number>(null);

  const steps: Step[] = [
    { 
      title: t('tutorial.welcome'), 
      description: t('tutorial.welcomeDesc') 
    },
    { 
      title: t('tutorial.nav'), 
      description: t('tutorial.navDesc'), 
      targetId: 'tutorial-nav' 
    },
    { 
      title: t('tutorial.stepLandingTitle'), 
      description: t('tutorial.stepLandingDesc'), 
      path: '/' 
    },
    { 
      title: t('tutorial.stepProvider'), 
      description: t('tutorial.stepProviderDesc'), 
      targetId: 'tutorial-provider',
      path: '/'
    },
    { 
      title: t('tutorial.stepModels'), 
      description: t('tutorial.stepModelsDesc'), 
      targetId: 'tutorial-models',
      path: '/'
    },
    { 
      title: t('tutorial.stepCobol'), 
      description: t('tutorial.stepCobolDesc'), 
      targetId: 'tutorial-cobol',
      path: '/'
    },
    { 
      title: t('tutorial.stepContinue'), 
      description: t('tutorial.stepContinueDesc'), 
      targetId: 'tutorial-continue',
      path: '/'
    },
    { 
      title: t('tutorial.stepDashboardTitle'), 
      description: t('tutorial.stepDashboardDesc'), 
      path: '/dashboard'
    },
    { 
      title: t('tutorial.stepScoreCards'), 
      description: t('tutorial.stepScoreCardsDesc'), 
      targetId: 'tutorial-score-cards',
      path: '/dashboard'
    },
    { 
      title: t('tutorial.stepTabs'), 
      description: t('tutorial.stepTabsDesc'), 
      targetId: 'tutorial-tabs',
      path: '/dashboard'
    },
    { 
      title: t('tutorial.stepGlossary'), 
      description: t('tutorial.stepGlossaryDesc'), 
      targetId: 'tutorial-glossary',
      path: '/dashboard'
    },
    { 
      title: t('tutorial.stepExplorerTitle'), 
      description: t('tutorial.stepExplorerDesc'), 
      path: '/explorer'
    },
    { 
      title: t('tutorial.stepSplitView'), 
      description: t('tutorial.stepSplitViewDesc'), 
      targetId: 'tutorial-split-view',
      path: '/explorer'
    },
    { 
      title: t('tutorial.stepTests'), 
      description: t('tutorial.stepTestsDesc'), 
      targetId: 'tutorial-tests',
      path: '/explorer'
    },
    { 
      title: t('tutorial.stepSandbox'), 
      description: t('tutorial.stepSandboxDesc'), 
      targetId: 'tutorial-sandbox-tab',
      path: '/explorer'
    },
    { 
      title: t('tutorial.stepFinishTitle'), 
      description: t('tutorial.stepFinishDesc') 
    },
  ];

  // Auto-open if first time
  useEffect(() => {
    const hasSeen = localStorage.getItem('pycobolix_tutorial_seen');
    if (!hasSeen) {
      setIsOpen(true);
    }
  }, []);

  // Update target rect
  useEffect(() => {
    if (!isOpen) return;

    const updateRect = () => {
      const step = steps[currentStep];
      if (step.targetId) {
        const el = document.getElementById(step.targetId);
        if (el) {
          setTargetRect(el.getBoundingClientRect());
        } else {
          setTargetRect(null);
        }
      } else {
        setTargetRect(null);
      }
      requestRef.current = requestAnimationFrame(updateRect);
    };

    requestRef.current = requestAnimationFrame(updateRect);
    return () => {
      if (requestRef.current) cancelAnimationFrame(requestRef.current);
    };
  }, [isOpen, currentStep]);

  // Handle path changes
  useEffect(() => {
    if (!isOpen) return;
    const step = steps[currentStep];
    if (step.path && pathname !== step.path) {
      router.push(step.path);
    }
  }, [currentStep, isOpen]);

  const handleNext = () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(currentStep + 1);
    } else {
      handleClose();
    }
  };

  const handlePrev = () => {
    if (currentStep > 0) {
      setCurrentStep(currentStep - 1);
    }
  };

  const handleClose = () => {
    setIsOpen(false);
    localStorage.setItem('pycobolix_tutorial_seen', 'true');
    setCurrentStep(0);
    
    // Redirect to home (landing page) and scroll to top
    router.push('/');
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  if (!isOpen) {
    return (
      <button className={styles.helpTrigger} onClick={() => setIsOpen(true)}>
        <HelpCircle size={20} />
      </button>
    );
  }

  const step = steps[currentStep];

  return (
    <div className={`${styles.overlay} ${!step.targetId ? styles.overlayBlur : ''}`}>
      {targetRect && (
        <>
          <div 
            className={styles.spotlight} 
            style={{
              top: targetRect.top - 16,
              left: targetRect.left - 16,
              width: targetRect.width + 32,
              height: targetRect.height + 32,
            }}
          />
          <div className={styles.lockout} />
        </>
      )}

      <div 
        className={`${styles.tooltip} ${targetRect ? styles.tooltipFloating : styles.tooltipCenter}`}
        style={targetRect ? {
          top: targetRect.bottom + 300 > window.innerHeight 
            ? Math.max(20, targetRect.top - 260) 
            : targetRect.bottom + 20,
          left: Math.max(10, Math.min(window.innerWidth - 350, targetRect.left + targetRect.width / 2 - 170)),
        } : {}}
      >
        <div className={styles.tooltipHeader}>
          <div className={styles.titleGroup}>
            <h3>{step.title}</h3>
            {currentStep === 0 && (
              <button 
                onClick={() => setLanguage(language === 'en' ? 'tr' : 'en')}
                className={styles.langToggle}
                title={t('language.toggle')}
              >
                <Languages size={14} />
                <span>{language.toUpperCase()}</span>
              </button>
            )}
            {currentStep === 0 && (
              <button 
                onClick={() => setTheme(theme === 'dark' ? 'light' : 'dark')}
                className={styles.langToggle}
                title={t('theme.toggle')}
              >
                {theme === 'dark' ? <Moon size={14} /> : <Sun size={14} />}
              </button>
            )}
          </div>
          <button onClick={handleClose} className={styles.closeBtn}><X size={18} /></button>
        </div>
        
        <div className={styles.tooltipBody}>
          <p>{step.description}</p>
        </div>

        <div className={styles.tooltipFooter}>
          <div className={styles.progress}>
            {currentStep + 1} / {steps.length}
          </div>
          <div className={styles.actions}>
            {currentStep > 0 && (
              <button onClick={handlePrev} className={styles.btnSecondary}>
                <ChevronLeft size={16} /> {t('tutorial.prev')}
              </button>
            )}
            <button onClick={handleNext} className={styles.btnPrimary}>
              {currentStep === steps.length - 1 ? t('tutorial.finish') : t('tutorial.next')}
              {currentStep < steps.length - 1 && <ChevronRight size={16} />}
            </button>
          </div>
        </div>
        
        {!targetRect && (
          <button onClick={handleClose} className={styles.skipBtn}>{t('tutorial.skip')}</button>
        )}
      </div>
    </div>
  );
}
