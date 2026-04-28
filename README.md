# 📊 AI Multi-Agent Data Analyst System

An end-to-end **AI-powered multi-agent system** that converts natural language queries into SQL, analyzes structured data, generates insights, validates them, and visualizes results — all with an interactive UI.

---

## 🚀 Overview

This project demonstrates how to build a **production-ready multi-agent system** using:

* **LangGraph** for orchestration
* **LangChain** for LLM workflows
* **FastAPI** for backend APIs
* **Streamlit** for UI

The system mimics a real-world **AI data analyst**, capable of:

* Understanding user queries
* Generating SQL
* Analyzing datasets
* Producing insights
* Validating results
* Learning from past queries

---

## 🧠 Architecture

```
User Query
   ↓
Planner Agent
   ↓
SQL Generator Agent
   ↓
SQL Execution Agent
   ↓
Visualization Agent
   ↓
Insight Generator Agent
   ↓
Critic Agent (Validation + Retry Loop)
   ↓
Memory Agent (Store Context)
   ↓
Final Response
```

---

## 🤖 Agents

| Agent                   | Responsibility                         |
| ----------------------- | -------------------------------------- |
| **Planner Agent**       | Breaks user query into tasks           |
| **SQL Agent**           | Converts query into SQL                |
| **Execution Agent**     | Executes SQL on dataset                |
| **Insight Agent**       | Generates business insights            |
| **Critic Agent**        | Validates output and retries if needed |
| **Memory Agent**        | Stores and retrieves past context      |
| **Visualization Agent** | Generates charts                       |

---

## 🔥 Features

* ✅ Multi-agent orchestration using LangGraph
* ✅ Natural language → SQL conversion
* ✅ Automated insight generation
* ✅ Critic-based validation loop (self-correction)
* ✅ Context-aware memory for follow-up queries
* ✅ Chart generation (visual insights)
* ✅ REST API with FastAPI
* ✅ Premium chat-based UI using Streamlit

---

## 📁 Project Structure

```
ai-multi-agent-data-analyst/
│
├── app/
│   ├── agents/
│   ├── api/
│   ├── core/
│   ├── graph/
│   ├── utils/
│
├── streamlit_app/
│   ├── components/
│   ├── utils/
│   ├── main.py
│
├── outputs/              # Generated charts
├── data/                 # Sample dataset
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone Repo

```bash
git clone https://github.com/your-username/ai-multi-agent-data-analyst.git
cd ai-multi-agent-data-analyst
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run Backend (FastAPI)

```bash
uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## 💬 Run Frontend (Streamlit)

```bash
streamlit run streamlit_app/main.py
```

UI:

```
http://localhost:8501
```

---

## 🧪 Sample Queries

* “Show revenue by region”
* “Why is south region performing high?”
* “Explain revenue trends”

---

## 🔁 Validation Loop

The system uses a **critic agent** to:

* Validate insights
* Provide feedback
* Retry generation (max 2 times)

This ensures **higher accuracy and reliability**.

---

## 📊 Example Output

```json
{
  "query": "Show revenue by region",
  "insight": "South region has highest revenue...",
  "data": [...],
  "chart_path": "outputs/chart.png",
  "is_valid": true
}
```

---

## 🧠 Key Learnings

* Designing multi-agent workflows
* Handling state with LangGraph
* Implementing retry + validation loops
* Building production-ready AI systems
* Integrating backend with UI

---

## 🚀 Future Improvements

* Add real-time data sources
* Deploy on AWS / Docker
* Add authentication
* Improve visualization (Plotly)
* Support multiple datasets

---

## 👨‍💻 Author

**Omkar Sutar**
AI/ML Engineer | GenAI Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub — it helps a lot!
