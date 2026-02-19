Agent Eval Lab

A project for building and evaluating a multi-step reasoning agent with tools, using:
Langfuse → Agent tracing & observability
DeepEval → Behavioral & regression evaluation

------------------------------------------------------------------------------------------------------------------------------------------------
🎯 Purpose

This project demonstrates how to:
Build a multi-step tool-using agent
Trace full agent trajectories
Evaluate agent behavior (not just final answers)
Detect tool misuse
Score reasoning quality
Prevent regressions using CI

-------------------------------------------------------------------------------------------------------------------------------------------------
🧠 Agent Architecture

User Input
   ↓
Planner (LLM)
   ↓
Tool Call(s)
   ↓
Observation
   ↓
Planner
   ↓
Final Answer

-------------------------------------------------------------------------------------------------------------------------------------------------
Each step is logged using Langfuse.
Evaluation is performed offline using DeepEval.

-------------------------------------------------------------------------------------------------------------------------------------------------
📂 Project Structure

agent-eval-lab/
│
├── agent/
│   ├── planner.py              # LLM planning logic
│   ├── tools.py                # Tool implementations
│   ├── executor.py             # Tool execution handler
│   └── agent.py                # Main agent loop
│
├── tracing/
│   └── langfuse_config.py      # Langfuse setup
│
├── evals/
│   ├── dataset.py              # Evaluation task dataset
│   ├── metrics/
│   │   ├── tool_usage.py
│   │   ├── tool_argument_accuracy.py
│   │   ├── reasoning_quality.py
│   │   └── task_success.py
│   └── run_evals.py            # Batch evaluation runner
│
├── tests/
│   └── test_regression.py      # CI regression test
│
├── requirements.txt
└── README.md

-------------------------------------------------------------------------------------------------------------------------------------------------
🏗 Evaluation Design

We evaluate:

1️⃣ Task Success
Final answer correctness

2️⃣ Tool Usage Accuracy
Did the agent choose the correct tools?

3️⃣ Tool Argument Accuracy
Were correct arguments passed?

4️⃣ Over-Tooling
Did the agent use unnecessary tools?

5️⃣ Reasoning Quality
Evaluated using LLM-as-judge (GEval)

-------------------------------------------------------------------------------------------------------------------------------------------------
📊 Dataset Categories

The evaluation dataset includes:
Single-step tool tasks
Multi-step reasoning tasks
No-tool tasks
Ambiguous tasks
Edge cases

This ensures meaningful evaluation coverage.

-------------------------------------------------------------------------------------------------------------------------------------------------
🔎 Observability

Langfuse logs:

Planning steps
Tool calls
Tool arguments
Tool outputs
Final answers
Latency & token usage

-------------------------------------------------------------------------------------------------------------------------------------------------
📈 Evaluation Workflow

