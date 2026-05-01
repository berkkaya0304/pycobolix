import React from 'react';
import {
  Document, Page, Text, View, StyleSheet, Font, Svg, Line, Rect, Circle, Link, G
} from '@react-pdf/renderer';
import { AnalysisResult } from '@/lib/data/types';
import { safeNumber, deepSanitize } from '@/lib/utils/pdfSanitizer';

// ─── FONTS ─────────────────────────────────────────────────────────────
Font.register({
  family: 'Inter',
  fonts: [
    { src: 'https://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuLyeMZhrib2Bg-4.ttf', fontWeight: 400 },
    { src: 'https://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuFuYMZhrib2Bg-4.ttf', fontWeight: 600 },
    { src: 'https://fonts.gstatic.com/s/inter/v12/UcCO3FwrK3iLTeHuS_fvQtMwCp50KnMw2boKoduKmMEVuGKYMZhrib2Bg-4.ttf', fontWeight: 700 }
  ]
});

// ─── PREMIUM DARK THEME (HIGH CONTRAST) ───────────────────────────────
const theme = {
  bg: '#0B0F1A',
  card: '#111827',
  border: '#1F2937',
  text: '#FFFFFF',
  muted: '#E2E8F0',    // Very light gray for visibility
  accent: '#60A5FA',
  success: '#34D399',
  warning: '#FBBF24',
  danger: '#FB7185',
  info: '#818CF8',
};

const chartColors = [theme.accent, theme.success, theme.warning, theme.info, theme.danger, theme.muted];

// ─── UTILS ─────────────────────────────────────────────────────────────
const mean = (arr: number[]) => {
  const nums = arr.map(n => safeNumber(n));
  return nums.length ? nums.reduce((a, b) => a + b, 0) / nums.length : 0;
};

const pctOf = (n: number, d: number) => {
  const sn = safeNumber(n);
  const sd = safeNumber(d);
  return sd > 0 ? Math.round((sn / sd) * 100) : 0;
};

// ─── STYLES ────────────────────────────────────────────────────────────
const styles = StyleSheet.create({
  page: { padding: 48, backgroundColor: theme.bg, fontFamily: 'Inter', fontSize: 11, color: theme.text, lineHeight: 1.5 },
  headerStrip: { position: 'absolute', top: 0, left: 0, right: 0, height: 6, backgroundColor: theme.accent },
  
  cover: { backgroundColor: theme.bg, color: theme.text, height: '100%', padding: 60, display: 'flex', flexDirection: 'column', justifyContent: 'center' },
  coverTitle: { fontSize: 48, fontWeight: 700, marginBottom: 12 },
  coverSubtitle: { fontSize: 22, color: theme.muted, marginBottom: 60 },
  coverBadge: { fontSize: 12, fontWeight: 700, color: theme.accent, textTransform: 'uppercase', marginBottom: 20 },
  coverStats: { flexDirection: 'row', gap: 40, marginTop: 40 },
  coverStatItem: { borderLeftWidth: 3, borderLeftColor: theme.accent, paddingLeft: 20, flexBasis: '33%' },
  coverStatVal: { fontSize: 24, fontWeight: 700, marginBottom: 6 },
  coverStatLabel: { fontSize: 8, fontWeight: 600, color: theme.muted, textTransform: 'uppercase' },
  
  sectionHeader: { marginBottom: 32, borderBottomWidth: 1, borderBottomColor: theme.border, paddingBottom: 16 },
  sectionTitle: { fontSize: 24, fontWeight: 700, color: theme.text, marginBottom: 4 },
  sectionSubtitle: { fontSize: 10, color: theme.muted },
  
  h3: { fontSize: 12, fontWeight: 700, color: theme.text, marginTop: 24, marginBottom: 16, textTransform: 'uppercase' },
  paragraph: { fontSize: 11, color: theme.muted, marginBottom: 12 },
  
  cardRow: { flexDirection: 'row', gap: 12, marginBottom: 24, flexWrap: 'wrap' },
  card: { width: '30%', backgroundColor: theme.card, borderRadius: 10, padding: 18, borderWidth: 1, borderColor: theme.border, minHeight: 80 },
  cardValue: { fontSize: 22, fontWeight: 700, color: theme.text, marginBottom: 4 },
  cardLabel: { fontSize: 9, fontWeight: 600, color: theme.muted, textTransform: 'uppercase' },
  
  aiBox: { backgroundColor: theme.card, borderRadius: 12, padding: 24, borderLeftWidth: 4, borderLeftColor: theme.accent, marginVertical: 16 },
  aiTitle: { fontSize: 11, fontWeight: 700, color: theme.accent, marginBottom: 8, textTransform: 'uppercase' },
  aiText: { fontSize: 11, lineHeight: 1.7, color: theme.text },
  
  // TABLE IMPROVEMENTS (ELIMINATING OVERLAPS)
  table: { marginTop: 12, borderRadius: 8, overflow: 'hidden', borderWidth: 1, borderColor: theme.border },
  tableHeader: { flexDirection: 'row', backgroundColor: theme.card, padding: 12 },
  th: { fontSize: 10, fontWeight: 700, color: theme.text, paddingHorizontal: 4 },
  tableRow: { flexDirection: 'row', borderBottomWidth: 1, borderBottomColor: theme.border, padding: 12, backgroundColor: theme.bg },
  tableRowAlt: { backgroundColor: theme.card },
  td: { fontSize: 10, color: theme.muted, paddingHorizontal: 4 },
  tdBold: { fontSize: 10, fontWeight: 700, color: theme.text, paddingHorizontal: 4 },
  
  chartContainer: { marginVertical: 12, padding: 16, backgroundColor: theme.card, borderRadius: 12, borderWidth: 1, borderColor: theme.border },
  footer: { position: 'absolute', bottom: 30, left: 48, right: 48, borderTopWidth: 1, borderTopColor: theme.border, paddingTop: 10, flexDirection: 'row', justifyContent: 'space-between' },
  footerText: { fontSize: 8, color: theme.muted },
  
  tocItem: { flexDirection: 'row', justifyContent: 'space-between', paddingVertical: 14, borderBottomWidth: 1, borderBottomColor: theme.border },
  tocLabel: { fontSize: 12, fontWeight: 600, color: theme.text },
  tocPage: { fontSize: 12, fontWeight: 700, color: theme.accent },
});

