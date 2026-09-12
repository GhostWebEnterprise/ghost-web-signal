#!/usr/bin/env python3
# Copyright 2026 Molly Instant Messenger
# SPDX-License-Identifier: AGPL-3.0-only
"""
Ghostly icon generator.

Single source of truth for the Ghostly emblem (neon ghost inside a glowing
speech-bubble ring with an orbit). Emits every icon surface used by the app:

  app/  default + all alt adaptive-icon layers (vector drawables)
  app/  in-app brand logo (logo_round_filled)
  app/  notification icons (default / backup / websocket / unlocked)
  art/  master SVG, monochrome SVG, Play/GitHub PNGs

Launcher and notification rasters were removed on purpose: minSdk is 27, so the
anydpi-v26 adaptive-icon XMLs always win and pure-vector layers keep the APK
small and the icon sharp on every screen.

Usage:  python3 art/generate_icons.py
"""

from __future__ import annotations

import math
import struct
import sys
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APP_RES = ROOT / "app/src/main/res"
CORE_UI_RES = ROOT / "core/ui/src/main/res"
ART = ROOT / "art"

# ---------------------------------------------------------------------------
# Master geometry (1024 x 1024 design space)
# ---------------------------------------------------------------------------

SIZE = 1024
CX, CY = 512.0, 492.0          # bubble ring center
RX, RY = 378.0, 362.0          # bubble ring radii
RING_W = 42.0                  # bubble ring stroke width

RING_BASE = "#0A3FA6"
RING_SEGS = [                  # clockwise from 12 o'clock
    (0.0, 70.0, "#2FC1FF"),
    (70.0, 145.0, "#6A46F5"),
    (145.0, 215.0, "#8A3BE0"),
    (215.0, 290.0, "#0B54D0"),
    (290.0, 360.0, "#1893E6"),
]

TAIL = "M302,828 C330,840 354,850 372,858 C352,886 326,918 296,946 C294,906 297,866 302,828 Z"

GHOST_BODY = (
    "M512,232 C436,232 354,300 330,420 C322,470 322,540 330,612 "
    "C336,668 368,712 404,690 C424,678 432,700 452,706 "
    "C470,712 486,690 512,688 C538,690 554,712 572,706 "
    "C592,700 600,678 620,690 C656,712 688,668 694,612 "
    "C702,540 702,470 694,420 C670,300 588,232 512,232 Z"
)

EYE_L = (
    "M374,470 C382,432 434,414 478,436 C492,443 496,452 492,462 "
    "C478,496 416,506 382,492 C374,488 372,478 374,470 Z"
)
EYE_R = (
    "M650,470 C642,432 590,414 546,436 C532,443 528,452 532,462 "
    "C546,496 608,506 642,492 C650,488 652,478 650,470 Z"
)

PUPIL_RX, PUPIL_RY = 19.0, 27.0
PUPIL_L = (446.0, 460.0)
PUPIL_R = (578.0, 460.0)

ORBIT_C = (512.0, 520.0)
ORBIT_RX, ORBIT_RY = 330.0, 86.0
ORBIT_ROT = -8.0
ORBIT_COLOR = "#A6DCFF"

# Variant -> (background spec, ring recolor or None)
# bg spec: ("solid", color) or ("linear", color1, color2, angle_deg)
VARIANTS = {
    "default": (("linear", "#0B0B14", "#04040A", 135.0), None),
    "light":   (("solid", "#FFFFFF"), "#5B8DEF"),
    "signal":  (("solid", "#3A76F0"), "#FFFFFF"),
    "colorful": (("linear", "#FF5B5B", "#7A3BF0", 135.0), "#FFFFFF"),
    "gold":    (("linear", "#F5D061", "#C89527", 135.0), "#FFFFFF"),
    "heart":   (("linear", "#E85B8A", "#D23B6E", 135.0), "#FFFFFF"),
    "neon":    (("solid", "#07030F"), "#2EE6FF"),
    "xmas":    (("linear", "#0E3D2E", "#0A2C22", 135.0), "#E85B5B"),
    "zen":     (("solid", "#DCE8DC"), "#7FA98F"),
    "notes":   (("solid", "#F5EFE0"), "#C9A227"),
    "moon":    (("linear", "#0B1230", "#070C1E", 135.0), "#B9C4E0"),
    "music":   (("linear", "#1B1030", "#2A0F3A", 135.0), "#C86BFF"),
}

