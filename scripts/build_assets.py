"""Generates every core visual asset for the profile README (dark + light).

Usage:  python scripts/build_assets.py [output_root]
"""
import json, os, sys, base64, io
from svgkit import SVG, measure, wrap, esc, THEMES
from icons_custom import icon

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..")
A = os.path.join(OUT, "assets")
SI = json.load(open(os.path.join(HERE, "icons.json")))
W = 840


def both(fn, *args, **kw):
    for th in ("dark", "light"):
        fn(th, *args, **kw)


def panel(s, h=None, rx=14):
    s.rect(0.5, 0.5, s.w - 1, (h or s.h) - 1, rx=rx, fill="bg", stroke="border")


def mono_label(s, x, y, txt, fill="muted", size=11, ls=2.0, anchor="start"):
    s.text(x, y, txt.upper(), fam="mono", size=size, weight=500, fill=fill, ls=ls, anchor=anchor)


def chip(s, x, y, txt, fill="muted", stroke="border", bg="surface", size=10.5, h=22, pad=9):
    w = measure(txt, "mono", 400, size) + pad * 2
    s.rect(x + .5, y + .5, w, h, rx=5, fill=bg, stroke=stroke)
    s.text(x + .5 + w / 2, y + h / 2 + size * 0.36 + .5, txt, fam="mono", size=size, fill=fill, anchor="middle")
    return w


