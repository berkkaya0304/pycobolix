import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const outputDir = path.join(root, 'article', 'pycobolix_last_converted');
const usagePath = path.join(root, 'public', 'output', 'llm_usage.json');
const resultsPath = path.join(root, 'public', 'output', 'results.json');

const modelNames = ['Claude-opus-4.6', 'Cogito-2.1', 'Gemini 3.1 Pro', 'Gemma4', 'Mistral-large-3'];
const modelLabels = ['Claude', 'Cogito', 'Gemini', 'Gemma', 'Mistral'];
const colors = {
  blue: '0.000 0.447 0.698',
  teal: '0.000 0.620 0.451',
  orange: '0.902 0.624 0.000',
  vermillion: '0.835 0.369 0.000',
  purple: '0.494 0.184 0.557',
  sky: '0.337 0.706 0.914',
  red: '0.780 0.165 0.216',
  gray: '0.34 0.36 0.40',
  axis: '0.18 0.20 0.23',
  grid: '0.88 0.90 0.93',
  band: '0.975 0.982 0.990',
  black: '0.06 0.07 0.09',
  white: '1 1 1',
};
const palette = [colors.blue, colors.teal, colors.orange, colors.purple, colors.vermillion];
const FIGURE_WIDTH = 420;
const FIGURE_HEIGHT = 252;

const aggregate = {
  semantic: [32.9, 10.8, 33.8, 10.5, 8.1],
  format: [4.9, 1.7, 4.0, 2.5, 1.7],
  pass: [26.2, 8.7, 25.4, 9.5, 7.1],
  pylint: [9.31, 7.34, 8.36, 7.48, 8.69],
  complexity: [66.4, 71.5, 52.6, 60.2, 68.7],
  halstead: [444, 791, 468, 485, 476],
  locRatio: [0.54, 0.67, 0.56, 0.59, 0.51],
  execMs: [117.7, 121.8, 116.0, 118.1, 115.8],
  boundary: [12.1, 5.4, 16.5, 5.9, 4.9],
  passFiles: [33, 11, 32, 12, 9],
  failedFiles: [93, 115, 94, 114, 117],
};

const errorCounts = {
  logic: [74, 79, 79, 101, 101],
  whitespace: [4, 2, 6, 1, 1],
  crash: [15, 34, 9, 12, 15],
};

function escapePdfText(value) {
  return String(value).replace(/\\/g, '\\\\').replace(/\(/g, '\\(').replace(/\)/g, '\\)');
}

function cmdText(x, y, value, size = 8, font = 'F1', color = colors.black) {
  return `${color} rg BT /${font} ${size} Tf ${x.toFixed(2)} ${y.toFixed(2)} Td (${escapePdfText(value)}) Tj ET\n`;
}

function textWidth(value, size = 8) {
  return String(value).length * size * 0.52;
}

function centerText(x, y, value, size = 8, font = 'F1', color = colors.black) {
  return cmdText(x - textWidth(value, size) / 2, y, value, size, font, color);
}

function rightText(x, y, value, size = 8, font = 'F1', color = colors.black) {
  return cmdText(x - textWidth(value, size), y, value, size, font, color);
}

function rect(x, y, w, h, color) {
  if (w <= 0 || h <= 0) return '';
  return `${color} rg ${x.toFixed(2)} ${y.toFixed(2)} ${w.toFixed(2)} ${h.toFixed(2)} re f\n`;
}

function strokeRect(x, y, w, h, color = colors.axis, width = 0.5) {
  if (w <= 0 || h <= 0) return '';
  return `${color} RG ${width} w ${x.toFixed(2)} ${y.toFixed(2)} ${w.toFixed(2)} ${h.toFixed(2)} re S\n`;
}

function line(x1, y1, x2, y2, color = colors.grid, width = 0.35) {
  return `${color} RG ${width} w ${x1.toFixed(2)} ${y1.toFixed(2)} m ${x2.toFixed(2)} ${y2.toFixed(2)} l S\n`;
}