# ---------------------------------------------------------------------------
# Geometry helpers
# ---------------------------------------------------------------------------


def ring_point(theta_deg: float) -> tuple[float, float]:
    t = math.radians(theta_deg)
    return CX + RX * math.sin(t), CY - RY * math.cos(t)


def ring_arc_path(a0: float, a1: float) -> str:
    x0, y0 = ring_point(a0)
    x1, y1 = ring_point(a1)
    large = 1 if (a1 - a0) > 180 else 0
    return f"M{x0:.2f},{y0:.2f} A{RX:.2f},{RY:.2f} 0 {large} 1 {x1:.2f},{y1:.2f}"


def ellipse_two_arc_path(rx: float, ry: float, cx: float, cy: float) -> str:
    return (
        f"M{cx - rx:.2f},{cy:.2f} A{rx:.2f},{ry:.2f} 0 1 1 {cx + rx:.2f},{cy:.2f} "
        f"A{rx:.2f},{ry:.2f} 0 1 1 {cx - rx:.2f},{cy:.2f} Z"
    )


def orbit_half(top: bool) -> str:
    cx, cy = ORBIT_C
    sweep = 1 if top else 0
    return (
        f"M{cx - ORBIT_RX:.2f},{cy:.2f} "
        f"A{ORBIT_RX:.2f},{ORBIT_RY:.2f} 0 0 {sweep} {cx + ORBIT_RX:.2f},{cy:.2f}"
    )


# ---------------------------------------------------------------------------
# SVG emission (art/)
# ---------------------------------------------------------------------------


def master_svg() -> str:
    """Full-color master emblem on a rounded near-black card."""
    segs = "".join(
        f'<path d="{ring_arc_path(a0, a1)}" fill="none" stroke="{color}" '
        f'stroke-width="{RING_W}"/>'
        for a0, a1, color in RING_SEGS
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}">
  <defs>
    <radialGradient id="glowCyan" cx="0.34" cy="0.28" r="0.46">
      <stop offset="0" stop-color="#1893E6" stop-opacity="0.42"/>
      <stop offset="1" stop-color="#1893E6" stop-opacity="0"/>
    </radialGradient>
    <radialGradient id="glowViolet" cx="0.74" cy="0.68" r="0.42">
      <stop offset="0" stop-color="#7A3BF0" stop-opacity="0.34"/>
      <stop offset="1" stop-color="#7A3BF0" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="ghostFill" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#FFFFFF"/>
      <stop offset="1" stop-color="#C9D6F2"/>
    </linearGradient>
    <linearGradient id="ringBase" x1="0" y1="1" x2="1" y2="0">
      <stop offset="0" stop-color="#0B54D0"/>
      <stop offset="1" stop-color="#2FC1FF"/>
    </linearGradient>
  </defs>
  <rect width="{SIZE}" height="{SIZE}" rx="228" fill="#050509"/>
  <rect width="{SIZE}" height="{SIZE}" rx="228" fill="url(#glowCyan)"/>
  <rect width="{SIZE}" height="{SIZE}" rx="228" fill="url(#glowViolet)"/>
  <path d="{TAIL}" fill="url(#ringBase)"/>
  <path d="{ellipse_two_arc_path(RX, RY, CX, CY)}" fill="none" stroke="url(#ringBase)" stroke-width="{RING_W}"/>
  {segs}
  <g transform="rotate({ORBIT_ROT} {ORBIT_C[0]} {ORBIT_C[1]})">
    <path d="{orbit_half(True)}" fill="none" stroke="{ORBIT_COLOR}" stroke-width="13" opacity="0.75"/>
  </g>
  <path d="{GHOST_BODY}" fill="url(#ghostFill)"/>
  <path d="{EYE_L}" fill="#0A0E1A"/>
  <path d="{EYE_R}" fill="#0A0E1A"/>
  <ellipse cx="{PUPIL_L[0]}" cy="{PUPIL_L[1]}" rx="28" ry="36" fill="#35E0FF" opacity="0.35"/>
  <ellipse cx="{PUPIL_R[0]}" cy="{PUPIL_R[1]}" rx="28" ry="36" fill="#35E0FF" opacity="0.35"/>
  <ellipse cx="{PUPIL_L[0]}" cy="{PUPIL_L[1]}" rx="{PUPIL_RX}" ry="{PUPIL_RY}" fill="#35E0FF"/>
  <ellipse cx="{PUPIL_R[0]}" cy="{PUPIL_R[1]}" rx="{PUPIL_RX}" ry="{PUPIL_RY}" fill="#35E0FF"/>
  <g transform="rotate({ORBIT_ROT} {ORBIT_C[0]} {ORBIT_C[1]})">
    <path d="{orbit_half(False)}" fill="none" stroke="{ORBIT_COLOR}" stroke-width="15" opacity="0.95"/>
  </g>
