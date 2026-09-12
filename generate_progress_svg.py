"""
DSA Progress card generator
============================
Edit the numbers in CONFIG below whenever you solve more problems,
then run this script. It regenerates assets/dsa-progress.svg, which
the README embeds. Nothing else needs to change.

    python generate_progress_svg.py
"""

import math
import os

# ------------------------------------------------------------------
# EDIT THESE NUMBERS ONLY
# ------------------------------------------------------------------
CONFIG = {
    "easy_solved": 54,
    "easy_total": 371,
    "medium_solved": 11,
    "medium_total": 470,
    "hard_solved": 0,
    "hard_total": 253,
}
# ------------------------------------------------------------------

OUTPUT_PATH = "dsa-progress.svg"

# Card / theme colors
BG = "#0d0d0d"
CARD_BG = "#161616"
CARD_STROKE = "#2a2a2a"
TRACK_COLOR = "#4a4520"
PROGRESS_COLOR = "#22c55e"
DOT_COLOR = "#e7ff5c"
TEXT_WHITE = "#f5f5f5"
TEXT_GRAY = "#8a8a8a"
EASY_COLOR = "#22c55e"
MEDIUM_COLOR = "#eab308"
HARD_COLOR = "#ef4444"

WIDTH, HEIGHT = 660, 300
RING_CX, RING_CY, RING_R, RING_STROKE = 175, 155, 88, 20


def build_svg(cfg):
    solved = cfg["easy_solved"] + cfg["medium_solved"] + cfg["hard_solved"]
    total = cfg["easy_total"] + cfg["medium_total"] + cfg["hard_total"]
    pct = (solved / total) if total else 0

    circumference = 2 * math.pi * RING_R
    dash = circumference * pct
    gap = circumference - dash

    # angle of the arc tip, starting at 12 o'clock, going clockwise
    tip_angle_deg = -90 + 360 * pct
    tip_angle_rad = math.radians(tip_angle_deg)
    dot_x = RING_CX + RING_R * math.cos(tip_angle_rad)
    dot_y = RING_CY + RING_R * math.sin(tip_angle_rad)

    legend_rows = [
        ("Easy", cfg["easy_solved"], cfg["easy_total"], EASY_COLOR),
        ("Medium", cfg["medium_solved"], cfg["medium_total"], MEDIUM_COLOR),
        ("Hard", cfg["hard_solved"], cfg["hard_total"], HARD_COLOR),
    ]
    legend_start_y = 110
    legend_gap = 46
    legend_x = 380

    legend_svg = ""
    for i, (label, s, t, color) in enumerate(legend_rows):
        y = legend_start_y + i * legend_gap
        legend_svg += f"""
    <circle cx="{legend_x}" cy="{y}" r="7" fill="{color}" />
    <text x="{legend_x + 22}" y="{y + 6}" font-family="Segoe UI, Arial, sans-serif"
          font-size="20" fill="{TEXT_GRAY}">{label}</text>
    <text x="{legend_x + 150}" y="{y + 6}"
          font-family="Segoe UI, Arial, sans-serif" font-size="20"
          font-weight="600" fill="{TEXT_WHITE}">{s}/{t}</text>"""

    svg = f"""<svg width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}"
     xmlns="http://www.w3.org/2000/svg">
  <rect x="1" y="1" width="{WIDTH - 2}" height="{HEIGHT - 2}" rx="26"
        fill="{CARD_BG}" stroke="{CARD_STROKE}" stroke-width="1.5" />

  <!-- header pill -->
  <rect x="{WIDTH/2 - 105}" y="24" width="210" height="46" rx="23"
        fill="#1f1f1f" stroke="#333333" />
  <text x="{WIDTH/2}" y="53" text-anchor="middle" font-family="Segoe UI, Arial, sans-serif"
        font-size="21" font-weight="700" fill="{TEXT_WHITE}">DSA Progress</text>

  <!-- info icon -->
  <circle cx="{WIDTH - 55}" cy="47" r="20" fill="none" stroke="#3a3a3a" stroke-width="1.5" />
  <text x="{WIDTH - 55}" y="54" text-anchor="middle" font-family="Georgia, serif"
        font-size="16" font-style="italic" fill="{TEXT_GRAY}">i</text>

  <!-- progress ring -->
  <circle cx="{RING_CX}" cy="{RING_CY}" r="{RING_R}" fill="none"
          stroke="{TRACK_COLOR}" stroke-width="{RING_STROKE}" />
  <circle cx="{RING_CX}" cy="{RING_CY}" r="{RING_R}" fill="none"
          stroke="{PROGRESS_COLOR}" stroke-width="{RING_STROKE}"
          stroke-linecap="round"
          stroke-dasharray="{dash:.2f} {gap:.2f}"
          transform="rotate(-90 {RING_CX} {RING_CY})" />
  <circle cx="{dot_x:.2f}" cy="{dot_y:.2f}" r="7" fill="{DOT_COLOR}" />

  <!-- center numbers -->
  <text x="{RING_CX}" y="{RING_CY - 2}" text-anchor="middle"
        font-family="Segoe UI, Arial, sans-serif" font-size="46"
        font-weight="700" fill="{TEXT_WHITE}">{solved}</text>
  <line x1="{RING_CX - 28}" y1="{RING_CY + 14}" x2="{RING_CX + 28}" y2="{RING_CY + 14}"
        stroke="#4a4a4a" stroke-width="1.5" />
  <text x="{RING_CX}" y="{RING_CY + 40}" text-anchor="middle"
        font-family="Segoe UI, Arial, sans-serif" font-size="20"
        fill="{TEXT_GRAY}">{total}</text>

  <!-- legend -->
  {legend_svg}
</svg>
"""
    return svg


def main():
    svg = build_svg(CONFIG)
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        f.write(svg)
    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