function hatchRect(x, y, w, h, color, hatch = 0) {
  let out = rect(x, y, w, h, color);
  out += strokeRect(x, y, w, h, colors.white, 0.35);
  out += strokeRect(x, y, w, h, colors.axis, 0.25);
  if (!hatch || w < 6 || h < 6) return out;

  out += `q ${x.toFixed(2)} ${y.toFixed(2)} ${w.toFixed(2)} ${h.toFixed(2)} re W n ${colors.white} RG 0.55 w\n`;
  if (hatch === 1) {
    for (let d = -h; d < w + h; d += 7) {
      out += `${(x + d).toFixed(2)} ${y.toFixed(2)} m ${(x + d + h).toFixed(2)} ${(y + h).toFixed(2)} l S\n`;
    }
  } else if (hatch === 2) {
    for (let d = 3; d < w; d += 7) {
      out += `${(x + d).toFixed(2)} ${y.toFixed(2)} m ${(x + d).toFixed(2)} ${(y + h).toFixed(2)} l S\n`;
    }
  } else if (hatch === 3) {
    for (let d = 4; d < h; d += 7) {
      out += `${x.toFixed(2)} ${(y + d).toFixed(2)} m ${(x + w).toFixed(2)} ${(y + d).toFixed(2)} l S\n`;
    }
  }
  out += 'Q\n';
  return out;
}

function marker(x, y, size, color, shape = 0) {
  const r = size / 2;
  if (shape === 1) {
    return `${color} rg ${(x).toFixed(2)} ${(y + r).toFixed(2)} m ${(x + r).toFixed(2)} ${y.toFixed(2)} l ${x.toFixed(2)} ${(y - r).toFixed(2)} l ${(x - r).toFixed(2)} ${y.toFixed(2)} l h f\n`;
  }
  if (shape === 2) {
    return `${color} rg ${x.toFixed(2)} ${(y + r).toFixed(2)} m ${(x + r).toFixed(2)} ${(y - r).toFixed(2)} l ${(x - r).toFixed(2)} ${(y - r).toFixed(2)} l h f\n`;
  }
  if (shape === 3) {
    return `${color} RG 1.1 w ${(x - r).toFixed(2)} ${(y - r).toFixed(2)} m ${(x + r).toFixed(2)} ${(y + r).toFixed(2)} l S ${color} RG 1.1 w ${(x - r).toFixed(2)} ${(y + r).toFixed(2)} m ${(x + r).toFixed(2)} ${(y - r).toFixed(2)} l S\n`;
  }
  if (shape === 4) {
    return `${color} rg ${(x - r).toFixed(2)} ${(y - r).toFixed(2)} ${size.toFixed(2)} ${size.toFixed(2)} re f\n`;
  }
  const c = 0.55228475 * r;
  return `${color} rg ${(x + r).toFixed(2)} ${y.toFixed(2)} m ${(x + r).toFixed(2)} ${(y + c).toFixed(2)} ${(x + c).toFixed(2)} ${(y + r).toFixed(2)} ${x.toFixed(2)} ${(y + r).toFixed(2)} c ${(x - c).toFixed(2)} ${(y + r).toFixed(2)} ${(x - r).toFixed(2)} ${(y + c).toFixed(2)} ${(x - r).toFixed(2)} ${y.toFixed(2)} c ${(x - r).toFixed(2)} ${(y - c).toFixed(2)} ${(x - c).toFixed(2)} ${(y - r).toFixed(2)} ${x.toFixed(2)} ${(y - r).toFixed(2)} c ${(x + c).toFixed(2)} ${(y - r).toFixed(2)} ${(x + r).toFixed(2)} ${(y - c).toFixed(2)} ${(x + r).toFixed(2)} ${y.toFixed(2)} c f\n`;
}

function poly(points, color, width = 1.2, fill = null) {
  if (points.length < 2) return '';
  let out = '';
  if (fill) out += `${fill} rg `;
  out += `${color} RG ${width} w ${points[0][0].toFixed(2)} ${points[0][1].toFixed(2)} m `;
  for (const [x, y] of points.slice(1)) out += `${x.toFixed(2)} ${y.toFixed(2)} l `;
  out += 'h ';
  out += fill ? 'B\n' : 'S\n';
  return out;
}

function buildPdf(content, width = FIGURE_WIDTH, height = FIGURE_HEIGHT) {
  const objects = [
    '<< /Type /Catalog /Pages 2 0 R >>',
    '<< /Type /Pages /Kids [3 0 R] /Count 1 >>',
    `<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${width} ${height}] /Resources << /Font << /F1 4 0 R /F2 5 0 R >> >> /Contents 6 0 R >>`,
    '<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>',
    '<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>',
    `<< /Length ${Buffer.byteLength(content, 'utf8')} >>\nstream\n${content}endstream`,
  ];
  let pdf = '%PDF-1.4\n';
  const offsets = [0];
  objects.forEach((object, index) => {
    offsets.push(Buffer.byteLength(pdf, 'utf8'));
    pdf += `${index + 1} 0 obj\n${object}\nendobj\n`;
  });
  const xrefOffset = Buffer.byteLength(pdf, 'utf8');
  pdf += `xref\n0 ${objects.length + 1}\n0000000000 65535 f \n`;
  for (let i = 1; i < offsets.length; i++) {
    pdf += `${String(offsets[i]).padStart(10, '0')} 00000 n \n`;
  }
  pdf += `trailer\n<< /Size ${objects.length + 1} /Root 1 0 R >>\nstartxref\n${xrefOffset}\n%%EOF\n`;
  return Buffer.from(pdf, 'utf8');
}

