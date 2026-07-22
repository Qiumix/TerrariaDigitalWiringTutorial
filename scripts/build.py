import re
import os
import sys
import subprocess
import html as html_mod

BUILD = sys.argv[1] if len(sys.argv) > 1 else "build"
ROOT = os.path.dirname(os.path.abspath(__file__ + "/.."))


def run(cmd):
    subprocess.run(cmd, shell=True, check=True)


def slug(text):
    s = text.strip().lower()
    s = re.sub(r"[^\w]+", "-", s)
    s = s.strip("-")
    return s or "page"


def has_text_content(body):
    cleaned = re.sub(r"<[^>]+>", "", body).strip()
    cleaned = re.sub(r"\s+", "", cleaned)
    return len(cleaned) > 0


def main():
    os.makedirs(BUILD, exist_ok=True)

    # Step 1: preprocess
    print("Preprocessing MPE markdown ...")
    run(f"python3 {ROOT}/scripts/preprocess.py {ROOT}/main.md {BUILD}/all.md")

    # Step 2: read and split by ## headings
    with open(f"{BUILD}/all.md", "r", encoding="utf-8") as f:
        content = f.read()

    raw_parts = re.split(r"^(?=## (?!##))", content, flags=re.MULTILINE)
    frontmatter = raw_parts[0].strip() if raw_parts else ""
    raw_parts = raw_parts[1:]

    parts = []
    for p in raw_parts:
        m = re.match(r"^## (.+)", p)
        if not m:
            continue
        title = m.group(1).strip()
        body = p[m.end() :].strip()
        if not body or not has_text_content(body):
            continue
        parts.append((title, p))

    if not parts:
        print("No chapters found!")
        sys.exit(1)

    # Step 3: generate chapter pages
    chapters = []
    for i, (title, p) in enumerate(parts):
        fileno = f"ch_{i}"
        filename = f"{slug(title)}.html"
        filepath = f"{BUILD}/{filename}"

        prev_link = ""
        next_link = ""
        if i > 0:
            pt = parts[i - 1][0]
            prev_link = f'<a href="{slug(pt)}.html" class="nav-prev">← {pt}</a>'
        if i < len(parts) - 1:
            nt = parts[i + 1][0]
            next_link = f'<a href="{slug(nt)}.html" class="nav-next">{nt} →</a>'

        nav = (
            f'<nav class="chapter-nav">\n'
            f"{prev_link}\n"
            f'<span class="nav-center">{title}</span>\n'
            f"{next_link}\n"
            f"</nav>"
        )

        navfile = f"{BUILD}/_{fileno}_nav.html"
        with open(navfile, "w", encoding="utf-8") as f:
            f.write(nav)

        with open(f"{BUILD}/{fileno}.md", "w", encoding="utf-8") as f:
            f.write(p)

        run(
            f"pandoc --from markdown+header_attributes+fenced_divs "
            f"--to html5 --standalone --mathjax "
            f'--metadata title="{title}" '
            f"--css=style.css "
            f"--include-after-body={navfile} "
            f"-o {filepath} {BUILD}/{fileno}.md"
        )
        os.remove(navfile)
        chapters.append((title, filename))

    # Step 4: copy assets
    run(f"cp {ROOT}/scripts/style.css {BUILD}/style.css")
    run(f"mkdir -p {BUILD}/chapters && cp -r {ROOT}/chapters/images {BUILD}/chapters/")
    run(f"cp {ROOT}/main.png {BUILD}/main.png")

    # Step 5: generate index page
    index_html = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>泰拉瑞亚数字电路文档</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<div class="index-container">
  <h1>泰拉瑞亚数字电路文档</h1>
  <div class="index-quote">
    <p>混乱沉睡，2025 年 12 月 25 日</p>
    <img src="main.png" alt="">
  </div>
  <ol class="index-toc">
"""
    for title, filename in chapters:
        index_html += f'    <li><a href="{filename}">{title}</a></li>\n'

    index_html += """  </ol>
  <p class="index-footer">
    <a href="all.html">阅读全文（单页版）</a>
  </p>
</div>
</body>
</html>
"""

    with open(f"{BUILD}/index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    # Step 6: single-page version (for print/PDF)
    run(
        f"pandoc --from markdown+header_attributes+fenced_divs "
        f"--to html5 --standalone --mathjax "
        f'--metadata title="泰拉瑞亚数字电路文档" '
        f"--css=style.css "
        f"-o {BUILD}/all.html {BUILD}/all.md"
    )

    print(f"Build complete → {BUILD}/")


if __name__ == "__main__":
    main()
