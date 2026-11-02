---
id: "0001"
kicker: Lesson 0001 · Arc 0
title: This thread is not a factory
lede: A factory is a system that starts agent sessions. You typing here is the opposite of that.
time: 11 min watch + 8 min cards + grill
watch: https://www.youtube.com/watch?v=E5-QK3CDVQM
read: https://www.aihero.dev/ai-coding-dictionary/software-factory
activity: Live grill — classify four setups. If they land, you write software factory into GLOSSARY.md in your own words (no paste).
source: Matt Pocock — YouTube + AI Coding Dictionary
next: "0002 — Model vs harness"
---

# This thread is not a factory

## Watch first

Watch [I Open-Sourced My Own AFK Software Factory](https://www.youtube.com/watch?v=E5-QK3CDVQM) (~11 min). Then read [Software factory](https://www.aihero.dev/ai-coding-dictionary/software-factory). Cards compress those. They do not replace them.

Do not skip the video to “save time.” Matt showing a factory is the lesson.

Also open the dictionary entry. One sentence is the whole idea:

> A system of work where agent sessions are started by triggers — an issue being created, a schedule, a CI failure, another session finishing — rather than by a human
> — [Software factory](https://www.aihero.dev/ai-coding-dictionary/software-factory)

This Desktop thread is a human starting a session. Teacher, not factory.

## Triggers, not humans

Without a factory, every session starts because someone started it. Even fully [AFK](https://www.aihero.dev/ai-coding-dictionary/afk) work still waited on a person to open the session, point it at a ticket, and set it going.

A factory takes the human out of **starting** sessions. Not necessarily out of anything else.

:::card
### Still a factory
One cron job that runs one kind of session and opens one reviewable PR. Narrow on purpose. Review the PRs; then decide whether to widen.
:::

That is the bar for *our* lab later. Not “Claude in GitHub Actions” as a costume. A trigger, a session, a draft PR you read.

## AFK is not a factory

You can walk away from this chat. That is AFK. It is still not a factory: **you** started the session.

:::redflag
### The cargo-cult
Calling Jorge-in-this-thread “the factory” because code got written while you made coffee. Matt’s cut is who *started* the work, not whether you watched it.
:::

[HITL](https://www.aihero.dev/ai-coding-dictionary/human-in-the-loop) is pairing during the session. Teaching lives here. Grilling only works with you answering. Factory comes last in this workspace, after brakes.

## Grey box, not dark

Humans can sit anywhere: writing the issue, approving a plan, [human review](https://www.aihero.dev/ai-coding-dictionary/human-review) before merge.

A [dark factory](https://www.aihero.dev/ai-coding-dictionary/dark-factory) is a factory whose output nobody reads. Agents merge what passes CI. When it breaks, you debug code no one on the team has seen.

:::win
**Today’s win.** Point at a setup and say: factory, AFK-but-not-factory, HITL teaching, or dark factory — and *why*.
:::

This repo: grey box. Draft PRs. You read the diff. No auto-merge.

## Quiz

:::quiz
Q: What makes a system a software factory?
- [x] A trigger starts the session; a person does not have to
- [ ] You start a session, then leave the agent AFK
- [ ] Agents merge green PRs and nobody reads them
ok: Yes. Factory = who starts the session. AFK is walking away. Dark factory is a factory plus no human review.
no: AFK still needed a human to start it. Auto-merge without review is a dark factory — a factory with the lights off, not the definition of factory.
:::

## Activity

Reply **ready** when the video + dictionary + cards are done.

I will grill four setups (this thread, a labelled issue that opens a draft PR, auto-merge on green, you kicking off an AFK run by hand). Wrong answers get pushed, not padded.

If the term is yours after that, **you** write `software factory` into [GLOSSARY.md](../GLOSSARY.md) in your own words. I do not paste Matt.

Sheet: [factory vs HITL vs dark](../reference/factory-vs-hitl.html). Ask if a card is thin or a case sits on a line.
