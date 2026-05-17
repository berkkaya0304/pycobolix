<div align="center">
  <h1>🐍 Pycobolix</h1>
  <p><strong>Zero-Shot COBOL-to-Python Modernization & Testing Framework</strong></p>
  
  [![Next.js](https://img.shields.io/badge/Next.js-15-black?logo=next.js)](https://nextjs.org/)
  [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
  [![LLM](https://img.shields.io/badge/Supported_Models-Gemini_%7C_Claude_%7C_Mistral_%7C_Gemma_%7C_Cogito-purple)](#)
  [![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
</div>

<br />

Pycobolix is an open-source, web-based framework designed to automate the translation, testing, and validation of legacy **COBOL** code into modern, readable **Python 3.11** code. Built to address the massive technical debt of billions of lines of enterprise COBOL still running in global financial and government systems, this framework leverages Large Language Models (LLMs) in a strict **zero-shot** setting—requiring absolutely no costly model fine-tuning.

Unlike standard code generation tools, Pycobolix does not blindly trust AI outputs. It features a robust, isolated sandbox environment that automatically executes both the generated Python code and the original GnuCOBOL code against dynamically generated edge-case inputs, verifying semantic equivalence before ever presenting the code to a human developer.

---

## ✨ Key Features

- **🤖 Zero-Shot LLM Translation:** Accurately translates complex COBOL paradigms (including `COMP-3` packed decimals, `REDEFINES` memory overlaps, and unstructured `PERFORM VARYING` loops) without any prior model training.
- **🛡️ Bidirectional Sandbox Validation:** Compares the original GnuCOBOL baseline against the generated Python execution in deeply isolated containers. It supports both **forward testing** (COBOL $\rightarrow$ Python) and **reverse testing** (Python $\rightarrow$ COBOL).
- **🧪 Hybrid Test Generation:** Automatically synthesizes 5 robust test cases per file by prioritizing deterministic Boundary Value Analysis (BVA) for numeric fields, and gracefully falling back to LLM-generated inputs when static analysis borders are exceeded.
- **📊 Comprehensive Metrics:** Computes rigorous empirical metrics, including Semantic Match Rate, Format Match (Hard Match), Pass@1, Halstead Effort, and Cyclomatic Complexity Reduction.
- **🔒 Data Privacy & Local Execution:** Fully supports locally-hosted open-weights models (like **Gemma 4** and **Cogito 21** via Ollama) alongside leading cloud APIs (**Google Gemini 3.1 Pro**, **Claude Opus 4.6**, and **Mistral Large 3**), allowing institutions with strict confidentiality requirements to run the entire pipeline offline or securely in the cloud.

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

## 💻 Tech Stack

- **Frontend & Backend:** [Next.js 15](https://nextjs.org/) (React 19, TypeScript)
- **AI/LLM Integration:** `@google/genai` (Gemini), `ollama` (Local Llama)
- **Code Editor:** `@monaco-editor/react` for in-browser COBOL/Python syntax highlighting
- **Visualizations:** `recharts` for token and metrics charting
- **Reporting:** `jspdf` & `@react-pdf/renderer` for PDF benchmark reports
- **Browser Automation:** `puppeteer` (for UI testing & exporting charts)

---

## 🛠️ Getting Started / Installation

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

3. **Configure Environment Variables:**
   Create a `.env.local` file in the root directory and add your API keys:
   ```env
   # Required if using Google Gemini models
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Start the development server:**
   ```bash
   npm run dev
   ```

5. **Access the Dashboard:**
   Open your browser and navigate to [http://localhost:3000](http://localhost:3000) to begin exploring the Pycobolix interface.

---

## 📁 Project Structure

```text
pycobolix/
├── article/            # LaTeX manuscript and research assets
├── dataset/            # COBOL source files and expected inputs/outputs
├── public/             # Static assets (images, docs, etc.)
├── scripts/            # Utility scripts (compiling articles, exporting charts)
├── src/                # Next.js application source code (app router, components)
├── README.md           # Project documentation
└── package.json        # Dependencies and scripts
```

---

## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is open-source and released under the [MIT License](LICENSE).

For questions, bug reports, or feature requests, please utilize the **GitHub Issues** tracker. Pull requests are warmly welcomed!
