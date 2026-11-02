# Software factory resources

Curated high-trust sources for this teaching workspace. Explainers draw from here, not from parametric memory of the paid cohort.

## Knowledge

- [Dictionary: Software Factory (AI Hero)](https://www.aihero.dev/ai-coding-dictionary/software-factory)
  Matt's definition: sessions started by **triggers**, not by opening a terminal. Use for: what counts as a factory (a nightly lint-fix PR already counts).
- [Sandcastle (MIT) — GitHub](https://github.com/mattpocock/sandcastle)
  Reference factory: label `agent:implement` → agent in GHA → draft PR → `agent:review`. Copy **patterns**, not v1 APIs (the library is being rewritten). Use for: the last arc, not week 0.
- [Sandcastle agent providers](https://www.aihero.dev/sandcastle/agent-providers)
  Built-ins: Claude Code, Codex, Pi, Copilot, Cursor, OpenCode. **No `grok()`.** Use for: why Grok in CI is a custom worker, not a drop-in.
- [Sandcastle getting started](https://www.aihero.dev/sandcastle/getting-started)
  `sandcastle.run()`, sandboxes, branch strategies. Use for: isolation vs "YOLO on the runner."
- [Boss letter — seven workshops](https://www.aihero.dev/boss/software-factories-for-real-engineers-xdy1m)
  Public outline of the cohort spine. Use as a **map**: Domain Language → Wayfinder → Review → Codebase Design → Feedback Loops → Factory (GHA) → Factory (your infra).
- [Course page](https://www.aihero.dev/cohorts/software-factories-for-real-engineers-xdy1m)
  Pricing, hours, "taught on Claude Code." Use for: what we are **not** buying yet.
- [Topic trap: "Build a Software Factory"](https://www.aihero.dev/topics/build-a-software-factory)
  Still **Ralph loops**. Use for: what not to start with. Brakes first.
- [Grok Build CLI — headless / CI](https://docs.x.ai/build/cli/headless-scripting)
  `grok -p`, `--always-approve`, `--no-auto-update`, `XAI_API_KEY`. Use for: a possible last-arc worker, not the course tape.
- Local: Hermes skills under `/opt/data/skills/matt-pocock/` (`teach`, `grilling` / `grill-with-docs`, `wayfinder`, `loop-me`, `codebase-design`, `implement`, `tdd`)
  Same MIT skills the cohort vendors. Use for: HITL weeks on this machine.
- Local: `/opt/data/src/learn-craft/` (paused)
  Ousterhout deep modules — Week 1 of the cohort map, already started in Python. Do not mix missions.

## Wisdom (Communities)

- Luiz opted out of paying for the cohort Discord / office hours until cash lands. Do not keep proposing "just join the Discord."
- [Matt Pocock on X (@mattpocockuk)](https://x.com/mattpocockuk)
  High-signal for factory thesis (agents = entropy; brakes then triggers). Use for: public clarifications, not as a syllabus.

## Gaps

- 59 lesson videos, mutation-testing teaching, and the factory-design skill live behind the paid seat. We reconstruct the *system*, not the tape.
- `ai-hero-dev/cohort-005-project` is public GitHub and **ARR / students only**. README is citable as a map. Do not clone it as the lab.
- Crash-course ($299) is bundled with the cohort; public pages are thin. Arc 0 in this workspace reconstructs the **ideas** (smart zone, harness, skills, grilling, specs) from public writing + the skills already on disk — not from paid videos.