function save(filename, content, width = FIGURE_WIDTH, height = FIGURE_HEIGHT) {
  fs.mkdirSync(outputDir, { recursive: true });
  fs.writeFileSync(path.join(outputDir, filename), buildPdf(content, width, height));
}

function niceMax(value) {
  if (value <= 10) return 10;
  if (value <= 40) return 40;
  if (value <= 80) return 80;
  if (value <= 140) return 140;
  if (value <= 850) return 850;
  return Math.ceil(value / 100) * 100;
}

function legend(items, x, y, maxWidth = FIGURE_WIDTH - x - 12) {
  let out = '';
  let cursorX = x;
  let cursorY = y;
  for (const item of items) {
    const itemW = 17 + textWidth(item.label, 8.4) + 12;
    if (cursorX > x && cursorX + itemW > x + maxWidth) {
      cursorX = x;
      cursorY -= 13;
    }
    out += hatchRect(cursorX, cursorY + 1, 8.5, 8.5, item.color, item.hatch || 0);
    out += cmdText(cursorX + 12.5, cursorY + 2.2, item.label, 8.4, 'F1', colors.axis);
    cursorX += itemW;
  }
  return out;
}

function groupedBar(filename, labels, series, options = {}) {
  const width = FIGURE_WIDTH;
  const height = FIGURE_HEIGHT;
  const margin = { left: 46, right: 14, top: 38, bottom: 43 };
  const chartW = width - margin.left - margin.right;
  const chartH = height - margin.top - margin.bottom;
  const maxY = options.maxY || niceMax(Math.max(...series.flatMap(s => s.values)) * 1.15);
  const groupW = chartW / labels.length;
  const barW = Math.min(series.length === 1 ? 26 : 19, (groupW * 0.74) / series.length);
  const baseY = margin.bottom;
  const topY = baseY + chartH;
  const showValues = options.showValues ?? series.length <= 2;
  let out = rect(0, 0, width, height, colors.white);
  out += rect(margin.left, baseY, chartW, chartH, colors.band);
  out += legend(series.map((s, index) => ({ label: s.label, color: s.color, hatch: s.hatch ?? index })), margin.left, height - 21);
  if (options.yLabel) out += cmdText(6, topY + 5, options.yLabel, 8.6, 'F2', colors.axis);
  for (let i = 0; i <= 4; i++) {
    const y = baseY + (chartH * i) / 4;
    const value = (maxY * i) / 4;
    out += line(margin.left, y, width - margin.right, y, colors.grid, 0.45);
    out += rightText(margin.left - 6, y - 3, options.valueLabel ? options.valueLabel(value) : value.toFixed(0), 8, 'F1', colors.gray);
  }
  out += line(margin.left, baseY, margin.left, topY, colors.axis, 0.8);
  out += line(margin.left, baseY, width - margin.right, baseY, colors.axis, 0.8);
  labels.forEach((label, i) => {
    const cx = margin.left + groupW * i + groupW / 2;
    series.forEach((s, j) => {
      const x = cx - (series.length * barW) / 2 + j * barW + 1.5;
      const h = (s.values[i] / maxY) * chartH;
      out += hatchRect(x, baseY, barW - 3, h, s.color, s.hatch ?? j);
      if (showValues) {
        out += centerText(x + (barW - 3) / 2, baseY + h + 5, options.valueLabel ? options.valueLabel(s.values[i]) : s.values[i].toFixed(1), 7.2, 'F2', colors.axis);
      }
    });
    out += centerText(cx, 26, label, 8.4, 'F1', colors.axis);
  });
  out += centerText(margin.left + chartW / 2, 9, options.xLabel || 'Model', 8.8, 'F2', colors.axis);
  save(filename, out, width, height);
}

