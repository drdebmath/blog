# AGENTS.md

Instructions for AI agents working on **The Oblivious Robot**, Dr. Debasish Pattanayak's blog
(https://drdebmath.github.io/blog/). Read `README.md` for the full mechanics; this file covers how to work here.

Like the robot in the title, you start every session with no memory. Everything you need is written down
here, in `README.md`, and in the existing posts. Read at least one post in `posts/` before writing a new one.

## What the blog is

Research, distributed algorithms (swarms of oblivious robots, mobile agents on graphs), writing papers with
AI, the coming AI singularity, and adapting to the new age. Readers include the author's students, so posts
are meant to be found again and referred back to.

## Repo at a glance

- Zero-build site: `index.html` renders `posts/<slug>.md` in the browser (marked + KaTeX, pinned versions).
- `posts.json`: one entry per post (`slug`, `title`, `date`, `updated`, `description`; optional `theme`,
  `page`, `declaration`).
- `config.json`: site title, nav, footer, default theme, default AI-use declaration.
- `base.css`: layout shared by all themes, using only theme variables. `themes/<name>.css`: colors, fonts,
  glyphs (`homepage`, `watercolor`, `pokemon`, `masala`). Every theme needs a dark mode.
- `agents/<topic>/AGENTS.md`: downloadable agent instructions that posts link to (e.g. `agents/writing-papers/`
  for the paper-writing post). Keep them in sync with their post, and bump the post's `updated` when they change.
- `build.py`: generates `p/<slug>.html`, `p/<slug>.png`, `feed.xml` and `llms.txt`. **Never edit these by
  hand**; run `python3 build.py` after adding, editing or retitling a post.
- Preview: `python3 -m http.server` → http://localhost:8000. Publishing is a push to `main` (GitHub Pages),
  so don't push unless asked.
- Pushing needs the **drdebmath** GitHub account; the other account on this machine (debasishiiti) gets a
  403. This repo's git config gets credentials from `gh auth git-credential` instead of the Keychain, so
  `gh` must have drdebmath active. If a push is denied, run `gh auth switch --user drdebmath` and retry.

## Turning the author's input into a post

The usual job: the author gives rough notes, a checklist or a few paragraphs, and you write the post.

1. **Keep the author's input.** Put it, lightly edited for coherence, at the end of the post in
   `<details class="original"><summary>Original input</summary> … </details>`, starting with
   `<p class="note">Lightly edited for coherence: …</p>` that says what was changed. Remove editing
   instructions meant for you, apply the author's later corrections, fix capitalization and punctuation.
   Don't change the meaning.
2. **Mark every piece of text by who wrote it**, honestly:
   - `by-human`: the author's own words, close to verbatim.
   - `by-collab`: the author's ideas, written up as prose by you.
   - `by-ai`: your own additions: framing, examples, transitions, prompts, conclusions.

   When unsure between two, pick the one that gives you more credit, never less. Never mark your own
   sentence as `by-human`.
3. **Use blocks correctly.** Wrap Markdown in `<div class="by-…">` with blank lines around the content.
   Inside a paragraph use `<span class="by-…">`. Never nest one kind inside another: use a plain
   `<div class="mixed">` holding sibling spans.
4. **Add the `posts.json` entry** with a one-line `description`, `date` and `updated` (today's date for a
   new post; bump `updated` on every edit). Give the post its own `declaration` that says what the input
   was, which model wrote what (e.g. "Claude (Anthropic, Opus 5.5)"), and whether the title and headings are
   AI-generated. Headings and titles count as AI-generated unless the author wrote them.
5. **Pick or make a theme** if the post wants one (`"theme": "<name>"`), following the existing theme
   files: variables only, a dark mode, glyphs kept in the gutters.
6. Run `python3 build.py` and check the post in the local preview, in light and dark mode, at phone width.

Building blocks available in posts (see `README.md`): `p.footnote` for marks in the title,
`aside.checklist` for a working checklist, `details.example` for a collapsible worked example, and fenced
code blocks, which get a Copy button and work as copyable prompts.

## How to write

The blog follows its own advice from
[Writing Papers When Your Co-author Has No Memory](posts/co-author-with-no-memory.md). Apply it to posts:

- **Plain and direct.** Short sentences, concrete nouns, no hype. The tone is dry and lightly funny
  ("jokes that are at least 60% math"), never breathless.
- **No "this" or "that" as a reference.** Name the object.
- **One term per concept.** Once something is an *agent*, it is never a *robot* two paragraphs later.
- **Define before use**, and put motivation before results.
- **Connectives** (*However*, *Thus*, *So*) to show how sentences relate.
- **No em dashes.** Use colons, commas, parentheses or a new sentence. The existing posts have none.
- **Math** in KaTeX: `$u$`, `$G = (V, E)$`. Write node $u$, not "u".
- **Don't pad.** If the author's point fits in three paragraphs, write three. Additions of your own should
  earn their place and are marked `by-ai`.
- **Verify links and references.** Never invent a paper, a URL or a quote. If you can't check it, leave it
  out or ask.
- First person ("I") is the author's voice. Don't put opinions in the author's mouth that the input doesn't
  contain; if you add one, it is `by-ai`.

## Editing code and styles

- Keep the site zero-build: no bundlers, no frameworks, no new runtime dependencies. Libraries load from a
  CDN at pinned versions; stylesheets only from Google Fonts.
- `base.css` uses theme variables only; colors and fonts belong in `themes/*.css`.
- Provenance cues must not rely on color alone (currently: highlighter tint plus a distinct typeface for
  collab and AI text). If you change how they look, update the legend text in `index.html` and the
  description in `README.md` to match.
- Match the surrounding code: short comments explaining *why*, compact CSS, no extra abstraction.

## Licensing

Everything is CC BY 4.0 (`LICENSE`, `posts/license.md`). Only add material the author has the right to
publish under that license, and credit quoted sources.
