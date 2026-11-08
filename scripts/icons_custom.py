"""Custom line icons on a 24px grid. One style: 1.6 stroke, round caps, no fills."""

ICONS = {
    "ml": '<path d="M5 6.5L12 4M5 6.5L12 12M5 17.5L12 12M5 17.5L12 20M12 4L19 9M12 12L19 9M12 12L19 15M12 20L19 15"/>'
          '<circle cx="5" cy="6.5" r="1.9"/><circle cx="5" cy="17.5" r="1.9"/><circle cx="12" cy="4" r="1.9"/>'
          '<circle cx="12" cy="12" r="1.9"/><circle cx="12" cy="20" r="1.9"/><circle cx="19" cy="9" r="1.9"/><circle cx="19" cy="15" r="1.9"/>',
    "llm": '<path d="M4 5.5A1.5 1.5 0 0 1 5.5 4h13A1.5 1.5 0 0 1 20 5.5v9a1.5 1.5 0 0 1-1.5 1.5H10l-4.5 4v-4h0A1.5 1.5 0 0 1 4 14.5z"/>'
           '<path d="M8.5 10h0M12 10h0M15.5 10h0" stroke-width="2.4"/>',
    "automation": '<rect x="3" y="3.5" width="7" height="6" rx="1.5"/><rect x="14" y="14.5" width="7" height="6" rx="1.5"/>'
                  '<path d="M10 6.5h4.5a3 3 0 0 1 3 3V14.5"/><path d="M15.5 12.5l2 2 2-2"/><path d="M3 17.5h7M7.5 15l2.5 2.5L7.5 20"/>',
    "backend": '<rect x="4" y="4" width="16" height="6.5" rx="1.5"/><rect x="4" y="13.5" width="16" height="6.5" rx="1.5"/>'
               '<path d="M7.5 7.25h0M7.5 16.75h0" stroke-width="2.4"/><path d="M11 7.25h5.5M11 16.75h5.5"/>',
    "data": '<ellipse cx="12" cy="5.5" rx="7" ry="2.5"/><path d="M5 5.5v13c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5v-13"/>'
            '<path d="M5 12c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5"/>',
    "systems": '<circle cx="12" cy="12" r="3"/><circle cx="4.5" cy="4.5" r="1.9"/><circle cx="19.5" cy="4.5" r="1.9"/>'
               '<circle cx="4.5" cy="19.5" r="1.9"/><circle cx="19.5" cy="19.5" r="1.9"/>'
               '<path d="M6 6l3.8 3.8M18 6l-3.8 3.8M6 18l3.8-3.8M18 18l-3.8-3.8"/>',
    "agent": '<circle cx="12" cy="12" r="3"/><ellipse cx="12" cy="12" rx="9" ry="4" transform="rotate(-30 12 12)"/>'
             '<circle cx="19.2" cy="7.4" r="1.6"/>',
    "voice": '<path d="M4 10v4M8 7v10M12 4v16M16 8v8M20 10.5v3"/>',
    "mlops": '<path d="M7.2 8.5a3.5 3.5 0 1 0 0 7c2.3 0 3.3-1.8 4.8-3.5s2.5-3.5 4.8-3.5a3.5 3.5 0 1 1 0 7c-2.3 0-3.3-1.8-4.8-3.5S9.5 8.5 7.2 8.5z"/>',
    "globe": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.4 2.4 3.5 5.2 3.5 8.5s-1.1 6.1-3.5 8.5c-2.4-2.4-3.5-5.2-3.5-8.5S9.6 5.9 12 3.5z"/>',
    "linkedin": '<rect x="3" y="3" width="18" height="18" rx="3"/><path d="M8 10.5v6M8 7.5v.01M11.5 16.5v-6M11.5 13a2.5 2.5 0 0 1 5 0v3.5"/>',
    "github": '<path d="M9 19c-4.3 1.4-4.3-2.5-6-3m12 5v-3.5c0-1 .1-1.4-.5-2 2.8-.3 5.5-1.4 5.5-6a4.6 4.6 0 0 0-1.3-3.2 4.2 4.2 0 0 0-.1-3.2s-1.1-.3-3.5 1.3a12.3 12.3 0 0 0-6.2 0C6.5 2.8 5.4 3.1 5.4 3.1a4.2 4.2 0 0 0-.1 3.2A4.6 4.6 0 0 0 4 9.5c0 4.6 2.7 5.7 5.5 6-.6.6-.6 1.2-.5 2V21"/>',
    "code": '<path d="M8 8l-4 4 4 4M16 8l4 4-4 4M13.5 5l-3 14"/>',
    "play": '<rect x="3" y="4.5" width="18" height="15" rx="2"/><path d="M10 9.5v5l4.5-2.5z"/>',
    "doc": '<path d="M6 3.5h8l4 4v13H6z"/><path d="M14 3.5v4h4M9 12h6M9 15.5h6"/>',
    "arrow":'<path d="M7 17L17 7M9 7h8v8"/>',
}


def icon(name, x, y, size, color, sw=1.6):
    s = size / 24
    return (f'<g transform="translate({x} {y}) scale({s})" fill="none" stroke="{color}" '
            f'stroke-width="{sw / s:.3f}" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')
