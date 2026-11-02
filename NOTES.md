# Teaching notes

## How Luiz wants to be taught

- Brutal honesty. No pep. Weak plans get named early.
- English: flag useful mistakes, don't turn every lesson into grammar class.
- Cadence: evenings / spare blocks. **One lesson + one playground change.** Stop. Do not double-up if a day slips.
- `learn-craft` (Ousterhout, lunch) is **paused** until he unpauses it. Do not steal that slot and do not start learn-craft 0003.
- **Skin:** cards, same idea as learn-craft. Author `lessons/NNNN-slug.md`, then `python3 scripts/render_lesson.py --all`. Do not hand-edit HTML as the source of truth.
- **Hermes file preview does not run `<script>`.** Open lesson HTML in a real browser on the laptop (`xdg-open`). Do not invent a no-JS card skin to paper over that.
- Quizzes: clarity over tricks. A quiz is **not** the activity.
- Examples: this playground (courses / lessons / progress / user switcher). Never paste Visian or SpaceXAI source.
- **Do not get locked in text.** Cards without Matt's own video/article, or without a thing he *does*, are a failed lesson. Compress, don't replace.

## Lesson contract (non-negotiable)

A lesson is invalid unless the markdown frontmatter (or the HTML header) names all three:

1. **Watch or read (Matt).** One primary URL from `RESOURCES.md` — YouTube, AI Hero article, dictionary entry, or a skill's own README. Prefer a **video** when one exists for the idea. He actually opens it (even 8–12 minutes). Jorge summarizing Matt is not the source.
2. **Cards.** Tight compression + one retrieval quiz. Tied to the mission. Not a blog post.
3. **Activity.** Something that can fail. Default: a change in `playground/` (failing test, page, user switcher, lint/typecheck). Also valid: a live `/grill-with-docs` that writes a glossary/ADR *he* owns, or a red-green `/tdd` cycle on the lab app. Invalid: "imagine…", "in your own words only", quiz-only, watching-only.

When the *real* source is a paid cohort video we don't have: pick the nearest **public** Matt artifact, label it `substitute (paid tape not in this workspace)`, and still require an activity.

Before authoring, search `RESOURCES.md` (Watch / Read / Do). If the arc has no video listed, search YouTube/`aihero.dev/posts` and add the link to RESOURCES **in the same session** — don't teach from memory.

## Daily session

Luiz says: “lesson” / “next” / `/teach`. That is one session.

1. Read `learning-records/` (what he showed, not what we covered).
2. Pick the next idea in his ZPD. Lock the Matt URL + the activity *before* writing cards.
3. He **watches or reads** the primary source (don't skip this to "save time").
4. Open today's cards in the Hermes preview (file path, never a Jorge localhost server).
5. He does the activity in `playground/` (or the named skill). We run the check (test, typecheck, grill output).
6. Write a `learning-records/NNNN-….md` only if he **demonstrated** the idea — watching is not demonstrating.
7. Stop.

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
