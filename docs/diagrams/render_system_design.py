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
text(100, 199, "Unreal + Blender + AI  /  owner-recruited second PC  /  31 October 2026", 32)

panel(100, 300, 530, 210, "NVIDIA RTX 4060 Ti", "8 GB shared VRAM\nCUDA AI + scheduled rendering")
panel(660, 300, 530, 210, "LOCAL AMD RADEON", "Unreal source / packaged views\nHIP asset rendering")
panel(1220, 300, 530, 210, "SECONDARY WORKER PC", "Blender 4.1.1 / two CPU threads\nOwner-recruited LOD helper")
panel(1780, 300, 520, 210, "CPU + HOSTED AI", "Local / Linux CPU work\nProvider image generation")

panel(100, 570, 2200, 130, "YOUR CREATIVE DIRECTION", "World, characters, equipment, art references, quests and game rules", True)
arrow([(425, 700), (425, 790)])
arrow([(1975, 700), (1975, 790)])
arrow([(800, 920), (850, 920)])
arrow([(1200, 1060), (1200, 1160)])
arrow([(1975, 1060), (1975, 1160)])

panel(100, 790, 700, 270, "IMAGE AI + TRELLIS / LOCALMESH", "Hosted reference images → local 3D candidates.\nTRELLIS.2, DINOv3, PyTorch + CUDA.\nNVIDIA GPU inference.", accent=True)
panel(850, 790, 700, 270, "BLENDER + PYTHON PIPELINES", "Models, rigs, portable PBR and retained UVs.\nWorker PC: optional LOD / UV / export jobs.\nHash review before controller-owned intake.", accent=True)
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
text(132, 2335, "METAHUMAN + NATIVE CLOTHING — RELEASE / SOURCE / LAB", 34, "#69532B", True)
pilot = [
    "MetaHuman / DNA / RigLogic, groom bindings, profile Data Assets and native animation banks.",
    "Epic Outfit and fitted modular garments preserve skin weights, UVs and portable PBR material routes.",
    "Journey46/schema47 promoted; Journey45 rollback. Independent equipment visuals are active AR-P02 work.",
    "Source-only equipment/LOD candidates, Cloth/Dataflow trials and real EOS/WAN retain separate gates.",
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
text(100, 3340, "Priority: NVIDIA → local AMD → worker PC. Independent compatible jobs may run concurrently.", 28)
text(100, 3382, "Two worker LOD candidates returned; native admission open. Owner playtests reserve NVIDIA; no pooled VRAM.", 28)

image.save(OUTPUT, optimize=True, dpi=(180, 180))
with Image.open(OUTPUT) as check:
    check.verify()
print(OUTPUT)
print("2400 x 3440 PNG; all panel text bounds checked")

# Recreate page 2 from drawing primitives rather than editing a prior bitmap.
image = Image.new("RGB", (2400, 2400), "#F5F7FB")
draw = ImageDraw.Draw(image)
text(100, 70, "THE ASH ROAD  /  SKILLS & EXPERIENCE", 28, "#57708E", True)
text(100, 125, "Advanced Custom Game Dev System Design", 64, "#172B48", True)
text(100, 222, "Page 2  /  capabilities supporting the system  /  31 October 2026", 32)
panel(100, 315, 2200, 150, "GAME DESIGN & CREATIVE DIRECTION", "Worldbuilding, art references, quests, combat, progression, economy and usable interfaces.", True)
arrow([(1200, 465), (1200, 535)])
panel(100, 535, 2200, 170, "SYSTEMS ARCHITECTURE & PROGRAMMING", "C++20 / Python, authority boundaries, stable identities, data contracts, debugging and dependency control.", accent=True)
for x in [450, 1200, 1950]:
    arrow([(x, 705), (x, 795)])
panel(100, 795, 700, 370, "BLENDER & CONTENT", "Topology, UV maps, portable PBR,\nrigs, weights and retargeting.\nAnimation, equipment attachments,\nvoice direction and audio mastering.\nReview actual exports and engine fit.", accent=True)
panel(850, 795, 700, 370, "UNREAL & GAMEPLAY", "Actors, Slate UI, physics and motion.\nReplication and server validation.\nSQLite transactions and persistence.\nReconnect and duplicate prevention.\nPreserve quest/item/save authority.", accent=True)
panel(1600, 795, 700, 370, "AI & PRODUCTION TOOLS", "TRELLIS / PyTorch / CUDA, Qwen TTS.\nPython / PowerShell automation.\nGPU memory and device scheduling.\nProvenance, logs and recovery.\nReview generated candidates.", accent=True)
arrow([(1950, 1165), (1950, 1250)])
panel(100, 1250, 2200, 260, "SECOND-PC ORCHESTRATION — OWNER-RECRUITED WORKER", "SSH / PowerShell job packets, compatible Blender 4.1.1 and a two-thread CPU limit.\nPersisted status, deadlines and SHA256/size-checked retrieval; preserve UVs and source identity.\nTwo LOD candidates returned. Geometry/material review and native acceptance remain separate.\nSchedule NVIDIA → local AMD → worker PC; protect owner playtests and the shared Unreal/build slot.", accent=True)
arrow([(450, 1165), (450, 1205), (65, 1205), (65, 1570), (450, 1570), (450, 1640)])
arrow([(1200, 1165), (1200, 1210), (2340, 1210), (2340, 1570), (1950, 1570), (1950, 1640)])
arrow([(1200, 1510), (1200, 1640)])
panel(100, 1640, 2200, 210, "QA, PROFILING & INTEGRATION ACCEPTANCE", "Select focused Core / native / rendered / packaged checks. Reuse evidence for unchanged dependencies.\nInspect actual output and resource use; preserve failures and distinguish candidate, integrated and released work.", True)
arrow([(1200, 1850), (1200, 1940)])
panel(100, 1940, 2200, 220, "INFRASTRUCTURE, BUILDS, RELEASES & RECOVERY", "Windows / Linux, Docker / SSH, Git, isolated environments, CMake and Unreal UBT / UHT / UAT.\nReproducible delivery, source history, reviewed publication, backups and rollback.\nOne controller owns Unreal imports/builds; optional workers do not become mandatory dependencies.", accent=True)
text(100, 2230, "Practical depth can be shared across people and tools. This graph maps responsibilities, not personal credentials.", 28)
OUTPUT = OUTPUT.with_name("ash-road-system-design-page-2-skills.png")
image.save(OUTPUT, optimize=True, dpi=(180, 180))
with Image.open(OUTPUT) as check:
    check.verify()
print(OUTPUT)
print("2400 x 2400 PNG; all panel text bounds checked")