function horizontalStacked(filename, labels, series, options = {}) {
  const width = FIGURE_WIDTH;
  const height = FIGURE_HEIGHT;
  const margin = { left: 96, right: 18, top: 40, bottom: 36 };
  const chartW = width - margin.left - margin.right;
  const rowGap = (height - margin.top - margin.bottom) / labels.length;
  const barH = Math.min(21, rowGap * 0.62);
  const maxX = options.maxX || niceMax(Math.max(...labels.map((_, i) => series.reduce((sum, s) => sum + s.values[i], 0))));
  let out = rect(0, 0, width, height, colors.white);
  out += legend(series.map((s, index) => ({ label: s.label, color: s.color, hatch: s.hatch ?? index })), margin.left, height - 21);
  if (options.yLabel) out += cmdText(8, height - margin.top + 5, options.yLabel, 8.6, 'F2', colors.axis);
  for (let i = 0; i <= 4; i++) {
    const x = margin.left + (chartW * i) / 4;
    const value = (maxX * i) / 4;
    out += line(x, margin.bottom - 8, x, height - margin.top + 8, colors.grid, 0.45);
    out += centerText(x, 20, options.valueLabel ? options.valueLabel(value) : value.toFixed(0), 8, 'F1', colors.gray);
  }
  labels.forEach((label, i) => {
    const y = height - margin.top - rowGap * (i + 1) + (rowGap - barH) / 2;
    if (i % 2 === 0) out += rect(margin.left, y - 4, chartW, barH + 8, colors.band);
    out += rightText(margin.left - 8, y + barH / 2 - 3, label, 8.8, 'F2', colors.axis);
    let x = margin.left;
    series.forEach((s, seriesIndex) => {
      const w = (s.values[i] / maxX) * chartW;
      out += hatchRect(x, y, w, barH, s.color, s.hatch ?? seriesIndex);
      const labelValue = options.valueLabel ? options.valueLabel(s.values[i]) : s.values[i].toFixed(1);
      if (w > textWidth(labelValue, 7.1) + 8) out += centerText(x + w / 2, y + barH / 2 - 2.5, labelValue, 7.1, 'F2', colors.white);
      x += w;
    });
    if (options.showTotals) {
      const total = series.reduce((sum, s) => sum + s.values[i], 0);
      out += cmdText(x + 4, y + barH / 2 - 3, options.valueLabel ? options.valueLabel(total) : total.toFixed(1), 7.4, 'F2', colors.axis);
    }
  });
  out += line(margin.left, margin.bottom - 8, margin.left + chartW, margin.bottom - 8, colors.axis, 0.8);
  out += centerText(margin.left + chartW / 2, 6, options.xLabel || '', 8.8, 'F2', colors.axis);
  save(filename, out, width, height);
}

function scatter(filename, pointsByModel, options = {}) {
  const width = FIGURE_WIDTH;
  const height = FIGURE_HEIGHT + 8;
  const margin = { left: 46, right: 14, top: 40, bottom: 44 };
  const chartW = width - margin.left - margin.right;
  const chartH = height - margin.top - margin.bottom;
  const xMin = options.xMin ?? 0;
  const xMax = options.xMax ?? 10;
  const yMin = options.yMin ?? 0;
  const yMax = options.yMax ?? 100;
  let out = rect(0, 0, width, height, colors.white);
  out += rect(margin.left, margin.bottom, chartW, chartH, colors.band);
  out += legend(modelLabels.map((label, i) => ({ label, color: palette[i], hatch: 0 })), margin.left, height - 21);
  if (options.yLabel) out += cmdText(6, margin.bottom + chartH + 5, options.yLabel, 8.4, 'F2', colors.axis);
  for (let i = 0; i <= 4; i++) {
    const y = margin.bottom + (chartH * i) / 4;
    const value = yMin + ((yMax - yMin) * i) / 4;
    out += line(margin.left, y, width - margin.right, y, colors.grid, 0.45);
    out += rightText(margin.left - 6, y - 3, options.yLabelFormat ? options.yLabelFormat(value) : value.toFixed(0), 8, 'F1', colors.gray);
  }
  for (let i = 0; i <= 5; i++) {
    const x = margin.left + (chartW * i) / 5;
    const value = xMin + ((xMax - xMin) * i) / 5;
    out += line(x, margin.bottom, x, margin.bottom + chartH, colors.grid, 0.35);
    out += centerText(x, 27, options.xLabelFormat ? options.xLabelFormat(value) : value.toFixed(1), 8, 'F1', colors.gray);
  }
  out += line(margin.left, margin.bottom, margin.left, margin.bottom + chartH, colors.axis, 0.8);
  out += line(margin.left, margin.bottom, margin.left + chartW, margin.bottom, colors.axis, 0.8);
  pointsByModel.forEach((points, modelIndex) => {
    points.forEach(([xValue, yValue]) => {
      const x = margin.left + ((xValue - xMin) / (xMax - xMin)) * chartW;
      const y = margin.bottom + ((yValue - yMin) / (yMax - yMin)) * chartH;
      out += marker(x, y, 3.7, palette[modelIndex], modelIndex);
    });
  });
  out += centerText(margin.left + chartW / 2, 9, options.xLabel || '', 8.8, 'F2', colors.axis);
  save(filename, out, width, height);
}

