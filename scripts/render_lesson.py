#!/usr/bin/env python3
"""Render a lesson markdown file to the cards HTML skin.

Usage:
  python3 scripts/render_lesson.py lessons/0001-this-thread-is-not-a-factory.md
  python3 scripts/render_lesson.py --all
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LESSONS = ROOT / "lessons"

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{id} — {title}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,600;1,6..72,400&display=swap" rel="stylesheet" />
  <style>
__CSS__
  </style>
</head>
<body>
  <article class="page">
    <header>
      <p class="kicker">{kicker}</p>
      <h1>{title}</h1>
      <p class="lede">{lede}</p>
      <p class="meta">{time} · {source}</p>
      {watch_line}
      {activity_line}
    </header>
    <div class="deck">
{beats}
    </div>
    <nav class="card-nav" aria-label="Lesson cards">
      <button type="button" id="prev-card">← Back</button>
      <span class="dots" id="dots"></span>
      <button type="button" id="next-card">Next →</button>
    </nav>
    <p class="progress-label" id="card-label"></p>
    <p class="meta" style="margin-top:1.2rem">{next_line} · Source: <span class="mono">{src_name}</span> · Ask me if anything is unclear.</p>
  </article>
  <script>
__JS__
  </script>
</body>
</html>
"""


def parse_frontmatter(raw: str) -> tuple[dict[str, str], str]:
    if not raw.startswith("---"):
        return {}, raw
    end = raw.find("\n---", 3)
    if end < 0:
        return {}, raw
    fm: dict[str, str] = {}
    for line in raw[4:end].splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        val = val.strip()
        if (val.startswith('"') and val.endswith('"')) or (
            val.startswith("'") and val.endswith("'")
        ):
            val = val[1:-1]
        fm[key.strip()] = val
    return fm, raw[end + 4 :].lstrip()


def inline(text: str) -> str:
    chunks: list[str] = []
    last = 0
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", text):
        chunks.append(_inline_plain(text[last : m.start()]))
        label = html.escape(m.group(1))
        href = html.escape(m.group(2), quote=True)
        chunks.append(f'<a href="{href}">{label}</a>')
        last = m.end()
    chunks.append(_inline_plain(text[last:]))
    return "".join(chunks)


def _inline_plain(text: str) -> str:
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
    return text


def slug(text: str) -> str:
    s = re.sub(r"<[^>]+>", "", text).lower()
    s = re.sub(r"[^\w]+", "-", s).strip("-")
    return s or "section"


def render_quiz(body: str) -> str:
    q = ""
    choices: list[tuple[str, str]] = []
    answer = ""
    ok = ""
    no = ""
    for line in body.splitlines():
        line = line.strip()
        if line.startswith("Q:"):
            q = line[2:].strip()
        elif m := re.match(r"- \[([ xX])\]\s+(.*)$", line):
            letter = chr(ord("a") + len(choices))
            if m.group(1) != " ":
                answer = letter
            choices.append((letter, m.group(2)))
        elif line.startswith("ok:"):
            ok = line[3:].strip()
        elif line.startswith("no:"):
            no = line[3:].strip()
    buttons = "".join(
        f'<button type="button" data-choice="{let}">{inline(txt)}</button>'
        for let, txt in choices
    )
    return (
        f'<div class="quiz" data-quiz data-answer="{html.escape(answer)}" '
        f'data-ok="{html.escape(ok)}" data-no="{html.escape(no)}">'
        f'<p class="q">{inline(q)}</p>{buttons}<p class="fb"></p></div>'
    )


def render_flow(text: str) -> str:
    lines = text.replace("\r", "").split("\n")
    out: list[str] = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("# "):
            i += 1
            continue
        if line.startswith("## "):
            title = inline(line[3:])
            out.append(f'<h2 id="{slug(line[3:])}">{title}</h2>')
            i += 1
            continue
        if line.startswith("### "):
            out.append(f"<h3>{inline(line[4:])}</h3>")
            i += 1
            continue
        if line.startswith("> ") or line == ">":
            quoted: list[str] = []
            cite = ""
            while i < n and (lines[i].startswith(">") or lines[i].startswith("> ")):
                body = re.sub(r"^>\s?", "", lines[i])
                if body.startswith("— ") or body.startswith("- "):
                    cite = re.sub(r"^[—-]\s*", "", body)
                elif body:
                    quoted.append(body)
                i += 1
            cite_html = f"<cite>{inline(cite)}</cite>" if cite else ""
            out.append(
                f"<blockquote><p>{inline(' '.join(quoted))}</p>{cite_html}</blockquote>"
            )
            continue
        if line.startswith("- "):
            items: list[str] = []
            while i < n and lines[i].startswith("- "):
                items.append(f"<li>{inline(lines[i][2:])}</li>")
                i += 1
            out.append(f"<ul>{''.join(items)}</ul>")
            continue
        para: list[str] = []
        while (
            i < n
            and lines[i].strip()
            and not lines[i].startswith("#")
            and not lines[i].startswith(">")
            and not lines[i].startswith("- ")
        ):
            para.append(lines[i])
            i += 1
        out.append(f"<p>{inline(' '.join(para))}</p>")
    return "".join(out)


