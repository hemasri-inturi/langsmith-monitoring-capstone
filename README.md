# ACME Support Agent — LangSmith Monitoring Capstone

Capstone project for **LangChain Academy: Foundation — Monitoring Production Agents**.

This project demonstrates production monitoring for an AI support agent using LangSmith:
uploading traces, tracking costs, and building automated evaluators for quality and security.

## What was built

- **Trace ingestion**: Uploaded 744 runs (131 conversation threads) to LangSmith with
  preserved costs, token counts, and timing information
- **Cost monitoring**: Tracked per-customer spend; identified highest-cost customer
  and expensive model usage patterns
- **Quality evaluators**: LLM-as-judge evaluators scoring thread-level user satisfaction
- **Security evaluators**: Automated PII-leakage and credit-card-number detection
  across agent outputs
- **Human feedback**: Imported 131 thumbs-up/down ratings for evaluator comparison

## Evaluators

| Evaluator | Purpose |
|-----------|---------|
| `pii-leakage-detection` | Flags PII leaks (emails, order numbers, credit cards) in agent responses |
| `credit-card-detection` | Flags credit card numbers in agent outputs |
| `thread-satisfaction` | LLM-judge estimate of user satisfaction per conversation thread |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install langsmith langchain-core langchain-openai python-dotenv

export LANGSMITH_API_KEY="your-key"
export OPENAI_API_KEY="your-key"

python upload_csa_traces.py --input capstone_traces.jsonl --project ACME-capstone
```

## Certificate

[Foundation: Monitoring Production Agents](https://academy.langchain.com/certificates/fqtl0wdbib) — LangChain Academy, Sep 2026
