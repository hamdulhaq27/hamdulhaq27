"""Expands README.tpl.md macros into README.md.

[[pic:path|alt|width]]   theme-aware <picture> for assets/<path>-{dark,light}.svg
[[btn:name|url|label]]   linked button (assets/buttons/<name>-{dark,light}.svg)
[[ext:key|alt]]          theme-aware live-data card from a third-party service
"""
import re, sys, os
from urllib.parse import urlencode

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..")
USER = "hamdulhaq27"
PAL = {
    "dark": dict(bg="0B0E14", title="E6EAF0", text="8A94A6", icon="3B82F6", ring="38BDD8", border="232C38", line="3B82F6", point="38BDD8"),
    "light": dict(bg="F7F9FC", title="0E1621", text="566173", icon="2563EB", ring="0E8FAD", border="D8DFE9", line="2563EB", point="0E8FAD"),
}


def ext_url(key, th):
    p = PAL[th]
    if key == "stats":
        q = dict(username=USER, show_icons="true", include_all_commits="true", rank_icon="github", border_radius=12,
                 bg_color=p["bg"], title_color=p["title"], text_color=p["text"], icon_color=p["icon"],
                 ring_color=p["ring"], border_color=p["border"], custom_title="GitHub overview")
        return "https://github-readme-stats.vercel.app/api?" + urlencode(q)
    if key == "langs":
        q = dict(username=USER, layout="compact", langs_count=8, border_radius=12, bg_color=p["bg"],
                 title_color=p["title"], text_color=p["text"], border_color=p["border"], custom_title="Most used languages")
        return "https://github-readme-stats.vercel.app/api/top-langs/?" + urlencode(q)
    if key == "streak":
        q = dict(user=USER, background=p["bg"], border=p["border"], stroke=p["border"], ring=p["icon"], fire=p["ring"],
                 currStreakNum=p["title"], sideNums=p["title"], currStreakLabel=p["icon"], sideLabels=p["text"],
                 dates=p["text"], border_radius=12, date_format="M j[, Y]")
        return "https://streak-stats.demolab.com/?" + urlencode(q)
    if key == "activity":
        q = dict(username=USER, bg_color=p["bg"], color=p["text"], title_color=p["title"], line=p["line"],
                 point=p["point"], area="true", area_color=p["line"], hide_border="false", radius=12,
                 custom_title="Contribution activity — last 31 days")
        return "https://github-readme-activity-graph.vercel.app/graph?" + urlencode(q)
    raise KeyError(key)


def picture(dark, light, alt, width=None):
    w = f' width="{width}"' if width else ""
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{dark}">'
            f'<source media="(prefers-color-scheme: light)" srcset="{light}">'
            f'<img src="{dark}" alt="{alt}"{w}></picture>')


def expand(tpl):
    def pic(m):
        path, alt, width = m.group(1).split("|")
        return picture(f"assets/{path}-dark.svg", f"assets/{path}-light.svg", alt.replace('"', "&quot;"), width or None)

    def btn(m):
        name, url, label = m.group(1).split("|")
        return f'<a href="{url}">' + picture(f"assets/buttons/{name}-dark.svg", f"assets/buttons/{name}-light.svg", label) + "</a>"

    def ext(m):
        key, alt = m.group(1).split("|")
        width = ""
        return picture(ext_url(key, "dark").replace("&", "&amp;"), ext_url(key, "light").replace("&", "&amp;"), alt).replace(
            f'alt="{alt}">', f'alt="{alt}"{width}>')

    tpl = re.sub(r"\[\[pic:(.+?)\]\]", pic, tpl)
    tpl = re.sub(r"\[\[btn:(.+?)\]\]", btn, tpl)
    tpl = re.sub(r"\[\[ext:(.+?)\]\]", ext, tpl)
    return tpl


if __name__ == "__main__":
    src = open(os.path.join(HERE, "README.tpl.md"), encoding="utf-8").read()
    open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write(expand(src))
    print("README.md written")
