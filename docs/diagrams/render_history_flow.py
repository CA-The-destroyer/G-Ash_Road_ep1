"""Render the history/publication flow as reproducible PNG, SVG and Mermaid."""
from pathlib import Path
from html import escape
import json
import math
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
DATA = json.loads((HERE.parent / "history/source-commits.json").read_text(encoding="utf-8"))
counts = DATA["counts"]
release = DATA.get("release", {"promoted": "Journey42", "rollback": "Journey41", "save_schema": 46})
W, H = 2160, 1450
im = Image.new("RGB", (W, H), "#0C1725")
d = ImageDraw.Draw(im)
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">',
       '<title id="title">The Ash Road development history and publication flow</title>',
       '<desc id="desc">Local authoring feeds the source commit history and reviewed Unreal release freezes. Neutral commit metadata and release evidence feed the separate GitHub documentation repository. The current HEAD count is a subset of all local source commits.</desc>',
       f'<rect width="{W}" height="{H}" fill="#0C1725"/>']


def font(size, heavy=False):
    return ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf" if heavy else "C:/Windows/Fonts/segoeui.ttf", size)


def text(x, y, value, size=27, color="#EAF0F7", heavy=False):
    ft = font(size, heavy)
    box = d.textbbox((x, y), value, font=ft)
    assert box[2] < W - 35 and box[3] < H - 20, (value, box)
    d.text((x, y), value, font=ft, fill=color)
    ascent, _ = ft.getmetrics()
    svg.append(f'<text x="{x}" y="{y+ascent}" font-family="Segoe UI,sans-serif" font-size="{size}" font-weight="{600 if heavy else 400}" fill="{color}">{escape(value)}</text>')


def rule(points, color="#88A3C0", width=3, arrow=True):
    d.line(points, fill=color, width=width)
    svg.append(f'<polyline points="{" ".join(f"{x},{y}" for x,y in points)}" fill="none" stroke="{color}" stroke-width="{width}"/>')
    if arrow:
        x, y = points[-1]
        px, py = points[-2]
        angle = math.atan2(y-py, x-px)
        triangle = [(x, y)] + [(x-16*math.cos(angle+s), y-16*math.sin(angle+s)) for s in [-.48, .48]]
        d.polygon(triangle, fill=color)
        svg.append(f'<polygon points="{" ".join(f"{a:.2f},{b:.2f}" for a,b in triangle)}" fill="{color}"/>')


def box(x, y, title, lines, accent):
    w, h = 590, 245
    d.rounded_rectangle((x, y, x+w, y+h), radius=18, fill="#14263A", outline=accent, width=2)
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="#14263A" stroke="{accent}" stroke-width="2"/>')
    text(x+28, y+24, title, 29, accent, True)
    for i, line in enumerate(lines):
        assert d.textlength(line, font=font(27)) <= w-56, line
        text(x+28, y+82+i*42, line, 27)


rule([(85, 52), (2075, 52)], "#CBA96D", 3, False)
text(85, 82, "THE ASH ROAD  /  30 OCTOBER 2026", 25, "#CBA96D", True)
text(80, 135, "Development history & publication flow", 58, heavy=True)
text(85, 220, "Source development, playable releases and public documentation retain separate histories.", 29, "#B7C6D9")
for x, value, label in [
    (85, counts["local_source_all_refs"], "LOCAL SOURCE COMMITS"),
    (790, counts["github_docs_published"], "GITHUB DOC COMMITS"),
    (1495, counts["combined_unique_published"], "COMBINED UNIQUE COMMITS"),
]:
    text(x, 290, f"{value:,}", 72, heavy=True)
    text(x, 387, label, 23, "#CBA96D", True)

xs = [85, 785, 1485]
top, bottom = 485, 940
box(xs[0], top, "LOCAL AUTHORING", ["UNREAL / BLENDER / AI", "Source, assets and working changes", "Existing actors and save authority"], "#AFC8E8")
box(xs[1], top, "REVIEWED FREEZE + UAT", ["Committed base + reviewed changes", "Focused checks; build / cook / archive", "Acceptance controls promotion"], "#DDB976")
box(xs[2], top, "PLAYABLE RELEASE", [f'{release["promoted"]} promoted / schema{release["save_schema"]}',
                                    f'{release["rollback"]} retained as previous',
                                    release.get("next_label", "Next increment follows source review")], "#A6D9BC")
box(xs[0], bottom, "LOCAL SOURCE GIT", [f'{counts["local_source_all_refs"]:,} distinct commits across local refs',
                                   f'{counts["local_source_HEAD"]:,} in current HEAD ancestry',
                                   f'{counts["local_source_outside_HEAD"]:,} additional commits outside HEAD'], "#8CCBCC")
