# Software factory resources

Curated high-trust sources. Explainers draw from here, not from parametric memory of the paid cohort.

**How to use this file:** every lesson picks one **Watch** or **Read** as primary, plus one **Do**. Cards are not a source. If you need a URL that is not here, add it in the same session.

## Watch (Matt, public)

Prefer these over a Jorge recap when a video exists.

- [Your codebase is NOT ready for AI](https://www.youtube.com/watch?v=uC44zFz7JSM) — Matt, YouTube
  Deep modules as the seam for agents; grey-box vs spaghetti. Use for: **arc 4**. Activity: name a shallow vs deep cut in `playground/`, or refuse a bad split.
- [How To De-Slop A Codebase Ruined By AI (with one skill)](https://www.youtube.com/watch?v=3MP8D-mdheA) — Matt, YouTube
  Entropy + `improve-codebase-architecture`. Use for: **arc 4** after the first playground spike. Activity: run that skill on `playground/` and keep or refuse one deepening.
- [Software Fundamentals Matter More Than Ever](https://www.youtube.com/watch?v=v4F1gFy-hqg) — Matt talk
  Ubiquitous language, vertical slices, TDD, deep modules. Use for: **arc 1–5** overview, not as the only source for one idea.
- [I Open-Sourced My Own AFK Software Factory](https://www.youtube.com/watch?v=E5-QK3CDVQM) — Matt, YouTube (~11 min)
  Factory in motion: triggers start sessions, review the PR later. Use for: **arc 0** (what a factory is) and **arc 6** (how he wired one). Activity: classify this Desktop thread vs a labelled-issue trigger. Pair with the [software factory](https://www.aihero.dev/ai-coding-dictionary/software-factory) entry — video first, dictionary for the cut.
- [Claude Code's system tools are SO BLOATED](https://www.youtube.com/watch?v=oLx4yCbeklQ) — Matt, YouTube (~2 min)
  Tools and system prompt are harness payload, billed every turn. Use for: **arc 0** (model vs harness). Pair with [model](https://www.aihero.dev/ai-coding-dictionary/model) + [harness](https://www.aihero.dev/ai-coding-dictionary/harness). Activity: classify this thread (Grok vs Hermes vs Jorge). Not a “trim Claude” lab.
- [Full Walkthrough: Workflow for AI Coding](https://www.youtube.com/watch?v=-QFHIoCo-Ko) — Matt
  Grill → spec → tickets → AFK. Use for: **arc 0 / 6** so he sees the whole loop before we build a factory. Activity: map the walkthrough onto *our* playground (what would a ticket look like), not onto Visian.

Paid cohort videos (~59) are **not** in this workspace. If a lesson would have been a tape, pick the nearest row above or an article below and mark `substitute`.

## Read (Matt, public)

- [AI Coding Dictionary](https://www.aihero.dev/ai-coding-dictionary) — 71 terms
  Crash-course vocabulary live here. Use for: **arc 0**. Start with [model](https://www.aihero.dev/ai-coding-dictionary/model), then harness / session / AX vs DX. Activity: Luiz uses the term correctly in a grill; only then it enters `GLOSSARY.md`.
- [Model](https://www.aihero.dev/ai-coding-dictionary/model) · [Harness](https://www.aihero.dev/ai-coding-dictionary/harness) · [Agent](https://www.aihero.dev/ai-coding-dictionary/agent)
  Parameters vs wrapper vs the thing you talk to. Use for: **arc 0** after the factory cut. Pair with the [system-tool bloat short](https://www.youtube.com/watch?v=oLx4yCbeklQ).
- [How To Kill The Bloat In Claude Code's System Prompt](https://www.aihero.dev/how-to-kill-the-bloat-in-claude-codes-system-prompt) — Matt
  Same cut as the short, with the settings. Use later if we ever tune a Claude harness. Not the 0002 activity.
- [Software factory (dictionary)](https://www.aihero.dev/ai-coding-dictionary/software-factory)
  Triggers start sessions. Use for: **arc 6** definition, **arc 0** so he doesn't call this chat a factory. Pair with [dark factory](https://www.aihero.dev/ai-coding-dictionary/dark-factory).
- [My 7 Phases of AI Development](https://www.aihero.dev/my-7-phases-of-ai-development)
  Idea → research → prototype → PRD → kanban → execute → QA. Use for: **arc 0** map (crash-course spine). Activity: label which phase a playground change is in — he will be wrong at first; that's the point.
- [5 agent skills I use every day](https://www.aihero.dev/5-agent-skills-i-use-every-day)
  grill-me → to-spec → to-tickets → tdd → improve-codebase-architecture. Use for: **arc 0–3**. Activity: run the named skill on *this* repo, don't describe it.
- [How To Make Codebases AI Agents Love](https://www.aihero.dev/how-to-make-codebases-ai-agents-love)
  Deep modules, grey box, tests as the contract. Use for: **arc 4**. Pair with the YouTube above.
- [Essential AI Coding Feedback Loops For TypeScript Projects](https://www.aihero.dev/essential-ai-coding-feedback-loops-for-type-script-projects)
  `typecheck`, Vitest, husky, frontend loop. Use for: **arc 5**. Activity: add the script to `playground/` and make a bad edit fail.
- [TDD skill guide](https://www.aihero.dev/skill-test-driven-development-claude-code)
  One test → one impl; no bulk tests. Use for: **arc 5** (and any playground feature). Activity: a red-green cycle on catalog/progress, not a test file written after the fact.
- [The /wayfinder Skill](https://www.aihero.dev/skills-wayfinder)
  Tickets answer decisions. Use for: **arc 2**.
- [Boss letter — seven workshops](https://www.aihero.dev/boss/software-factories-for-real-engineers-xdy1m)
  Public map of the cohort spine. Use as a **map**, not as a lesson.
- [Course page](https://www.aihero.dev/cohorts/software-factories-for-real-engineers-xdy1m)
  What we are not buying yet.
- [Topic trap: "Build a Software Factory"](https://www.aihero.dev/topics/build-a-software-factory)
  Still Ralph loops. Use for: what **not** to start with.
- [Sandcastle getting started](https://www.aihero.dev/sandcastle/getting-started) · [agent providers](https://www.aihero.dev/sandcastle/agent-providers) · [GitHub (MIT)](https://github.com/mattpocock/sandcastle)
  Isolation, labels `agent:implement` / `agent:review`. Use for: **arc 6**. Copy patterns, not v1 APIs. **No `grok()`.**
- [Grok Build CLI — headless](https://docs.x.ai/build/cli/headless-scripting)
  Possible last-arc worker. Not Matt; keep it in the factory-worker decision, not in arc 0.
- Local: `/opt/data/skills/matt-pocock/` (`teach`, `grilling` / `grill-with-docs`, `wayfinder`, `loop-me`, `codebase-design`, `implement`, `tdd`)
  Same MIT skills the cohort vendors. The README of the skill *is* a primary source.
- Local: `/opt/data/src/learn-craft/` (paused)
  Ousterhout. Do not mix missions; point at it from arc 4 if a playground module is shallow.

## Do (default activities — pick one per lesson)

These are the *kinds* of activity. Name a concrete one in the lesson frontmatter.

| Arc | Default activity |
|---|---|
| 0 crash-course | Grill until one dictionary term is *his*; write it into `GLOSSARY.md`. Or sketch the 7 phases against one playground ticket. |
| 1 domain language | `/grill-with-docs` on the Udemy-like app until an ADR or three glossary terms land. |
| 2 wayfinder | Produce a vertical-slice ticket for the next playground feature an implementer could start without asking. |
| 3 review | Luiz reviews a playground diff using the three layers; `/retro` if we shipped something. No auto-merge. |
| 4 codebase design | Deepen or refuse a module in `playground/`. Optional: watch the deep-modules video first. |
| 5 feedback loops | Add `typecheck` + Vitest (then lint). A bad edit must fail. Later: Playwright against the real page + user switcher. |
| 6 factory | One trigger → draft PR on *this* repo. Implementer ≠ reviewer. Worker still unlocked. |

Invalid activities: quiz-only, "summarize the article", watching-only, Visian/SpaceXAI as the lab.

## Wisdom (Communities)

- Luiz opted out of paying for the cohort Discord / office hours until cash lands. Do not keep proposing "just join the Discord."
- [Matt Pocock on X (@mattpocockuk)](https://x.com/mattpocockuk)
  Public clarifications (factory thesis, entropy). Not a syllabus.
- Crash course sales page: [aihero.dev/s/crash-course](https://www.aihero.dev/s/crash-course) — use to know what the paid mini-course covers; do not scrape it as if we owned the videos.

## Gaps

- 59 lesson videos, mutation-testing teaching, and the factory-design skill live behind the paid seat. We reconstruct the *system* from public Matt (dictionary, posts, YouTube, MIT skills, Sandcastle), then **do the work on our playground**.
- `ai-hero-dev/cohort-005-project` is public GitHub and **ARR / students only**. README is a map. Do not clone it as the lab.
- If a needed Matt video is missing from **Watch**, that is a gap to fill with a search, not a reason to lecture.
