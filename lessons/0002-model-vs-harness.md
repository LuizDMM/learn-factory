---
id: "0002"
kicker: Lesson 0002 · Arc 0
title: Model vs harness
lede: The model predicts tokens. The harness is everything that makes that look like an agent.
time: 2 min watch + 8 min read + cards + grill
watch: https://www.youtube.com/watch?v=oLx4yCbeklQ
read: https://www.aihero.dev/ai-coding-dictionary/harness
activity: Live grill — classify four setups as model, harness, or agent. If they land, you write model and harness into GLOSSARY.md in your own words (no paste).
source: Matt Pocock — YouTube short + AI Coding Dictionary
next: "0003 — Session, context, turn"
---

# Model vs harness

## Watch first

Watch [Claude Code's system tools are SO BLOATED](https://www.youtube.com/watch?v=oLx4yCbeklQ) (~2 min). Then read [Model](https://www.aihero.dev/ai-coding-dictionary/model) and [Harness](https://www.aihero.dev/ai-coding-dictionary/harness). Cards compress those. They do not replace them.

The short is not “how to tune Claude.” It is the cut: **tools and the system prompt live in the harness.** Matt is not changing the model. He is shrinking what the harness ships on every request.

Dictionary, two sentences:

> The parameters. Stateless — does next-token prediction and nothing else. Cannot do anything agentic on its own.
> — [Model](https://www.aihero.dev/ai-coding-dictionary/model)

> Everything around the model that turns it into an agent: tools, system prompt, context-window management, permissions, hooks.
> — [Harness](https://www.aihero.dev/ai-coding-dictionary/harness)

## The model does one thing

Tokens in, tokens out, once per request. It cannot read a file, run `git`, open YouTube, or remember yesterday. Those are not “the model being an agent.” They are **someone else** looping predictions.

:::card
### Same weights, different day
Swapping grok-4.6 for Opus is a **model** change. Editing `AGENTS.md`, adding a tool, or disabling a skill is **not**.
:::

“The model is bad at this” is a specific claim. Same model, different harness or different context, often behaves like a different product.

## The harness runs the loop

The harness assembles context, executes tool calls, feeds results back, stores the session, asks permission, and decides when to compact. **Model proposes, harness executes, repeat.**

Matt’s example: [Claude.ai](https://www.aihero.dev/ai-coding-dictionary/harness) and Claude Code can run the **same model**. One answers in a tab. The other edits your repo. Different tools, system prompt, permissions — different harness.

This Desktop thread: **grok-4.6** is the model. **Hermes** (tools, skills, SOUL, `AGENTS.md`) is the harness. **Jorge** is the agent — the thing you talk to. Agent is not a third machine; it is model-plus-harness addressed as one actor. See [Agent](https://www.aihero.dev/ai-coding-dictionary/agent).

## Blame the wrapper first

:::redflag
### The cargo-cult
Buying a smarter model because the agent “can’t see the repo.” If the harness has no filesystem tools, Opus still cannot `cat` a file. The model was never the variable.
:::

When behaviour differs between products, or between yesterday and today, check harness and context before parameters: system prompt, tool set, permission default, compaction.

The short’s punchline is the same diagnosis from the other side: extra tools in the payload are extra tokens **every turn**, and they distract the model. That is harness cost, not model quality.

:::win
**Today’s win.** Point at a setup and say: model, harness, or agent — and *why*. Do not call Jorge “the model.”
:::

This lab later: a factory trigger starts a **session of an agent**. The worker (Grok Build vs something else) is a model-inside-a-harness choice. Not this week.

## Quiz

:::quiz
Q: Claude.ai and Claude Code can share a model. Why do they behave differently?
- [x] Harness: tools, prompt, and permissions
- [ ] Model: a coding-only weights file
- [ ] Factory: Code started, chat did not
ok: Yes. Same parameters; different tools, system prompt, permissions. The model is not the variable.
no: A “coding model” is the cargo-cult. Factory is who starts the session — both of these still wait on a human.
:::

## Activity

Reply **ready** when the short + both dictionary entries + cards are done.

I will grill four setups (this thread’s grok-4.6 vs Hermes tools; the same Grok in a no-tools chatbot; this repo’s `AGENTS.md`; “Jorge got worse at git” with no model change). Wrong answers get pushed, not padded.

If the terms are yours after that, **you** write `model` and `harness` into [GLOSSARY.md](../GLOSSARY.md) in your own words. I do not paste Matt.

Sheet: [model vs harness](../reference/model-vs-harness.html). Ask if a card is thin or a case sits on a line.