box(xs[1], bottom, "REVIEWED METADATA", ["Commit hashes, dates and public subjects", "Aggregate statistics + release evidence", "Source ledger exported as documentation"], "#DDB976")
box(xs[2], bottom, "GITHUB DOCUMENTATION", [f'{counts["github_docs_published"]:,} commits / {DATA["pull_requests"]["total"]} pull requests',
                                         "Status / ledger / diagrams / JSON", "Direct selected-file commits to main"], "#AFC8E8")
for y in [top+122, bottom+122]:
    for left, right in [(xs[0]+590, xs[1]), (xs[1]+590, xs[2])]:
        rule([(left+5, y), (right-8, y)])
for x, label in [(xs[0]+295, "Record commits"), (xs[1]+295, "Publish evidence"), (xs[2]+295, "Record release status")]:
    rule([(x, top+249), (x, bottom-14)])
    ft = font(24)
    label_width = d.textlength(label, font=ft)
    d.rectangle((x-label_width/2-12, 804, x+label_width/2+12, 847), fill="#0C1725")
    svg.append(f'<rect x="{x-label_width/2-12}" y="804" width="{label_width+24}" height="43" fill="#0C1725"/>')
    text(x-label_width/2, 809, label, 24, "#B7C6D9")
rule([(85, 1250), (2075, 1250)], "#33445A", 2, False)
text(85, 1280, f'{counts["local_source_HEAD"]:,} is already within {counts["local_source_all_refs"]:,}. It is not added again to the combined total.', 29, "#DDB976", True)
text(85, 1333, "Unique commit objects are counted by SHA. Cherry-picked commits can represent related work.", 26, "#B7C6D9")
text(85, 1377, "The ledger records source history as metadata; it does not merge source trees into the documentation repository.", 25, "#8EA3BE")
svg.append("</svg>")
im.save(HERE / "development-history-flow.png", optimize=True)
(HERE / "development-history-flow.svg").write_text("\n".join(svg) + "\n", encoding="utf-8", newline="\n")
mmd = f'''flowchart LR
    authorWork["UNREAL / BLENDER / AI authoring"] --> freezeUat["Reviewed freeze and Unreal build / cook / archive"]
    freezeUat --> playableRelease["{release['promoted']} promoted; {release['rollback']} rollback"]
    authorWork -->|"Record commits"| sourceHistory["Local source Git: {counts['local_source_all_refs']} all-ref commits; {counts['local_source_HEAD']} in HEAD ancestry"]
    sourceHistory -->|"Export ledger"| publicMetadata["Reviewed commit metadata and aggregate statistics"]
    freezeUat -->|"Publish evidence"| publicMetadata
    publicMetadata --> docsHistory["GitHub documentation: {counts['github_docs_published']} commits; {DATA['pull_requests']['total']} pull requests"]
    playableRelease -->|"Record status"| docsHistory
    classDef source fill:#DDEFEF,stroke:#478F91,color:#102B32;
    classDef delivery fill:#FFF0D2,stroke:#B98E49,color:#443315;
    classDef released fill:#DDEFE3,stroke:#508965,color:#173625;
    classDef docs fill:#E2EBF7,stroke:#6686B0,color:#172D48;
    class authorWork,sourceHistory source;
    class freezeUat,publicMetadata delivery;
    class playableRelease released;
    class docsHistory docs;
'''
(HERE / "development-history-flow.mmd").write_text(mmd, encoding="utf-8", newline="\n")
(HERE / "development-history-flow.md").write_text('''# Development history and publication flow

![The Ash Road development history and publication flow](development-history-flow.png)

[History and combined statistics](../history/README.md) · [PNG](development-history-flow.png) · [SVG](development-history-flow.svg) · [Mermaid source](development-history-flow.mmd)

Working source and authoring assets feed both local source commits and reviewed release freezes. A freeze includes its committed base plus reviewed working changes; the current source HEAD alone does not describe every later playable package. Unreal build/cook/archive and focused acceptance determine promotion.

Commit metadata, aggregate statistics and release evidence are published to the separate documentation repository. Its direct commits to main explain the zero pull-request count. Source hashes are recorded in the ledger without implying that their source trees or Git objects are hosted in this repository.

The current HEAD ancestry is a subset of all reachable local source commits. Combined statistics deduplicate the two repository histories by full commit SHA. Unique commit objects are not unique features, accepted releases or independent patches.

```mermaid
''' + mmd + '```\n\n[render_history_flow.py](render_history_flow.py) recreates the PNG, SVG and Mermaid from the published history JSON using Python/Pillow and installed Windows Segoe UI fonts. Fonts are not redistributed.\n', encoding="utf-8", newline="\n")
print("Rendered history flow PNG, SVG, editable Mermaid and explanation.")