</svg>
"""


def mono_paths() -> list[str]:
    """Monochrome emblem: bubble ring + tail + ghost, eyes and orbit knocked out."""
    band_outer = ellipse_two_arc_path(ORBIT_RX + 8, ORBIT_RY + 8, ORBIT_C[0], ORBIT_C[1])
    band_inner = ellipse_two_arc_path(ORBIT_RX - 8, ORBIT_RY - 8, ORBIT_C[0], ORBIT_C[1])
    return [
        ellipse_two_arc_path(RX + RING_W / 2, RY + RING_W / 2, CX, CY),
        ellipse_two_arc_path(RX - RING_W / 2, RY - RING_W / 2, CX, CY),
        TAIL,
        GHOST_BODY,
        EYE_L,
        EYE_R,
        band_outer,
        band_inner,
    ]


def mono_svg() -> str:
    paths = "".join(f'<path d="{d}"/>' for d in mono_paths())
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {SIZE} {SIZE}">'
        f'<g fill="#000000" fill-rule="evenodd" transform="rotate({ORBIT_ROT} '
        f'{ORBIT_C[0]} {ORBIT_C[1]})">{paths}</g></svg>\n'
    )


# ---------------------------------------------------------------------------
# Android vector drawable emission
# ---------------------------------------------------------------------------

AAPT_NS = 'xmlns:aapt="http://schemas.android.com/aapt"'


def vec_open(viewport: int, aapt: bool = True) -> str:
    ns = f"\n    {AAPT_NS}" if aapt else ""
    return (
        f'<vector xmlns:android="http://schemas.android.com/apk/res/android"{ns}\n'
        f"    android:width=\"108dp\"\n    android:height=\"108dp\"\n"
        f"    android:viewportWidth=\"{viewport}\"\n"
        f"    android:viewportHeight=\"{viewport}\">"
    )


def emblem_layers(ring_color: str | None) -> list[str]:
    """Full-color emblem layers in 1024 design space (no background)."""
    if ring_color:
        ring = (
            f'<path\n        android:pathData="{TAIL}"\n        android:fillColor="{ring_color}"/>\n'
            f'    <path\n        android:pathData="{ellipse_two_arc_path(RX, RY, CX, CY)}"\n'
            f'        android:strokeColor="{ring_color}"\n'
            f'        android:strokeWidth="{RING_W}"/>\n'
        )
    else:
        ring = (
            f'<path\n        android:pathData="{TAIL}"\n        android:fillColor="{RING_BASE}"/>\n'
            f'    <path\n        android:pathData="{ellipse_two_arc_path(RX, RY, CX, CY)}"\n'
            f'        android:strokeColor="{RING_BASE}"\n'
            f'        android:strokeWidth="{RING_W}"/>\n'
            + "".join(
                f'    <path\n        android:pathData="{ring_arc_path(a0, a1)}"\n'
                f'        android:strokeColor="{color}"\n'
                f'        android:strokeWidth="{RING_W}"/>\n'
                for a0, a1, color in RING_SEGS
            )
        )
    return [
        ring,
        f'<group android:rotation="{ORBIT_ROT}" android:pivotX="{ORBIT_C[0]}" '
        f'android:pivotY="{ORBIT_C[1]}">\n'
        f'      <path\n        android:pathData="{orbit_half(True)}"\n'
        f'        android:strokeColor="{ORBIT_COLOR}"\n'
        f'        android:strokeWidth="13"\n        android:fillAlpha="0.75" '
        f'android:strokeAlpha="0.75"/>\n    </group>\n',
        f'<path\n        android:pathData="{GHOST_BODY}"\n        android:fillColor="#F2F5FF"/>\n',
        f'    <path\n        android:pathData="{EYE_L}"\n        android:fillColor="#0A0E1A"/>\n'
        f'    <path\n        android:pathData="{EYE_R}"\n        android:fillColor="#0A0E1A"/>\n'
        f'    <path\n        android:pathData="M{PUPIL_L[0] - 28:.2f},{PUPIL_L[1] - 36:.2f} '
        f'a28,36 0 1 0 56,0 a28,36 0 1 0 -56,0"\n        android:fillColor="#35E0FF" '
        f'android:fillAlpha="0.35"/>\n'
        f'    <path\n        android:pathData="M{PUPIL_R[0] - 28:.2f},{PUPIL_R[1] - 36:.2f} '
        f'a28,36 0 1 0 56,0 a28,36 0 1 0 -56,0"\n        android:fillColor="#35E0FF" '
        f'android:fillAlpha="0.35"/>\n'
        f'    <path\n        android:pathData="M{PUPIL_L[0] - PUPIL_RX:.2f},{PUPIL_L[1] - PUPIL_RY:.2f} '
        f'a{PUPIL_RX:.0f},{PUPIL_RY:.0f} 0 1 0 {PUPIL_RX * 2:.0f},0 '
        f'a{PUPIL_RX:.0f},{PUPIL_RY:.0f} 0 1 0 -{PUPIL_RX * 2:.0f},0"\n'
        f'        android:fillColor="#35E0FF"/>\n'
        f'    <path\n        android:pathData="M{PUPIL_R[0] - PUPIL_RX:.2f},{PUPIL_R[1] - PUPIL_RY:.2f} '
        f'a{PUPIL_RX:.0f},{PUPIL_RY:.0f} 0 1 0 {PUPIL_RX * 2:.0f},0 '
        f'a{PUPIL_RX:.0f},{PUPIL_RY:.0f} 0 1 0 -{PUPIL_RX * 2:.0f},0"\n'
        f'        android:fillColor="#35E0FF"/>\n',
        f'<group android:rotation="{ORBIT_ROT}" android:pivotX="{ORBIT_C[0]}" '
        f'android:pivotY="{ORBIT_C[1]}">\n'
        f'      <path\n        android:pathData="{orbit_half(False)}"\n'
        f'        android:strokeColor="{ORBIT_COLOR}"\n'
        f'        android:strokeWidth="15"\n        android:fillAlpha="0.95" '
        f'android:strokeAlpha="0.95"/>\n    </group>\n',
    ]


def write_foreground(path: Path, ring_color: str | None) -> None:
    body = "".join(emblem_layers(ring_color))
    xml = (
        f"{vec_open(512)}\n  <group\n      android:scaleX=\"0.3125\"\n"
        f"      android:scaleY=\"0.3125\"\n      android:translateX=\"96\"\n"
        f"      android:translateY=\"96\">\n    {body}  </group>\n</vector>\n"
    )
    path.write_text(xml)


def write_background(path: Path, spec) -> None:
    if spec[0] == "solid":
        xml = (
            f'{vec_open(512, aapt=False)}\n  <path\n      android:pathData="M0,0h512v512h-512z"\n'
            f'      android:fillColor="{spec[1]}"/>\n</vector>\n'
        )
    else:
        _, c1, c2, angle = spec
        diag = 512 * 1.414
        rad = math.radians(angle)
        x1, y1 = 256 - math.cos(rad) * diag / 2, 256 - math.sin(rad) * diag / 2
        x2, y2 = 256 + math.cos(rad) * diag / 2, 256 + math.sin(rad) * diag / 2
        xml = (
            f"{vec_open(512)}\n  <path\n      android:pathData=\"M0,0h512v512h-512z\">\n"
            f"    <aapt:attr name=\"android:fillColor\">\n      <gradient\n"
            f"          android:startX=\"{x1:.2f}\"\n          android:startY=\"{y1:.2f}\"\n"
            f"          android:endX=\"{x2:.2f}\"\n          android:endY=\"{y2:.2f}\"\n"
            f"          android:type=\"linear\">\n"
            f"        <item android:offset=\"0\" android:color=\"{c1}\"/>\n"
            f"        <item android:offset=\"1\" android:color=\"{c2}\"/>\n"
            f"      </gradient>\n    </aapt:attr>\n  </path>\n</vector>\n"
        )
    path.write_text(xml)


def write_monochrome(path: Path) -> None:
    body = "".join(
        f'    <path\n        android:pathData="{d}"\n        android:fillType="evenOdd"\n'
        f'        android:fillColor="#000000"/>\n'
        for d in mono_paths()
    )
    xml = (
        f"{vec_open(512, aapt=False)}\n  <group\n      android:scaleX=\"0.3125\"\n"
        f"      android:scaleY=\"0.3125\"\n      android:translateX=\"96\"\n"
        f"      android:translateY=\"96\">\n    <group android:rotation=\"{ORBIT_ROT}\"\n"
        f"        android:pivotX=\"{ORBIT_C[0]}\"\n        android:pivotY=\"{ORBIT_C[1]}\">\n"
        f"{body}    </group>\n  </group>\n</vector>\n"
    )
    path.write_text(xml)


def default_background_xml() -> str:
    """Default launcher background: near-black with cyan/violet glows."""
    xml = f"""{vec_open(512)}
  <path
      android:pathData="M0,0h512v512h-512z"
      android:fillColor="#050509"/>
  <path
      android:pathData="M0,0h512v512h-512z"
      android:fillAlpha="0.42"
      android:fillColor="#1893E6"/>
