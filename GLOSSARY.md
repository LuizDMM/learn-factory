# Software factory glossary

Canonical language for this workspace. Add a term **only when Luiz can use it correctly** — this is not a dump of Matt's dictionary.

## Terms

### Software factory

A system of work where a **trigger** starts the agent session (label, cron, CI failure, another session finishing) — not a human opening a chat and pointing it at a ticket. The session can implement, fix, review, lint, whatever. One cron that opens one reviewable PR still counts. This Desktop `/teach` thread is not a factory.

### AFK

The human starts the session, then leaves it unattended. Coffee-after-enter is AFK. It is **not** a factory: you still started it.

### HITL

Human-in-the-loop: you pair **during** the session — redirecting, answering, grilling. This teaching thread. Not the same as reading a PR afterwards.

### Grey box (this lab)

A factory whose output a human still **reads** (draft PR, you review). Humans can also write the issue or approve a plan. Guiding the agent live while it works is HITL, not “grey box factory.”

### Dark factory

A factory where **nobody reads the diff**. Green CI merges. Humans may still file issues. We are not building this. (Not “black box” — that name hides the cut.)

### Model

The frozen parameters used to generate tokens. grok-4.6 in this thread. Not the provider’s servers, not Hermes.

### Harness

The code that uses the model and gives it capabilities: tool calling, the system prompt, MCPs, and so on. Hermes in this thread. `AGENTS.md` is instructions to the harness — not to the agent, and not to the model.
