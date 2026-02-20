# 🧠 Agent Eval Lab
Author-Aniket Waichal

<p align="center">
  <b>A Production-Style Multi-Step Agent Evaluation Lab</b><br>
  Built with Ollama, Langfuse, and DeepEval — Fully Local & Free
</p>

---

<p align="center">
  <img src="https://img.shields.io/badge/LLM-Ollama%20%7C%20Llama3-blue" />
  <img src="https://img.shields.io/badge/Tracing-Langfuse-orange" />
  <img src="https://img.shields.io/badge/Evaluation-DeepEval-green" />
  <img src="https://img.shields.io/badge/Testing-Pytest-yellow" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

---

## 🚀 Overview

**Agent Eval Lab** Agent Eval Lab is a fully local framework for evaluating multi-step, tool-using LLM agents. It tracks execution traces, audits tool behavior, scores reasoning quality, and prevents regressions using automated tests.

It demonstrates how to:

- Build a tool-using reasoning agent
- Trace full execution trajectories
- Evaluate agent behavior (not just final answers)
- Detect tool misuse and over-tooling
- Score reasoning quality using LLM-as-judge
- Prevent regressions via automated testing

This project mirrors production-style agent evaluation workflows used in modern AI systems.

---
🧠 Why This Project Is Valuable

This lab demonstrates understanding of:

- Agent orchestration
- Tool-augmented reasoning
- LLM-as-judge evaluation
- Observability-driven debugging
- Regression-safe AI systems

It reflects production-level agent evaluation design.

---
## 👥 Who Is This For?
- ML engineers building tool-using agents
- Researchers studying LLM reasoning
- Developers learning evaluation workflows

---

# 🧠 System Architecture

```text
                ┌────────────────────────┐
                │        User Input       │
                └────────────┬───────────┘
                             ↓
                ┌────────────────────────┐
                │      Planner (LLM)     │
                │   Ollama - llama3      │
                └────────────┬───────────┘
                             ↓
                ┌────────────────────────┐
                │       Tool Calls        │
                │  calculator, converter  │
                └────────────┬───────────┘
                             ↓
                ┌────────────────────────┐
                │       Observations      │
                └────────────┬───────────┘
                             ↓
                ┌────────────────────────┐
                │     Final Answer        │
                └────────────────────────┘
```
---
🔎 Observability Layer (Langfuse)

Each agent run is traced using self-hosted Langfuse.

We capture:

- Planning steps
- Tool selection
- Tool arguments
- Tool outputs
- Execution spans
- Final outputs

---
Langfuse runs locally via Docker:
```bash
http://localhost:3000
```
---

📊 Evaluation Framework (DeepEval + Ollama)

All evaluation is performed locally using:
OllamaModel(model="llama3")

No OpenAI. No paid APIs. Fully offline.

---
🏗 Implemented Metrics
1️⃣ Task Success

Final answer correctness.

2️⃣ Tool Usage Accuracy

Did the agent choose the correct tool?

3️⃣ Tool Argument Accuracy

Were correct arguments passed?

4️⃣ Over-Tooling Detection

Did the agent use unnecessary tools?

5️⃣ Reasoning Quality (GEval)

LLM-as-judge evaluation of reasoning coherence and logical planning.

---
📂 Project Structure
```text
agent-eval-lab/
│
├── agent/
│   ├── planner.py
│   ├── tools.py
│   ├── executor.py
│   └── agent.py
│
├── tracing/
│   └── langfuse_config.py
│
├── evals/
│   ├── dataset.py
│   ├── metrics/
│       ├── tool_usage.py
│       ├── tool_argument_accuracy.py
│       ├── reasoning_quality.py
│       └── task_success.py
│   
│
├── tests/
│   └── test_regression.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
└── run_evals.py
```
---
🎯 Evaluation Philosophy

Traditional evaluation checks only final outputs.

This lab evaluates:

- Behavioral correctness
- Tool decision quality
- Argument precision
- Multi-step reasoning integrity
- Regression stability

This shifts evaluation from output-only validation to trajectory-aware validation.

---
🚀 Setup Guide
1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

2️⃣ Start Ollama
```bash
ollama serve
ollama pull llama3
```

3️⃣ Start Langfuse (Free & Local)
```bash
docker compose up
```

Open:
```bash
http://localhost:3000
```
Create a project and copy the generated keys.

4️⃣ Configure Environment

Create .env:
```bash
LANGFUSE_PUBLIC_KEY=your_local_public_key
LANGFUSE_SECRET_KEY=your_local_secret_key
LANGFUSE_HOST=http://localhost:3000
```

---
📈 Run Evaluations
python run_evals.py

---
🧪 Run Regression Tests
pytest

---

Tests fail if:
- Task success decreases
- Tool behavior changes
- Reasoning quality degrades

---
🔮 Future Improvements

- Latency & performance metrics
- Hallucination detection
- Trajectory scoring benchmarks
- Multi-agent evaluation
- CI/CD integration (GitHub Actions)
- Experiment tracking layer

---