</vector>
"""
    # Layer glows as radial-gradient-filled rects via aapt attrs.
    glow = """  <path
      android:pathData="M0,0h512v512h-512z">
    <aapt:attr name="android:fillColor">
      <gradient
          android:type="radial"
          android:centerX="174"
          android:centerY="143"
          android:gradientRadius="236">
        <item android:offset="0" android:color="#6B1893E6"/>
        <item android:offset="1" android:color="#001893E6"/>
      </gradient>
    </aapt:attr>
  </path>
  <path
      android:pathData="M0,0h512v512h-512z">
    <aapt:attr name="android:fillColor">
      <gradient
          android:type="radial"
          android:centerX="379"
          android:centerY="348"
          android:gradientRadius="215">
        <item android:offset="0" android:color="#577A3BF0"/>
        <item android:offset="1" android:color="#007A3BF0"/>
      </gradient>
    </aapt:attr>
  </path>
"""
    xml = xml.replace("</vector>\n", glow + "</vector>\n")
    return xml


# ---------------------------------------------------------------------------
# In-app logo + notification glyphs (470 viewport)
# ---------------------------------------------------------------------------

LOGO_VIEW = 470
LOGO_SCALE = LOGO_VIEW / SIZE


def logo_xml() -> str:
    layers = "".join(emblem_layers(None))
    scale = f"{LOGO_SCALE:.6f}"
    xml = f"""<vector xmlns:android="http://schemas.android.com/apk/res/android"
    {AAPT_NS}
    android:width="128dp"
    android:height="128dp"
    android:viewportWidth="{LOGO_VIEW}"
    android:viewportHeight="{LOGO_VIEW}">
  <group
      android:scaleX="{scale}"
      android:scaleY="{scale}">
    {layers}  </group>