BLOCK_RE = re.compile(r":::(\w+)\n(.*?)\n:::", re.S)


def render_body(md: str) -> str:
    parts: list[str] = []
    last = 0
    for m in BLOCK_RE.finditer(md):
        if m.start() > last:
            parts.append(render_flow(md[last : m.start()]))
        kind, body = m.group(1), m.group(2).strip()
        if kind == "quiz":
            parts.append(render_quiz(body))
        elif kind == "formula":
            parts.append(
                f'<div class="formula">{inline(body).replace(chr(10), "<br>")}</div>'
            )
        else:
            cls = "callout" if kind == "card" else f"callout {kind}"
            parts.append(f'<div class="{cls}">{render_flow(body)}</div>')
        last = m.end()
    if last < len(md):
        parts.append(render_flow(md[last:]))
    return "".join(parts)


def split_beats(inner: str) -> list[tuple[str, str, str]]:
    matches = list(re.finditer(r'<h2 id="([^"]+)">', inner))
    if not matches:
        return [("open", "Open", inner)]
    beats: list[tuple[str, str, str]] = []
    if matches[0].start() > 0:
        lead = inner[: matches[0].start()].strip()
        if lead:
            beats.append(("open", "Open", lead))
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(inner)
        chunk = inner[m.start() : end]
        title_m = re.search(r"<h2[^>]*>(.*?)</h2>", chunk, re.S)
        title = re.sub(r"<[^>]+>", "", title_m.group(1)) if title_m else m.group(1)
        beats.append((m.group(1), title, chunk))
    return beats


def render_file(src: Path) -> Path:
    raw = src.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(raw)
    inner = render_body(body)
    beats = split_beats(inner)
    beats_html = "\n".join(
        f'      <section class="beat{" active" if i == 0 else ""}" id="{html.escape(bid)}">{chunk}</section>'
        for i, (bid, _title, chunk) in enumerate(beats)
    )
    nxt = fm.get("next", "")
    next_line = f"Next: {html.escape(nxt)}" if nxt else ""
    watch = fm.get("watch", "")
    read = fm.get("read", "")
    watch_bits = []
    if watch:
        watch_bits.append(
            f'Watch: <a href="{html.escape(watch, quote=True)}">{html.escape(watch)}</a>'
        )
    if read:
        watch_bits.append(
            f'Read: <a href="{html.escape(read, quote=True)}">{html.escape(read)}</a>'
        )
    watch_line = f'<p class="meta">{" · ".join(watch_bits)}</p>' if watch_bits else ""
    activity = fm.get("activity", "")
    activity_line = (
        f'<p class="meta">Activity: {html.escape(activity)}</p>' if activity else ""
    )
    out = TEMPLATE.format(
        id=html.escape(fm.get("id", src.stem.split("-")[0])),
        title=html.escape(fm.get("title", src.stem)),
        kicker=html.escape(fm.get("kicker", "Lesson")),
        lede=html.escape(fm.get("lede", "")),
        time=html.escape(fm.get("time", "")),
        source=html.escape(fm.get("source", "")),
        watch_line=watch_line,
        activity_line=activity_line,
        beats=beats_html,
        next_line=next_line,
        src_name=html.escape(src.name),
    )
    css = (ROOT / "assets" / "lesson.css").read_text(encoding="utf-8")
    js = (ROOT / "assets" / "lesson.js").read_text(encoding="utf-8")
    out = out.replace("__CSS__", css).replace("__JS__", js)
    dest = src.with_suffix(".html")
    dest.write_text(out, encoding="utf-8")
    return dest


def lesson_mds() -> list[Path]:
    return sorted(
        p for p in LESSONS.glob("*.md") if re.match(r"^\d{4}-", p.name)
    )


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("paths", nargs="*", type=Path)
    p.add_argument("--all", action="store_true")
    args = p.parse_args()
    files = lesson_mds() if args.all else [Path(x) for x in args.paths]
    if not files:
        raise SystemExit("No lesson markdown to render.")
    for f in files:
        src = f if f.is_absolute() else ROOT / f
        dest = render_file(src)
        print(f"{src.relative_to(ROOT)} -> {dest.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
