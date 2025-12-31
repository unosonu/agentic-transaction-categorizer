# 📊 Agentic Transaction Categorizer

### *Turning Cryptic Bank Statements into High-Fidelity Market Intelligence*

This repository provides an end-to-end framework for high-precision transaction enrichment. Unlike traditional rule-based systems that fail on obscure merchant strings, this project uses an **Agentic Workflow** (via LangGraph) and **Graph RAG** to research and categorize merchants in real-time using local LLMs.

---

## 📁 Repository Structure

```text
agentic-transaction-categorizer/
├── .env.example            # Template for API keys (Rename to .env)
├── .gitignore              # Prevents leaking keys/data
├── main.py                 # CLI Entry point: runs the research/graph pipeline
├── requirements.txt        # Project dependencies
├── src/
│   ├── graph.py            # LangGraph State Machine & routing logic
│   ├── nodes.py            # Node logic: Router, WebSearch, and Categorizer
│   └── prompts.py          # Llama 3 optimized system prompts
└── data/                   # Sample anonymized transaction datasets


---

## 🚀 Key Features

- **Autonomous Research Agent:** A self-correcting loop that identifies obscure merchants (e.g., *"See the Light"*) and performs deep web research before categorizing.  
- **Privacy-First Architecture:** Powered by **Ollama** and **Llama 3**. Sensitive financial data never leaves your local machine.  
- **Graph RAG Intelligence:** Maps merchants to their parent companies and industry nodes, enabling macro-economic analysis.  
- **Strict JSON Output:** Uses a `JsonOutputParser` to ensure results are ready for database ingestion.  

---

## 🛠️ Quick Start

### 1. Prerequisites

- Install [Ollama](https://ollama.ai/) and pull the model:  

ollama run llama3

- Get a free [Serper API Key](https://serper.dev/) for web research.

### 2. Installation

git clone https://github.com/your-username/agentic-transaction-categorizer.git
cd agentic-transaction-categorizer
pip install -r requirements.txt

### 3. Configuration

cp .env.example .env

Open .env and add your SERPER_API_KEY
text

### 4. Run Categorization

python main.py --merchant "LEBARA MOBILE LIMITED"

---

## 🧠 Success Stories (Verified Results)

These examples show how the agent turns raw, cryptic input into precise, context-aware classifications.

| Raw Input         | Research Result (Context)                              | Category  | Subcategory       |
|-------------------|--------------------------------------------------------|------------|-------------------|
| LEBARA MOBILE     | MVNO operating in the UK using Vodafone network.       | Bills      | Mobile Networks   |
| SEE THE LIGHT     | UK-based fiber optic and utility provider.             | Bills      | Telecommunications |
| SAINSBURY'S       | Major UK supermarket chain and food retailer.          | Groceries  | Supermarkets      |
| MARKS AND SPENCER | Traditional multichannel department store.             | Shopping   | Department Store  |

**Example Output Logic:**

---

## 📈 The "Alpha" Advantage: Market Prediction

This tool isn't just for budgeting — it's for **Market Alpha**. By aggregating high-fidelity categories, you can:

- **Revenue Forecasting:** Track daily spending volume for public companies (e.g., Sainsbury’s, Marks & Spencer) weeks before quarterly earnings calls.  
- **Consumer Sentiment Shifts:** Detect when spending moves from "Entertainment" to "Bills" categories in real-time.  
- **Substitution Trends:** Monitor if consumers are switching from high-end retailers to discount grocery chains based on the agent’s categorizations.  

---

**License:** [Apache 2.0](LICENSE)  