function radar(filename) {
  const width = FIGURE_WIDTH;
  const height = FIGURE_HEIGHT;
  const cx = 210;
  const cy = 118;
  const r = 86;
  const axes = ['Pass@1', 'Pylint', 'Complexity'];
  const values = modelNames.map((_, i) => [
    aggregate.pass[i],
    aggregate.pylint[i] * 10,
    aggregate.complexity[i],
  ]);
  let out = rect(0, 0, width, height, colors.white);
  out += legend(modelLabels.map((label, i) => ({ label, color: palette[i] })), 42, height - 21);
  for (const rr of [0.25, 0.5, 0.75, 1]) {
    const pts = axes.map((_, i) => {
      const a = -Math.PI / 2 + (i * 2 * Math.PI) / axes.length;
      return [cx + Math.cos(a) * r * rr, cy + Math.sin(a) * r * rr];
    });
    out += poly(pts, colors.grid, 0.45);
    out += cmdText(cx + 5, cy + r * rr - 2, `${Math.round(rr * 100)}`, 6.8, 'F1', colors.gray);
  }
  axes.forEach((label, i) => {
    const a = -Math.PI / 2 + (i * 2 * Math.PI) / axes.length;
    out += line(cx, cy, cx + Math.cos(a) * r, cy + Math.sin(a) * r, colors.grid, 0.45);
    out += centerText(cx + Math.cos(a) * (r + 19), cy + Math.sin(a) * (r + 19) - 2, label, 8.6, 'F2', colors.axis);
  });
  values.forEach((vals, modelIndex) => {
    const pts = vals.map((v, i) => {
      const a = -Math.PI / 2 + (i * 2 * Math.PI) / axes.length;
      return [cx + Math.cos(a) * r * (v / 100), cy + Math.sin(a) * r * (v / 100)];
    });
    out += poly(pts, palette[modelIndex], 1.35);
    pts.forEach(([x, y]) => {
      out += marker(x, y, 4.3, palette[modelIndex], modelIndex);
    });
  });
  save(filename, out, width, height);
}

function readScatterData() {
  if (!fs.existsSync(resultsPath)) return { pylint: [], exec: [] };
  const results = JSON.parse(fs.readFileSync(resultsPath, 'utf8'));
  const pylint = modelNames.map(() => []);
  const exec = modelNames.map(() => []);
  for (const file of results) {
    for (const model of Object.values(file.models || {})) {
      const index = modelNames.indexOf(model.model_name);
      if (index === -1) continue;
      const metrics = model.metrics || {};
      if (Number.isFinite(metrics.pylint_score)) {
        const total = metrics.unit_tests_total || 1;
        const formatPct = ((metrics.format_match_passed || 0) / total) * 100;
        pylint[index].push([metrics.pylint_score, formatPct]);
      }
      if (Number.isFinite(metrics.loc_ratio) && Number.isFinite(metrics.exec_time_python_avg_ms)) {
        exec[index].push([metrics.loc_ratio, metrics.exec_time_python_avg_ms]);
      }
    }
  }
  return { pylint, exec };
}

function exportTokenUsage() {
  if (!fs.existsSync(usagePath)) return;
  const taskLabels = {
    translation: 'Translation',
    python_to_cobol_inputs: 'P2C Inputs',
    boundary_test_generation: 'Boundary Tests',
    input_generation: 'Forward Inputs',
    executive_summary: 'Executive Summary',
  };
  const taskOrder = ['translation', 'python_to_cobol_inputs', 'boundary_test_generation', 'input_generation', 'executive_summary'];
  const usage = JSON.parse(fs.readFileSync(usagePath, 'utf8'));
  const stats = {};
  for (const entry of usage) {
    const type = entry.type || 'unknown';
    stats[type] ||= { prompt: 0, completion: 0, requests: 0 };
    stats[type].prompt += entry.prompt_tokens || 0;
    stats[type].completion += entry.completion_tokens || 0;
    stats[type].requests += 1;
  }
  const labels = taskOrder.filter(type => stats[type]).map(type => taskLabels[type]);
  const prompt = taskOrder.filter(type => stats[type]).map(type => stats[type].prompt / 1000);
  const completion = taskOrder.filter(type => stats[type]).map(type => stats[type].completion / 1000);
  horizontalStacked('fig_new_token_usage.pdf', labels, [
    { label: 'Prompt', color: colors.blue, hatch: 0, values: prompt },
    { label: 'Completion', color: colors.vermillion, hatch: 1, values: completion },
  ], { maxX: 1000, xLabel: 'Tokens (thousands)', valueLabel: v => `${v.toFixed(0)}k` });
}