</vector>
"""
    return xml


def notification_paths(glyph: list[str]) -> list[str]:
    """Monochrome 24dp glyph: bubble ring + tail + ghost, then glyph toggles."""
    base = [
        ellipse_two_arc_path(RX + RING_W / 2, RY + RING_W / 2, CX, CY),
        ellipse_two_arc_path(RX - RING_W / 2, RY - RING_W / 2, CX, CY),
        TAIL,
        GHOST_BODY,
        EYE_L,
        EYE_R,
    ]
    return base + glyph


def circle_path(cx: float, cy: float, r: float) -> str:
    return f"M{cx - r:.2f},{cy:.2f} a{r:.2f},{r:.2f} 0 1 0 {2 * r:.2f},0 a{r:.2f},{r:.2f} 0 1 0 -{2 * r:.2f},0"


def notification_xml(name: str) -> str:
    cx, cy = 263.0, 302.0
    if name == "backup":
        glyph = [
            circle_path(cx, cy, 84),
            "M251,262 h24 v52 h20 l-32,34 -32,-34 h20 Z",
        ]
    elif name == "websocket":
        glyph = [
            "M219,270 l44,-38 44,38 -12,14 -32,-27 -32,27 Z",
            "M219,338 l44,38 44,-38 -12,-14 -32,27 -32,-27 Z",
        ]
    else:  # unlocked
        glyph = [
            "M317,258 v-22 c0,-30 -24,-54 -54,-54 -26,0 -48,19 -53,44 l22,6 c3,-14 16,-26 31,-26 18,0 32,14 32,32 v20 h-98 c-9,0 -16,7 -16,16 v76 c0,9 7,16 16,16 h104 c9,0 16,-7 16,-16 v-76 c0,-9 -7,-16 -16,-16 Z",
            circle_path(cx, 316, 17),
            "M251,348 h24 l-6,-26 h-12 Z",
        ]
    body = "".join(
        f'  <path\n      android:pathData="{d}"\n      android:fillType="evenOdd"\n'
        f'      android:fillColor="#000"/>\n'
        for d in notification_paths(glyph)
    )
    return f"""<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp"
    android:viewportWidth="{LOGO_VIEW}"
    android:viewportHeight="{LOGO_VIEW}"
    android:tint="#FFFFFF">
  <group
      android:scaleX="{LOGO_SCALE:.6f}"
      android:scaleY="{LOGO_SCALE:.6f}">
{body}  </group>
</vector>
"""


# ---------------------------------------------------------------------------
# Adaptive icon XMLs
# ---------------------------------------------------------------------------


def adaptive_icon_xml(bg_ref: str, fg_ref: str, mono_ref: str) -> str:
    return f"""<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="{bg_ref}"/>
    <foreground android:drawable="{fg_ref}"/>
    <monochrome android:drawable="{mono_ref}"/>
