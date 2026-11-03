---
id: "0003"
kicker: Lesson 0003 · Arc 0
title: Session, context, turn
lede: The model is stateless. What looks like memory is the session filling a finite box, one turn at a time.
time: 9 min watch + 8 min read + cards + grill
watch: https://www.youtube.com/watch?v=-uW5-TaVXu4
read: https://www.aihero.dev/ai-coding-dictionary/session
activity: Live grill — classify four setups as session, turn, context window, or model-provider request. If they land, you write session, turn, and context window into GLOSSARY.md in your own words (no paste).
source: Matt Pocock — YouTube + AI Coding Dictionary
next: "0004 — Smart zone"
---

# Session, context, turn

## Watch first

Watch [Most devs don’t understand how context windows work](https://www.youtube.com/watch?v=-uW5-TaVXu4) (~9 min). Then read [Session](https://www.aihero.dev/ai-coding-dictionary/session), [Turn](https://www.aihero.dev/ai-coding-dictionary/turn), and [Context window](https://www.aihero.dev/ai-coding-dictionary/context-window). Cards compress those. They do not replace them.

The video is the box. The dictionary is the names for what fills it.

> If the context window is the box, the session is the stuff slowly filling it up.
> — [Session](https://www.aihero.dev/ai-coding-dictionary/session)

> One user message plus everything the agent does in response, up until it yields back to the user.
> — [Turn](https://www.aihero.dev/ai-coding-dictionary/turn)

## The box is finite

Every [model provider request](https://www.aihero.dev/ai-coding-dictionary/model-provider-request) re-sends a single sequence of tokens: system prompt, the conversation so far, every tool result. That sequence **is** the [context window](https://www.aihero.dev/ai-coding-dictionary/context-window). If it is not in that sequence, grok-4.6 does not know it exists.

:::card
### Not memory
The window is working state for this request. It does not persist across sessions. [Memory](https://www.aihero.dev/ai-coding-dictionary/memory-system) is a separate layer that writes to disk and reloads later.
:::

Matt’s punchline in the video: bigger advertised windows still [lose the middle](https://www.aihero.dev/what-is-the-context-window). Quality drops before the harness errors. Plan the task for a usable window, not the marketing number.

## Session > turn > request

A [session](https://www.aihero.dev/ai-coding-dictionary/session) is one bounded run with an agent. It starts empty, accumulates messages and tool results, and ends when you close it, [clear](https://www.aihero.dev/ai-coding-dictionary/clearing) it, or [compact](https://www.aihero.dev/ai-coding-dictionary/compaction) it into a fresh session.

A [turn](https://www.aihero.dev/ai-coding-dictionary/turn) is one of your messages plus everything Jorge does until he yields. One turn can contain many provider requests — each tool call is another round-trip that re-sends the whole prefix.

This Desktop `/teach` thread is **one session**. “Ready” later is **one turn**. Each `read_file` I run inside that turn is **one request**.

:::redflag
### The cargo-cult
Treating yesterday’s chat as if Jorge still has it. The model is [stateless](https://www.aihero.dev/ai-coding-dictionary/stateless). What survives a new session is the [filesystem](https://www.aihero.dev/ai-coding-dictionary/filesystem) — `GLOSSARY.md`, the lesson files, `AGENTS.md` — not the transcript in his head.
:::

Unrelated work in the same session is residue. It colours the next answer. One task per session is the default; a factory later is a machine that **starts** those sessions, not a longer one.

## Why this lab cares

Work too large for one window must be split across sessions. That is why tickets exist. That is why this teaching thread is HITL and the factory, when we build it, fires **new** sessions instead of stuffing more into this one.

:::win
**Today’s win.** Point at a setup and say: session, turn, context window, or provider request — and *why*. Do not call the window “memory.”
:::

Smart zone / dumb zone (same model, more context, worse work) is next. Not today.

## Quiz

:::quiz
Q: You send one message. Jorge makes six tool calls, then answers. What happened?
- [x] One turn, several provider requests
- [ ] Several turns, one provider request
- [ ] One session, therefore one request
ok: Yes. A turn is until he yields. Each tool call is another round-trip that re-sends the context.
no: Turns are your messages, not his tool calls. A session holds many turns, and each turn can hold many requests.
:::

## Activity

Reply **ready** when the video + three dictionary entries + cards are done.

I will grill four setups (this Desktop thread until `/new`; you saying ready and me grilling until I stop; grok-4.6 seeing the prompt + history on one API call; one tool round-trip inside that grill). Wrong answers get pushed, not padded.

If the terms are yours after that, **you** write `session`, `turn`, and `context window` into [GLOSSARY.md](../GLOSSARY.md) in your own words. I do not paste Matt.

Sheet: [session vs turn vs window](../reference/session-context-turn.html). Ask if a card is thin or a case sits on a line.
