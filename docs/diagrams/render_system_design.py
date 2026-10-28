"""Render the system overview PNG. Run with the existing Python/Pillow runtime."""
from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

OUTPUT = Path(__file__).with_name("ash-road-system-design.png")
image = Image.new("RGB", (2400, 3440), "#F5F7FB")
draw = ImageDraw.Draw(image)
REGULAR = r"C:\Windows\Fonts\segoeui.ttf"
BOLD = r"C:\Windows\Fonts\seguisb.ttf"


def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REGULAR, size)


def text(x, y, value, size=28, color="#39455B", bold=False):
    draw.text((x, y), value, font=font(size, bold), fill=color)


def wrap(value, width, size=28, bold=False):
    lines = []
    for paragraph in value.split("\n"):
        line = ""
        for word in paragraph.split():
            candidate = (line + " " + word).strip()
            if line and draw.textlength(candidate, font=font(size, bold)) > width:
                lines.append(line)
                line = word
            else:
                line = candidate
        lines.append(line)
    return lines


def panel(x, y, width, height, title, body, dark=False, accent=False):
    draw.rounded_rectangle((x, y + 5, x + width, y + height + 5), radius=22, fill="#E4E9F1")
    draw.rounded_rectangle(
        (x, y, x + width, y + height), radius=22,
        fill="#172B48" if dark else "#FFFFFF",
        outline=None if dark else "#CED7E4", width=2,
    )
    if accent:
        draw.rounded_rectangle((x, y, x + width, y + 8), radius=4, fill="#274D80")
    cursor = y + 24
    for line in wrap(title, width - 64, 32, True):
        text(x + 32, cursor, line, 32, "#FFFFFF" if dark else "#172B48", True)
        cursor += 42
    cursor += 12
    for line in wrap(body, width - 64):
        text(x + 32, cursor, line, 28, "#DCE7F6" if dark else "#39455B")
        cursor += 38
    if cursor > y + height - 10:
        raise ValueError(f"Text exceeds panel: {title}")


def arrow(points, dashed=False):
    color = "#73829A"
    for start, end in zip(points, points[1:]):
        if not dashed:
            draw.line((start, end), fill=color, width=5)
            continue
        dx, dy = end[0] - start[0], end[1] - start[1]
        length = math.hypot(dx, dy)
        for step in range(0, int(length), 25):
            a, b = step / length, min(step + 14, length) / length
            draw.line(
                ((start[0] + dx * a, start[1] + dy * a),
                 (start[0] + dx * b, start[1] + dy * b)),
                fill=color, width=5,
            )
    start, end = points[-2:]
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    draw.polygon([
        end,
        (end[0] - 18 * math.cos(angle - .48), end[1] - 18 * math.sin(angle - .48)),
        (end[0] - 18 * math.cos(angle + .48), end[1] - 18 * math.sin(angle + .48)),
    ], fill=color)


text(100, 65, "THE ASH ROAD  /  SYSTEM OVERVIEW", 26, "#57708E", True)
text(100, 108, "Advanced Custom Game Dev System Design", 64, "#172B48", True)
text(100, 199, "Expanded Unreal technology stack  /  28 October 2026", 32)

panel(100, 300, 530, 210, "NVIDIA RTX 4060 Ti", "8 GB shared VRAM\nCUDA AI + scheduled rendering")
panel(660, 300, 530, 210, "AMD RADEON GRAPHICS", "Verified Unreal NPC previews\nNative diagnostics / fallback")
panel(1220, 300, 530, 210, "CPU PROCESSING", "Authoring, audio, rules,\nsaves, builds and exports")
panel(1780, 300, 520, 210, "HOSTED AI", "Image generation on\nprovider-managed compute")

panel(100, 570, 2200, 130, "YOUR CREATIVE DIRECTION", "World, characters, equipment, art references, quests and game rules", True)
arrow([(425, 700), (425, 790)])
arrow([(1975, 700), (1975, 790)])
arrow([(800, 920), (850, 920)])
arrow([(1200, 1060), (1200, 1160)])
arrow([(1975, 1060), (1975, 1160)])

panel(100, 790, 700, 270, "IMAGE AI + TRELLIS / LOCALMESH", "Hosted reference images → local 3D candidates.\nTRELLIS.2, DINOv3, PyTorch + CUDA.\nNVIDIA GPU inference.", accent=True)
panel(850, 790, 700, 270, "BLENDER + PYTHON PIPELINES", "Models, rigs and portable PBR materials.\nPreserved UVs + UV-layout image exports.\nManifests, source readback and validation.", accent=True)
panel(1600, 790, 700, 270, "QWEN3-TTS / VOICEFORGE", "Voice profiles and dialogue → FFmpeg audio.\n0.6B: GPU when admitted; 1.7B: CPU.\nApproved takes, subtitles and manifests.", accent=True)
panel(100, 1160, 2200, 170, "SHARED CONTENT LIBRARY & ENGINE INTAKE", "Models, animation, textures, icons and audio with stable IDs and provenance. Visual/audio review, optimization, native import and per-asset acceptance.")
arrow([(1200, 1330), (1200, 1420)])

