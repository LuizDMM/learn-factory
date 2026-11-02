# Teaching notes

## How Luiz wants to be taught

- Brutal honesty. No pep. Weak plans get named early.
- English: flag useful mistakes, don't turn every lesson into grammar class.
- Cadence: evenings / spare blocks. **One lesson + one playground change.** Stop. Do not double-up if a day slips.
- `learn-craft` (Ousterhout, lunch) is **paused** until he unpauses it. Do not steal that slot and do not start learn-craft 0003.
- Skin: cards, same idea as learn-craft. Author `lessons/NNNN-slug.md`, render to HTML when the renderer is copied here. Do not hand-edit HTML as the source of truth.
- Quizzes: clarity over tricks.
- Examples: this playground (courses / lessons / progress / user switcher). Never paste Visian or SpaceXAI source.

## Daily session

Luiz says: “lesson” / “next” / `/teach`. That is one session.

1. Read `learning-records/` (what he showed, not what we covered).
2. Open today's cards in the Hermes preview (file path, never a Jorge localhost server).
3. He walks the cards. Playground change is in `playground/`.
4. Write a `learning-records/NNNN-….md` only if he **demonstrated** the idea.
5. Stop.

## Progress

| Signal | Where | Means |
|---|---|---|
| Exposed | `lessons/` exist | We wrote it. Not mastery. |
| Practiced | a playground change or a grill answer he owns | He used it. |
| Learned | `learning-records/` | Evidence. Floor for the next lesson. |

No streak, no XP. If 0001 has no learning record, we do not start 0002.

## Curriculum map (not a schedule)

Arc 0 — crash-course ideas: smart zone, harness vs model, skills, grilling, specs as the handoff.
Arc 1 — domain language / ADRs (`/grill-with-docs`) until `GLOSSARY.md` is real.
Arc 2 — wayfinder: slice the playground so an implementer can start without asking.
Arc 3 — review layers + retro. Luiz reads the area. No auto-merge.
Arc 4 — codebase design (deep modules). Point at paused `learn-craft`; do not restart Ousterhout here unless a playground module is shallow.
Arc 5 — feedback loops: typecheck, tests, lint on every commit; mutation testing later; Playwright against the real page + user switcher.
Arc 6 — factory: trigger → implementer → draft PR → **separate** review. Worker (Grok in GHA vs Hermes cron) decided here.

Brakes before triggers. Factory is last.

## Agent rules

- Do **not** clone `https://github.com/ai-hero-dev/cohort-005-project`. Public ≠ licensed.
- Do **not** copy that app's source, lesson commits, or `npx ai-hero-cli reset` flow.
- Sandcastle is the factory reference. The playground is our original course-platform-shaped app.
- Never commit `.env`, `XAI_API_KEY`, or Claude/Grok tokens.
- Never auto-merge.
- This Desktop thread is HITL teaching. The factory, when it exists, is a trigger + a new session or a GHA job.