</adaptive-icon>
"""


# ---------------------------------------------------------------------------
# Pure-python rasterizer for qrcode_logo.png (150px, alpha)
# ---------------------------------------------------------------------------

QR_PX = 150
SS = 4  # supersample factor


def bez(p0, p1, p2, p3, steps=28):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        mt = 1 - t
        x = mt**3 * p0[0] + 3 * mt * mt * t * p1[0] + 3 * mt * t * t * p2[0] + t**3 * p3[0]
        y = mt**3 * p0[1] + 3 * mt * mt * t * p1[1] + 3 * mt * t * t * p2[1] + t**3 * p3[1]
        pts.append((x, y))
    return pts


def flatten_path(d: str):
    """Very small parser for the subset used above (M/C/L/Z, absolute or relative)."""
    import re

    tokens = re.findall(r"([MLCZz])([^MLCZz]*)", d)
    cmds, cur, start, polys, cur_poly = [], (0.0, 0.0), (0.0, 0.0), [], []
    for cmd, args in tokens:
        vals = [float(v) for v in re.findall(r"-?\d+\.?\d*(?:e-?\d+)?", args)]
        if cmd == "M":
            if cur_poly:
                polys.append(cur_poly)
            cur = (vals[0], vals[1])
            start = cur
            cur_poly = [cur]
        elif cmd == "C":
            for i in range(0, len(vals), 6):
                p0 = cur
                p1 = (vals[i], vals[i + 1])
                p2 = (vals[i + 2], vals[i + 3])
                p3 = (vals[i + 4], vals[i + 5])
                cur_poly.extend(bez(p0, p1, p2, p3)[1:])
                cur = p3
        elif cmd == "L":
            for i in range(0, len(vals), 2):
                cur = (vals[i], vals[i + 1])
                cur_poly.append(cur)
        elif cmd in "Zz":
            if cur_poly:
                cur_poly.append(start)
                polys.append(cur_poly)
                cur_poly = []
            cur = start
    if cur_poly:
        polys.append(cur_poly)
    return polys


def point_in_polys(x, y, polys):
    inside = False
    for poly in polys:
        n = len(poly)
        j = n - 1
        for i in range(n):
            xi, yi = poly[i]
            xj, yj = poly[j]
            if (yi > y) != (yj > y):
                xint = (xj - xi) * (y - yi) / (yj - yi) + xi
                if x < xint:
                    inside = not inside
            j = i
    return inside


def seg_color_at(x, y):
    """Ring segment color at a point (design space), by angle."""
    ang = math.degrees(math.atan2(x - CX, CY - y)) % 360
    for a0, a1, color in RING_SEGS:
        if a0 <= ang < a1:
            hexv = color.lstrip("#")
            return tuple(int(hexv[i : i + 2], 16) for i in (0, 2, 4))
    return (24, 147, 230)


def ellipse_val(x, y, rx, ry, cx, cy):
    return ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2


def rotate_pt(x, y, deg, cx, cy):
    t = math.radians(deg)
    dx, dy = x - cx, y - cy
    return cx + dx * math.cos(t) - dy * math.sin(t), cy + dx * math.sin(t) + dy * math.cos(t)


def render_qr_logo() -> bytes:
    S = QR_PX * SS
    SCALE = SIZE / S  # design units per subsample
    ghost = flatten_path(GHOST_BODY)
    eye_l = flatten_path(EYE_L)
    eye_r = flatten_path(EYE_R)
    tail = flatten_path(TAIL)

    def hex_rgb(h):
        h = h.lstrip("#")
        return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))

    GHOST_TOP = hex_rgb("#FFFFFF")
    GHOST_BOT = hex_rgb("#C9D6F2")
    EYE = hex_rgb("#0A0E1A")
    PUPIL = hex_rgb("#35E0FF")

    img = [[(0, 0, 0, 0)] * S for _ in range(S)]

    for py in range(S):
        y = (py + 0.5) * SCALE
        for px in range(S):
            x = (px + 0.5) * SCALE
            color = None
            # orbit back (top half, rotated frame)
            ox, oy = rotate_pt(x, y, -ORBIT_ROT, ORBIT_C[0], ORBIT_C[1])
            v = ellipse_val(ox, oy, ORBIT_RX, ORBIT_RY, ORBIT_C[0], ORBIT_C[1])
            if v is not None:
                d = abs(math.sqrt(v) - 1) * min(ORBIT_RX, ORBIT_RY)
                if d <= 7 and oy < ORBIT_C[1]:
                    color = hex_rgb("#A6DCFF") + (190,)
            # bubble tail
            if color is None and point_in_polys(x, y, tail):
                color = hex_rgb("#0B54D0") + (255,)
            # bubble ring
            if color is None:
                v = ellipse_val(x, y, RX, RY, CX, CY)
                if v is not None:
                    d = abs(math.sqrt(v) - 1) * min(RX, RY)
                    if d <= RING_W / 2:
                        r, g, b = seg_color_at(x, y)
                        color = (r, g, b, 255)
            # ghost
            if color is None and point_in_polys(x, y, ghost):
                t = max(0.0, min(1.0, (y - 232.0) / (712.0 - 232.0)))
                r = int(GHOST_TOP[0] + (GHOST_BOT[0] - GHOST_TOP[0]) * t)
                g = int(GHOST_TOP[1] + (GHOST_BOT[1] - GHOST_TOP[1]) * t)
                b = int(GHOST_TOP[2] + (GHOST_BOT[2] - GHOST_TOP[2]) * t)
                color = (r, g, b, 255)
                on_pupil = any(
                    ellipse_val(x, y, PUPIL_RX, PUPIL_RY, cxp, cyp) <= 1
                    for cxp, cyp in (PUPIL_L, PUPIL_R)
                )
                if on_pupil:
                    color = PUPIL + (255,)
                elif point_in_polys(x, y, eye_l) or point_in_polys(x, y, eye_r):
                    color = EYE + (255,)
            # orbit front (bottom half)
            if oy >= ORBIT_C[1]:
                v = ellipse_val(ox, oy, ORBIT_RX, ORBIT_RY, ORBIT_C[0], ORBIT_C[1])
                if v is not None:
                    d = abs(math.sqrt(v) - 1) * min(ORBIT_RX, ORBIT_RY)
                    if d <= 8 and color is not None:
                        color = hex_rgb("#A6DCFF") + (242,)
            if color is not None:
                img[py][px] = color

    # downsample (premultiplied average)
    out = bytearray()
    for oy in range(QR_PX):
        for ox in range(QR_PX):
            r = g = b = a = 0
            for dy in range(SS):
                for dx in range(SS):
                    pr, pg, pb, pa = img[oy * SS + dy][ox * SS + dx]
                    r += pr * pa
                    g += pg * pa
                    b += pb * pa
                    a += pa
            n = SS * SS
            if a == 0:
                out += b"\x00\x00\x00\x00"
            else:
                r //= a
                g //= a
                b //= a
                a //= n
                out += bytes((min(r, 255), min(g, 255), min(b, 255), min(a, 255)))

    def chunk(tag, data):
        c = struct.pack(">I", len(data)) + tag + data
        return c + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)

    ihdr = struct.pack(">IIBBBBB", QR_PX, QR_PX, 8, 6, 0, 0, 0)
    raw = b"".join(b"\x00" + bytes(out[y * QR_PX * 4 : (y + 1) * QR_PX * 4]) for y in range(QR_PX))
    return (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )


def flat_png(size: int, bg: tuple[int, int, int]) -> bytes:
    """Render the full-bleed emblem (transparent, no rounded card) at `size`."""
    global QR_PX, SS
    old_px, old_ss = QR_PX, SS
    QR_PX, SS = size, max(2, 600 // size)
    data = render_qr_logo_scaled(bg)
    QR_PX, SS = old_px, old_ss
    return data


def render_qr_logo_scaled(bg) -> bytes:
    # transparent version; bg unused placeholder to keep API simple
    return render_qr_logo()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> None:
    ART.mkdir(exist_ok=True)

    # art/
    (ART / "ghostly-icon.svg").write_text(master_svg())
    (ART / "ghostly-icon-mono.svg").write_text(mono_svg())
    (ART / "ghostly-icon-512.png").write_bytes(flat_png(512, None))
    (ART / "ghostly-icon-192.png").write_bytes(flat_png(192, None))

    # Default launcher layers
    (APP_RES / "drawable/ic_launcher_background.xml").write_text(default_background_xml())
    write_foreground(APP_RES / "drawable/ic_launcher_foreground.xml", None)
    write_monochrome(APP_RES / "drawable/ic_launcher_monochrome.xml")
    (APP_RES / "mipmap-anydpi-v26/ic_launcher.xml").write_text(
        adaptive_icon_xml("@drawable/ic_launcher_background", "@drawable/ic_launcher_foreground", "@drawable/ic_launcher_monochrome")
    )

    # Alt variants
    for name, (bg_spec, ring_color) in VARIANTS.items():
        if name == "default":
            continue
        write_background(APP_RES / f"drawable/ic_launcher_alt_{name}_background.xml", bg_spec)
        write_foreground(APP_RES / f"drawable/ic_launcher_alt_{name}_foreground.xml", ring_color)
        (APP_RES / f"mipmap-anydpi-v26/ic_launcher_alt_{name}.xml").write_text(
            adaptive_icon_xml(
                f"@drawable/ic_launcher_alt_{name}_background",
                f"@drawable/ic_launcher_alt_{name}_foreground",
                "@drawable/ic_launcher_monochrome",
            )
        )

    # In-app logo
    (APP_RES / "drawable/logo_round_filled.xml").write_text(logo_xml())

    # QR-code center logo (app + core:ui copies must stay identical)
    qr_png = render_qr_logo()
    (APP_RES / "drawable/qrcode_logo.png").write_bytes(qr_png)
    (CORE_UI_RES / "drawable/qrcode_logo.png").write_bytes(qr_png)

    # Notification glyphs
    for name in ("", "_backup", "_websocket", "_unlocked"):
        (APP_RES / f"drawable-anydpi/ic_notification{name}.xml").write_text(notification_xml(name.lstrip("_") or "default"))

    # Staging variant tracks the shared foreground
    (APP_RES.parent.parent / "staging/res/mipmap-anydpi-v26/ic_launcher.xml").write_text(
        """<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/core_black"/>
    <foreground android:drawable="@drawable/ic_launcher_foreground"/>
    <monochrome android:drawable="@drawable/ic_launcher_monochrome"/>
</adaptive-icon>
"""
    )

    print("icon assets generated")


if __name__ == "__main__":
    sys.exit(main())