# Unreal occupies the dominant area; source previews and Lab trials are labeled.
draw.rounded_rectangle((70, 1420, 2330, 3040), radius=26, fill="#EAF0F8", outline="#B8C8DE", width=3)
text(110, 1450, "UNREAL ENGINE 5.8", 49, "#172B48", True)
text(110, 1521, "CURRENT GAME SYSTEMS & ENGINE CONFIGURATION", 26, "#57708E", True)

cards = [
    (100, 1590, "WORLD & STREAMING", "Native Landscape terrain\nWorld Partition cells\nHISM vegetation / repeated meshes\nProceduralMeshComponent support"),
    (850, 1590, "RENDERING & MATERIALS", "Lumen lighting / reflections\nVirtual Shadow Maps\nD3D12 + Shader Model 6\nNanite on selected owned meshes"),
    (1600, 1590, "CHAOS & NETWORKED PHYSICS", "Rigid bodies + CCD collision\nAsync physics at 60 Hz\nPredictive Interpolation\nSaved authoritative resting poses"),
    (100, 1940, "MULTIPLAYER & MOVEMENT", "Server RPCs + property replication\nCharacterMovement prediction\nServer-side interaction validation\nShared authoritative gameplay state"),
    (850, 1940, "SKELETAL ANIMATION", "Skeletal meshes + AnimSequences\nBlend spaces / native animation proxies\nAnimGraphRuntime evaluation\nProfile Data Assets + attachments"),
    (1600, 1940, "SLATE UI & ENGINE AUDIO", "Slate / SlateCore interfaces\nMoviePlayer loading presentation\nSpatialized sound + attenuation\nOcclusion and concurrency controls"),
]
for x, y, title, body in cards:
    panel(x, y, 700, 300, title, body, accent=True)

draw.rounded_rectangle((100, 2310, 2300, 2600), radius=22, fill="#F6EFE0", outline="#D7C49D", width=2)
text(132, 2335, "METAHUMAN + NATIVE CLOTHING — SOURCE PREVIEW / LAB", 34, "#69532B", True)
pilot = [
    "MetaHuman assemblies, DNA/RigLogic and profile Data Assets: three NPCs have functional source previews.",
    "Epic Outfit resizing preserves source geometry, skin weights, UVs and exportable material routes.",
    "Chaos Cloth + Dataflow cape trials and native IK-retargeted action candidates remain bounded Lab work.",
    "Journey40 is the cooked master. Final art, broader combat/crowd acceptance and creator sliders remain open.",
]
y = 2395
for paragraph in pilot:
    for line in wrap(paragraph, 2136, 27):
        text(132, y, line, 27, "#69532B")
        y += 37
    y += 7
if y > 2588:
    raise ValueError("Pilot text overflow")

text(110, 2650, "GAME AUTHORITY + UNREAL AUTHORING / DELIVERY", 26, "#57708E", True)
panel(100, 2710, 1070, 275, "CUSTOM C++20 + SQLITE AUTHORITY", "Quest facts, item ownership, inventory and rewards.\nTransactions, migrations, retries and saved state.\nConnected to Unreal server gameplay; custom core.")
panel(1230, 2710, 1070, 275, "UNREAL EDITOR & BUILD PIPELINE", "Unreal Python + Editor Scripting Utilities.\nCustom AshRoadWorldEditor authoring module.\nUBT / UHT / UAT → cook, stage and archive.")

arrow([(1200, 3040), (1200, 3160)])
caption = "Focused native / rendered / packaged checks + persistence verification"
caption_width = draw.textlength(caption, font=font(29))
caption_x = (2400 - caption_width) / 2
draw.rectangle((caption_x - 20, 3074, caption_x + caption_width + 20, 3124), fill="#F5F7FB")
text(caption_x, 3080, caption, 29, "#57708E")
panel(100, 3160, 2200, 140, "THE ASH ROAD — PLAYABLE COOPERATIVE RPG", "Cooked release, functional source previews and prepared content retain separate acceptance states.", True)
text(100, 3354, "NVIDIA and AMD jobs are coordinated; verified use does not imply pooled VRAM or concurrent rendering.", 28)

image.save(OUTPUT, optimize=True, dpi=(180, 180))
with Image.open(OUTPUT) as check:
    check.verify()
print(OUTPUT)
print("2400 x 3440 PNG; all panel text bounds checked")
