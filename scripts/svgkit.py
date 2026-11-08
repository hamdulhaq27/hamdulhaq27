"""Tiny SVG toolkit for the profile design system.

Every SVG embeds only the glyphs it uses (Inter + JetBrains Mono subsets, OFL)
so typography renders identically on GitHub without external requests.
"""
import base64, io, html, os
from fontTools.ttLib import TTFont
from fontTools import subset as ftsubset

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(HERE, "fonts")

THEMES = {
    "dark": dict(
        bg="#0B0E14", surface="#131922", border="#232C38", grid="#151B24",
        text="#E6EAF0", muted="#8A94A6", faint="#4A5466",
        blue="#3B82F6", cyan="#38BDD8", bluebg="#14213A", cyanbg="#0F2A33",
    ),
    "light": dict(
        bg="#F7F9FC", surface="#FFFFFF", border="#D8DFE9", grid="#EAEFF5",
        text="#0E1621", muted="#566173", faint="#9AA4B2",
        blue="#2563EB", cyan="#0E8FAD", bluebg="#E6EEFD", cyanbg="#E3F4F8",
    ),
}

FONTS = {
    ("sans", 400): "inter-400.woff2", ("sans", 500): "inter-500.woff2", ("sans", 600): "inter-600.woff2",
    ("mono", 400): "jbm-400.woff2", ("mono", 500): "jbm-500.woff2",
}
_tt = {}
def _font(key):
    if key not in _tt:
        _tt[key] = TTFont(os.path.join(FONT_DIR, FONTS[key]))
    return _tt[key]

def measure(txt, fam="sans", weight=400, size=14, ls=0.0):
    f = _font((fam, weight)); cmap = f.getBestCmap(); hmtx = f["hmtx"]; upm = f["head"].unitsPerEm
    w = 0
    for ch in txt:
        g = cmap.get(ord(ch))
        w += hmtx[g][0] if g else upm * 0.5
    return w * size / upm + ls * max(len(txt) - 1, 0)

def wrap(txt, maxw, fam="sans", weight=400, size=14):
    words, lines, cur = txt.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if measure(t, fam, weight, size) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines

def esc(s):
    return html.escape(s, quote=True)


class SVG:
    def __init__(self, w, h, theme, title, desc=""):
        self.w, self.h, self.t, self.theme = w, h, THEMES[theme], theme
        self.title, self.desc = title, desc
        self.els, self.defs, self.css = [], [], []
        self.chars = {}

    def c(self, name):
        return self.t.get(name, name)

    def add(self, s):
        self.els.append(s); return self

    def rect(self, x, y, w, h, rx=0, fill="none", stroke=None, sw=1, extra=""):
        st = f' stroke="{self.c(stroke)}" stroke-width="{sw}"' if stroke else ""
        return self.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{self.c(fill)}"{st} {extra}/>')

    def line(self, x1, y1, x2, y2, stroke="border", sw=1, extra=""):
        return self.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{self.c(stroke)}" stroke-width="{sw}" {extra}/>')

    def text(self, x, y, txt, fam="sans", size=14, weight=400, fill="text", anchor="start", ls=0, extra="", raw=False):
        self.chars.setdefault((fam, weight), set()).update(txt)
        cls = f"{'s' if fam == 'sans' else 'm'}{weight}"
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        l = f' letter-spacing="{ls}"' if ls else ""
        body = txt if raw else esc(txt)
        return self.add(f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" fill="{self.c(fill)}"{a}{l} {extra}>{body}</text>')

    def text_el(self, x, y, txt, fam="sans", size=14, weight=400, fill="text", anchor="start", ls=0, extra=""):
        """Return a text element string (not added) — for nesting in groups."""
        self.chars.setdefault((fam, weight), set()).update(txt)
        cls = f"{'s' if fam == 'sans' else 'm'}{weight}"
        a = f' text-anchor="{anchor}"' if anchor != "start" else ""
        l = f' letter-spacing="{ls}"' if ls else ""
        return f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" fill="{self.c(fill)}"{a}{l} {extra}>{esc(txt)}</text>'

    def _font_css(self):
        out = []
        for (fam, weight), chars in sorted(self.chars.items()):
            f = TTFont(os.path.join(FONT_DIR, FONTS[(fam, weight)]))
            opts = ftsubset.Options(); opts.flavor = "woff2"; opts.layout_features = ["kern", "liga", "calt", "tnum", "cv05"]
            opts.name_IDs = []; opts.notdef_outline = True
            sub = ftsubset.Subsetter(opts)
            sub.populate(text="".join(chars) + " ")
            sub.subset(f)
            buf = io.BytesIO(); f.flavor = "woff2"; f.save(buf)
            b64 = base64.b64encode(buf.getvalue()).decode()
            fname = f"{'HI' if fam == 'sans' else 'HM'}{weight}"
            stack = ("-apple-system,'Segoe UI',Helvetica,Arial,sans-serif" if fam == "sans"
                     else "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace")
            out.append(f"@font-face{{font-family:'{fname}';src:url(data:font/woff2;base64,{b64}) format('woff2');}}")
            out.append(f".{'s' if fam == 'sans' else 'm'}{weight}{{font-family:'{fname}',{stack};font-weight:{weight};{"font-feature-settings:'cv05' 1;" if fam == "sans" else ""}}}")
        return "".join(out)

    def render(self):
        css = self._font_css() + "".join(self.css)
        tid = "t-" + self.title[:12].replace(" ", "")
        parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{self.h}" viewBox="0 0 {self.w} {self.h}" role="img" aria-labelledby="title desc">',
            f"<title id=\"title\">{esc(self.title)}</title><desc id=\"desc\">{esc(self.desc or self.title)}</desc>",
            f"<style>{css}</style>",
        ]
        if self.defs:
            parts.append("<defs>" + "".join(self.defs) + "</defs>")
        parts += self.els
        parts.append("</svg>")
        return "".join(parts)

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(self.render())
