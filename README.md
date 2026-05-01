# 🐍 Pycobolix: Zero-Shot COBOL-to-Python Modernization & Testing Framework

[![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![LLM](https://img.shields.io/badge/Supported_Models-Gemini_3.1_Pro_%7C_Llama_3-purple)](#)

Pycobolix is an open-source, web-based framework designed to automate the translation, testing, and validation of legacy **COBOL** code into modern, readable **Python 3.11** code. Built to address the massive technical debt of billions of lines of enterprise COBOL still running in global financial and government systems, this framework leverages Large Language Models (LLMs) in a strict **zero-shot** setting—requiring absolutely no costly model fine-tuning.

Unlike standard code generation tools, Pycobolix does not blindly trust AI outputs. It features a robust, isolated sandbox environment that automatically executes both the generated Python code and the original GnuCOBOL code against dynamically generated edge-case inputs, verifying semantic equivalence before ever presenting the code to a human developer.

---

## 📸 User Interface (Web Dashboard)

Pycobolix comes with a modern Next.js-based dashboard that allows researchers and engineers to monitor translation queues, inspect sandbox execution metrics, and dive deep into AI-generated benchmark summaries.

| Home | Dashboard |
|:---:|:---:|
| ![Home](./public/docs/ui_home.png) | ![Dashboard](./public/docs/ui_dashboard.png) |
| **Code Explorer** | **Metrics Analysis** |
| ![Explorer](./public/docs/ui_explorer.png) | ![Analysis](./public/docs/ui_analysis.png) |

*(Additional views include Model Settings and Token Usage monitors.)*

---

## ✨ Key Features

- **🤖 Zero-Shot LLM Translation:** Accurately translates complex COBOL paradigms (including `COMP-3` packed decimals, `REDEFINES` memory overlaps, and unstructured `PERFORM VARYING` loops) without any prior model training.
- **🛡️ Bidirectional Sandbox Validation:** Compares the original GnuCOBOL baseline against the generated Python execution in deeply isolated containers. It supports both **forward testing** (COBOL $\rightarrow$ Python) and **reverse testing** (Python $\rightarrow$ COBOL).
- **🧪 Hybrid Test Generation:** Automatically synthesizes 5 robust test cases per file by prioritizing deterministic Boundary Value Analysis (BVA) for numeric fields, and gracefully falling back to LLM-generated inputs when static analysis borders are exceeded.
- **📊 Comprehensive Academic Metrics:** Computes rigorous empirical metrics, including Semantic Match Rate, Format Match (Hard Match), Pass@1, Halstead Effort, and Cyclomatic Complexity Reduction.
- **🔒 Data Privacy & Local Execution:** Fully supports locally-hosted open-weights models (like **Meta Llama 3 via Ollama**) alongside cloud APIs (**Google Gemini 3.1 Pro**), allowing institutions with strict confidentiality requirements to run the entire pipeline offline.

---

## 🏗️ Architecture & Pipeline

To handle the inherent non-determinism of generative AI, Pycobolix is split into two distinct, secure architectural boundaries:

### 1. Generation Environment
- **Ingestion & Prompting:** Raw COBOL source files are ingested and wrapped in optimized, zero-shot prompt templates.
- **Dual-Track Generation:** The translation to Python and the generation of BVA/LLM test inputs occur in parallel via asynchronous API calls, maximizing throughput.

### 2. Execution & Evaluation Environment
- **Cross-Language Sandboxes:** Python 3.11 and GnuCOBOL containers run the identically generated test inputs.
- **Semantic Comparison:** Outputs are compared. Even if formatting (like padding and whitespace) differs, the system strips artifacts to check for a true **Semantic Match**.
- **AI Summary Reporting:** Failing tests are categorized by error type (Logic Error, Whitespace Error, Crash). An auxiliary LLM call aggregates this data into a human-readable PDF benchmark report.

---

## 📈 Experimental Setup & Custom Dataset

General-purpose coding benchmarks (like HumanEval) fail to capture the procedural verbosity and rigid data types of enterprise COBOL. To evaluate Pycobolix, we authored a custom dataset of **110 COBOL programs** ($\approx$9,200 LOC), simulating real-world scenarios like tax calculators, payroll systems, and inventory managers.

Programs were categorized into **Simple, Medium, and Complex** tiers using a custom COBOL-specific complexity score ($C$) that accounts for decision nodes (`IF`, `EVALUATE`), iteration (`PERFORM`), and modular depth (`Paragraphs`).

---

## 🏆 Results & Findings

We benchmarked **Google Gemini 3.1 Pro** (Cloud) against **Meta Llama 3 8B** (Local). The entire pipeline for 110 files—including zero-shot translation, test generation, cross-language sandboxing, and PDF reporting—completed in just **50 minutes**, drastically reducing the estimated 180-200 hours it would take a senior human engineer.

### 1. Translation Accuracy
- **Gemini 3.1 Pro** achieved a **37.3% Semantic Match Rate** across the dataset and a **20.9% Pass@1 Rate** (passing all 5 rigorous test cases on the first try).
- **Llama 3 8B** struggled with COBOL's logic, achieving only a **3.6% Semantic Match**.
- **Format Match (Hard Match):** Both models scored under 5%, proving that exact character-by-character alignment (which COBOL is famous for) remains extremely difficult for generative AI. 

### 2. Reverse Translation Phenomenon
When we evaluated the models in reverse (extracting test inputs from the generated Python, and running them against the original COBOL), accuracy jumped significantly. Gemini improved from 37.3% to **43.6%**, and Llama 3 soared from 3.6% to **30.0%**. This indicates that LLMs often grasp the underlying business logic perfectly, but fail simply due to output formatting discrepancies.

### 3. Code Quality & Optimization
- **Complexity Reduction:** The generated Python code was vastly simpler than the original COBOL. Gemini reduced Cyclomatic Complexity by **51.9%**, and Llama 3 by **63.9%**.
- **Lines of Code (LOC) Ratio:** The Python outputs averaged a ratio of **0.59** (Gemini) and **0.53** (Llama 3), effectively cutting the length of the codebase in half.
- **Type Safety:** The automated `mypy` type checker reported **0 errors** across all generated Python files, confirming excellent adherence to modern type-hinting standards.

### 4. The BVA Penalty & COBOL Truncation
Both models showed **0% boundary faithfulness**. When a field like `PIC 99` was fed an out-of-range value (e.g., `150`), COBOL silently truncates it to `50`. The Python translations consistently threw `ValueError` exceptions instead. This highlights a critical limitation in current LLMs: they fail to replicate language-specific, implicit memory truncation behaviors.

---

## 🛠️ Getting Started / Installation

The Pycobolix dashboard and backend are built on **Next.js**.

### Prerequisites
- **Node.js** (v18.x or higher)
- **npm**, **yarn**, **pnpm**, or **bun**
- *(Optional)* **Ollama** installed and running locally (if using local Llama 3 models)
- *(Optional)* **GnuCOBOL** installed on your host system (for executing baseline sandbox tests)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/berkkaya0304/pycobolix.git
   cd pycobolix
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   ```

4. **Access the Dashboard:**
   Open your browser and navigate to [http://localhost:3000](http://localhost:3000) to begin exploring the Pycobolix interface.

---

## 📄 License & Academic Citation

This project is open-source and released as part of an academic research effort into legacy modernization. 

If you utilize Pycobolix in your research, enterprise modernization pipelines, or literature reviews, please cite the corresponding academic paper (citation details will be provided upon publication). For questions, bug reports, or feature requests, please utilize the **GitHub Issues** tracker. Pull requests are warmly welcomed!