// ─── REUSABLE COMPONENTS ──────────────────────────────────────────────
const MarkdownText = ({ text, style }: { text?: string, style?: any }) => {
  if (!text) return <Text style={[style, { color: theme.muted, fontStyle: 'italic' }]}>Data for this section is still being analyzed...</Text>;
  const parts = text.split(/(\*\*.*?\*\*)/g);
  return (
    <Text style={style}>
      {parts.map((p, i) => (p.startsWith('**') && p.endsWith('**')) ? <Text key={i} style={{ fontWeight: 700 }}>{p.slice(2, -2)}</Text> : p)}
    </Text>
  );
};

const SectionHeader = ({ title, subtitle, id }: { title: string, subtitle?: string, id?: string }) => (
  <View style={styles.sectionHeader} id={id}>
    <Text style={styles.sectionTitle}>{title}</Text>
    {subtitle && <Text style={styles.sectionSubtitle}>{subtitle}</Text>}
  </View>
);

const MetricCard = ({ label, value, color = theme.text }: { label: string, value: string | number, color?: string }) => (
  <View style={styles.card}>
    <Text style={[styles.cardValue, { color }]}>{value}</Text>
    <Text style={styles.cardLabel}>{label}</Text>
  </View>
);

const ChartLegend = ({ items }: { items: { label: string, color: string }[] }) => (
  <View style={{ flexDirection: 'row', flexWrap: 'wrap', gap: 12, marginTop: 12, marginLeft: 45 }}>
    {items.map((item, i) => (
      <View key={i} style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
        <View style={{ width: 12, height: 12, backgroundColor: item.color, borderRadius: 3 }} />
        <Text style={{ fontSize: 10, color: theme.text }}>{item.label}</Text>
      </View>
    ))}
  </View>
);

