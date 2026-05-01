'use client';

import React, { useState, useEffect } from 'react';
import styles from './page.module.css';
import { LlmUsageEntry } from '@/lib/data/types';
import { useTranslation } from '@/lib/i18n/LanguageContext';
import { 
  Coins, 
  Clock, 
  Cpu, 
  Hash, 
  Calendar,
  History,
  FileCode,
  Zap,
  Filter,
  CheckCircle,
  AlertCircle,
  Database,
  Activity,
  FileText,
  SearchX
} from 'lucide-react';
import { 
  LineChart, 
  Line, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer,
  AreaChart,
  Area
} from 'recharts';

export default function TokenUsagePage() {
  const [usage, setUsage] = useState<LlmUsageEntry[]>([]);
  const [loading, setLoading] = useState(true);
  const { t } = useTranslation();

  useEffect(() => {
    async function fetchUsage() {
      try {
        const res = await fetch('/api/llm-usage');
        const data = await res.json();
        setUsage(Array.isArray(data) ? data : []);
      } catch (err) {
        console.error('Failed to fetch LLM usage:', err);
      } finally {
        setLoading(false);
      }
    }
    fetchUsage();
  }, []);

  const totalTokens = usage.reduce((acc, curr) => acc + curr.total_tokens, 0);
  const totalPrompt = usage.reduce((acc, curr) => acc + curr.prompt_tokens, 0);
  const totalCompletion = usage.reduce((acc, curr) => acc + curr.completion_tokens, 0);
  const totalDuration = usage.reduce((acc, curr) => acc + curr.duration_ms, 0);
  const avgDuration = usage.length > 0 ? totalDuration / usage.length : 0;

  const chartData = usage.map(entry => ({
    time: new Date(entry.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }),
    tokens: entry.total_tokens,
    duration: entry.duration_ms / 1000, // in seconds
    fullDate: new Date(entry.timestamp).toLocaleString()
  })).slice(-20); // Last 20 calls for chart

  const getModelBadge = (model: string) => {
    const m = model.toLowerCase();
    const isGpt = m.includes('gpt');
    const isClaude = m.includes('claude');
    const isGemini = m.includes('gemini');
    
    let badgeClass = styles.modelBadgeDefault;
    if (isGpt) badgeClass = styles.modelBadgeGpt;
    if (isClaude) badgeClass = styles.modelBadgeClaude;
    if (isGemini) badgeClass = styles.modelBadgeGemini;

    return (
      <div className={`${styles.modelBadge} ${badgeClass}`}>
        <Cpu size={12} />
        <span>{model}</span>
      </div>
    );
  };

  return (
    <main className={styles.main}>
      <div className={styles.pageHeader}>
        <div>
          <h1 className={styles.headerTitle}>LLM Usage Insights</h1>
          <p className={styles.headerSub}>Track token consumption and performance metrics across different AI operations.</p>
        </div>
      </div>

      <div className={styles.statsGrid}>
        <div className={styles.statCard}>
          <div className={styles.statLabel}><Hash size={16} /> Total Tokens</div>
          <div className={styles.statValue}>{totalTokens.toLocaleString()}</div>
          <div className={styles.statSubtext}>{totalPrompt.toLocaleString()} prompt / {totalCompletion.toLocaleString()} completion</div>
        </div>
        <div className={styles.statCard}>
          <div className={styles.statLabel}><Clock size={16} /> Avg. Response Time</div>
          <div className={styles.statValue}>{(avgDuration / 1000).toFixed(2)}s</div>
          <div className={styles.statSubtext}>Based on {usage.length} total calls</div>
        </div>
        <div className={styles.statCard}>
          <div className={styles.statLabel}><Zap size={16} /> Total Compute Time</div>
          <div className={styles.statValue}>{(totalDuration / 1000 / 60).toFixed(1)}m</div>
          <div className={styles.statSubtext}>Accumulated LLM processing time</div>
        </div>
        <div className={styles.statCard}>
          <div className={styles.statLabel}><Cpu size={16} /> Active Models</div>
          <div className={styles.statValue}>{new Set(usage.map(u => u.model)).size}</div>
          <div className={styles.statSubtext}>Primary model: {usage[usage.length - 1]?.model || 'None'}</div>
        </div>
      </div>

      <div className={styles.sectionContainer}>
        <div className={styles.sectionHeader}>
          <div className={styles.sectionIcon}><History size={20} /></div>
          <div className={styles.sectionTitleGroup}>
            <h2 className={styles.sectionTitle}>Recent Activity</h2>
            <p className={styles.sectionSubtitle}>Last 20 LLM interactions timeline.</p>
          </div>
        </div>
        <div style={{ height: 300, width: '100%' }}>
          <ResponsiveContainer width="100%" height="100%">
            <AreaChart data={chartData}>
              <defs>
                <linearGradient id="colorTokens" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="5%" stopColor="var(--primary)" stopOpacity={0.3}/>
                  <stop offset="95%" stopColor="var(--primary)" stopOpacity={0}/>
                </linearGradient>
              </defs>
              <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="var(--border)" />
              <XAxis dataKey="time" stroke="var(--muted-foreground)" fontSize={12} tickLine={false} axisLine={false} />
              <YAxis stroke="var(--muted-foreground)" fontSize={12} tickLine={false} axisLine={false} />
              <Tooltip 
                contentStyle={{ backgroundColor: 'var(--card)', borderColor: 'var(--border)', borderRadius: '8px' }}
                itemStyle={{ color: 'var(--foreground)' }}
              />
              <Area type="monotone" dataKey="tokens" stroke="var(--primary)" fillOpacity={1} fill="url(#colorTokens)" strokeWidth={2} />
            </AreaChart>
          </ResponsiveContainer>
        </div>
      </div>

      <div className={styles.sectionContainer}>
        <div className={styles.sectionHeader}>
          <div className={styles.sectionIcon}><FileCode size={20} /></div>
          <div className={styles.sectionTitleGroup}>
            <h2 className={styles.sectionTitle}>Detailed Usage Logs</h2>
            <p className={styles.sectionSubtitle}>Complete history of LLM calls during analysis and translation.</p>
          </div>
        </div>
        <div className={styles.tableContainer}>
          <table className={styles.usageTable}>
            <thead>
              <tr>
                <th><div className={styles.thContent}><Calendar size={14} /> Timestamp</div></th>
                <th><div className={styles.thContent}><Cpu size={14} /> Model</div></th>
                <th><div className={styles.thContent}><Hash size={14} /> Tokens</div></th>
                <th><div className={styles.thContent}><Clock size={14} /> Duration</div></th>
                <th><div className={styles.thContent}><FileText size={14} /> Source File</div></th>
              </tr>
            </thead>
            <tbody>
              {usage.slice().reverse().map((entry) => {
                const date = new Date(entry.timestamp);
                return (
                  <tr key={entry.id} className={styles.tableRow}>
                    <td>
                      <div className={styles.timeCell}>
                        <span className={styles.dateText}>{date.toLocaleDateString(undefined, { month: 'short', day: 'numeric' })}</span>
                        <span className={styles.timeText}>{date.toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit', second: '2-digit' })}</span>
                      </div>
                    </td>
                    <td>{getModelBadge(entry.model)}</td>
                    <td>
                      <div className={styles.tokenCell}>
                        <span className={styles.tokenValue}>{entry.total_tokens.toLocaleString()}</span>
                        <span className={styles.tokenSub}>{entry.prompt_tokens}p / {entry.completion_tokens}c</span>
                      </div>
                    </td>
                    <td>
                      <div className={styles.durationCell}>
                        <Activity size={14} className={styles.durationIcon} />
                        {(entry.duration_ms / 1000).toFixed(2)}s
                      </div>
                    </td>
                    <td>
                      <div className={styles.fileCell}>
                        <FileCode size={14} />
                        <span className={styles.fileName} title={entry.file_name || 'System'}>{entry.file_name || 'System Action'}</span>
                      </div>
                    </td>
                  </tr>
                );
              })}
              {usage.length === 0 && (
                <tr>
                  <td colSpan={5}>
                    <div className={styles.emptyState}>
                      <SearchX size={48} />
                      <p>No usage data available.</p>
                      <span>Run an analysis or translation to see results.</span>
                    </div>
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </main>
  );
}
