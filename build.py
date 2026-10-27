"""Build the static extras the in-browser renderer can't provide:
- p/<slug>.html + p/<slug>.png: each post's own page (index.html plus the post's link-preview tags, since crawlers
  for X, WhatsApp, Slack don't run JavaScript), the PNG a card in the post's own theme;
- feed.xml: RSS with each post's full Markdown, and llms.txt: an index for AI agents pointing at the raw Markdown.

Run after adding, editing or retitling a post:  python3 build.py
Share posts as  <site url>p/<slug>.html
Images need Google Chrome or Microsoft Edge installed; without one, pages are still made, just without images.
"""
import html, json, os, re, subprocess, tempfile
from email.utils import format_datetime
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.abspath(__file__))
BROWSERS = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "/usr/bin/google-chrome", "/usr/bin/chromium"]
ROBOT = re.search(r'<svg class="robot".*?</svg>', open(os.path.join(ROOT, "index.html")).read()).group(0)

CARD = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<link rel="stylesheet" href="{root}/base.css"><link rel="stylesheet" href="{root}/themes/{theme}.css">
<style>
  html {{ background: var(--bg) !important; }}
  body {{ margin: 0; max-width: none; height: 630px; padding: 64px 80px; display: flex; flex-direction: column;
         justify-content: space-between; background: var(--bg) !important; }}
  body::before, body::after {{ display: none !important; }}
  .brand {{ display: flex; flex-direction: row; align-items: center; gap: 18px; font: 700 30px var(--display); }}
  .brand svg {{ width: 64px; height: 64px; color: var(--fg); }}
  h1 {{ margin: 0; font-size: 66px; line-height: 1.12; color: var(--fg); }}
  p {{ margin: 0; font: 28px/1.45 var(--body); color: var(--muted); }}
  .bar {{ height: 12px; border-radius: 6px; background: linear-gradient(90deg, var(--human), var(--collab), var(--ai)); }}
</style></head><body>
<div class="brand">{robot}<span>{site}</span></div><h1>{title}</h1><p>{desc}</p><div class="bar"></div>
</body></html>"""

# Each post's own page: index.html with the post's preview tags, <base href="../"> so every relative
# path still resolves, and <meta name="slug"> telling the renderer which post to show.
SHELL = open(os.path.join(ROOT, "index.html")).read()
HEAD = re.compile(r"<title>.*?<meta name=\"twitter:card\"[^>]*>\n", re.S)
PAGE = """<base href="../">
<meta name="slug" content="{slug}">
<title>{title} · {site}</title>
<meta name="description" content="{desc}">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="{kind}">
<meta property="og:url" content="{url}p/{slug}.html">
{image}<meta name="twitter:card" content="{card}">
<link rel="canonical" href="{url}p/{slug}.html">
"""


def screenshot(browser, card_html, out_png):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(card_html)
    try:
        subprocess.run([browser, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1200,630",
                        "--virtual-time-budget=4000", f"--screenshot={out_png}", "file://" + f.name],
                       check=True, capture_output=True, timeout=60)
    finally:
        os.remove(f.name)


def main():
    config = json.load(open(os.path.join(ROOT, "config.json")))
    posts = json.load(open(os.path.join(ROOT, "posts.json")))
    browser = next((b for b in BROWSERS if os.path.exists(b)), None)
    os.makedirs(os.path.join(ROOT, "p"), exist_ok=True)
    site, url = config["title"], config["url"]
    home = {"slug": "home", "title": site, "description": config["description"], "theme": config["theme"]}
    for post in posts + [home]:
        slug, theme = post["slug"], post.get("theme", config["theme"])
        plain = re.sub(r"<[^>]+>", "", post["title"])
        desc = post.get("description", config["description"])
        esc = lambda s: html.escape(s, quote=True)
        png = os.path.join(ROOT, "p", f"{slug}.png")
        if browser:
            screenshot(browser, CARD.format(root=ROOT, theme=theme, robot=ROBOT, site=esc(site),
                                            title=post["title"], desc=esc(desc)), png)
        has_img = os.path.exists(png)
        if slug == "home":
            continue  # the home page's own tags live in index.html
        page = PAGE.format(title=esc(plain), site=esc(site), desc=esc(desc), url=url, slug=slug,
                           kind="profile" if post.get("page") else "article",
                           image=f'<meta property="og:image" content="{url}p/{slug}.png">\n' if has_img else "",
                           card="summary_large_image" if has_img else "summary")
        open(os.path.join(ROOT, "p", f"{slug}.html"), "w").write(HEAD.sub(lambda _: page, SHELL, count=1))
        print(f"p/{slug}.html" + (" + .png" if has_img else ""))
    if not browser:
        print("No Chrome/Edge found: preview pages made without images.")
    write_feeds(config, [p for p in posts if not p.get("page")], posts)


def write_feeds(config, articles, everything):
    """feed.xml (RSS 2.0, full Markdown in content:encoded) and llms.txt (https://llmstxt.org) for AI agents."""
    site, url, esc = config["title"], config["url"], lambda s: html.escape(s, quote=True)
    plain = lambda t: re.sub(r"<[^>]+>", "", t)
    rfc822 = lambda d: format_datetime(datetime.fromisoformat(d).replace(tzinfo=timezone.utc))
    articles = sorted(articles, key=lambda p: p["date"], reverse=True)
    items = []
    for p in articles:
        md = open(os.path.join(ROOT, "posts", f"{p['slug']}.md")).read().replace("]]>", "]]]]><![CDATA[>")
        items.append(f"""  <item>
    <title>{esc(plain(p['title']))}</title>
    <link>{url}p/{p['slug']}.html</link>
    <guid isPermaLink="false">{url}#{p['slug']}</guid>
    <pubDate>{rfc822(p['date'])}</pubDate>
    <description>{esc(p.get('description', ''))}</description>
    <content:encoded><![CDATA[{md}]]></content:encoded>
    <source url="{url}posts/{p['slug']}.md">{esc(site)}</source>
  </item>""")
    last = max(p.get("updated", p["date"]) for p in articles)
    open(os.path.join(ROOT, "feed.xml"), "w").write(f"""<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:content="http://purl.org/rss/1.0/modules/content/">
<channel>
  <title>{esc(site)}</title>
  <link>{url}</link>
  <description>{esc(config['description'])}</description>
  <language>en</language>
  <copyright>CC BY 4.0, Debasish Pattanayak</copyright>
  <lastBuildDate>{rfc822(last)}</lastBuildDate>
{chr(10).join(items)}
</channel>
</rss>
""")
    lines = [f"# {site}", "", f"> {config['description']}", "",
             "Posts are Markdown files. Text is marked by who wrote it: `by-human` (the author's own words), "
             "`by-collab` (the author's ideas written up by AI) and `by-ai` (written by AI). "
             f"Everything is licensed under CC BY 4.0: share and adapt it, with credit. Details: {url}posts/license.md", "", "## Posts", ""]
    lines += [f"- [{plain(p['title'])}]({url}posts/{p['slug']}.md): {p.get('description', '')} "
              f"(published {p['date']}" + (f", updated {p['updated']}" if p.get("updated") else "") + ")" for p in articles]
    lines += ["", "## Pages", ""]
    lines += [f"- [{plain(p['title'])}]({url}posts/{p['slug']}.md): {p.get('description', '')}" for p in everything if p.get("page")]
    open(os.path.join(ROOT, "llms.txt"), "w").write("\n".join(lines) + "\n")
    print("feed.xml, llms.txt")


if __name__ == "__main__":
    main()
