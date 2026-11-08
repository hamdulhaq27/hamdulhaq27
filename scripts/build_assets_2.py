"""Timeline, process diagram, tech stack, project illustrations and closing panel."""
import os, io, base64
from svgkit import SVG, measure, wrap, esc
from icons_custom import icon
from build_assets import A, W, SI, panel, mono_label, chip, arrow_marker

# ------------------------------------------------------------- timeline
JOURNEY = [
    dict(kind="edu", stage="2023 — Present", title="BS Artificial Intelligence",
         meta="FAST-NUCES · Islamabad",
         desc="Third-year undergraduate. Coursework that turned into real systems: neural networks, natural language processing and software engineering.",
         tags=["Machine learning", "NLP", "Neural networks"]),
    dict(kind="proj", stage="Deep learning", title="XDL-IDS · CNN-Attention-GRU",
         meta="Team project · Artificial Neural Networks",
         desc="Extended a published CAN-bus intrusion detector with multi-head self-attention and tested it on a merged CICIoV2024 + Car Hacking dataset, with SHAP explainability.",
         tags=["TensorFlow", "Keras", "SHAP"]),
    dict(kind="proj", stage="LLM systems", title="La Bella Tavola assistant",
         meta="Team project · Natural Language Processing",
         desc="Built a fully local reservation assistant: slot extraction and a state machine around a small LLM, voice in and out, RAG with tool calls, and an evaluation suite.",
         tags=["Ollama", "Chroma", "FastAPI", "Whisper"]),
    dict(kind="proj", stage="ML in production", title="Zameen Intelligence Platform",
         meta="Deployed · daily automated pipeline",
         desc="Shipped a lead-intelligence product for Karachi real estate that scrapes, segments and scores new listings every morning and redeploys its API and dashboard.",
         tags=["Selenium", "scikit-learn", "GitHub Actions"]),
    dict(kind="proj", stage="Automation", title="Lead Scraping & Outreach",
         meta="Queue-backed scraping and email outreach",
         desc="Designed a Celery + Redis job system that scrapes Google Maps, enriches leads with web, LinkedIn and social data, syncs them to Google Sheets and runs staggered outreach.",
         tags=["Celery", "Redis", "Apify", "Sheets API"]),
    dict(kind="now", stage="Now", title="Agentic AI and applied LLM systems",
         meta="Current focus",
         desc="Going deeper on agents, voice interfaces and the MLOps needed to keep models reliable after deployment.",
         tags=["Agents", "Voice AI", "MLOps"]),
]