const SafeBarChart = ({ data, maxY, yLabel, height = 150 }: { data: any[], maxY: number, yLabel: string, height?: number }) => {
  const chartW = 480;
  const chartH = height;
  const padL = 45;
  const padB = 35;
  const W = chartW - padL;
  const H = chartH - padB;
  const mY = Math.max(1, safeNumber(maxY));
  const sData = data.map(d => ({
    ...d,
    bars: d.bars.map((b: any) => ({ ...b, value: Math.min(mY, Math.max(0, safeNumber(b.value))) }))
  }));
  const barGroupWidth = Math.max(20, (W / sData.length));
  
  return (
    <View style={styles.chartContainer} wrap={false}>
      <Text style={{ fontSize: 10, color: theme.accent, marginBottom: 12, textTransform: 'uppercase', fontWeight: 700 }}>{yLabel}</Text>
      <Svg width={chartW} height={chartH} viewBox={`0 0 ${chartW} ${chartH}`}>
        {[0, 0.5, 1].map((p, i) => {
          const yPos = H - (p * H);
          return (
            <G key={i}>
              <Line x1={padL} y1={yPos} x2={chartW} y2={yPos} stroke={theme.border} strokeWidth={1} strokeDasharray="3 3" />
              <Text style={{ fontSize: 10, fill: theme.text }} x={5} y={yPos + 4}>{Math.round(p * mY)}%</Text>
            </G>
          );
        })}
        {sData.map((group, i) => {
          const xBase = padL + i * barGroupWidth + 10;
          return group.bars.map((bar: any, bi: number) => {
            const bWidth = (barGroupWidth - 20) / group.bars.length;
            const bH = (bar.value / mY) * H;
            const x = xBase + bi * bWidth;
            const y = H - bH;
            return <Rect key={`${i}-${bi}`} x={x} y={y} width={Math.max(6, bWidth - 4)} height={Math.max(2, bH)} fill={bar.color || theme.accent} rx={3} />;
          });
        })}
      </Svg>
    </View>
  );
};

