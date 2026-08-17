# ai-runbook

A 180-day log of moving from platform reliability into AI engineering.

I work on container platform reliability and diagnostics. I'm building toward AI systems
engineering — retrieval, evaluation, agents, and the observability layer underneath them.
This repository is the daily record: every commit is one session's work.

**Rules I'm holding myself to**

- One session a day, 45 minutes, timer running
- No AI writes my code during learning sessions — I struggle for 15 minutes first, then read the docs
- Every week I delete something I built and rebuild it from an empty file, no reference
- Days are numbered, never dated — a missed week means I resume at the same number, not restart

**Structure**

| Path | What's in it |
|---|---|
| `days/` | One folder per day. The session's code. |
| `katas/` | 8-minute origination drills, written from empty files |
| `notes/` | Teach-back notes — each day explained in five sentences |
| `projects/` | Real systems. Starts empty; earns its contents around day 60. |
| `PROGRESS.md` | The day log |
| `questions.md` | Rabbit holes I parked instead of chasing |

**Phases**

| Phase | Days | Focus |
|---|---|---|
| 01 | 1–28 | Python to production standard, and originating code from nothing |
| 02 | 29–56 | LLM APIs, structured output, cost, failure modes |
| 03 | 57–91 | Retrieval: chunking, embeddings, hybrid search, reranking |
| 04 | 92–119 | Evaluation: golden sets, faithfulness, CI regression gates |
| 05 | 120–147 | Agents and observability: tracing, cost attribution, SLOs |
| 06 | 148–180 | Vertex AI, the signature project, and shipping it |

Each phase ends in a gate. I don't advance on schedule; I advance when I can rebuild the
phase's work unaided.

---

*Started August 2026. Currently in Phase 01.*
