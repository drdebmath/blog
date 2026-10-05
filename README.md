# The Oblivious Robot

Dr. Debasish Pattanayak's blog. Zero-build: `index.html` renders `posts/*.md` in the browser
(marked + KaTeX, pinned versions). Hosted on GitHub Pages at https://drdebmath.github.io/blog/.

**Preview locally:** `python3 -m http.server` → http://localhost:8000
**Publish:** push to `main` (GitHub → Settings → Pages → deploy from branch `main`, root).

## Writing a post

1. Add `posts/<slug>.md`. The slug is the URL: `…/blog/#<slug>`.
2. Add an entry to `posts.json`:

   ```json
   { "slug": "my-post", "title": "My Post", "date": "2026-10-01", "updated": "2026-10-01",
     "description": "One line for link previews and feeds." }
   ```

   `date` is when it was first published; bump `updated` whenever you change the post. Both show under the title.

   Optional fields:
   - `"theme": "pokemon"`: this post uses a different theme.
   - `"page": true`: reachable by link/nav, hidden from the post list (like `about`).
   - `"declaration": "…"`: this post's own AI-use declaration (Markdown) behind the "?".
   - The title may contain HTML, e.g. `<sup>*</sup>` for a footnote mark.
3. Run `python3 build.py` to rebuild link previews, `feed.xml` and `llms.txt` (see below).

Raw HTML inside Markdown works for one-off layouts.

## Marking who wrote what

Every page gets the legend and the "?" AI-use declaration automatically (from `config.json`, or the post's
`"declaration"`). In a post, mark text by wrapping it; keep blank lines around Markdown inside a div:

```html
<div class="by-human">   <!-- or by-collab, by-ai -->

Your text here.

</div>
```

Inside a paragraph use `<span class="by-ai">…</span>`. Don't nest one kind inside another: split the text
into sibling spans in a plain `<div>` instead, so each piece gets its own style. Collab and AI text get a
highlighter tint, collab text is set in a slab serif, AI text in a book serif, and the author's own words are plain, so readers who can't tell the
colors apart still can.

Other building blocks:
- `<p class="footnote">* …</p>`: small note under the legend, for a mark in the title.
- `<aside class="checklist"> <p class="checklist-title">…</p> <p class="pass">…</p> <ul><li>…</li></ul> </aside>`:
  a working checklist (ticks saved in the reader's browser, with a Clear button); a fixed sidebar on wide screens.
- `<details class="example"><summary>…</summary> … </details>`: a collapsible worked example.
- Fenced code blocks get a Copy button, so they work as copyable prompts.
- `<details class="original"><summary>Original input</summary> … </details>`: the author's input, at the end.

## Build step for extras: `python3 build.py`

The pages themselves need no build, but a few things can't be made in the browser:
- **Link previews.** Crawlers (X, WhatsApp, Slack) don't run JavaScript, so each post gets `p/<slug>.html`
  (preview tags + redirect to the post) and `p/<slug>.png` (a card in the post's theme, drawn with headless
  Chrome or Edge). Posts show this share link at the bottom, next to "Discuss on X".
- **`feed.xml`**: RSS with each post's full Markdown, for feed readers and AI agents.
- **`llms.txt`**: an index for AI agents ([llmstxt.org](https://llmstxt.org)) pointing at the raw Markdown.

Re-run it after adding, editing or retitling a post.

## License

Everything is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) (`LICENSE`). The `#license` page (`posts/license.md`), linked from the footer, explains it.

## Customizing

| What | Where |
|------|-------|
| Title, tagline, home intro, nav, footer, default theme, site URL, X handle, declaration | `config.json` |
| Colors, fonts, background glyphs | `themes/<name>.css` |
| Layout shared by all themes | `base.css` (uses only theme variables) |

Themes: `homepage` (default; matches drdebmath.github.io, with robot and distributed-algorithm glyphs),
`watercolor` (washes and ink magic circles), `pokemon` (Poké Ball red, type-symbol glyphs).
Every theme has a dark mode; the header button switches it and remembers the choice.
Background glyphs sit in the side gutters on wide screens and in a ribbon under the header and above the
footer on small screens, so they never sit behind text.
