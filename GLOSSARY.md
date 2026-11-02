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
