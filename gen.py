# Stop stalking the code weirdo
NAME, DUR, CW, X0 = "Freakah", 8, 40, 80
THEMES = {
    "dark": dict(bg="#0d1117", border="#30363d", text="#e6edf3", muted="#7d8590", accent="#58a6ff"),
    "light": dict(bg="#ffffff", border="#d0d7de", text="#1f2328", muted="#656d76", accent="#0969da"),
}
n = len(NAME)
appear = [(0.4 + 0.16 * i) / DUR for i in range(n)]
erase = [(6.2 + 0.06 * (n - 1 - i)) / DUR for i in range(n)]
cur = [(0, X0)] + [(appear[i], X0 + CW * (i + 1)) for i in range(n)]
cur += [(erase[i], X0 + CW * i) for i in reversed(range(n))] + [(1, X0)]
times = [t for t, _ in cur]
assert times == sorted(times) and times[-1] == 1, times

def svg(c):
    chars = "\n".join(
        f'    <text x="{X0 + CW * i}" y="140" fill="{c["text"]}" opacity="0">{ch}'
        f'<animate attributeName="opacity" values="0;0;1;1;0;0" '
        f'keyTimes="0;{appear[i]:.4f};{appear[i]:.4f};{erase[i]:.4f};{erase[i]:.4f};1" '
        f'dur="{DUR}s" repeatCount="indefinite"/></text>'
        for i, ch in enumerate(NAME)
    )
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="260" viewBox="0 0 1200 260">
  <rect x="1" y="1" width="1198" height="258" rx="14" fill="{c["bg"]}" stroke="{c["border"]}"/>
  <rect x="1" y="1" width="1198" height="258" rx="14" fill="none" stroke="{c["accent"]}" stroke-width="2" stroke-linecap="round" stroke-dasharray="220 2700">
    <animate attributeName="stroke-dashoffset" from="0" to="-2920" dur="6s" repeatCount="indefinite"/>
  </rect>
  <g font-family="ui-monospace, 'SF Mono', Consolas, monospace" font-size="64">
{chars}
  </g>
  <rect y="92" width="4" height="60" fill="{c["accent"]}">
    <animate attributeName="x" values="{";".join(str(x) for _, x in cur)}" keyTimes="{";".join(f"{t:.4f}" for t in times)}" calcMode="discrete" dur="{DUR}s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0" dur="1s" calcMode="discrete" repeatCount="indefinite"/>
  </rect>
  <text x="80" y="205" font-family="ui-monospace, 'SF Mono', Consolas, monospace" font-size="18" letter-spacing="1" fill="{c["muted"]}">github.com/Freakah</text>
</svg>
'''

for theme, colors in THEMES.items():
    with open(f"banner-{theme}.svg", "w", newline="\n") as f:
        f.write(svg(colors))
