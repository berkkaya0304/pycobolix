'use client';

import React, { useRef, useState, useCallback } from 'react';
import { Download, ChevronDown } from 'lucide-react';
import html2canvas from 'html2canvas';
import jsPDF from 'jspdf';

interface ExportWrapperProps {
  children: React.ReactNode;
  filename: string;          // base name without extension, e.g. "complexity_chart"
  title?: string;            // optional figure title for the export (academic caption)
  paperStyle?: boolean;      // if true, adds white bg + serif font for paper look
  exportConfig?: any;        // If provided, uses Python backend to generate from scratch
}

export default function ExportWrapper({ children, filename, title, paperStyle = true, exportConfig }: ExportWrapperProps) {
  const contentRef = useRef<HTMLDivElement>(null);
  const [menuOpen, setMenuOpen] = useState(false);
  const [exporting, setExporting] = useState(false);

  const captureCanvas = useCallback(async () => {
    if (!contentRef.current) return null;

    const el = contentRef.current;

    // Save original CSS custom properties from :root
    const root = document.documentElement;
    const savedVars: Record<string, string> = {};
    
    // Academic-style overrides: white bg, dark text, clean borders
    const academicOverrides: Record<string, string> = {
      '--background': '#ffffff',
      '--foreground': '#1a1a2e',
      '--surface': '#ffffff',
      '--card-bg': '#ffffff',
      '--text': '#1a1a2e',
      '--text-secondary': '#4a5568',
      '--border': '#4b5563',
      '--accent': '#2563eb',
    };

    let styleEl: HTMLStyleElement | null = null;
    if (paperStyle) {
      // Inject style to strip dark gradients
      styleEl = document.createElement('style');
      styleEl.innerHTML = `
        [data-export-target] [class*="card"], 
        [data-export-target] [class*="wrap"],
        [data-export-target] [class*="chartContainer"] {
          background-image: none !important;
          background-color: #ffffff !important;
          border: none !important;
          box-shadow: none !important;
        }
        [data-export-target] [class*="statsPanel"] {
          background: none !important;
          border: 1px solid #e2e8f0 !important;
        }
        [data-export-target] [class*="statCardMainIcon"] {
          background: none !important;
        }
        [data-export-target] text,
        [data-export-target] [class*="barLabel"],
        [data-export-target] [class*="axisLabel"] {
          fill: #0f172a !important;
        }
        [data-no-export] {
          display: none !important;
        }
      `;
      document.head.appendChild(styleEl);

      // Save & override root CSS variables
      for (const [key, val] of Object.entries(academicOverrides)) {
        savedVars[key] = root.style.getPropertyValue(key);
        root.style.setProperty(key, val);
      }
      el.style.background = '#ffffff';
      el.style.padding = '24px';
      el.style.border = 'none';
      el.style.borderRadius = '0';
      el.style.boxShadow = 'none';
      el.style.color = '#1a1a2e';
    }

    // Hide the export button itself during capture
    const btnContainer = el.parentElement?.querySelector('[data-export-btn]') as HTMLElement | null;
    if (btnContainer) btnContainer.style.display = 'none';

    // Small delay for repaint
    await new Promise(r => setTimeout(r, 100));

    const canvas = await html2canvas(el, {
      backgroundColor: '#ffffff',
      scale: 3,  // high DPI for academic quality (300 DPI equivalent)
      useCORS: true,
      logging: false,
      allowTaint: true,
    });

    // Restore everything
    if (btnContainer) btnContainer.style.display = '';
    if (styleEl) document.head.removeChild(styleEl);
    if (paperStyle) {
      for (const [key] of Object.entries(academicOverrides)) {
        if (savedVars[key]) root.style.setProperty(key, savedVars[key]);
        else root.style.removeProperty(key);
      }
      el.style.background = '';
      el.style.padding = '';
      el.style.border = '';
      el.style.borderRadius = '';
      el.style.boxShadow = '';
      el.style.color = '';
    }

    return canvas;
  }, [paperStyle]);

  const exportViaPython = async (format: 'png' | 'pdf') => {
    try {
      const res = await fetch('/api/export-chart', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ ...exportConfig, format, title })
      });
      if (!res.ok) throw new Error('Export failed');
      
      const blob = await res.blob();
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = `${filename}.${format}`;
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
      URL.revokeObjectURL(url);
    } catch (e) {
      console.error(e);
      alert('Failed to generate premium academic chart via Python backend. Python a sahip olmanız gerekmektedir.');
    }
  };

  const exportAsPNG = useCallback(async () => {
    setExporting(true);
    setMenuOpen(false);
    try {
      if (exportConfig) {
        await exportViaPython('png');
        return;
      }
      const canvas = await captureCanvas();
      if (!canvas) return;
      const link = document.createElement('a');
      link.download = `${filename}.png`;
      link.href = canvas.toDataURL('image/png', 1.0);
      link.click();
    } finally {
      setExporting(false);
    }
  }, [captureCanvas, filename, exportConfig, title]);

  const exportAsJPG = useCallback(async () => {
    setExporting(true);
    setMenuOpen(false);
    try {
      if (exportConfig) {
        await exportViaPython('jpg');
        return;
      }
      const canvas = await captureCanvas();
      if (!canvas) return;
      const link = document.createElement('a');
      link.download = `${filename}.jpg`;
      link.href = canvas.toDataURL('image/jpeg', 0.95);
      link.click();
    } finally {
      setExporting(false);
    }
  }, [captureCanvas, filename, exportConfig, title]);

  const exportAsPDF = useCallback(async () => {
    setExporting(true);
    setMenuOpen(false);
    try {
      if (exportConfig) {
        await exportViaPython('pdf');
        return;
      }
      const canvas = await captureCanvas();
      if (!canvas) return;

      const imgWidth = canvas.width;
      const imgHeight = canvas.height;
      
      // Use landscape or portrait based on aspect ratio
      const isLandscape = imgWidth > imgHeight * 1.3;
      const pdfDoc = new jsPDF({
        orientation: isLandscape ? 'landscape' : 'portrait',
        unit: 'mm',
        format: 'a4',
      });

      const pageW = pdfDoc.internal.pageSize.getWidth();
      const pageH = pdfDoc.internal.pageSize.getHeight();
      const margin = 15; // mm
      const usableW = pageW - margin * 2;
      const usableH = pageH - margin * 2 - (title ? 12 : 0);

      // Scale image to fit
      const ratio = Math.min(usableW / imgWidth, usableH / imgHeight);
      const w = imgWidth * ratio;
      const h = imgHeight * ratio;

      // Center horizontally
      const x = margin + (usableW - w) / 2;
      let y = margin;

      // Add academic-style figure title
      if (title) {
        pdfDoc.setFont('times', 'bold');
        pdfDoc.setFontSize(11);
        pdfDoc.text(title, pageW / 2, y + 6, { align: 'center' });
        y += 12;
      }

      const imgData = canvas.toDataURL('image/png', 1.0);
      pdfDoc.addImage(imgData, 'PNG', x, y, w, h);

      pdfDoc.save(`${filename}.pdf`);
    } finally {
      setExporting(false);
    }
  }, [captureCanvas, filename, title, exportConfig]);

  return (
    <div style={{ position: 'relative', width: '100%', height: '100%' }}>
      {/* Export button - top right corner */}
      <div data-export-btn style={{
        position: 'absolute',
        top: 8,
        right: 8,
        zIndex: 20,
      }}>
        <button
          onClick={() => setMenuOpen(prev => !prev)}
          disabled={exporting}
          aria-label="Export figure"
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: 4,
            padding: '5px 10px',
            fontSize: '0.72rem',
            fontWeight: 600,
            letterSpacing: '0.02em',
            color: 'var(--text-secondary, #94a3b8)',
            background: 'var(--card-bg, rgba(30,41,59,0.6))',
            border: '1px solid var(--border, rgba(148,163,184,0.15))',
            borderRadius: 6,
            cursor: 'pointer',
            backdropFilter: 'blur(8px)',
            transition: 'all 0.15s ease',
            opacity: exporting ? 0.5 : 0.7,
          }}
          onMouseEnter={e => { (e.target as HTMLElement).style.opacity = '1'; }}
          onMouseLeave={e => { if (!menuOpen) (e.target as HTMLElement).style.opacity = '0.7'; }}
        >
          <Download size={12} />
          Export
          <ChevronDown size={10} style={{ transform: menuOpen ? 'rotate(180deg)' : 'none', transition: 'transform 0.2s' }} />
        </button>

        {menuOpen && (
          <div
            style={{
              position: 'absolute',
              top: '100%',
              right: 0,
              marginTop: 4,
              background: 'var(--card-bg, rgba(15,23,42,0.95))',
              border: '1px solid var(--border, rgba(148,163,184,0.2))',
              borderRadius: 8,
              padding: '4px 0',
              minWidth: 140,
              boxShadow: '0 8px 24px rgba(0,0,0,0.3)',
              backdropFilter: 'blur(12px)',
              zIndex: 30,
            }}
            onMouseLeave={() => setMenuOpen(false)}
          >
            {[
              { label: 'PNG (High-Res)', fn: exportAsPNG, desc: 'Best for articles' },
              { label: 'JPG (Compressed)', fn: exportAsJPG, desc: 'Smaller file size' },
              { label: 'PDF (Vector)', fn: exportAsPDF, desc: 'Print quality' },
            ].map(opt => (
              <button
                key={opt.label}
                onClick={opt.fn}
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  width: '100%',
                  padding: '8px 14px',
                  border: 'none',
                  background: 'transparent',
                  cursor: 'pointer',
                  textAlign: 'left',
                  transition: 'background 0.15s',
                }}
                onMouseEnter={e => { (e.target as HTMLElement).style.background = 'rgba(99,102,241,0.12)'; }}
                onMouseLeave={e => { (e.target as HTMLElement).style.background = 'transparent'; }}
              >
                <span style={{ fontSize: '0.8rem', fontWeight: 600, color: 'var(--text, #e2e8f0)' }}>{opt.label}</span>
                <span style={{ fontSize: '0.65rem', color: 'var(--text-secondary, #64748b)', marginTop: 1 }}>{opt.desc}</span>
              </button>
            ))}
            {exportConfig && (
              <div style={{ padding: '8px 14px', fontSize: '0.65rem', color: 'var(--text-secondary, #64748b)', borderTop: '1px solid var(--border, rgba(148,163,184,0.2))', marginTop: '4px', fontStyle: 'italic' }}>
                * Not: Bu özellik için Python'a sahip olmanız gerekmektedir.
              </div>
            )}
          </div>
        )}
      </div>

      {/* Content to capture */}
      <div ref={contentRef} data-export-target style={{ width: '100%', height: '100%' }}>
        {children}
      </div>
    </div>
  );
}