const pct = value => `${value.toFixed(1)}%`;
const one = value => value.toFixed(1);
const integer = value => value.toFixed(0);

groupedBar('fig_new_match_comparison.pdf', modelLabels, [
  { label: 'Format Match', color: colors.teal, hatch: 1, values: aggregate.format },
  { label: 'Semantic Match', color: colors.orange, hatch: 0, values: aggregate.semantic },
], { maxY: 40, yLabel: 'Percent', valueLabel: pct });

groupedBar('fig_new_hard_soft_delta.pdf', modelLabels, [
  { label: 'Format Match', color: colors.teal, hatch: 1, values: aggregate.format },
  { label: 'Semantic Match', color: colors.orange, hatch: 0, values: aggregate.semantic },
  { label: 'Gap', color: colors.blue, hatch: 2, values: aggregate.semantic.map((v, i) => v - aggregate.format[i]) },
], { maxY: 40, yLabel: 'Percent', valueLabel: pct, showValues: false });

horizontalStacked('fig_new_test_outcome.pdf', modelLabels, [
  { label: 'Pass@1', color: colors.teal, hatch: 0, values: aggregate.pass },
  { label: 'Partial Semantic Match', color: colors.orange, hatch: 1, values: aggregate.semantic.map((v, i) => Math.max(v - aggregate.pass[i], 0)) },
  { label: 'Failed', color: colors.red, hatch: 2, values: aggregate.semantic.map(v => Math.max(100 - v, 0)) },
], { maxX: 100, xLabel: 'Percent of model-file evaluations', valueLabel: pct });

groupedBar('fig_new_consensus_failure.pdf', modelLabels, [
  { label: 'Failed Files', color: colors.orange, hatch: 1, values: aggregate.failedFiles },
], { maxY: 126, yLabel: 'Files', valueLabel: integer });

groupedBar('fig_new_error_pattern.pdf', modelLabels, [
  { label: 'Logic Error', color: colors.purple, hatch: 0, values: errorCounts.logic },
  { label: 'Whitespace Error', color: colors.sky, hatch: 1, values: errorCounts.whitespace },
  { label: 'Runtime Crash', color: colors.red, hatch: 2, values: errorCounts.crash },
], { maxY: 120, yLabel: 'Failed Files', valueLabel: integer, showValues: false });

groupedBar('fig_new_boundary_faithfulness.pdf', modelLabels, [
  { label: 'Boundary Faithfulness', color: colors.orange, hatch: 1, values: aggregate.boundary },
], { maxY: 20, yLabel: 'Percent', valueLabel: pct });

radar('fig_new_radar_quality.pdf');

const scatterData = readScatterData();
scatter('fig_new_pylint_scatter.pdf', scatterData.pylint, {
  xMin: 0, xMax: 10, yMin: 0, yMax: 100, xLabel: 'Pylint Score', yLabel: 'Format Match (%)',
});

groupedBar('fig_new_complexity.pdf', modelLabels, [
  { label: 'Complexity Reduction', color: colors.blue, hatch: 1, values: aggregate.complexity },
], { maxY: 80, yLabel: 'Percent', valueLabel: pct });

groupedBar('fig_new_maintainability.pdf', modelLabels, [
  { label: 'Halstead Effort', color: colors.purple, hatch: 1, values: aggregate.halstead },
], { maxY: 850, yLabel: 'Effort', valueLabel: integer });

scatter('fig_new_exec_vs_size.pdf', scatterData.exec, {
  xMin: 0, xMax: 1.3, yMin: 80, yMax: 180, xLabel: 'LOC ratio', yLabel: 'Local Execution Time (ms)',
  xLabelFormat: value => value.toFixed(1),
});

exportTokenUsage();

console.log(`Exported article figures to ${outputDir}`);
