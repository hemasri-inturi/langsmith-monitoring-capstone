"""Upload capstone CSA traces to LangSmith.

Uploads customer-support-agent (CSA) runs to a LangSmith project using the
two-step batch_ingest_runs() create+update pattern: create runs first, then
update them with timing, costs, token counts, and feedback (thumbs up/down).
Timestamps are shifted into a recent window and per-thread user-satisfaction
LLM-judge scores are attached as feedback.

Usage:
    python upload_csa_traces.py --input capstone_traces.jsonl --project ACME-capstone

Full script available in project workspace.
"""