def arrow_marker(s, color_key, mid="a"):
    s.defs.append(f'<marker id="{mid}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" '
                  f'orient="auto-start-reverse"><path d="M1 1.5L8 5 1 8.5" fill="none" stroke="{s.c(color_key)}" '
                  f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></marker>')


# --------------------------------------------------------------------- hero
PHRASES = ["AI Engineer", "Machine Learning Developer", "Building Intelligent Systems",
           "AI Automation Engineer", "Exploring LLMs and Applied AI"]


def hero(th):
    s = SVG(W, 330, th, "Hamd Ul Haq — AI Engineer",
            "Animated header: Hamd Ul Haq, BS Artificial Intelligence at FAST-NUCES Islamabad. Typewriter cycles: "
            + ", ".join(PHRASES) + ". A small system graph links data, model, RAG, API, agent and deploy nodes.")
    panel(s)
    # grid on the right
    s.defs.append('<clipPath id="gc"><rect x="520" y="1" width="318" height="328" rx="13"/></clipPath>')
    g = [f'<path d="M{x} 0V330" />' for x in range(528, 840, 24)] + [f'<path d="M520 {y}H840" />' for y in range(18, 330, 24)]
    s.add(f'<g clip-path="url(#gc)" stroke="{s.c("grid")}" stroke-width="1">{"".join(g)}</g>')
    s.line(520, 1, 520, 329, stroke="border")
    # system graph
    N = {"data": (572, 90), "clean": (572, 234), "model": (668, 62), "rag": (668, 162),
         "api": (668, 266), "agent": (770, 112), "deploy": (770, 226)}
    E = [("data", "model"), ("data", "rag"), ("clean", "rag"), ("clean", "api"), ("model", "agent"),
         ("rag", "agent"), ("rag", "deploy"), ("api", "deploy"), ("agent", "deploy")]
    hot = {("data", "rag"), ("rag", "agent"), ("agent", "deploy")}
    for a, b in E:
        (x1, y1), (x2, y2) = N[a], N[b]
        s.line(x1, y1, x2, y2, stroke="blue" if (a, b) in hot else "border", sw=1.5 if (a, b) in hot else 1)
    hotn = {"data", "rag", "agent", "deploy"}
    for k, (x, y) in N.items():
        s.rect(x - 6, y - 6, 12, 12, rx=3, fill="bg", stroke="blue" if k in hotn else "faint", sw=1.5)
        if k == "agent":
            s.rect(x - 2.5, y - 2.5, 5, 5, rx=1, fill="cyan")
        s.text(x + 12, y + 4, k, fam="mono", size=10.5, fill="text" if k in hotn else "muted")
    s.add(f'<circle r="3" fill="{s.c("cyan")}"><animateMotion dur="4.8s" repeatCount="indefinite" '
          f'path="M572 90L668 162L770 112L770 226" keyPoints="0;1" keyTimes="0;1" calcMode="linear"/>'
          f'<animate attributeName="opacity" values="0;1;1;0" keyTimes="0;0.08;0.9;1" dur="4.8s" repeatCount="indefinite"/></circle>')
    # left copy
    s.rect(48, 50, 7, 7, rx=1.5, fill="blue")
    mono_label(s, 64, 57, "BS Artificial Intelligence  ·  FAST-NUCES Islamabad", ls=1.8)
    s.text(45, 138, "Hamd Ul Haq", size=58, weight=600, ls=-1.6)
    # typewriter
    size, x0, y = 22, 48, 194
    cw = size * 0.6
    s.text(x0, y, ">", fam="mono", size=size, fill="cyan")
    px = x0 + 2 * cw
    tc, hold, td, gap = 0.07, 1.9, 0.032, 0.5
    starts, t = [], 0.4
    for p in PHRASES:
        starts.append(t)
        t += len(p) * tc + hold + len(p) * td + gap
    T = round(t, 3)
    cursor = [(0.0, 0.0)]
    for i, p in enumerate(PHRASES):
        n, st = len(p), starts[i]
        ev = [(0.0, 0.0)]
        for k in range(1, n + 1):
            ev.append((st + k * tc, k * cw))
        dstart = st + n * tc + hold
        for k in range(1, n + 1):
            ev.append((dstart + k * td, (n - k) * cw))
        cursor += ev[1:]
        kt = ";".join(f"{e[0] / T:.5f}" for e in ev)
        vals = ";".join(f"{e[1]:.2f}" for e in ev)
        s.defs.append(f'<clipPath id="tw{i}"><rect x="{px}" y="{y - 22}" height="30" width="0">'
                      f'<animate attributeName="width" values="{vals}" keyTimes="{kt}" dur="{T}s" calcMode="discrete" repeatCount="indefinite"/>'
                      f'</rect></clipPath>')
        s.add(s.text_el(px, y, p, fam="mono", size=size, fill="text", extra=f'clip-path="url(#tw{i})"'))
    cursor.sort()
    kt = ";".join(f"{e[0] / T:.5f}" for e in cursor)
    vals = ";".join(f"{e[1]:.2f}" for e in cursor)
    s.add(f'<rect x="{px + 1}" y="{y - 18}" width="{cw - 2:.1f}" height="22" rx="1" fill="{s.c("blue")}">'
          f'<animate attributeName="x" values="{";".join(f"{px + 1 + float(v):.2f}" for v in vals.split(";"))}" keyTimes="{kt}" dur="{T}s" calcMode="discrete" repeatCount="indefinite"/>'
          f'<animate attributeName="opacity" values="1;0.15" keyTimes="0;0.5" dur="1.05s" calcMode="discrete" repeatCount="indefinite"/></rect>')
    s.line(48, 236.5, 480, 236.5, stroke="border")
    s.line(48, 236.5, 96, 236.5, stroke="blue", sw=2)
    mono_label(s, 48, 272, "LLM apps · RAG · Voice AI · Automation · ML pipelines", size=11, ls=1.4)
    s.save(f"{A}/hero/hero-{th}.svg")


# ---------------------------------------------------------- section headers
SECTIONS = [
    ("02", "About", "Practical AI, built end to end"),
    ("03", "Journey", "Professional journey"),
    ("04", "Capabilities", "What I build"),
    ("05", "Stack", "Tech stack"),
    ("06", "Projects", "Featured projects"),
    ("07", "Analytics", "GitHub analytics"),
    ("08", "Process", "Engineering process"),
    ("09", "Focus", "Currently exploring"),
    ("10", "Connect", "Connect"),
]


def section_header(th, num, label, title):
    s = SVG(W, 78, th, f"{num} — {title}", f"Section {num}: {title}")
    s.text(0, 18, num, fam="mono", size=11.5, weight=500, fill="blue", ls=2)
    x = measure(num, "mono", 500, 11.5, 2) + 12
    mono_label(s, x, 18, f"—  {label}", size=11.5, ls=2.2)
    s.text(W, 18, f"{num} / {len(SECTIONS) + 1:02d}", fam="mono", size=11, fill="faint", anchor="end", ls=1.5)
    s.text(-1, 56, title, size=28, weight=600, ls=-0.5)
    s.line(0, 76.5, W, 76.5, stroke="border")
    s.line(0, 76, 56, 76, stroke="blue", sw=2)
    s.rect(W - 5, 73, 5, 5, rx=1, fill="cyan")
    s.save(f"{A}/decorations/section-{num}-{th}.svg")


# ------------------------------------------------------------ label chips
def label_chip(th, name, txt):
    w = measure(txt.upper(), "mono", 500, 11, 1.8) + 34
    s = SVG(int(w) + 2, 26, th, txt, f"Label: {txt}")
    s.rect(0.5, 0.5, w, 25, rx=6, fill="surface", stroke="border")
    s.rect(11, 10, 6, 6, rx=1.5, fill="blue")
    s.text(24, 17.2, txt.upper(), fam="mono", size=11, weight=500, fill="text", ls=1.8)
    s.save(f"{A}/decorations/label-{name}-{th}.svg")


# ------------------------------------------------- capability / focus heads
def card_head(th, folder, name, num, label, title, ic):
    s = SVG(400, 84, th, f"{num} — {title}", f"{label}: {title}")
    s.rect(0.5, 0.5, 52, 52, rx=11, fill="surface", stroke="border")
    s.add(icon(ic, 14.5, 14.5, 24, s.c("blue")))
    s.text(70, 19, num, fam="mono", size=11, weight=500, fill="cyan", ls=1.8)
    mono_label(s, 70 + measure(num, "mono", 500, 11, 1.8) + 10, 19, label, size=11, ls=1.8)
    s.text(69, 45, title, size=19, weight=600, ls=-0.3)
    s.line(0, 82.5, 400, 82.5, stroke="border")
    s.line(0, 82, 32, 82, stroke="blue", sw=2)
    s.save(f"{A}/{folder}/{name}-{th}.svg")


def focus_head(th, name, num, label, title, ic):
    s = SVG(280, 124, th, f"{num} — {title}", f"{label}: {title}")
    s.rect(0.5, 0.5, 46, 46, rx=10, fill="surface", stroke="border")
    s.add(icon(ic, 12, 12, 23, s.c("blue")))
    s.text(62, 28, num, fam="mono", size=11, weight=500, fill="cyan", ls=1.8)
    mono_label(s, 62 + measure(num, "mono", 500, 11, 1.8) + 10, 28, label, size=11, ls=1.8)
    for i, ln in enumerate(wrap(title, 270, "sans", 600, 19)):
        s.text(-1, 80 + i * 24, ln, size=19, weight=600, ls=-0.3)
    s.line(0, 122.5, 280, 122.5, stroke="border")
    s.line(0, 122, 32, 122, stroke="blue", sw=2)
    s.save(f"{A}/focus/{name}-{th}.svg")


CAPS = [
    ("ml", "01", "AI & ML", "Models that predict and detect", "ml"),
    ("llm", "02", "LLM apps", "Assistants, RAG and tool use", "llm"),
    ("automation", "03", "Automation", "Pipelines that run themselves", "automation"),
    ("backend", "04", "Backend", "APIs, queues and streaming", "backend"),
    ("data", "05", "Data", "Scraping, enrichment, cleaning", "data"),
    ("systems", "06", "Systems", "Models wired into products", "systems"),
]
FOCUS = [
    ("agentic", "A", "Exploring", "Agentic AI architectures", "agent"),
    ("voice", "B", "Exploring", "Voice and conversational AI", "voice"),
    ("mlops", "C", "Exploring", "MLOps and production ML", "mlops"),
]


# ------------------------------------------------------------- buttons
def button(th, name, label, ic):
    tw = measure(label.upper(), "mono", 500, 11.5, 1.6)
    w = int(14 + 18 + 10 + tw + 14 + 12 + 14)
    s = SVG(w + 1, 42, th, label, f"Button: {label}")
    s.rect(0.5, 0.5, w, 41, rx=9, fill="surface", stroke="border")
    s.add(icon(ic, 14, 12, 18, s.c("blue")))
    s.text(42, 25.5, label.upper(), fam="mono", size=11.5, weight=500, fill="text", ls=1.6)
    s.add(icon("arrow", w - 26, 15, 12, s.c("muted"), sw=1.6))
    s.save(f"{A}/buttons/{name}-{th}.svg")


# ------------------------------------------------------------- divider
def divider(th):
    s = SVG(W, 28, th, "Divider", "Section divider")
    s.line(0, 14.5, W / 2 - 20, 14.5, stroke="border")
    s.line(W / 2 + 20, 14.5, W, 14.5, stroke="border")
    s.rect(W / 2 - 4, 10.5, 8, 8, rx=1.5, fill="none", stroke="blue", sw=1.5)
    s.rect(W / 2 - 15, 13.5, 2, 2, fill="faint")
    s.rect(W / 2 + 13, 13.5, 2, 2, fill="faint")
    s.save(f"{A}/decorations/divider-{th}.svg")


if __name__ == "__main__":
    from build_assets_2 import build_rest
    both(hero)
    for n, l, t in SECTIONS:
        both(section_header, n, l, t)
    for k, t in [("focus", "Focus"), ("interests", "Interests"), ("approach", "Approach"), ("domains", "Domains")]:
        both(label_chip, k, t)
    for name, num, label, title, ic in CAPS:
        both(card_head, "capabilities", name, num, label, title, ic)
    for name, num, label, title, ic in FOCUS:
        both(focus_head, name, num, label, title, ic)
    for name, label, ic in [("linkedin", "LinkedIn", "linkedin"), ("github", "GitHub", "github"),
                            ("repo", "Repository", "code"), ("demo", "Live demo", "play")]:
        both(button, name, label, ic)
    both(divider)
    build_rest(both)
    print("assets written to", A)
