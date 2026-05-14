import fs from 'node:fs';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const root = process.cwd();
const args = process.argv.slice(2);

function getArg(name, fallback) {
  const prefix = `--${name}=`;
  const match = args.find(arg => arg.startsWith(prefix));
  return match ? match.slice(prefix.length) : fallback;
}

function hasFlag(name) {
  return args.includes(`--${name}`);
}

const articleDir = path.resolve(root, getArg('article-dir', path.join('article', 'pycobolix_last_converted')));
const mainFile = getArg('main', 'main.tex');
const requestedEngine = getArg('engine', 'auto');
const shouldClean = hasFlag('clean');

function fail(message, code = 1) {
  console.error(message);
  process.exit(code);
}

function commandExists(command, versionArgs = ['--version']) {
  const result = spawnSync(command, versionArgs, { stdio: 'ignore' });
  return !result.error && result.status === 0;
}

const commonLatexBinDirs = [
  process.env.LOCALAPPDATA && path.join(process.env.LOCALAPPDATA, 'Programs', 'MiKTeX', 'miktex', 'bin', 'x64'),
  process.env.ProgramFiles && path.join(process.env.ProgramFiles, 'MiKTeX', 'miktex', 'bin', 'x64'),
  process.env['ProgramFiles(x86)'] && path.join(process.env['ProgramFiles(x86)'], 'MiKTeX', 'miktex', 'bin', 'x64'),
].filter(Boolean);

function commandCandidates(command) {
  const executableName = process.platform === 'win32' && !path.extname(command)
    ? `${command}.exe`
    : command;
  return [
    command,
    ...commonLatexBinDirs.map(dir => path.join(dir, executableName)),
  ];
}

function resolveCommand(command, versionArgs = ['--version']) {
  for (const candidate of commandCandidates(command)) {
    if (commandExists(candidate, versionArgs)) {
      return candidate;
    }
  }
  return null;
}

const resolvedCommands = {
  latexmk: resolveCommand('latexmk'),
  tectonic: resolveCommand('tectonic'),
  pdflatex: resolveCommand('pdflatex'),
  bibtex: resolveCommand('bibtex', ['--version']),
};

function run(command, commandArgs, options = {}) {
  const result = spawnSync(command, commandArgs, {
    cwd: articleDir,
    stdio: 'inherit',
    shell: false,
    ...options,
  });

  if (result.error) {
    fail(`Failed to run ${command}: ${result.error.message}`);
  }
  if (result.status !== 0) {
    fail(`${command} exited with code ${result.status}.`);
  }
}

function pickEngine() {
  if (requestedEngine !== 'auto') {
    return requestedEngine;
  }
  if (resolvedCommands.latexmk) return 'latexmk';
  if (resolvedCommands.tectonic) return 'tectonic';
  if (resolvedCommands.pdflatex) return 'pdflatex';
  return null;
}

if (!fs.existsSync(articleDir)) {
  fail(`Article directory not found: ${articleDir}`);
}

const mainPath = path.join(articleDir, mainFile);
if (!fs.existsSync(mainPath)) {
  fail(`Main LaTeX file not found: ${mainPath}`);
}

const engine = pickEngine();
if (!engine) {
  fail([
    'No LaTeX engine found.',
    'Install one of: latexmk, tectonic, or pdflatex + bibtex.',
    `Then run: npm run article:compile`,
  ].join('\n'));
}

if (shouldClean && engine === 'latexmk') {
  run(resolvedCommands.latexmk || 'latexmk', ['-C', mainFile]);
}

if (engine === 'latexmk') {
  run(resolvedCommands.latexmk || 'latexmk', ['-pdf', '-interaction=nonstopmode', '-halt-on-error', mainFile]);
} else if (engine === 'tectonic') {
  run(resolvedCommands.tectonic || 'tectonic', [mainFile]);
} else if (engine === 'pdflatex') {
  const pdflatex = resolvedCommands.pdflatex || 'pdflatex';
  run(pdflatex, ['-interaction=nonstopmode', '-halt-on-error', mainFile]);
  const auxFile = mainFile.replace(/\.tex$/i, '.aux');
  if (fs.existsSync(path.join(articleDir, auxFile)) && resolvedCommands.bibtex) {
    run(resolvedCommands.bibtex, [mainFile.replace(/\.tex$/i, '')]);
  }
  run(pdflatex, ['-interaction=nonstopmode', '-halt-on-error', mainFile]);
  run(pdflatex, ['-interaction=nonstopmode', '-halt-on-error', mainFile]);
} else {
  fail(`Unsupported engine: ${engine}`);
}

const pdfPath = path.join(articleDir, mainFile.replace(/\.tex$/i, '.pdf'));
if (fs.existsSync(pdfPath)) {
  console.log(`Compiled ${pdfPath}`);
} else {
  console.warn(`Compilation finished, but expected PDF was not found: ${pdfPath}`);
}
