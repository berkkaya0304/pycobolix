import fs from 'node:fs';
import path from 'node:path';

const root = process.cwd();
const usagePath = path.join(root, 'public', 'output', 'llm_usage.json');
const outputDir = path.join(root, 'article', 'pycobolix_last_converted');
const outputPath = path.join(outputDir, 'fig_new_token_usage.pdf');

const taskLabels = {
  translation: 'Translation',
  python_to_cobol_inputs: 'Python-to-COBOL Inputs',
  boundary_test_generation: 'Boundary Tests',
  input_generation: 'Forward Inputs',
  executive_summary: 'Executive Summary',
};

const taskOrder = [
  'translation',
  'python_to_cobol_inputs',
  'boundary_test_generation',
  'input_generation',
  'executive_summary',
];

function fail(message) {
  console.error(message);
  process.exit(1);
}

function escapePdfText(value) {
  return String(value).replace(/\\/g, '\\\\').replace(/\(/g, '\\(').replace(/\)/g, '\\)');
}

function formatK(value) {
  return `${(value / 1000).toFixed(1)}k`;
}

function text(x, y, value, size = 9, font = 'F1') {
  return `BT /${font} ${size} Tf ${x.toFixed(2)} ${y.toFixed(2)} Td (${escapePdfText(value)}) Tj ET\n`;
}

function rect(x, y, w, h, color) {
  return `${color} rg ${x.toFixed(2)} ${y.toFixed(2)} ${w.toFixed(2)} ${h.toFixed(2)} re f\n`;
}

function line(x1, y1, x2, y2, color = '0.65 0.65 0.65', width = 0.4) {
  return `${color} RG ${width} w ${x1.toFixed(2)} ${y1.toFixed(2)} m ${x2.toFixed(2)} ${y2.toFixed(2)} l S\n`;
}

function buildPdf(content, width = 612, height = 396) {
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
  pdf += `xref\n0 ${objects.length + 1}\n`;
  pdf += '0000000000 65535 f \n';
  for (let i = 1; i < offsets.length; i++) {
    pdf += `${String(offsets[i]).padStart(10, '0')} 00000 n \n`;
  }
  pdf += `trailer\n<< /Size ${objects.length + 1} /Root 1 0 R >>\nstartxref\n${xrefOffset}\n%%EOF\n`;
  return Buffer.from(pdf, 'utf8');
}

if (!fs.existsSync(usagePath)) {
  fail(`Missing usage file: ${usagePath}`);
}

const usage = JSON.parse(fs.readFileSync(usagePath, 'utf8'));
const stats = {};

for (const entry of usage) {
  const type = entry.type || 'unknown';
  if (!stats[type]) {
    stats[type] = { prompt: 0, completion: 0, requests: 0 };
  }
  stats[type].prompt += entry.prompt_tokens || 0;
  stats[type].completion += entry.completion_tokens || 0;
  stats[type].requests += 1;
}

const rows = taskOrder
  .filter(type => stats[type])
  .map(type => ({
    label: taskLabels[type] || type,
    prompt: stats[type].prompt,
    completion: stats[type].completion,
    total: stats[type].prompt + stats[type].completion,
    requests: stats[type].requests,
  }));

const pageWidth = 612;
const pageHeight = 396;
const chartX = 190;
const chartY = 90;
const chartW = 330;
const barH = 19;
const rowGap = 33;
const maxTotal = Math.max(...rows.map(row => row.total), 1);
let content = '';

content += rect(0, 0, pageWidth, pageHeight, '1 1 1');
content += rect(58, 344, 10, 10, '0.388 0.400 0.945');
content += text(73, 346, 'Prompt Tokens', 8, 'F1');
content += rect(170, 344, 10, 10, '0.925 0.282 0.600');
content += text(185, 346, 'Completion Tokens', 8, 'F1');

for (let i = 0; i <= 4; i++) {
  const x = chartX + (chartW * i) / 4;
  const value = (maxTotal * i) / 4;
  content += line(x, chartY - 12, x, chartY + rowGap * rows.length + 4, '0.88 0.88 0.88', 0.35);
  content += text(x - 12, chartY - 30, formatK(value), 7, 'F1');
}

rows.forEach((row, index) => {
  const y = chartY + rowGap * (rows.length - 1 - index);
  const promptW = (row.prompt / maxTotal) * chartW;
  const completionW = (row.completion / maxTotal) * chartW;
  content += text(58, y + 5, row.label, 8, 'F2');
  content += text(58, y - 7, `${row.requests} requests`, 7, 'F1');
  content += rect(chartX, y, promptW, barH, '0.388 0.400 0.945');
  content += rect(chartX + promptW, y, completionW, barH, '0.925 0.282 0.600');
  content += text(chartX + promptW + completionW + 8, y + 5, formatK(row.total), 8, 'F2');
});

content += line(chartX, chartY - 12, chartX + chartW, chartY - 12, '0.45 0.45 0.45', 0.5);
content += text(chartX + 105, 32, 'Tokens (thousands)', 8, 'F1');

fs.mkdirSync(outputDir, { recursive: true });
fs.writeFileSync(outputPath, buildPdf(content, pageWidth, pageHeight));
console.log(`Exported ${outputPath}`);