def timeline(th):
    s = SVG(W, 100, th, "Professional journey timeline",
            " | ".join(f"{e['stage']}: {e['title']} — {e['desc']}" for e in JOURNEY))
    spine_x, cx, cw = 200, 232, 560
    y = 104
    nodes = []
    body = []
    for e in JOURNEY:
        ty = y
        nodes.append((e["kind"], ty - 6))
        s.text(spine_x - 30, ty - 1, e["stage"].upper(), fam="mono", size=10.5, weight=500,
               fill="cyan" if e["kind"] == "now" else "muted", anchor="end", ls=1.5)
        s.text(cx, ty, e["title"], size=19, weight=600, ls=-0.3)
        s.text(cx, ty + 23, e["meta"], fam="mono", size=11, fill="cyan", ls=0.3)
        lines = wrap(e["desc"], cw, "sans", 400, 14.5)
        for i, ln in enumerate(lines):
            s.text(cx, ty + 50 + i * 22, ln, size=14.5, fill="muted")
        tyy = ty + 50 + (len(lines) - 1) * 22 + 16
        x = cx
        for t in e["tags"]:
            x += chip(s, x, tyy, t) + 8
        y = tyy + 22 + 46
    H = y - 26
    s.h = H
    # panel + header behind content
    s.els.insert(0, f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="14" fill="{s.c("bg")}" stroke="{s.c("border")}"/>')
    s.text(32, 42, "JOURNEY", fam="mono", size=11, weight=500, fill="blue", ls=2.2)
    s.text(W - 32, 42, "Education  →  Projects  →  Now", fam="mono", size=11, fill="faint", anchor="end", ls=0.6)
    s.line(32, 60.5, W - 32, 60.5, stroke="border")
    # spine
    s.line(spine_x, nodes[0][1], spine_x, nodes[-1][1], stroke="border", sw=2)
    for kind, ny in nodes:
        s.line(spine_x + 9, ny, cx - 10, ny, stroke="border")
        if kind == "edu":
            s.add(f'<rect x="{spine_x - 7}" y="{ny - 7}" width="14" height="14" rx="2" fill="{s.c("bg")}" '
                  f'stroke="{s.c("blue")}" stroke-width="2" transform="rotate(45 {spine_x} {ny})"/>')
        elif kind == "now":
            s.add(f'<circle cx="{spine_x}" cy="{ny}" r="7" fill="none" stroke="{s.c("cyan")}" stroke-width="1.5">'
                  f'<animate attributeName="r" values="7;17" dur="2.4s" repeatCount="indefinite"/>'
                  f'<animate attributeName="opacity" values="0.9;0" dur="2.4s" repeatCount="indefinite"/></circle>')
            s.add(f'<circle cx="{spine_x}" cy="{ny}" r="7" fill="{s.c("cyan")}"/>')
        else:
            s.add(f'<circle cx="{spine_x}" cy="{ny}" r="7" fill="{s.c("bg")}" stroke="{s.c("blue")}" stroke-width="2"/>')
            s.add(f'<circle cx="{spine_x}" cy="{ny}" r="2.2" fill="{s.c("blue")}"/>')
    s.save(f"{A}/timeline/journey-{th}.svg")


# ------------------------------------------------------- process diagram
STAGES = [
    ("Understand", "Find the real problem, the users, the data and the constraints."),
    ("Architect", "Design the system, data flow and integration points."),
    ("Build", "Develop the backend, automation and AI layer."),
    ("Integrate", "Connect models, tools, APIs, databases and services."),
    ("Test & optimize", "Validate reliability, performance and practical usability."),
    ("Deploy", "Ship a maintainable, working solution — then watch it run."),
]


def process(th):
    s = SVG(W, 452, th, "Engineering process: six stages",
            " → ".join(f"{i + 1:02d} {n}: {d}" for i, (n, d) in enumerate(STAGES)))
    panel(s)
    arrow_marker(s, "blue", "pa")
    s.text(32, 42, "WORKFLOW", fam="mono", size=11, weight=500, fill="blue", ls=2.2)
    s.text(W - 32, 42, "6 stages · iterative", fam="mono", size=11, fill="faint", anchor="end", ls=0.6)
    s.line(32, 60.5, W - 32, 60.5, stroke="border")
    xs, rows = [140, 420, 700], [118, 314]
    pos = [(xs[i % 3], rows[i // 3]) for i in range(6)]
    r = 27
    # connectors: row 1 left→right, loop around the right edge, row 2 left→right
    yb = rows[0] + 132
    segs = [f"M{xs[0] + r} {rows[0]}H{xs[1] - r - 4}", f"M{xs[1] + r} {rows[0]}H{xs[2] - r - 4}",
            f"M{xs[2] + r} {rows[0]}H{W - 44}Q{W - 32} {rows[0]} {W - 32} {rows[0] + 12}V{yb - 12}"
            f"Q{W - 32} {yb} {W - 44} {yb}H{xs[0] + 12}Q{xs[0]} {yb} {xs[0]} {yb + 12}V{rows[1] - r - 4}",
            f"M{xs[0] + r} {rows[1]}H{xs[1] - r - 4}", f"M{xs[1] + r} {rows[1]}H{xs[2] - r - 4}"]
    for sg in segs:
        s.add(f'<path d="{sg}" fill="none" stroke="{s.c("border")}" stroke-width="1.6" marker-end="url(#pa)"/>')
    flow = (f"M{xs[0]} {rows[0]}H{W - 44}Q{W - 32} {rows[0]} {W - 32} {rows[0] + 12}V{yb - 12}"
            f"Q{W - 32} {yb} {W - 44} {yb}H{xs[0] + 12}Q{xs[0]} {yb} {xs[0]} {yb + 12}V{rows[1]}H{xs[2]}")
    s.add(f'<circle r="3.2" fill="{s.c("cyan")}"><animateMotion dur="10s" repeatCount="indefinite" path="{flow}"/></circle>')
    for i, ((x, y), (name, desc)) in enumerate(zip(pos, STAGES)):
        s.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{s.c("surface")}" stroke="{s.c("blue")}" stroke-width="1.8"/>')
        s.text(x, y + 6, f"{i + 1:02d}", fam="mono", size=16, weight=500, fill="blue", anchor="middle")
        s.text(x, y + r + 26, name.upper(), fam="mono", size=12.5, weight=500, fill="text", anchor="middle", ls=1.8)
        for j, ln in enumerate(wrap(desc, 214, "sans", 400, 13.5)):
            s.text(x, y + r + 49 + j * 19, ln, size=13.5, fill="muted", anchor="middle")
    s.save(f"{A}/process/engineering-workflow-{th}.svg")


# ------------------------------------------------------------ tech stack
STACK = [
    ("Languages", ["python", "typescript", "javascript", "cplusplus", "#C#"]),
    ("AI & machine learning", ["pytorch", "tensorflow", "keras", "scikitlearn", "pandas", "numpy", "opencv", "#SHAP"]),
    ("LLMs & generative AI", ["huggingface", "langchain", "ollama", "qwen", "#SBERT", "#Whisper", "#Piper"]),
    ("Backend & APIs", ["fastapi", "#WS", "celery", "#REST"]),
    ("Automation & integrations", ["selenium", "#BS4", "#Apify", "googlesheets", "gmail", "githubactions"]),
    ("Databases & vector stores", ["redis", "sqlite", "#Chroma"]),
    ("Frontend, DevOps & tools", ["docker", "git", "react", "vite", "tailwindcss", "vercel", "render", "googlecolab"]),
]
NAMES = {"qwen": "Qwen", "cplusplus": "C++", "scikitlearn": "scikit-learn", "huggingface": "HuggingFace", "googlesheets": "Sheets API",
         "gmail": "SMTP", "githubactions": "Actions", "tailwindcss": "Tailwind", "googlecolab": "Colab",
         "#WS": "WebSockets", "#REST": "REST", "#SBERT": "SBERT", "#BS4": "BS4", "#Whisper": "Whisper",
         "#Piper": "Piper TTS", "#C#": "C#", "#SHAP": "SHAP", "#Apify": "Apify", "#Chroma": "Chroma",
         "javascript": "JavaScript", "typescript": "TypeScript"}


def stack_row(th, idx, title, items):
    s = SVG(W, 118, th, f"Tech stack — {title}",
            f"{title}: " + ", ".join(NAMES.get(i, SI.get(i, {}).get("title", i.strip("#"))) for i in items))
    s.rect(0.5, 0.5, W - 1, 117, rx=12, fill="bg", stroke="border")
    s.text(24, 34, f"{idx:02d}", fam="mono", size=11, weight=500, fill="blue", ls=2)
    for j, ln in enumerate(wrap(title, 150, "sans", 600, 15.5)):
        s.text(24, 58 + j * 20, ln, size=15.5, weight=600, ls=-0.2)
    s.line(190.5, 20, 190.5, 98, stroke="border")
    x = 214
    for it in items:
        s.rect(x + .5, 18.5, 50, 50, rx=11, fill="surface", stroke="border")
        if it.startswith("#"):
            lab = it[1:]
            fs = 14 if len(lab) <= 2 else (12 if len(lab) <= 4 else 10.5)
            s.text(x + 25.5, 43.5 + fs * 0.36, lab, fam="mono", size=fs, weight=500, fill="text", anchor="middle")
        else:
            s.add(f'<path transform="translate({x + 13.5} {31.5})" d="{SI[it]["path"]}" fill="{s.c("text")}"/>')
        name = NAMES.get(it, SI.get(it, {}).get("title", it))
        s.text(x + 25.5, 90, name, fam="mono", size=10.5, fill="muted", anchor="middle")
        x += 76
    s.save(f"{A}/stack/{idx:02d}-{title.split()[0].lower().strip(',')}-{th}.svg")


# ------------------------------------------------------- project visuals
def proj_frame(s, kind, label, right):
    panel(s)
    s.text(28, 36, kind, fam="mono", size=10.5, weight=500, fill="blue", ls=2)
    kx = 28 + measure(kind, "mono", 500, 10.5, 2) + 10
    s.text(kx, 36, f"·  {label}", fam="mono", size=10.5, weight=500, fill="muted", ls=2)
    s.text(W - 28, 36, right, fam="mono", size=10.5, fill="faint", anchor="end", ls=0.4)
    s.line(28, 52.5, W - 28, 52.5, stroke="border")


def box(s, x, y, w, h, title, sub=None, hot=False, tsize=13):
    s.rect(x + .5, y + .5, w, h, rx=9, fill="bluebg" if hot else "surface", stroke="blue" if hot else "border", sw=1.2)
    cy = y + h / 2 + (-4 if sub else 4.5)
    s.text(x + w / 2, cy, title, size=tsize, weight=600, anchor="middle", fill="text")
    if sub:
        s.text(x + w / 2, cy + 18, sub, fam="mono", size=10.5, fill="muted", anchor="middle")


def harrow(s, x1, x2, y, color="faint", mid="pa"):
    s.add(f'<path d="M{x1} {y}H{x2}" stroke="{s.c(color)}" stroke-width="1.4" marker-end="url(#{mid})"/>')


def lead_scraper(th):
    s = SVG(W, 400, th, "Lead Scraping and Outreach Automation — architecture illustration",
            "Illustration: browser control panel → FastAPI (enqueue, status) → Redis broker → Celery worker → Google Sheets. "
            "Scrape pipeline: maps_scraper → enrichment → social_enrichment → cleaning → sheets sync. "
            "Outreach: one send task per lead at +0s, +30s, +60s, writing email_status back to the sheet.")
    proj_frame(s, "ILLUSTRATION", "SYSTEM ARCHITECTURE", "Leads-Scraping-and-Outreach-Automation")
    arrow_marker(s, "muted", "pa")
    arrow_marker(s, "blue", "pb")
    bw, gap, x0, y0 = 136, 24, 32, 78
    boxes = [("Browser", "control panel"), ("FastAPI", "enqueue · status"), ("Redis", "broker + results"),
             ("Celery worker", "runs the job"), ("Google Sheets", "single data store")]
    for i, (t, sub) in enumerate(boxes):
        x = x0 + i * (bw + gap)
        box(s, x, y0, bw, 62, t, sub, hot=(i == 3))
        if i < 4:
            harrow(s, x + bw + 4, x + bw + gap - 4, y0 + 31, "muted")
    s.text(x0 + bw + gap + bw / 2, y0 + 82, "polls /api/task-status", fam="mono", size=10.5, fill="faint", anchor="middle")
    # pipeline
    mono_label(s, 32, 202, "Scrape pipeline", fill="cyan", size=10.5, ls=2)
    stages = [("maps_scraper", "Apify Maps actor"), ("enrichment", "website crawl"),
              ("social_enrichment", "LinkedIn · FB · IG · YT"), ("cleaning", "E.164 · dedupe · rank"),
              ("sheets sync", "new place_ids only")]
    x, y = 32, 216
    widths = [measure(n, "mono", 500, 11.5) + 28 for n, _ in stages]
    total = sum(widths)
    g = (W - 64 - total) / 4
    for i, ((n, sub), w) in enumerate(zip(stages, widths)):
        s.rect(x + .5, y + .5, w, 30, rx=7, fill="surface", stroke="blue" if i == 4 else "border")
        s.text(x + w / 2, y + 20, n, fam="mono", size=11.5, weight=500, fill="text", anchor="middle")
        s.text(x + w / 2, y + 50, sub, fam="sans", size=11.5, fill="muted", anchor="middle")
        if i < 4:
            harrow(s, x + w + 4, x + w + g - 4, y + 15, "muted")
        x += w + g
    # outreach
    mono_label(s, 32, 306, "Outreach · staggered sends", fill="cyan", size=10.5, ls=2)
    ax0, ax1, ay = 40, 600, 350
    s.line(ax0, ay, ax1, ay, stroke="border", sw=1.4)
    for i, lab in enumerate(["+0s", "+30s", "+60s", "+90s", "+120s"]):
        tx = ax0 + 20 + i * 120
        s.line(tx, ay - 6, tx, ay + 6, stroke="faint")
        s.text(tx, ay + 24, lab, fam="mono", size=10.5, fill="muted", anchor="middle")
        s.rect(tx - 13, ay - 34, 26, 18, rx=3, fill="surface", stroke="blue" if i < 3 else "border", sw=1.2)
        s.add(f'<path d="M{tx - 13} {ay - 33}L{tx} {ay - 24}L{tx + 13} {ay - 33}" fill="none" '
              f'stroke="{s.c("blue" if i < 3 else "faint")}" stroke-width="1.2"/>')
    box(s, 640, 316, 168, 56, "email_status = sent", "written back per lead", tsize=12.5)
    harrow(s, 604, 636, ay - 6, "blue", "pb")
    s.save(f"{A}/projects/lead-scraping-{th}.svg")


def tavola(th):
    s = SVG(W, 400, th, "La Bella Tavola conversational assistant — pipeline illustration",
            "Illustration: chat 'Book a table tomorrow' / 'Sure, for how many people?'. Voice in via Faster-Whisper, "
            "regex slot extraction and a finite-state machine, stage-specific prompts, Qwen via Ollama streamed over "
            "WebSockets, Chroma RAG and tools (CRM, menu, weather, SQLite), Piper TTS out.")
    proj_frame(s, "ILLUSTRATION", "TEXT + VOICE PIPELINE", "Conversational-AI")
    arrow_marker(s, "muted", "pa"); arrow_marker(s, "blue", "pb")
    # chat column
    s.rect(28.5, 72.5, 270, 300, rx=12, fill="surface", stroke="border")
    s.text(46, 98, "La Bella Tavola", size=13.5, weight=600)
    s.text(46, 116, "front-desk assistant", fam="mono", size=10.5, fill="muted")
    s.add(f'<circle cx="276" cy="94" r="4" fill="{s.c("cyan")}"/>')
    s.line(29, 130.5, 298, 130.5, stroke="border")
    ut = "Book a table tomorrow"
    uw = measure(ut, "sans", 400, 13) + 26
    s.rect(282 - uw, 146, uw, 34, rx=10, fill="blue")
    s.text(282 - uw + 13, 167.5, ut, size=13, fill="#FFFFFF")
    at = "Sure, for how many people?"
    aw = measure(at, "sans", 400, 13) + 26
    s.rect(44.5, 194.5, aw, 34, rx=10, fill="bg", stroke="border")
    s.text(57, 216, at, size=13, fill="text")
    # voice row
    s.rect(44.5, 252.5, 238, 40, rx=10, fill="bg", stroke="border")
    for i, hgt in enumerate([8, 16, 24, 12, 20, 28, 14, 22, 10, 18, 26, 12, 8]):
        xx = 60 + i * 7
        s.line(xx, 272.5 - hgt / 2, xx, 272.5 + hgt / 2, stroke="cyan", sw=2.2, extra='stroke-linecap="round"')
    s.text(158, 277, "voice input", fam="mono", size=10.5, fill="muted")
    s.text(46, 322, "STAGES", fam="mono", size=10, weight=500, fill="faint", ls=1.8)
    x = 46
    for i, st in enumerate(["collecting", "confirming", "confirmed"]):
        w = chip(s, x, 334, st, fill="cyan" if i == 2 else "muted", size=10)
        x += w + 6
    # pipeline
    bw, gx = 140, 18
    xs = [324, 324 + bw + gx, 324 + 2 * (bw + gx)]
    box(s, xs[0], 78, bw, 58, "Faster-Whisper", "speech → text")
    box(s, xs[1], 78, bw, 58, "Slots + FSM", "regex · stage")
    box(s, xs[2], 78, bw, 58, "Prompt builder", "few-shot · rules")
    harrow(s, xs[0] + bw + 3, xs[1] - 3, 107, "muted"); harrow(s, xs[1] + bw + 3, xs[2] - 3, 107, "muted")
    box(s, xs[1], 196, bw, 66, "Qwen · Ollama", "local LLM · CPU", hot=True)
    s.add(f'<path d="M{xs[2] + bw / 2} 140V170Q{xs[2] + bw / 2} 178 {xs[2] + bw / 2 - 8} 178H{xs[1] + bw / 2 + 8}'
          f'Q{xs[1] + bw / 2} 178 {xs[1] + bw / 2} 186V192" fill="none" stroke="{s.c("muted")}" stroke-width="1.4" marker-end="url(#pa)"/>')
    box(s, xs[2], 196, bw, 66, "Chroma RAG", "+ tool calls")
    harrow(s, xs[2] - 3, xs[1] + bw + 4, 229, "muted")
    box(s, xs[0], 196, bw, 66, "Piper TTS", "text → speech")
    harrow(s, xs[1] - 3, xs[0] + bw + 4, 229, "blue", "pb")
    s.text(xs[2] + bw / 2, 284, "CRM · menu · weather · SQLite", fam="mono", size=10.5, fill="faint", anchor="middle")
    s.add(f'<path d="M{xs[1] + bw / 2} 266V318H{xs[0] - 12}" fill="none" stroke="{s.c("blue")}" stroke-width="1.4" '
          f'stroke-dasharray="4 4" marker-end="url(#pb)"/>')
    s.text(xs[1] + bw / 2 + 12, 344, "token stream over WebSockets → React UI", fam="mono", size=10.5, fill="muted")
    s.text(xs[0], 368, "MAX_TOKENS 250 · stop sequences · 4-turn sliding window", fam="mono", size=10.5, fill="faint")
    s.save(f"{A}/projects/la-bella-tavola-{th}.svg")


def xdl(th):
    s = SVG(W, 400, th, "XDL-IDS CNN-Attention-GRU — model illustration",
            "Illustration: CAN bus frames (ID, DATA_0–DATA_7) flow through Conv1D, multi-head self-attention, GRU and "
            "dense layers to classify normal traffic or DoS/spoofing attacks. Reported results: 100% binary accuracy on "
            "CICIoV2024; ~93–94% binary and ~75% multiclass on the merged CICIoV2024 + Car Hacking dataset.")
    proj_frame(s, "ILLUSTRATION", "MODEL ARCHITECTURE", "CNN-GRU-IDS-Reproduction")
    arrow_marker(s, "muted", "pa"); arrow_marker(s, "blue", "pb")
    # CAN frames
    s.rect(28.5, 72.5, 250, 196, rx=12, fill="surface", stroke="border")
    s.text(44, 96, "CAN BUS FRAMES", fam="mono", size=10, weight=500, fill="faint", ls=1.8)
    s.text(44, 120, "ID    D0 D1 D2 D3 D4 D5 D6 D7", fam="mono", size=10.5, fill="muted", extra='xml:space="preserve"')
    rows = ["0316  05 21 68 09 21 21 00 6F", "018F  FE 5B 00 00 00 3C 00 00", "0000  00 00 00 00 00 00 00 00",
            "02B0  FF 7F 00 00 49 03 05 2E", "0000  00 00 00 00 00 00 00 00", "0153  00 21 10 FF 00 FF 00 00"]
    for i, r in enumerate(rows):
        attack = r.startswith("0000")
        if attack:
            s.rect(38, 126.5 + i * 20, 230, 18, rx=4, fill="cyanbg")
        s.text(44, 140 + i * 20, r, fam="mono", size=10.5, fill="cyan" if attack else "text", extra='xml:space="preserve"')
    s.text(44, 262, "hex → decimal · unified schema", fam="mono", size=10, fill="faint")
    # layers
    layers = [("Conv1D", "local patterns", False), ("Multi-head", "self-attention", True),
              ("GRU", "temporal", False), ("Dense", "softmax", False)]
    lx, lw, lg = 300, 96, 12
    for i, (t, sub, hot) in enumerate(layers):
        x = lx + i * (lw + lg)
        box(s, x, 96, lw, 150, t, sub, hot=hot)
        if hot:
            s.text(x + lw / 2, 88, "ADDED", fam="mono", size=9.5, weight=500, fill="blue", anchor="middle", ls=1.6)
    harrow(s, 282, lx - 4, 171, "muted")
    for i in range(3):
        x = lx + i * (lw + lg) + lw
        harrow(s, x + 2, x + lg - 2, 171, "muted")
    ox = lx + 4 * (lw + lg) - 4
    harrow(s, ox - lg + 6, ox + 6, 171, "blue", "pb")
    for i, (t, hot) in enumerate([("Normal", False), ("DoS", True), ("Spoofing", True)]):
        chip(s, ox + 10, 130 + i * 30, t, fill="cyan" if hot else "muted", size=10.5)
    # results
    mono_label(s, 28, 304, "Reported results", fill="cyan", size=10.5, ls=2)
    tiles = [("100%", "binary · CICIoV2024"), ("~93–94%", "binary · merged data"),
             ("~75%", "multiclass · merged data"), ("DATA_0/1", "top SHAP features")]
    tw = (W - 56 - 3 * 12) / 4
    for i, (v, l) in enumerate(tiles):
        x = 28 + i * (tw + 12)
        s.rect(x + .5, 318.5, tw, 58, rx=10, fill="surface", stroke="border")
        s.text(x + 16, 346, v, size=19, weight=600, fill="blue" if i == 0 else "text", ls=-0.3)
        s.text(x + 16, 366, l, fam="mono", size=10.5, fill="muted")
    s.save(f"{A}/projects/xdl-ids-{th}.svg")


def zameen(th, shot):
    from PIL import Image
    im = Image.open(shot).convert("RGB")
    iw = W - 56
    ih = round(im.height * iw / im.width)
    im = im.resize((iw * 2, ih * 2), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=72, optimize=True, progressive=True)
    b64 = base64.b64encode(buf.getvalue()).decode()
    H = 72 + ih + 28
    s = SVG(W, H, th, "Zameen Intelligence Platform — dashboard screenshot",
            "Screenshot of the live Lead Dashboard: KPI cards (total leads, today's listings, average lead score, "
            "average price, price per square foot, verified agencies), top locations by volume, market segment "
            "distribution and highest-scored leads.")
    proj_frame(s, "SCREENSHOT", "LIVE DASHBOARD", "b2-b-lead-intelligence-platform.vercel.app")
    s.defs.append(f'<clipPath id="sc"><rect x="28" y="72" width="{iw}" height="{ih}" rx="8"/></clipPath>')
    s.add(f'<image x="28" y="72" width="{iw}" height="{ih}" clip-path="url(#sc)" '
          f'href="data:image/jpeg;base64,{b64}" preserveAspectRatio="xMidYMid slice"/>')
    s.rect(28.5, 72.5, iw - 1, ih - 1, rx=8, fill="none", stroke="border")
    s.save(f"{A}/projects/zameen-dashboard-{th}.svg")


# --------------------------------------------------------------- connect
def connect(th):
    s = SVG(W, 210, th, "Let's build something useful",
            "Closing panel: open to collaborations and conversations about applied AI, LLM systems and automation.")
    panel(s)
    s.text(40, 52, "OPEN TO COLLABORATION", fam="mono", size=11, weight=500, fill="blue", ls=2.2)
    s.text(38, 100, "Let's build something useful.", size=32, weight=600, ls=-0.8)
    s.text(40, 134, "Collaborations and conversations about applied AI,", size=15, fill="muted")
    s.text(40, 156, "LLM systems and automation are always welcome.", size=15, fill="muted")
    s.text(40, 188, "FAST-NUCES · ISLAMABAD", fam="mono", size=10.5, fill="faint", ls=1.8)
    # node line motif
    pts = [(560, 150), (620, 98), (690, 132), (750, 70), (800, 110)]
    d = "M" + "L".join(f"{x} {y}" for x, y in pts)
    s.add(f'<path d="{d}" fill="none" stroke="{s.c("border")}" stroke-width="1.5"/>')
    for i, (x, y) in enumerate(pts):
        last = i == len(pts) - 1
        s.rect(x - 5, y - 5, 10, 10, rx=2.5, fill="cyan" if last else "bg", stroke="cyan" if last else "blue", sw=1.5)
    s.add(f'<circle r="3" fill="{s.c("cyan")}"><animateMotion dur="5s" repeatCount="indefinite" path="{d}"/></circle>')
    s.save(f"{A}/decorations/connect-{th}.svg")


# Non-blank source lines per language across hamdulhaq27's public repositories
# (B2B-Lead-Intelligence-Platform, CNN-GRU-IDS-Reproduction, Conversational-AI,
# Leads-Scraping-and-Outreach-Automation, Stock-Sense-AI-Trade-Bot, Street-Fighter-AI-Bot,
# Transport-Management-System). Notebook code cells count as Python; dependencies,
# data, build output and generated designer files are excluded. Re-measure to update.
LANGS = [("Python", 12509), ("TypeScript", 7657), ("HTML", 1013), ("C#", 795),
         ("CSS", 498), ("JavaScript", 245), ("PowerShell", 123)]
LANG_SCOPE = "7 public repos · lines of code · Nov 2026"
LANG_COLORS = {
    "dark": ["#3B82F6", "#38BDD8", "#7C8BA6", "#5E6C84", "#4A5568", "#3A4454", "#2E3644"],
    "light": ["#2563EB", "#0E8FAD", "#7D8AA0", "#9AA5B6", "#B4BDCA", "#C9D0DA", "#DCE1E8"],
}


def languages(th):
    total = sum(v for _, v in LANGS)
    pct = [(n, 100 * v / total) for n, v in LANGS]
    s = SVG(W, 212, th, "Most used languages",
            "Most used languages by lines of code across 7 public repositories: "
            + ", ".join(f"{n} {p:.1f}%" for n, p in pct))
    panel(s)
    cols = LANG_COLORS[th]
    s.text(32, 42, "MOST USED LANGUAGES", fam="mono", size=11, weight=500, fill="blue", ls=2.2)
    s.text(W - 32, 42, LANG_SCOPE, fam="mono", size=11, fill="faint", anchor="end", ls=0.4)
    s.line(32, 60.5, W - 32, 60.5, stroke="border")
    # stacked bar
    bx, bw, by, bh = 32, W - 64, 84, 12
    s.defs.append(f'<clipPath id="bar"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="6"/></clipPath>')
    x, segs = bx, []
    for i, (n, p) in enumerate(pct):
        w = bw * p / 100
        segs.append(f'<rect x="{x:.2f}" y="{by}" width="{w + 0.6:.2f}" height="{bh}" fill="{cols[i]}"/>')
        x += w
    s.add('<g clip-path="url(#bar)">' + "".join(segs) + "</g>")
    # legend: 4 columns
    cw = (W - 64) / 4
    for i, (n, p) in enumerate(pct):
        cx = 32 + (i % 4) * cw
        cy = 132 + (i // 4) * 40
        s.rect(cx, cy - 10, 10, 10, rx=2.5, fill=cols[i])
        s.text(cx + 20, cy, n, size=14.5, weight=600 if i < 2 else 400, fill="text" if i < 2 else "muted")
        s.text(cx + cw - 24, cy, f"{p:.1f}%", fam="mono", size=12.5, fill="text" if i < 2 else "muted", anchor="end")
    s.save(f"{A}/analytics/languages-{th}.svg")


def build_rest(both):
    both(languages)
    both(timeline)
    both(process)
    for i, (t, items) in enumerate(STACK, 1):
        both(stack_row, i, t, items)
    both(lead_scraper)
    both(tavola)
    both(xdl)
    shot = os.path.join(os.path.dirname(os.path.abspath(__file__)), "zameen-dashboard.png")
    both(zameen, shot)
    both(connect)
