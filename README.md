# TriageFlow

## A Real-Time Patient Priority Queue Platform

TriageFlow is a real-time priority queue management platform, built as a
backend-engineering portfolio project. It uses a hospital "patient triage"
scenario as its demonstration use case — the underlying platform architecture
itself is domain-agnostic and could equally represent a bank, clinic, airport,
university, or support-center queue.

This is **not** intended for real medical, financial, or governmental use.

## Design Philosophy

TriageFlow's hospital-triage presentation is a demonstration layer only. The
backend architecture underneath is deliberately kept domain-agnostic: queues,
entries, priority ordering, roles, and real-time updates are all modeled as
generic concepts, not hospital-specific ones. The same backend could support
a bank's teller queue, a university service desk, an airport gate, or a
customer support line with different seed data and business rules — not a
different architecture. Where this document or the code says "TriageFlow,"
it refers to this specific demonstration; where it describes the platform's
architecture, that description is intended to remain generic.

## Backend Setup

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
uvicorn app.main:app --reload
```

Then verify:
- `http://localhost:8000/health` — should return a JSON status payload.
- `http://localhost:8000/docs` — Swagger UI, showing the `/health` route.