// ─── MAIN DOCUMENT ───────────────────────────────────────────────────
export const ReactPDFReport = ({ data, aiComments, dict }: { data: AnalysisResult[], aiComments: any, dict: any }) => {
  const sData: AnalysisResult[] = deepSanitize(data || [], 'data');
  const sAi: any = deepSanitize(aiComments || {}, 'ai');
  
  const filesCount = sData.length;
  const models = [...new Set(sData.flatMap(f => (f.models || []).map(m => m.model_name)))];
  const modelCount = models.length;

  const aggByModel = models.map(mName => {
    const results = sData.flatMap(f => (f.models || []).filter(m => m.model_name === mName));
    return {
      name: mName,
      semanticAvg: safeNumber(mean(results.map(r => pctOf(r.metrics?.unit_tests_passed || 0, r.metrics?.unit_tests_total || 0)))),
      pylintAvg: safeNumber(mean(results.map(r => r.metrics?.pylint_score || 0))),
      maintainabilityAvg: safeNumber(mean(results.map(r => r.metrics?.maintainability_index || 0))),
      complexityAvg: safeNumber(mean(results.map(r => r.metrics?.complexity_score || 0))),
      speedAvgPy: safeNumber(mean(results.map(r => r.metrics?.exec_time_python_avg_ms || 0))),
      speedAvgCob: safeNumber(mean(results.map(r => r.metrics?.exec_time_cobol_avg_ms || 0))),
    };
  });

  const tableData = sData.flatMap(f => (f.models || []).map(m => ({
    fileName: f.source_file.split('/').pop() || 'Untitled',
    modelName: m.model_name,
    semantic: pctOf(m.metrics?.unit_tests_passed || 0, m.metrics?.unit_tests_total || 0),
    pylint: safeNumber(m.metrics?.pylint_score),
    maintainability: safeNumber(m.metrics?.maintainability_index),
    execTimePy: safeNumber(m.metrics?.exec_time_python_avg_ms),
    execTimeCob: safeNumber(m.metrics?.exec_time_cobol_avg_ms),
  })));

  // CHUNKING (STABILITY)
  const CHUNK_SIZE = 15; // Smaller chunks to prevent page overflow
  const chunks = [];
  for (let i = 0; i < tableData.length; i += CHUNK_SIZE) {
    chunks.push(tableData.slice(i, i + CHUNK_SIZE));
  }

  const Footer = () => (
    <View style={styles.footer} fixed>
      <Text style={styles.footerText}>Pycobolix Strategic Audit • {new Date().toLocaleDateString()}</Text>
      <Text style={styles.footerText} render={({ pageNumber, totalPages }) => `Page ${pageNumber} of ${totalPages}`} />
    </View>
  );

  return (
    <Document>
      {/* 1. COVER */}
      <Page size="A4" style={styles.cover}>
        <View style={{ flex: 1, justifyContent: 'center' }}>
          <Text style={styles.coverBadge}>Confidential Modernization Audit</Text>
          <Text style={styles.coverTitle}>Ultimate Report</Text>
          <Text style={styles.coverSubtitle}>System-Wide Fidelity & AI-Performance Benchmark</Text>
          <View style={{ width: 140, height: 8, backgroundColor: theme.accent, marginBottom: 44 }} />
          <View style={styles.coverStats}>
            <View style={styles.coverStatItem}><Text style={styles.coverStatVal}>{filesCount}</Text><Text style={styles.coverStatLabel}>Modules</Text></View>
            <View style={styles.coverStatItem}><Text style={styles.coverStatVal}>{modelCount}</Text><Text style={styles.coverStatLabel}>Models</Text></View>
            <View style={styles.coverStatItem}><Text style={styles.coverStatVal}>{tableData.length}</Text><Text style={styles.coverStatLabel}>Validations</Text></View>
          </View>
        </View>
        {sAi?.executiveSummary && (
          <View style={{ backgroundColor: theme.card, borderRadius: 12, padding: 32, borderLeftWidth: 6, borderLeftColor: theme.accent }}>
            <Text style={styles.aiTitle}>EXECUTIVE STRATEGY SNAPSHOT</Text>
            <MarkdownText text={sAi.executiveSummary} style={{ fontSize: 12, color: theme.text, lineHeight: 1.8 }} />
          </View>
        )}
      </Page>

      {/* 2. TOC */}
      <Page size="A4" style={styles.page}>
        <SectionHeader title="Report Architecture" subtitle="Professional audit navigation and strategic roadmap." />
        <View style={{ marginVertical: 32, borderTopWidth: 1, borderTopColor: theme.border }}>
          <View style={styles.tocItem}><Link href="#fidelity"><Text style={styles.tocLabel}>1. Transformation Fidelity Benchmarks</Text></Link><Text style={styles.tocPage}>3</Text></View>
          <View style={styles.tocItem}><Link href="#quality"><Text style={styles.tocLabel}>2. Structural Integrity & Quality Audit</Text></Link><Text style={styles.tocPage}>4</Text></View>
          <View style={styles.tocItem}><Link href="#performance"><Text style={styles.tocLabel}>3. Runtime Performance Comparison</Text></Link><Text style={styles.tocPage}>5</Text></View>
          <View style={styles.tocItem}><Link href="#insights"><Text style={styles.tocLabel}>4. AI Strategy & Observations</Text></Link><Text style={styles.tocPage}>6</Text></View>
          <View style={styles.tocItem}><Link href="#audit"><Text style={styles.tocLabel}>5. Appendix: Granular Audit Trail</Text></Link><Text style={styles.tocPage}>7+</Text></View>
        </View>
        <Footer />
      </Page>

      {/* 3. FIDELITY */}
      <Page size="A4" style={styles.page}>
        <View style={styles.headerStrip} />
        <SectionHeader id="fidelity" title="Transformation Fidelity" subtitle="Validating functional parity through comprehensive boundary test execution." />
        <View style={styles.cardRow}>
           {aggByModel.map((m, i) => (
             <MetricCard key={i} label={`${m.name} Fidelity`} value={`${m.semanticAvg.toFixed(1)}%`} color={chartColors[i % chartColors.length]} />
           ))}
        </View>
        <Text style={styles.h3}>Fidelity Score Distribution</Text>
        <SafeBarChart maxY={100} yLabel="Avg Fidelity rate (%)" data={aggByModel.map((m, i) => ({
           label: m.name,
           bars: [{ value: m.semanticAvg, color: chartColors[i % chartColors.length] }]
        }))} />
        <ChartLegend items={aggByModel.map((m, i) => ({ label: m.name, color: chartColors[i % chartColors.length] }))} />
        <Footer />
      </Page>

      {/* 4. QUALITY */}
      <Page size="A4" style={styles.page}>
        <View style={styles.headerStrip} />
        <SectionHeader id="quality" title="Structural Integrity" subtitle="Audit of code maintainability, technical debt, and Pylint performance." />
        <View style={styles.cardRow}>
           {aggByModel.map((m, i) => (
             <MetricCard key={i} label={`${m.name} Pylint`} value={m.pylintAvg.toFixed(1)} color={chartColors[i % chartColors.length]} />
           ))}
        </View>
        <Text style={styles.h3}>Complexity vs Maintainability Balance</Text>
        <SafeBarChart maxY={100} yLabel="Index (%)" data={aggByModel.map(m => ({
           label: m.name,
           bars: [
             { value: m.complexityAvg, color: theme.danger },
             { value: m.maintainabilityAvg, color: theme.success }
           ]
        }))} />
        <ChartLegend items={[{ label: 'Complexity Stress', color: theme.danger }, { label: 'Maintainability Score', color: theme.success }]} />
        <Footer />
      </Page>

      {/* 5. PERFORMANCE */}
      <Page size="A4" style={styles.page}>
        <View style={styles.headerStrip} />
        <SectionHeader id="performance" title="Performance Comparison" subtitle="Comparing execution speed between legacy COBOL and modernized Python." />
        <Text style={styles.h3}>Execution Speed Comparison (Lower is Faster)</Text>
        <SafeBarChart maxY={Math.max(10, ...aggByModel.map(m => Math.max(m.speedAvgPy, m.speedAvgCob)))} yLabel="Avg Execution Time (ms)" data={aggByModel.map((m, i) => ({
           label: m.name,
           bars: [
             { value: m.speedAvgPy, color: theme.accent },
             { value: m.speedAvgCob, color: theme.muted }
           ]
        }))} />
        <ChartLegend items={[{ label: 'Python (Target)', color: theme.accent }, { label: 'COBOL (Source)', color: theme.muted }]} />
        <Footer />
      </Page>

      {/* 6. INSIGHTS */}
      <Page size="A4" style={styles.page}>
        <View style={styles.headerStrip} />
        <SectionHeader id="insights" title="Strategic Perspectives" subtitle="AI-driven analysis of transformation patterns and systemic health." />
        {sAi?.matchRates && <View style={styles.aiBox}><Text style={styles.aiTitle}>Insight: Transformation Parity</Text><MarkdownText text={sAi.matchRates} style={styles.aiText} /></View>}
        {sAi?.pylintAndComplexity && <View style={styles.aiBox}><Text style={styles.aiTitle}>Insight: Structural Quality</Text><MarkdownText text={sAi.pylintAndComplexity} style={styles.aiText} /></View>}
        {sAi?.errorPatterns && <View style={styles.aiBox}><Text style={styles.aiTitle}>Insight: Critical Failure Analysis</Text><MarkdownText text={sAi.errorPatterns} style={styles.aiText} /></View>}
        {sAi?.pythonToCobol && <View style={styles.aiBox}><Text style={styles.aiTitle}>Insight: Reverse Testing (Python → COBOL)</Text><MarkdownText text={sAi.pythonToCobol} style={styles.aiText} /></View>}
        <Footer />
      </Page>

      {/* 7. AUDIT TRAIL (STABLE CHUNKS) */}
      {chunks.map((chunk, chunkIdx) => (
        <Page key={chunkIdx} size="A4" style={styles.page}>
          <View style={styles.headerStrip} />
          <SectionHeader title="Module Audit Detail" id="audit" subtitle={`Detailed technical metrics Analysis (Part ${chunkIdx + 1})`} />
          <View style={styles.table}>
            <View style={styles.tableHeader}>
              <Text style={[styles.th, { width: '38%' }]}>Module Fragment</Text>
              <Text style={[styles.th, { width: '12%' }]}>Model</Text>
              <Text style={[styles.th, { width: '10%' }]}>Fid.</Text>
              <Text style={[styles.th, { width: '10%' }]}>Pylint</Text>
              <Text style={[styles.th, { width: '10%' }]}>Maint.</Text>
              <Text style={[styles.th, { width: '10%' }]}>Py ms</Text>
              <Text style={[styles.th, { width: '10%' }]}>Cob ms</Text>
            </View>
            {chunk.map((item, i) => (
              <View key={i} style={[styles.tableRow, i % 2 === 1 ? styles.tableRowAlt : {}]} wrap={false}>
                {/* Truncated Filename to prevent overlapping */}
                <Text style={[styles.tdBold, { width: '38%', fontSize: 9 }]} numberOfLines={1}>{item.fileName}</Text>
                <Text style={[styles.td, { width: '12%', fontSize: 9, color: theme.text }]}>{item.modelName}</Text>
                <Text style={[styles.td, { width: '10%', fontSize: 10, fontWeight: 700, color: item.semantic > 80 ? theme.success : theme.warning }]}>{item.semantic}%</Text>
                <Text style={[styles.td, { width: '10%', fontSize: 10, color: theme.text }]}>{item.pylint.toFixed(1)}</Text>
                <Text style={[styles.td, { width: '10%', fontSize: 10, color: theme.text }]}>{item.maintainability.toFixed(0)}</Text>
                <Text style={[styles.td, { width: '10%', fontSize: 10, color: theme.text }]}>{item.execTimePy.toFixed(0)}</Text>
                <Text style={[styles.td, { width: '10%', fontSize: 10, color: theme.text }]}>{item.execTimeCob.toFixed(0)}</Text>
              </View>
            ))}
          </View>
          <Footer />
        </Page>
      ))}
    </Document>
  );
};
