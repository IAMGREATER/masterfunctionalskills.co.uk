#!/usr/bin/env python3
"""
Master Functional Skills - Visual Revision Cards Overhaul
All Subjects & Levels: Maths L2/L1/E3, English L2/L1/E3, Digital Skills L1/E3.
Rich Dual-Coded SVGs, One Focused Learning Point Per Card, Rounded Landscape Postcards.
Middle-School & Adult Friendly Design.
"""
import json
import os
import subprocess
import tempfile
import shutil
import xml.etree.ElementTree as ET

# =============================================================================
# SVG ILLUSTRATION ASSETS (INLINE, CLEAN, DUAL-CODED, HIGH-CONTRAST)
# =============================================================================

def svg_area_rectangle():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr1" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#475569"/>
        </marker>
      </defs>
      <rect x="70" y="30" width="280" height="95" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5" />
      <text x="210" y="75" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#0369a1" text-anchor="middle">Area = Length × Width</text>
      <text x="210" y="100" font-family="system-ui, sans-serif" font-size="15" font-weight="700" fill="#0f172a" text-anchor="middle">24 cm × 6 cm = <tspan fill="#059669" font-weight="800">144 cm²</tspan></text>
      <line x1="70" y1="18" x2="350" y2="18" stroke="#475569" stroke-width="1.8" marker-start="url(#arr1)" marker-end="url(#arr1)"/>
      <rect x="180" y="6" width="60" height="22" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
      <text x="210" y="21" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#1e293b" text-anchor="middle">24 cm</text>
      <line x1="50" y1="30" x2="50" y2="125" stroke="#475569" stroke-width="1.8" marker-start="url(#arr1)" marker-end="url(#arr1)"/>
      <rect x="25" y="65" width="50" height="22" rx="4" fill="#ffffff" stroke="#cbd5e1"/>
      <text x="50" y="80" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#1e293b" text-anchor="middle">6 cm</text>
    </svg>"""

def svg_area_trapezium():
    return """<svg viewBox="0 0 460 175" width="100%" height="175" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="arr2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#334155"/>
        </marker>
      </defs>
      <polygon points="120,40 280,40 360,135 60,135" fill="#fef3c7" stroke="#d97706" stroke-width="2.5" />
      <line x1="120" y1="40" x2="120" y2="135" stroke="#059669" stroke-width="2.2" stroke-dasharray="4,4" />
      <path d="M 120,120 L 135,120 L 135,135" fill="none" stroke="#059669" stroke-width="2" />
      <rect x="130" y="80" width="50" height="20" rx="4" fill="#ffffff" stroke="#059669"/>
      <text x="155" y="94" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">h = 4 m</text>
      <line x1="120" y1="26" x2="280" y2="26" stroke="#2563eb" stroke-width="2" marker-start="url(#arr2)" marker-end="url(#arr2)"/>
      <rect x="180" y="15" width="45" height="20" rx="4" fill="#ffffff" stroke="#2563eb"/>
      <text x="202" y="29" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#2563eb" text-anchor="middle">a = 6 m</text>
      <line x1="60" y1="150" x2="360" y2="150" stroke="#2563eb" stroke-width="2" marker-start="url(#arr2)" marker-end="url(#arr2)"/>
      <rect x="190" y="140" width="50" height="20" rx="4" fill="#ffffff" stroke="#2563eb"/>
      <text x="215" y="154" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#2563eb" text-anchor="middle">b = 10 m</text>
      <line x1="315" y1="75" x2="360" y2="110" stroke="#e11d48" stroke-width="3" stroke-linecap="round"/>
      <line x1="360" y1="75" x2="315" y2="110" stroke="#e11d48" stroke-width="3" stroke-linecap="round"/>
      <rect x="330" y="55" width="85" height="22" rx="4" fill="#ffe4e6" stroke="#f43f5e"/>
      <text x="372" y="70" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#be123c" text-anchor="middle">IGNORE SLANT!</text>
    </svg>"""

def svg_circle_formulas():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <circle cx="110" cy="85" r="55" fill="#fdf2f8" stroke="#db2777" stroke-width="2.5" />
      <line x1="55" y1="85" x2="165" y2="85" stroke="#db2777" stroke-width="2" stroke-dasharray="3,3"/>
      <circle cx="110" cy="85" r="3.5" fill="#db2777"/>
      <text x="110" y="78" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#be185d" text-anchor="middle">diameter (d)</text>
      <rect x="30" y="130" width="160" height="26" rx="6" fill="#be185d"/>
      <text x="110" y="147" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" fill="#ffffff" text-anchor="middle">Circumference = 3.142 × d</text>
      <circle cx="340" cy="85" r="55" fill="#ecfdf5" stroke="#059669" stroke-width="2.5" />
      <line x1="340" y1="85" x2="395" y2="85" stroke="#059669" stroke-width="2.5"/>
      <circle cx="340" cy="85" r="3.5" fill="#059669"/>
      <text x="365" y="78" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">radius (r)</text>
      <rect x="235" y="130" width="210" height="26" rx="6" fill="#047857"/>
      <text x="340" y="147" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">Area = π r² = 3.142 × r² (r² = r × r)</text>
    </svg>"""

def svg_cylinder_volume():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(60, 20)">
        <ellipse cx="60" cy="25" rx="45" ry="16" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2.2"/>
        <path d="M 15,25 L 15,105 A 45,16 0 0,0 105,105 L 105,25" fill="#e0e7ff" stroke="#4f46e5" stroke-width="2.2"/>
        <line x1="15" y1="25" x2="15" y2="105" stroke="#4f46e5" stroke-width="2.2"/>
        <line x1="105" y1="25" x2="105" y2="105" stroke="#4f46e5" stroke-width="2.2"/>
        <line x1="60" y1="25" x2="105" y2="25" stroke="#e11d48" stroke-width="2"/>
        <text x="80" y="20" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#be123c">r</text>
        <line x1="118" y1="25" x2="118" y2="105" stroke="#4338ca" stroke-width="1.8"/>
        <text x="128" y="70" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#4338ca">h</text>
      </g>
      <g transform="translate(230, 25)">
        <rect x="0" y="0" width="210" height="120" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
        <text x="105" y="25" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#1e293b" text-anchor="middle">CYLINDER VOLUME</text>
        <rect x="10" y="38" width="190" height="30" rx="6" fill="#4f46e5"/>
        <text x="105" y="58" font-family="system-ui, sans-serif" font-size="11.5" font-weight="800" fill="#ffffff" text-anchor="middle">V = π r² h = 3.142 × r² × h</text>
        <text x="105" y="88" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#475569" text-anchor="middle">Base (π r² = 3.142 × r × r) × h</text>
        <text x="105" y="105" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" fill="#059669" text-anchor="middle">Always cubic units: cm³, m³</text>
      </g>
    </svg>"""

def svg_bearings():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(130, 85)">
        <circle cx="0" cy="0" r="60" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
        <line x1="0" y1="0" x2="0" y2="-68" stroke="#e11d48" stroke-width="2.5"/>
        <polygon points="0,-72 -5,-62 5,-62" fill="#e11d48"/>
        <text x="0" y="-76" font-family="system-ui, sans-serif" font-size="13" font-weight="900" fill="#e11d48" text-anchor="middle">NORTH (000°)</text>
        <line x1="0" y1="0" x2="54" y2="-25" stroke="#2563eb" stroke-width="2.5"/>
        <circle cx="54" cy="-25" r="4" fill="#2563eb"/>
        <text x="68" y="-22" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#1d4ed8">Ship B</text>
        <path d="M 0,-35 A 35,35 0 0,1 32,-14" fill="none" stroke="#f59e0b" stroke-width="3"/>
        <polygon points="32,-14 30,-22 24,-17" fill="#f59e0b"/>
        <text x="24" y="-38" font-family="system-ui, sans-serif" font-size="13" font-weight="900" fill="#b45309">065°</text>
      </g>
      <g transform="translate(265, 25)">
        <rect x="0" y="0" width="180" height="120" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="90" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">THE 3 GOLDEN RULES</text>
        <text x="12" y="48" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b">1. Start from NORTH</text>
        <text x="12" y="68" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b">2. Measure CLOCKWISE</text>
        <text x="12" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b">3. Always use 3 DIGITS</text>
        <text x="90" y="108" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#e11d48" text-anchor="middle">Write 065°, NEVER just 65°!</text>
      </g>
    </svg>"""

def svg_scale_map():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 20)">
        <rect x="0" y="0" width="200" height="125" rx="8" fill="#ecfdf5" stroke="#059669" stroke-width="2"/>
        <circle cx="35" cy="65" r="6" fill="#047857"/>
        <text x="35" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#065f46" text-anchor="middle">Town A</text>
        <circle cx="165" cy="65" r="6" fill="#047857"/>
        <text x="165" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#065f46" text-anchor="middle">Town B</text>
        <line x1="35" y1="65" x2="165" y2="65" stroke="#2563eb" stroke-width="2" stroke-dasharray="3,3"/>
        <rect x="80" y="52" width="40" height="20" rx="4" fill="#ffffff" stroke="#2563eb"/>
        <text x="100" y="66" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" fill="#1d4ed8" text-anchor="middle">4 cm</text>
        <rect x="15" y="105" width="80" height="6" fill="#065f46"/>
        <text x="100" y="112" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#065f46">Scale 1 : 25,000</text>
      </g>
      <g transform="translate(250, 25)">
        <rect x="0" y="0" width="190" height="115" rx="8" fill="#fffbeb" stroke="#d97706" stroke-width="1.5"/>
        <text x="95" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#92400e" text-anchor="middle">MAP SCALE CONVERSION</text>
        <text x="15" y="50" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b">1 cm on map = 25,000 cm</text>
        <text x="15" y="70" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b">25,000 cm ÷ 100 = 250 m</text>
        <rect x="15" y="82" width="160" height="24" rx="4" fill="#d97706"/>
        <text x="95" y="98" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">4 cm × 250 m = 1,000 m (1 km)</text>
      </g>
    </svg>"""

def svg_speed_triangle():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(40, 15)">
        <polygon points="100,5 15,135 185,135" fill="#f8fafc" stroke="#334155" stroke-width="3" />
        <line x1="50" y1="75" x2="150" y2="75" stroke="#334155" stroke-width="2.5" />
        <line x1="100" y1="75" x2="100" y2="135" stroke="#334155" stroke-width="2.5" />
        <text x="100" y="58" font-family="system-ui, sans-serif" font-size="28" font-weight="800" fill="#2563eb" text-anchor="middle">D</text>
        <text x="60" y="115" font-family="system-ui, sans-serif" font-size="26" font-weight="800" fill="#d97706" text-anchor="middle">S</text>
        <text x="140" y="115" font-family="system-ui, sans-serif" font-size="26" font-weight="800" fill="#059669" text-anchor="middle">T</text>
      </g>
      <g transform="translate(250, 20)">
        <rect x="0" y="0" width="180" height="125" rx="10" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
        <text x="90" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#b45309" text-anchor="middle">DECIMAL TIME TRAP</text>
        <text x="15" y="50" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#1e293b">2.5 hrs = 2 hrs 30 mins</text>
        <text x="15" y="72" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#1e293b">2.25 hrs = 2 hrs 15 mins</text>
        <text x="15" y="94" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#1e293b">2.75 hrs = 2 hrs 45 mins</text>
        <text x="90" y="115" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" fill="#dc2626" text-anchor="middle">⚠️ 2.4 hrs ≠ 2h 40m!</text>
      </g>
    </svg>"""

def svg_reverse_percentage():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="revArr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#059669"/>
        </marker>
      </defs>
      <g transform="translate(40, 25)">
        <rect x="0" y="0" width="220" height="45" rx="6" fill="#3b82f6"/>
        <text x="110" y="28" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">Original Price = 100%</text>
        <rect x="220" y="0" width="60" height="45" fill="#f59e0b"/>
        <text x="250" y="28" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">+20%</text>
        <rect x="295" y="5" width="95" height="35" rx="6" fill="#1e293b"/>
        <text x="342" y="27" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#38bdf8" text-anchor="middle">120% = £144</text>
      </g>
      <g transform="translate(40, 85)">
        <path d="M 330,20 Q 200,60 110,25" fill="none" stroke="#059669" stroke-width="3" marker-end="url(#revArr)"/>
        <rect x="160" y="32" width="130" height="24" rx="6" fill="#ecfdf5" stroke="#059669"/>
        <text x="225" y="48" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#065f46" text-anchor="middle">DIVIDE BY 1.20</text>
        <text x="210" y="76" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">£144 ÷ 1.20 = <tspan fill="#059669">£120 Original Price</tspan></text>
      </g>
    </svg>"""

def svg_ratio_sharing():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 20)">
        <text x="0" y="16" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#1e293b">Share £50 in the ratio 3 : 2</text>
        <rect x="0" y="28" width="45" height="40" rx="4" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5"/>
        <text x="22" y="52" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">£10</text>
        <rect x="48" y="28" width="45" height="40" rx="4" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5"/>
        <text x="70" y="52" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">£10</text>
        <rect x="96" y="28" width="45" height="40" rx="4" fill="#3b82f6" stroke="#1d4ed8" stroke-width="1.5"/>
        <text x="118" y="52" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">£10</text>
        <text x="70" y="84" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#1d4ed8" text-anchor="middle">Amir (3) = £30</text>
        <rect x="155" y="28" width="45" height="40" rx="4" fill="#10b981" stroke="#047857" stroke-width="1.5"/>
        <text x="177" y="52" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">£10</text>
        <rect x="203" y="28" width="45" height="40" rx="4" fill="#10b981" stroke="#047857" stroke-width="1.5"/>
        <text x="225" y="52" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#ffffff" text-anchor="middle">£10</text>
        <text x="202" y="84" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#047857" text-anchor="middle">Beth (2) = £20</text>
      </g>
      <g transform="translate(290, 20)">
        <rect x="0" y="0" width="145" height="125" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
        <text x="72" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">THE 3 STEPS</text>
        <text x="10" y="46" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#2563eb">1. ADD: 3 + 2 = 5</text>
        <text x="10" y="70" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#d97706">2. DIVIDE: 50 ÷ 5 = 10</text>
        <text x="10" y="94" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#059669">3. MULTIPLY: ×10</text>
        <text x="72" y="115" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" fill="#475569" text-anchor="middle">Check: 30 + 20 = £50 ✓</text>
      </g>
    </svg>"""

def svg_mean_table():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 15)">
        <rect x="0" y="0" width="390" height="95" rx="6" fill="#ffffff" stroke="#cbd5e1"/>
        <rect x="0" y="0" width="390" height="24" fill="#1e293b"/>
        <text x="50" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">Group</text>
        <text x="150" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#38bdf8" text-anchor="middle">Midpoint (m)</text>
        <text x="250" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#ffffff" text-anchor="middle">Frequency (f)</text>
        <text x="335" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#34d399" text-anchor="middle">m × f</text>
        <text x="50" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">0 - 2</text>
        <text x="150" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#0284c7" text-anchor="middle">1</text>
        <text x="250" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">4</text>
        <text x="335" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#059669" text-anchor="middle">4</text>
        <text x="50" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">2 - 4</text>
        <text x="150" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#0284c7" text-anchor="middle">3</text>
        <text x="250" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b" text-anchor="middle">6</text>
        <text x="335" y="65" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#059669" text-anchor="middle">18</text>
        <line x1="0" y1="74" x2="390" y2="74" stroke="#cbd5e1" stroke-width="1"/>
        <text x="100" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#64748b">TOTALS:</text>
        <text x="250" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#1e293b" text-anchor="middle">Total f = 10</text>
        <text x="335" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#059669" text-anchor="middle">Total = 22</text>
      </g>
      <g transform="translate(30, 120)">
        <rect x="0" y="0" width="390" height="32" rx="6" fill="#f0fdf4" stroke="#22c55e"/>
        <text x="195" y="21" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#15803d" text-anchor="middle">
          Estimated Mean = Total (m × f) ÷ Total Frequency = 22 ÷ 10 = <tspan fill="#b91c1c">2.2</tspan>
        </text>
      </g>
    </svg>"""

def svg_fraction_basics():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(60, 45)">
        <path d="M 0,0 L 35,0 A 35,35 0 0,1 -35,0 Z" fill="#ef4444" transform="rotate(-90)"/>
        <circle cx="0" cy="0" r="35" fill="none" stroke="#334155" stroke-width="1.8"/>
        <text x="0" y="60" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#ef4444" text-anchor="middle">½</text>
      </g>
      <g transform="translate(170, 45)">
        <path d="M 0,0 L 35,0 A 35,35 0 0,1 0,35 Z" fill="#f59e0b"/>
        <circle cx="0" cy="0" r="35" fill="none" stroke="#334155" stroke-width="1.8"/>
        <line x1="-35" y1="0" x2="35" y2="0" stroke="#94a3b8" stroke-dasharray="2,2"/>
        <line x1="0" y1="-35" x2="0" y2="35" stroke="#94a3b8" stroke-dasharray="2,2"/>
        <text x="0" y="60" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#d97706" text-anchor="middle">¼</text>
      </g>
      <g transform="translate(260, 20)">
        <rect x="0" y="0" width="160" height="35" rx="6" fill="#f8fafc" stroke="#334155" stroke-width="1.8"/>
        <rect x="0" y="0" width="40" height="35" fill="#3b82f6"/>
        <rect x="40" y="0" width="40" height="35" fill="#3b82f6"/>
        <rect x="80" y="0" width="40" height="35" fill="#3b82f6"/>
        <line x1="40" y1="0" x2="40" y2="35" stroke="#ffffff" stroke-width="2"/>
        <line x1="80" y1="0" x2="80" y2="35" stroke="#ffffff" stroke-width="2"/>
        <line x1="120" y1="0" x2="120" y2="35" stroke="#94a3b8" stroke-width="1.5"/>
        <text x="80" y="60" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#2563eb" text-anchor="middle">¾ (3 parts out of 4)</text>
      </g>
      <rect x="30" y="125" width="400" height="30" rx="8" fill="#f1f5f9"/>
      <text x="230" y="145" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#1e293b" text-anchor="middle">
        <tspan fill="#ef4444" font-weight="800">Top (Numerator)</tspan> = parts you have | <tspan fill="#0284c7" font-weight="800">Bottom (Denominator)</tspan> = total parts
      </text>
    </svg>"""

def svg_place_value():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(15, 15)">
        <rect x="0" y="0" width="60" height="50" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <text x="30" y="32" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#1d4ed8" text-anchor="middle">2</text>
        <text x="30" y="65" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#3b82f6" text-anchor="middle">MILLIONS</text>
        <rect x="70" y="0" width="55" height="50" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
        <text x="97" y="32" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#b91c1c" text-anchor="middle">5</text>
        <text x="97" y="65" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#ef4444" text-anchor="middle">100 Th</text>
        <rect x="130" y="0" width="55" height="50" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
        <text x="157" y="32" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#b91c1c" text-anchor="middle">6</text>
        <text x="157" y="65" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#ef4444" text-anchor="middle">10 Th</text>
        <rect x="190" y="0" width="55" height="50" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
        <text x="217" y="32" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#b91c1c" text-anchor="middle">3</text>
        <text x="217" y="65" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#ef4444" text-anchor="middle">1,000s</text>
        <rect x="255" y="0" width="55" height="50" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
        <text x="282" y="32" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#047857" text-anchor="middle">1</text>
        <text x="282" y="65" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#059669" text-anchor="middle">100s</text>
        <rect x="315" y="0" width="55" height="50" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
        <text x="342" y="32" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#047857" text-anchor="middle">7</text>
        <text x="342" y="65" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#059669" text-anchor="middle">10s</text>
        <rect x="375" y="0" width="55" height="50" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
        <text x="402" y="32" font-family="system-ui, sans-serif" font-size="22" font-weight="800" fill="#047857" text-anchor="middle">8</text>
        <text x="402" y="65" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#059669" text-anchor="middle">UNITS</text>
      </g>
      <g transform="translate(30, 110)">
        <line x1="0" y1="20" x2="400" y2="20" stroke="#1e293b" stroke-width="2.5"/>
        <line x1="40" y1="12" x2="40" y2="28" stroke="#1e293b" stroke-width="2"/>
        <text x="40" y="44" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#ef4444" text-anchor="middle">-3</text>
        <line x1="120" y1="12" x2="120" y2="28" stroke="#1e293b" stroke-width="2"/>
        <text x="120" y="44" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#ef4444" text-anchor="middle">-1</text>
        <line x1="200" y1="8" x2="200" y2="32" stroke="#1e293b" stroke-width="3"/>
        <text x="200" y="46" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#0f172a" text-anchor="middle">0</text>
        <line x1="280" y1="12" x2="280" y2="28" stroke="#1e293b" stroke-width="2"/>
        <text x="280" y="44" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">+1</text>
        <line x1="360" y1="12" x2="360" y2="28" stroke="#1e293b" stroke-width="2"/>
        <text x="360" y="44" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#059669" text-anchor="middle">+3</text>
      </g>
    </svg>"""

def svg_money_conversion():
    return """<svg viewBox="0 0 460 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="marr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#059669"/>
        </marker>
        <marker id="marr2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb"/>
        </marker>
      </defs>
      <rect x="25" y="25" width="195" height="110" rx="12" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
      <text x="122" y="55" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#065f46" text-anchor="middle">Pounds (£) ➔ Pence (p)</text>
      <line x1="55" y1="78" x2="190" y2="78" stroke="#059669" stroke-width="3" marker-end="url(#marr)"/>
      <rect x="90" y="66" width="65" height="24" rx="6" fill="#059669"/>
      <text x="122" y="83" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">× 100</text>
      <text x="122" y="118" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#047857" text-anchor="middle">£3.50 × 100 = 350p</text>
      <rect x="240" y="25" width="195" height="110" rx="12" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
      <text x="337" y="55" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#1e40af" text-anchor="middle">Pence (p) ➔ Pounds (£)</text>
      <line x1="270" y1="78" x2="405" y2="78" stroke="#2563eb" stroke-width="3" marker-end="url(#marr2)"/>
      <rect x="305" y="66" width="65" height="24" rx="6" fill="#2563eb"/>
      <text x="337" y="83" font-family="system-ui, sans-serif" font-size="14" font-weight="800" fill="#ffffff" text-anchor="middle">÷ 100</text>
      <text x="337" y="118" font-family="system-ui, sans-serif" font-size="12" font-weight="700" fill="#1d4ed8" text-anchor="middle">75p ÷ 100 = £0.75</text>
    </svg>"""

def svg_percentage_bubbles():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <circle cx="230" cy="85" r="42" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
      <text x="230" y="80" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#ffffff" text-anchor="middle">FIND %</text>
      <text x="230" y="96" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#dbeafe" text-anchor="middle">OF AMOUNT</text>
      <g transform="translate(60, 20)">
        <rect x="0" y="0" width="95" height="48" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.8"/>
        <text x="47" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#065f46" text-anchor="middle">50% = ÷ 2</text>
        <text x="47" y="38" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#059669" text-anchor="middle">Half the number</text>
      </g>
      <g transform="translate(305, 20)">
        <rect x="0" y="0" width="95" height="48" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="1.8"/>
        <text x="47" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#b45309" text-anchor="middle">10% = ÷ 10</text>
        <text x="47" y="38" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#d97706" text-anchor="middle">Move 1 decimal left</text>
      </g>
      <g transform="translate(60, 100)">
        <rect x="0" y="0" width="95" height="48" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="1.8"/>
        <text x="47" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#991b1b" text-anchor="middle">5% = Half of 10%</text>
        <text x="47" y="38" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#dc2626" text-anchor="middle">Divide 10% by 2</text>
      </g>
      <g transform="translate(305, 100)">
        <rect x="0" y="0" width="95" height="48" rx="8" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.8"/>
        <text x="47" y="22" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#5b21b6" text-anchor="middle">1% = ÷ 100</text>
        <text x="47" y="38" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#7c3aed" text-anchor="middle">Move 2 decimals left</text>
      </g>
    </svg>"""

def svg_averages_rhyme():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(20, 15)">
        <rect x="0" y="0" width="95" height="135" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <text x="47" y="26" font-family="system-ui, sans-serif" font-size="13" font-weight="900" fill="#1d4ed8" text-anchor="middle">MODE</text>
        <text x="47" y="55" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#2563eb" text-anchor="middle">Most Often</text>
        <text x="47" y="95" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">The number that</text>
        <text x="47" y="110" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">appears most!</text>
        <rect x="108" y="0" width="95" height="135" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
        <text x="155" y="26" font-family="system-ui, sans-serif" font-size="13" font-weight="900" fill="#065f46" text-anchor="middle">MEDIAN</text>
        <text x="155" y="55" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#059669" text-anchor="middle">The Middle</text>
        <text x="155" y="95" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">Put in order first,</text>
        <text x="155" y="110" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">pick middle!</text>
        <rect x="216" y="0" width="95" height="135" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
        <text x="263" y="26" font-family="system-ui, sans-serif" font-size="13" font-weight="900" fill="#92400e" text-anchor="middle">MEAN</text>
        <text x="263" y="55" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#d97706" text-anchor="middle">Add &amp; Divide</text>
        <text x="263" y="95" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">Sum all values ÷</text>
        <text x="263" y="110" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">how many items</text>
        <rect x="324" y="0" width="95" height="135" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
        <text x="371" y="26" font-family="system-ui, sans-serif" font-size="13" font-weight="900" fill="#991b1b" text-anchor="middle">RANGE</text>
        <text x="371" y="55" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#dc2626" text-anchor="middle">Difference</text>
        <text x="371" y="95" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">Highest value</text>
        <text x="371" y="110" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">minus Lowest!</text>
      </g>
    </svg>"""

def svg_compound_l_shape():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <polygon points="60,20 180,20 180,70 260,70 260,140 60,140" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5"/>
      <text x="120" y="14" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">4 m</text>
      <text x="272" y="110" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0369a1">5 m</text>
      <text x="160" y="156" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0369a1" text-anchor="middle">TOTAL = 10 m</text>
      <text x="40" y="85" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0369a1">8 m</text>
      <rect x="290" y="25" width="150" height="110" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="1.8"/>
      <text x="365" y="48" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#991b1b" text-anchor="middle">FIND MISSING SIDES!</text>
      <text x="305" y="75" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b">Horizontal: 10 - 4 = 6 m</text>
      <text x="305" y="98" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b">Vertical: 8 - 5 = 3 m</text>
      <text x="365" y="122" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" fill="#b91c1c" text-anchor="middle">Perimeter = sum of ALL 6!</text>
    </svg>"""

def svg_angles_rules():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(40, 30)">
        <line x1="0" y1="60" x2="160" y2="60" stroke="#1e293b" stroke-width="3"/>
        <line x1="80" y1="60" x2="130" y2="15" stroke="#2563eb" stroke-width="2.5"/>
        <path d="M 45,60 A 35,35 0 0,1 115,29" fill="none" stroke="#2563eb" stroke-width="2"/>
        <text x="80" y="85" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#1e40af" text-anchor="middle">Straight Line = 180°</text>
        <text x="80" y="105" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">a + b = 180°</text>
      </g>
      <g transform="translate(250, 20)">
        <circle cx="80" cy="50" r="35" fill="none" stroke="#059669" stroke-width="2.5" stroke-dasharray="4,4"/>
        <circle cx="80" cy="50" r="3.5" fill="#059669"/>
        <line x1="80" y1="50" x2="115" y2="50" stroke="#059669" stroke-width="2"/>
        <path d="M 100,50 A 20,20 0 1,1 80,30" fill="none" stroke="#d97706" stroke-width="2.5"/>
        <text x="80" y="105" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#065f46" text-anchor="middle">Full Turn = 360°</text>
        <text x="80" y="125" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">Right angle = 90°</text>
      </g>
    </svg>"""

def svg_metric_units_ladder():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <marker id="ladArr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#2563eb"/>
        </marker>
        <marker id="ladArrL" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M 0 1.5 L 8 5 L 0 8.5 z" fill="#059669"/>
        </marker>
      </defs>
      <g transform="translate(20, 50)">
        <rect x="0" y="10" width="70" height="40" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <text x="35" y="35" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#1d4ed8" text-anchor="middle">km</text>
        <path d="M 75,20 L 135,20" stroke="#2563eb" stroke-width="2" marker-end="url(#ladArr)"/>
        <text x="105" y="14" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#2563eb" text-anchor="middle">× 1000</text>
        <rect x="140" y="10" width="65" height="40" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <text x="172" y="35" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#1d4ed8" text-anchor="middle">m</text>
        <path d="M 210,20 L 265,20" stroke="#2563eb" stroke-width="2" marker-end="url(#ladArr)"/>
        <text x="237" y="14" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#2563eb" text-anchor="middle">× 100</text>
        <rect x="270" y="10" width="65" height="40" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <text x="302" y="35" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#1d4ed8" text-anchor="middle">cm</text>
        <path d="M 340,20 L 375,20" stroke="#2563eb" stroke-width="2" marker-end="url(#ladArr)"/>
        <text x="357" y="14" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#2563eb" text-anchor="middle">× 10</text>
        <rect x="380" y="10" width="55" height="40" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <text x="407" y="35" font-family="system-ui, sans-serif" font-size="16" font-weight="800" fill="#1d4ed8" text-anchor="middle">mm</text>
        <path d="M 375,45 L 340,45" stroke="#059669" stroke-width="2" marker-end="url(#ladArrL)"/>
        <text x="357" y="58" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#059669" text-anchor="middle">÷ 10</text>
        <path d="M 265,45 L 210,45" stroke="#059669" stroke-width="2" marker-end="url(#ladArrL)"/>
        <text x="237" y="58" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#059669" text-anchor="middle">÷ 100</text>
        <path d="M 135,45 L 75,45" stroke="#059669" stroke-width="2" marker-end="url(#ladArrL)"/>
        <text x="105" y="58" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#059669" text-anchor="middle">÷ 1000</text>
      </g>
      <rect x="30" y="125" width="400" height="30" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
      <text x="230" y="145" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#1e293b" text-anchor="middle">
        Mass: 1 kg = 1,000 g | Capacity: 1 Litre = 1,000 ml
      </text>
    </svg>"""

def svg_rounding_hill():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <path d="M 40,130 Q 230,10 420,130" fill="none" stroke="#0284c7" stroke-width="4"/>
      <circle cx="100" cy="85" r="14" fill="#fee2e2" stroke="#ef4444" stroke-width="2"/>
      <text x="100" y="90" font-family="system-ui, sans-serif" font-size="12" font-weight="900" fill="#991b1b" text-anchor="middle">4↓</text>
      <rect x="50" y="135" width="130" height="26" rx="6" fill="#fef2f2" stroke="#ef4444"/>
      <text x="115" y="152" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#991b1b" text-anchor="middle">0, 1, 2, 3, 4 = ROUND DOWN</text>
      <circle cx="230" cy="30" r="18" fill="#fef08a" stroke="#ca8a04" stroke-width="2.5"/>
      <text x="230" y="36" font-family="system-ui, sans-serif" font-size="15" font-weight="900" fill="#854d0e" text-anchor="middle">5</text>
      <circle cx="360" cy="85" r="14" fill="#dcfce7" stroke="#16a34a" stroke-width="2"/>
      <text x="360" y="90" font-family="system-ui, sans-serif" font-size="12" font-weight="900" fill="#166534" text-anchor="middle">6↑</text>
      <rect x="280" y="135" width="140" height="26" rx="6" fill="#f0fdf4" stroke="#16a34a"/>
      <text x="350" y="152" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#166534" text-anchor="middle">5, 6, 7, 8, 9 = ROUND UP</text>
    </svg>"""

def svg_clock_time():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(65, 30)">
        <circle cx="50" cy="50" r="45" fill="#f8fafc" stroke="#334155" stroke-width="2.5"/>
        <line x1="50" y1="50" x2="50" y2="20" stroke="#1e293b" stroke-width="3" stroke-linecap="round"/>
        <line x1="50" y1="50" x2="78" y2="50" stroke="#2563eb" stroke-width="3.5" stroke-linecap="round"/>
        <circle cx="50" cy="50" r="3.5" fill="#1e293b"/>
        <text x="50" y="112" font-family="system-ui, sans-serif" font-size="13" font-weight="800" fill="#1d4ed8" text-anchor="middle">3:00 PM</text>
      </g>
      <g transform="translate(195, 65)">
        <path d="M 0,15 L 50,15" stroke="#f59e0b" stroke-width="4"/>
        <polygon points="55,15 45,8 45,22" fill="#f59e0b"/>
        <text x="25" y="8" font-family="system-ui, sans-serif" font-size="12" font-weight="900" fill="#b45309" text-anchor="middle">+ 12</text>
      </g>
      <g transform="translate(280, 40)">
        <rect x="0" y="0" width="140" height="60" rx="10" fill="#0f172a" stroke="#334155" stroke-width="2"/>
        <text x="70" y="42" font-family="monospace, sans-serif" font-size="28" font-weight="900" fill="#38bdf8" text-anchor="middle">15:00</text>
        <text x="70" y="85" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#059669" text-anchor="middle">24-HOUR CLOCK</text>
        <text x="70" y="105" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#dc2626" text-anchor="middle">Never write 'pm' on 24h!</text>
      </g>
    </svg>"""

def svg_bar_chart_key():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 20)">
        <text x="0" y="15" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#1e293b">Patients Attending Clinic:</text>
        <text x="0" y="48" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#475569">Mon:</text>
        <circle cx="55" cy="45" r="10" fill="#3b82f6"/>
        <circle cx="85" cy="45" r="10" fill="#3b82f6"/>
        <circle cx="115" cy="45" r="10" fill="#3b82f6"/>
        <circle cx="145" cy="45" r="10" fill="#3b82f6"/>
        <text x="180" y="48" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#059669">4 symbols × 5 = 20 patients</text>
        <text x="0" y="85" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#475569">Tue:</text>
        <circle cx="55" cy="82" r="10" fill="#3b82f6"/>
        <circle cx="85" cy="82" r="10" fill="#3b82f6"/>
        <path d="M 115,72 A 10,10 0 0,1 115,92 Z" fill="#3b82f6"/>
        <text x="145" y="85" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#059669">2.5 symbols × 5 = 12.5</text>
      </g>
      <g transform="translate(30, 115)">
        <rect x="0" y="0" width="390" height="38" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="2"/>
        <circle cx="35" cy="19" r="9" fill="#3b82f6"/>
        <text x="195" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#991b1b" text-anchor="middle">
          KEY: 🔵 = 5 Patients (ALWAYS check the key before counting!)
        </text>
      </g>
    </svg>"""

def svg_money_columns():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(110, 15)">
        <rect x="0" y="0" width="240" height="135" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
        <text x="50" y="32" font-family="monospace, sans-serif" font-size="18" font-weight="800" fill="#1e293b">£ 1 4 . 5 0</text>
        <text x="30" y="58" font-family="monospace, sans-serif" font-size="18" font-weight="800" fill="#1e293b">+ £ 0 3 . 8 5</text>
        <line x1="20" y1="72" x2="220" y2="72" stroke="#1e293b" stroke-width="2"/>
        <text x="50" y="96" font-family="monospace, sans-serif" font-size="20" font-weight="900" fill="#059669">£ 1 8 . 3 5</text>
        <line x1="20" y1="106" x2="220" y2="106" stroke="#1e293b" stroke-width="2"/>
        <line x1="148" y1="15" x2="148" y2="120" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="3,3"/>
        <text x="148" y="130" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#dc2626" text-anchor="middle">Keep points in a straight line!</text>
      </g>
    </svg>"""

def svg_semicolon_bridge():
    return """<svg viewBox="0 0 460 160" width="100%" height="160" xmlns="http://www.w3.org/2000/svg">
      <rect x="15" y="35" width="170" height="80" rx="10" fill="#f5f3ff" stroke="#7c3aed" stroke-width="2"/>
      <text x="100" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">INDEPENDENT CLAUSE 1</text>
      <text x="100" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#4b5563" text-anchor="middle">"The hospital was busy"</text>
      <circle cx="230" cy="75" r="28" fill="#7c3aed"/>
      <text x="230" y="88" font-family="system-ui, sans-serif" font-size="34" font-weight="900" fill="#ffffff" text-anchor="middle">;</text>
      <rect x="275" y="35" width="170" height="80" rx="10" fill="#f5f3ff" stroke="#7c3aed" stroke-width="2"/>
      <text x="360" y="65" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#6d28d9" text-anchor="middle">INDEPENDENT CLAUSE 2</text>
      <text x="360" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#4b5563" text-anchor="middle">"the doctors worked late"</text>
      <text x="230" y="142" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#374151" text-anchor="middle">
        Both sides MUST make complete sense alone as separate sentences!
      </text>
    </svg>"""

def svg_formal_letter():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <rect x="130" y="10" width="200" height="150" rx="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1.8"/>
      <rect x="230" y="18" width="90" height="12" rx="3" fill="#cbd5e1"/>
      <rect x="250" y="33" width="70" height="8" rx="2" fill="#94a3b8"/>
      <rect x="250" y="44" width="70" height="7" rx="2" fill="#64748b"/>
      <rect x="140" y="56" width="75" height="8" rx="2" fill="#cbd5e1"/>
      <rect x="140" y="66" width="65" height="6" rx="2" fill="#e2e8f0"/>
      <rect x="140" y="78" width="60" height="7" rx="2" fill="#3b82f6"/>
      <rect x="140" y="90" width="180" height="4" rx="2" fill="#cbd5e1"/>
      <rect x="140" y="98" width="180" height="4" rx="2" fill="#cbd5e1"/>
      <rect x="140" y="106" width="150" height="4" rx="2" fill="#cbd5e1"/>
      <rect x="140" y="116" width="180" height="4" rx="2" fill="#cbd5e1"/>
      <g transform="translate(10, 45)">
        <rect x="0" y="0" width="110" height="45" rx="6" fill="#ecfdf5" stroke="#10b981"/>
        <text x="55" y="18" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#065f46" text-anchor="middle">KNOW THE NAME?</text>
        <text x="55" y="34" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#047857" text-anchor="middle">Yours sincerely</text>
      </g>
      <g transform="translate(340, 45)">
        <rect x="0" y="0" width="110" height="45" rx="6" fill="#eff6ff" stroke="#3b82f6"/>
        <text x="55" y="18" font-family="system-ui, sans-serif" font-size="9" font-weight="800" fill="#1e40af" text-anchor="middle">NO NAME (Dear Sir)?</text>
        <text x="55" y="34" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#1d4ed8" text-anchor="middle">Yours faithfully</text>
      </g>
    </svg>"""

def svg_fact_opinion_bias():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 20)">
        <rect x="0" y="0" width="185" height="120" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <text x="92" y="26" font-family="system-ui, sans-serif" font-size="13" font-weight="900" fill="#1d4ed8" text-anchor="middle">FACT</text>
        <text x="12" y="52" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#1e293b">✓ Can be PROVEN true</text>
        <text x="12" y="72" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#1e293b">✓ Contains data, dates, stats</text>
        <rect x="10" y="85" width="165" height="24" rx="4" fill="#ffffff" stroke="#93c5fd"/>
        <text x="92" y="101" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#1e40af" text-anchor="middle">"The train arrives at 14:30."</text>
      </g>
      <g transform="translate(245, 20)">
        <rect x="0" y="0" width="185" height="120" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
        <text x="92" y="26" font-family="system-ui, sans-serif" font-size="13" font-weight="900" fill="#b45309" text-anchor="middle">OPINION / BIAS</text>
        <text x="12" y="52" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#1e293b">⚠️ Personal feeling or belief</text>
        <text x="12" y="72" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#1e293b">⚠️ Uses loaded adjectives</text>
        <rect x="10" y="85" width="165" height="24" rx="4" fill="#ffffff" stroke="#fde68a"/>
        <text x="92" y="101" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#92400e" text-anchor="middle">"Travelling by train is awful."</text>
      </g>
    </svg>"""

def svg_comparing_texts():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 20)">
        <rect x="0" y="0" width="110" height="75" rx="6" fill="#f8fafc" stroke="#475569" stroke-width="1.8"/>
        <text x="55" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">TEXT A</text>
        <text x="55" y="42" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#64748b" text-anchor="middle">NHS Leaflet</text>
        <text x="55" y="60" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#0284c7" text-anchor="middle">Informative / Formal</text>
      </g>
      <g transform="translate(155, 30)">
        <rect x="0" y="0" width="150" height="55" rx="8" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.8"/>
        <text x="75" y="18" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" fill="#6d28d9" text-anchor="middle">CONNECTIVE WORDS</text>
        <text x="75" y="34" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#4c1d95" text-anchor="middle">"Similarly..." / "Whereas..."</text>
        <text x="75" y="48" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#4c1d95" text-anchor="middle">"In contrast to Text A..."</text>
      </g>
      <g transform="translate(320, 20)">
        <rect x="0" y="0" width="110" height="75" rx="6" fill="#f8fafc" stroke="#475569" stroke-width="1.8"/>
        <text x="55" y="22" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">TEXT B</text>
        <text x="55" y="42" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#64748b" text-anchor="middle">Patient Blog</text>
        <text x="55" y="60" font-family="system-ui, sans-serif" font-size="8.5" font-weight="700" fill="#d97706" text-anchor="middle">Personal / Emotive</text>
      </g>
      <rect x="30" y="115" width="400" height="32" rx="6" fill="#ecfdf5" stroke="#10b981"/>
      <text x="230" y="135" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#065f46" text-anchor="middle">
        Always compare: 1. Main Purpose  2. Tone  3. Key Facts/Perspectives
      </text>
    </svg>"""

def svg_apostrophes():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 20)">
        <rect x="0" y="0" width="185" height="85" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <text x="92" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="900" fill="#1d4ed8" text-anchor="middle">1. CONTRACTION</text>
        <text x="92" y="44" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">Shows missing letters:</text>
        <text x="92" y="66" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#2563eb" text-anchor="middle">do not ➔ don't | it is ➔ it's</text>
      </g>
      <g transform="translate(245, 20)">
        <rect x="0" y="0" width="185" height="85" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
        <text x="92" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="900" fill="#065f46" text-anchor="middle">2. POSSESSION</text>
        <text x="92" y="44" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">Shows ownership:</text>
        <text x="92" y="66" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#047857" text-anchor="middle">1 doctor: doctor's badge</text>
      </g>
      <rect x="30" y="120" width="400" height="32" rx="6" fill="#fef2f2" stroke="#ef4444"/>
      <text x="230" y="140" font-family="system-ui, sans-serif" font-size="10.5" font-weight="800" fill="#991b1b" text-anchor="middle">
        ⚠️ Plural noun ending in -s: put apostrophe AFTER the s: "the doctors' badges"
      </text>
    </svg>"""

def svg_formal_report():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(40, 15)">
        <rect x="0" y="0" width="380" height="135" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
        <rect x="15" y="12" width="350" height="22" rx="4" fill="#1e293b"/>
        <text x="190" y="27" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#ffffff" text-anchor="middle">REPORT TITLE &amp; AUTHOR (To: Management | Date)</text>
        <text x="25" y="52" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#2563eb">1. Introduction / Terms of Reference</text>
        <line x1="25" y1="58" x2="350" y2="58" stroke="#cbd5e1" stroke-width="2"/>
        <text x="25" y="78" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#2563eb">2. Key Findings &amp; Analysis (Use subheadings &amp; bullet points)</text>
        <circle cx="35" cy="90" r="2.5" fill="#475569"/>
        <line x1="45" y1="90" x2="330" y2="90" stroke="#cbd5e1" stroke-width="2"/>
        <text x="25" y="112" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#059669">3. Recommendations (Concrete actionable next steps)</text>
        <line x1="25" y1="120" x2="350" y2="120" stroke="#cbd5e1" stroke-width="2"/>
      </g>
    </svg>"""

def svg_email_format():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(40, 15)">
        <rect x="0" y="0" width="380" height="135" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
        <rect x="0" y="0" width="380" height="26" rx="8 8 0 0" fill="#f1f5f9"/>
        <text x="15" y="17" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#475569">To: centre.lead@masterfunctionalskills.co.uk</text>
        <text x="15" y="42" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#2563eb">Subject: Shift Cover Request - Saturday 18th Oct [Clear &amp; Specific]</text>
        <line x1="15" y1="50" x2="365" y2="50" stroke="#e2e8f0"/>
        <text x="15" y="68" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b">Dear Sarah,</text>
        <text x="15" y="86" font-family="system-ui, sans-serif" font-size="9" font-weight="500" fill="#475569">I am writing to confirm our clinic staffing plan...</text>
        <text x="15" y="112" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#1e293b">Kind regards,</text>
        <text x="15" y="125" font-family="system-ui, sans-serif" font-size="9.5" font-weight="800" fill="#0f172a">Subi • Healthcare Assistant</text>
      </g>
    </svg>"""

def svg_comma_rules():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 20)">
        <rect x="0" y="0" width="185" height="85" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.8"/>
        <text x="92" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#1d4ed8" text-anchor="middle">1. COMMAS IN LISTS</text>
        <text x="10" y="48" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">"I packed gloves<tspan fill="#e11d48" font-weight="900">,</tspan> masks<tspan fill="#e11d48" font-weight="900">,</tspan></text>
        <text x="10" y="68" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">bandages and saline."</text>
      </g>
      <g transform="translate(245, 20)">
        <rect x="0" y="0" width="185" height="85" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="1.8"/>
        <text x="92" y="24" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#065f46" text-anchor="middle">2. FRONTED ADVERBIAL</text>
        <text x="10" y="48" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">"Early yesterday morning<tspan fill="#e11d48" font-weight="900">,</tspan></text>
        <text x="10" y="68" font-family="system-ui, sans-serif" font-size="9.5" font-weight="600" fill="#1e293b">the ward team assembled."</text>
      </g>
      <rect x="30" y="118" width="400" height="32" rx="6" fill="#fef2f2" stroke="#ef4444"/>
      <text x="230" y="138" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#991b1b" text-anchor="middle">
        ⚠️ COMMA SPLICE TRAP: Never join 2 full sentences with just a comma!
      </text>
    </svg>"""

def svg_paf_purpose():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 20)">
        <rect x="0" y="0" width="115" height="110" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <text x="57" y="28" font-family="system-ui, sans-serif" font-size="18" font-weight="900" fill="#1d4ed8" text-anchor="middle">P</text>
        <text x="57" y="48" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#1e40af" text-anchor="middle">PURPOSE</text>
        <text x="57" y="72" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">Why write?</text>
        <text x="57" y="90" font-family="system-ui, sans-serif" font-size="8.5" font-weight="600" fill="#475569" text-anchor="middle">Persuade/Inform</text>
      </g>
      <g transform="translate(170, 20)">
        <rect x="0" y="0" width="115" height="110" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
        <text x="57" y="28" font-family="system-ui, sans-serif" font-size="18" font-weight="900" fill="#047857" text-anchor="middle">A</text>
        <text x="57" y="48" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#065f46" text-anchor="middle">AUDIENCE</text>
        <text x="57" y="72" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">Who reads it?</text>
        <text x="57" y="90" font-family="system-ui, sans-serif" font-size="8.5" font-weight="600" fill="#475569" text-anchor="middle">Public / Manager</text>
      </g>
      <g transform="translate(310, 20)">
        <rect x="0" y="0" width="115" height="110" rx="8" fill="#fffbeb" stroke="#f59e0b" stroke-width="2"/>
        <text x="57" y="28" font-family="system-ui, sans-serif" font-size="18" font-weight="900" fill="#b45309" text-anchor="middle">F</text>
        <text x="57" y="48" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#92400e" text-anchor="middle">FORMAT</text>
        <text x="57" y="72" font-family="system-ui, sans-serif" font-size="9" font-weight="700" fill="#475569" text-anchor="middle">What layout?</text>
        <text x="57" y="90" font-family="system-ui, sans-serif" font-size="8.5" font-weight="600" fill="#475569" text-anchor="middle">Letter/Email/Article</text>
      </g>
    </svg>"""

def svg_capital_letters():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(40, 15)">
        <rect x="0" y="0" width="380" height="135" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
        <text x="190" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="800" fill="#1e293b" text-anchor="middle">ALWAYS CAPITALISE (M.I.N.T.S.)</text>
        <text x="20" y="50" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#2563eb">M</text>
        <text x="40" y="50" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#475569">= Months &amp; Days (October, Friday)</text>
        <text x="20" y="70" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#2563eb">I</text>
        <text x="40" y="70" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#475569">= The word "I" alone ("When I arrived...")</text>
        <text x="20" y="90" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#2563eb">N</text>
        <text x="40" y="90" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#475569">= Names of people &amp; places (Carmen, London)</text>
        <text x="20" y="110" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#2563eb">T</text>
        <text x="40" y="110" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#475569">= Titles of books &amp; films (Pride and Prejudice)</text>
        <text x="20" y="130" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#2563eb">S</text>
        <text x="40" y="130" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#475569">= Start of every sentence</text>
      </g>
    </svg>"""

def svg_spreadsheet_formulas():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 15)">
        <rect x="0" y="0" width="400" height="26" rx="4" fill="#f1f5f9" stroke="#cbd5e1"/>
        <text x="12" y="17" font-family="monospace, sans-serif" font-size="11" font-weight="800" fill="#2563eb">fx</text>
        <text x="35" y="17" font-family="monospace, sans-serif" font-size="12" font-weight="800" fill="#0f172a">=SUM(B2:B5)</text>
        <g transform="translate(0, 32)">
          <rect x="0" y="0" width="400" height="75" fill="#ffffff" stroke="#cbd5e1"/>
          <rect x="0" y="0" width="40" height="20" fill="#e2e8f0" stroke="#cbd5e1"/>
          <rect x="40" y="0" width="120" height="20" fill="#e2e8f0" stroke="#cbd5e1"/>
          <text x="100" y="14" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#475569" text-anchor="middle">A (Item)</text>
          <rect x="160" y="0" width="120" height="20" fill="#e2e8f0" stroke="#cbd5e1"/>
          <text x="220" y="14" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#475569" text-anchor="middle">B (Cost)</text>
          <text x="20" y="38" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">2</text>
          <text x="100" y="38" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#1e293b" text-anchor="middle">PPE Masks</text>
          <text x="220" y="38" font-family="monospace, sans-serif" font-size="10" font-weight="800" fill="#059669" text-anchor="middle">£12.50</text>
          <text x="20" y="58" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#64748b" text-anchor="middle">3</text>
          <text x="100" y="58" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#1e293b" text-anchor="middle">Sanitiser</text>
          <text x="220" y="58" font-family="monospace, sans-serif" font-size="10" font-weight="800" fill="#059669" text-anchor="middle">£8.00</text>
          <rect x="160" y="20" width="120" height="45" fill="none" stroke="#2563eb" stroke-width="2"/>
        </g>
      </g>
      <g transform="translate(30, 125)">
        <rect x="0" y="0" width="400" height="30" rx="6" fill="#f8fafc" stroke="#cbd5e1"/>
        <text x="200" y="20" font-family="monospace, sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">
          =SUM(range) | =AVERAGE(range) | =MAX(range) | =MIN(range)
        </text>
      </g>
    </svg>"""

def svg_phishing_flags():
    return """<svg viewBox="0 0 460 170" width="100%" height="170" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 15)">
        <rect x="0" y="0" width="400" height="135" rx="8" fill="#ffffff" stroke="#ef4444" stroke-width="2"/>
        <rect x="0" y="0" width="400" height="24" rx="8 8 0 0" fill="#fee2e2"/>
        <text x="15" y="16" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#b91c1c">⚠️ SUSPICIOUS EMAIL RECEIVED</text>
        <text x="15" y="44" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b">From: security@oxf0rd-health-service.co.biz</text>
        <rect x="270" y="32" width="120" height="18" rx="4" fill="#ef4444"/>
        <text x="330" y="45" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" fill="#ffffff" text-anchor="middle">🚩 FAKE DOMAIN</text>
        <text x="15" y="70" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b">"URGENT: Your account will be locked in 1 hour!"</text>
        <rect x="270" y="58" width="120" height="18" rx="4" fill="#ef4444"/>
        <text x="330" y="71" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" fill="#ffffff" text-anchor="middle">🚩 FALSE PANIC</text>
        <text x="15" y="96" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#1e293b">Greeting: "Dear Valued Customer" (Not your name)</text>
        <rect x="270" y="84" width="120" height="18" rx="4" fill="#ef4444"/>
        <text x="330" y="97" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" fill="#ffffff" text-anchor="middle">🚩 GENERIC GREETING</text>
        <text x="15" y="122" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#2563eb">Link: Click Here ➔ (points to external scam site)</text>
        <rect x="270" y="110" width="120" height="18" rx="4" fill="#ef4444"/>
        <text x="330" y="123" font-family="system-ui, sans-serif" font-size="8.5" font-weight="800" fill="#ffffff" text-anchor="middle">🚩 MISMATCHED URL</text>
      </g>
    </svg>"""

def svg_strong_passwords_2fa():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(30, 20)">
        <rect x="0" y="0" width="185" height="120" rx="8" fill="#eff6ff" stroke="#3b82f6" stroke-width="2"/>
        <text x="92" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="900" fill="#1d4ed8" text-anchor="middle">PASSPHRASE</text>
        <rect x="15" y="38" width="155" height="30" rx="6" fill="#1e293b"/>
        <text x="92" y="58" font-family="monospace, sans-serif" font-size="10.5" font-weight="800" fill="#38bdf8" text-anchor="middle">Blue#Tiger!Walk99</text>
        <text x="92" y="88" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">✓ 3+ Random Words</text>
        <text x="92" y="104" font-family="system-ui, sans-serif" font-size="9.5" font-weight="700" fill="#059669" text-anchor="middle">✓ Symbols + Numbers</text>
      </g>
      <g transform="translate(245, 20)">
        <rect x="0" y="0" width="185" height="120" rx="8" fill="#ecfdf5" stroke="#10b981" stroke-width="2"/>
        <text x="92" y="24" font-family="system-ui, sans-serif" font-size="12" font-weight="900" fill="#065f46" text-anchor="middle">2-FACTOR AUTH (2FA)</text>
        <text x="92" y="48" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">1. Something you KNOW (Password)</text>
        <text x="92" y="66" font-family="system-ui, sans-serif" font-size="12" font-weight="900" fill="#059669" text-anchor="middle">+</text>
        <text x="92" y="86" font-family="system-ui, sans-serif" font-size="10" font-weight="700" fill="#475569" text-anchor="middle">2. Something you HAVE (Phone)</text>
        <rect x="35" y="94" width="115" height="20" rx="4" fill="#059669"/>
        <text x="92" y="108" font-family="monospace, sans-serif" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">OTP: 492 817</text>
      </g>
    </svg>"""

def svg_file_management():
    return """<svg viewBox="0 0 460 165" width="100%" height="165" xmlns="http://www.w3.org/2000/svg">
      <g transform="translate(40, 15)">
        <rect x="0" y="0" width="380" height="135" rx="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8"/>
        <text x="20" y="26" font-family="system-ui, sans-serif" font-size="11" font-weight="800" fill="#2563eb">📁 Documents</text>
        <text x="45" y="48" font-family="system-ui, sans-serif" font-size="11" font-weight="700" fill="#d97706">└── 📁 Master_Functional_Skills_Centre</text>
        <text x="80" y="70" font-family="system-ui, sans-serif" font-size="10.5" font-weight="700" fill="#059669">├── 📁 Maths_Level_2</text>
        <text x="110" y="88" font-family="system-ui, sans-serif" font-size="10" font-weight="600" fill="#475569">└── 📄 Trapezium_Area_2026-10-11.pdf ✓</text>
        <rect x="15" y="104" width="350" height="24" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
        <text x="190" y="120" font-family="system-ui, sans-serif" font-size="10" font-weight="800" fill="#0f172a" text-anchor="middle">
          Naming: Topic_Version_Date.pdf (Never "final_doc_new2.pdf"!)
        </text>
      </g>
    </svg>"""

## =============================================================================
# COMPLETE CURRICULUM-MAPPED REVISION CARDS (ALL 6 DECKS - 266 CARDS)
# =============================================================================
from decks import maths_l2
from decks import maths_l1
from decks import english_l2
from decks import english_l1
from decks import digital_skills
from decks import entry_level_3

OVERHAULED_CARDS = (
    maths_l2.CARDS +
    maths_l1.CARDS +
    english_l2.CARDS +
    english_l1.CARDS +
    digital_skills.CARDS +
    entry_level_3.CARDS
)

# Theme colors dictionary
THEMES = {
    "emerald": {"primary": "#059669", "pill_bg": "#064e3b", "border": "#10b981", "badge_bg": "#d1fae5", "badge_text": "#065f46"},
    "teal": {"primary": "#0d9488", "pill_bg": "#134e4a", "border": "#14b8a6", "badge_bg": "#ccfbf1", "badge_text": "#115e59"},
    "orange": {"primary": "#ea580c", "pill_bg": "#7c2d12", "border": "#f97316", "badge_bg": "#ffedd5", "badge_text": "#9a3412"},
    "amber": {"primary": "#d97706", "pill_bg": "#78350f", "border": "#f59e0b", "badge_bg": "#fef3c7", "badge_text": "#92400e"},
    "purple": {"primary": "#7c3aed", "pill_bg": "#4c1d95", "border": "#8b5cf6", "badge_bg": "#ede9fe", "badge_text": "#5b21b6"},
    "blue": {"primary": "#2563eb", "pill_bg": "#1e3a8a", "border": "#3b82f6", "badge_bg": "#dbeafe", "badge_text": "#1e40af"},
    "cyan": {"primary": "#0891b2", "pill_bg": "#164e63", "border": "#06b6d4", "badge_bg": "#cffafe", "badge_text": "#155e75"},
    "rose": {"primary": "#e11d48", "pill_bg": "#881337", "border": "#f43f5e", "badge_bg": "#ffe4e6", "badge_text": "#9f1239"}
}

def validate_svgs():
    for card in OVERHAULED_CARDS:
        try:
            ET.fromstring(card["svg_html"])
        except Exception as e:
            print(f"ERROR in SVG for {card['title']}: {e}")
            raise


def apply_tight_viewboxes():
    """Tighten SVG viewBoxes to remove dead outer whitespace so diagrams and examples
    fill the maximum possible space without altering internal layouts, fonts or coordinates."""
    import re
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "data", "card_viewboxes.json")
    if not os.path.exists(path):
        print("! card_viewboxes.json not found, skipping viewBox tightening")
        return
    with open(path, "r", encoding="utf-8") as f:
        boxes = json.load(f)
    if "m-l2-017" in boxes and "m-l2-17" not in boxes:
        boxes["m-l2-17"] = boxes["m-l2-017"]
    applied = 0
    for card in OVERHAULED_CARDS:
        cid = card.get("id")
        if cid in boxes and boxes[cid] and cid != "m-l2-23" and cid != "m-l1-33":
            b = boxes[cid]
            bx, by, bw, bh = b["x"], b["y"], b["w"], b["h"]
            new_vb = f'viewBox="{bx} {by} {bw} {bh}"'
            card["svg_html"] = re.sub(r'viewBox="[^"]+"', new_vb, card["svg_html"])
            applied += 1
    print(f"✓ Maximized {applied}/{len(OVERHAULED_CARDS)} diagrams and examples to fill full container space!")


def generate_js():
    local_dir = os.path.dirname(os.path.abspath(__file__))
    target_paths = [
        os.path.join(local_dir, "assets", "js", "revision_cards_data.js"),
        "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/assets/js/revision_cards_data.js"
    ]
    payload = "/**\n * Master Functional Skills - Overhauled Visual Revision Cards Deck\n"
    payload += f" * Total Cards: {len(OVERHAULED_CARDS)} mapped across Maths, English & Digital Skills\n */\n"
    payload += "window.MFS_OVERHAULED_CARDS = "
    payload += json.dumps(OVERHAULED_CARDS, indent=2, ensure_ascii=False)
    payload += ";\n\n// Backwards compatibility mirror\n"
    payload += "window.MFS_REVISION_CARDS = window.MFS_OVERHAULED_CARDS;\n"
    
    for target_path in target_paths:
        try:
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(payload)
            print(f"Generated JS Data: {target_path} ({len(OVERHAULED_CARDS)} visual cards)")
        except Exception as e:
            print(f"Warning: could not write JS to {target_path}: {e}")

DECK_METADATA = {
    "all_cards": {
        "key": "all_cards",
        "title": "Functional Skills Revision Cards",
        "subtitle": "Complete All-In-One Visual Revision Deck",
        "subject_tag": "Mathematics • English • Digital Skills",
        "level_label": "Entry Level 3, Level 1 & Level 2",
        "badge_level": "All Levels (Ofqual Regulated)",
        "gradient": "linear-gradient(135deg, #0b1329 0%, #1e3a8a 50%, #1d4ed8 100%)",
        "accent": "#60a5fa",
        "features": [
            "Mapped to UK DfE &amp; Ofqual Subject Criteria",
            "Pearson Edexcel &amp; City &amp; Guilds Aligned",
            "Visual Diagrams &amp; Golden Rules on Every Card",
            "Quick Exam Challenges &amp; Step-by-Step Model Steps",
            "A6 Postcard Cardstock Size (148 × 105 mm)"
        ]
    },
    "maths_l2": {
        "key": "maths_l2",
        "title": "Maths Level 2 Revision Cards",
        "subtitle": "Visual Rules • Exam Challenges • Step-by-Step Solutions",
        "subject_tag": "Functional Skills Mathematics",
        "level_label": "Level 2 (GCSE Grade 4 / C Equivalent)",
        "badge_level": "Level 2 Specialist",
        "gradient": "linear-gradient(135deg, #064e3b 0%, #047857 50%, #059669 100%)",
        "accent": "#34d399",
        "features": [
            "Shapes, Circles, Trapeziums &amp; Cylinders",
            "Reverse Percentages &amp; Compound Interest",
            "Reverse Ratios &amp; Grouped Frequency Mean",
            "Step-by-Step Pearson &amp; C&amp;G Model Answers"
        ]
    },
    "maths_l1": {
        "key": "maths_l1",
        "title": "Maths Level 1 Revision Cards",
        "subtitle": "Visual Rules • Exam Challenges • Step-by-Step Solutions",
        "subject_tag": "Functional Skills Mathematics",
        "level_label": "Level 1 Functional Skills",
        "badge_level": "Level 1 Essential",
        "gradient": "linear-gradient(135deg, #0c4a6e 0%, #0284c7 50%, #38bdf8 100%)",
        "accent": "#7dd3fc",
        "features": [
            "Perimeter, Area &amp; Metric Conversions",
            "Fractions, Decimals, Percentages &amp; BODMAS",
            "Averages (Mean &amp; Range) &amp; Probability",
            "Targeted Exam Hacks &amp; Common Traps"
        ]
    },
    "english_l2": {
        "key": "english_l2",
        "title": "English Level 2 Revision Cards",
        "subtitle": "Reading • Writing Formats • SPaG • Speaking & Listening",
        "subject_tag": "Functional Skills English",
        "level_label": "Level 2 (GCSE Grade 4 / C Equivalent)",
        "badge_level": "Level 2 Complete Suite",
        "gradient": "linear-gradient(135deg, #312e81 0%, #4338ca 50%, #6366f1 100%)",
        "accent": "#a5b4fc",
        "features": [
            "Formal Letters, Reports, Articles &amp; Reviews",
            "Persuasive Devices, Tone &amp; Text Comparison",
            "Punctuation, Complex Sentences &amp; SPaG",
            "Speaking, Listening &amp; Communicating (SLC)"
        ]
    },
    "english_l1": {
        "key": "english_l1",
        "title": "English Level 1 Revision Cards",
        "subtitle": "Reading • Writing Layouts • SPaG • Speaking & Listening",
        "subject_tag": "Functional Skills English",
        "level_label": "Level 1 Functional Skills",
        "badge_level": "Level 1 Complete Suite",
        "gradient": "linear-gradient(135deg, #134e4a 0%, #0f766e 50%, #14b8a6 100%)",
        "accent": "#5eead4",
        "features": [
            "Professional Email, Letter &amp; Article Layouts",
            "Purpose of Text (Inform, Persuade, Instruct)",
            "Apostrophes, Commas &amp; Core Spellings",
            "Speaking, Listening &amp; Communicating (SLC)"
        ]
    },
    "digital_skills": {
        "key": "digital_skills",
        "title": "Digital Functional Skills Revision Cards",
        "subtitle": "Spreadsheet Formulas • Online Security • Devices",
        "subject_tag": "Digital Functional Skills (DFSQ)",
        "level_label": "Level 1 & Entry Level 3",
        "badge_level": "Digital DFSQ Standard",
        "gradient": "linear-gradient(135deg, #7c2d12 0%, #c2410c 50%, #ea580c 100%)",
        "accent": "#fdba74",
        "features": [
            "Essential Excel/Sheets Formulas (=SUM, =AVERAGE)",
            "Strong Passwords &amp; Two-Factor Authentication",
            "File Extensions (.pdf, .docx, .xlsx, .csv)",
            "Phishing Detection &amp; GDPR Privacy Rules"
        ]
    },
    "entry_level_3": {
        "key": "entry_level_3",
        "title": "Entry Level 3 Revision Cards",
        "subtitle": "Core Maths • English • Digital Foundations",
        "subject_tag": "Functional Skills Foundations",
        "level_label": "Entry Level 3 (Edexcel & C&G)",
        "badge_level": "Entry Level 3 Core",
        "gradient": "linear-gradient(135deg, #78350f 0%, #b45309 50%, #d97706 100%)",
        "accent": "#fde68a",
        "features": [
            "Column Addition, Subtraction, Division &amp; Fractions",
            "24-Hour Time, Money, Metric Units &amp; Scales",
            "Reading Purpose, Email Layout, SPaG &amp; SLC",
            "Device Settings, Shortcuts, Spreadsheets &amp; Safety"
        ]
    }
}

LOGO_BADGE_WHITE = """
<div style="background:#ffffff; padding:3px 8px; border-radius:6px; box-shadow:0 2px 6px rgba(0,0,0,0.25); display:inline-flex; align-items:center; gap:5px;">
  <svg viewBox="0 0 64 64" width="18" height="18" style="vertical-align:middle; flex-shrink:0;">
    <rect x="2" y="2" width="60" height="60" rx="12" fill="#1d4ed8"/>
    <path d="M 32 10 L 48 17 L 32 24 L 16 17 Z" fill="#60a5fa"/>
    <path d="M 44 20.5 L 44 28 C 44 31 38 33 32 33 C 26 33 20 31 20 28 L 20 20.5" fill="none" stroke="#60a5fa" stroke-width="2.5"/>
    <path d="M 48 17 L 50 25" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="50" cy="26" r="1.5" fill="#f59e0b"/>
    <path d="M 17 50 L 17 29 L 24 29 L 32 41 L 40 29 L 47 29 L 47 50 L 40 50 L 40 37 L 34 46 L 30 46 L 24 37 L 24 50 Z" fill="#ffffff"/>
  </svg>
  <span style="font-weight:900; color:#0f172a; font-size:7.8pt; letter-spacing:0.2px;">MASTER<span style="color:#2563eb;">FUNCTIONALSKILLS</span></span>
</div>
"""

FOOTER_LOGO_MICRO = """
<div class="card-footer-logo" style="display:inline-flex; align-items:center; gap:4px;">
  <svg viewBox="0 0 64 64" width="13" height="13" style="border-radius:2px; flex-shrink:0;">
    <rect x="2" y="2" width="60" height="60" rx="12" fill="#1d4ed8"/>
    <path d="M 32 10 L 48 17 L 32 24 L 16 17 Z" fill="#60a5fa"/>
    <path d="M 44 20.5 L 44 28 C 44 31 38 33 32 33 C 26 33 20 31 20 28 L 20 20.5" fill="none" stroke="#60a5fa" stroke-width="2.5"/>
    <path d="M 48 17 L 50 25" stroke="#f59e0b" stroke-width="2"/>
    <circle cx="50" cy="26" r="1.5" fill="#f59e0b"/>
    <path d="M 17 50 L 17 29 L 24 29 L 32 41 L 40 29 L 47 29 L 47 50 L 40 50 L 40 37 L 34 46 L 30 46 L 24 37 L 24 50 Z" fill="#ffffff"/>
  </svg>
  <span style="font-weight:900; color:#0f172a; font-size:6.3pt; letter-spacing:0.2px;">MASTER<span style="color:#2563eb;">FUNCTIONALSKILLS</span></span>
</div>
"""

def render_cover_card_front_html(deck_meta, is_quadrant=False):
    features_html = "".join([f'<div style="display:flex; align-items:center; gap:4px;"><span>★</span> <span>{feat}</span></div>' for feat in deck_meta["features"]])
    inner_content = f"""
    <!-- TOP ROW -->
    <div style="display:flex; justify-content:space-between; align-items:center;">
      {LOGO_BADGE_WHITE}
      <div style="background:rgba(255,255,255,0.22); border:1px solid rgba(255,255,255,0.45); color:#ffffff; font-weight:800; font-size:7.8pt; padding:3.5px 10px; border-radius:12px; letter-spacing:0.4px;">
        ★ OFQUAL REGULATED STANDARDS
      </div>
    </div>

    <!-- HORIZONTAL ACCENT STRIP (PFS STYLE) -->
    <div style="background:#0f172a; color:#f8fafc; border-radius:6px; padding:4px 12px; display:flex; justify-content:space-between; align-items:center; margin:2.5mm 0 1.5mm; box-shadow:0 2px 4px rgba(0,0,0,0.2);">
      <span style="font-size:8.5pt; font-weight:900; letter-spacing:0.8px; text-transform:uppercase; color:{deck_meta['accent']};">{deck_meta['subject_tag']}</span>
      <span style="font-size:7.8pt; font-weight:800; background:{deck_meta['accent']}; color:#0f172a; padding:2px 8px; border-radius:10px;">{deck_meta['badge_level']}</span>
    </div>

    <!-- MAIN TITLE -->
    <div style="margin:1mm 0;">
      <div style="font-size:21pt; font-weight:900; line-height:1.05; letter-spacing:-0.5px; text-shadow:0 2px 4px rgba(0,0,0,0.3); color:#ffffff;">
        {deck_meta['title']}
      </div>
      <div style="font-size:10.5pt; font-weight:700; color:#fef08a; margin-top:1.5mm; letter-spacing:0.2px;">
        {deck_meta['subtitle']}
      </div>
    </div>

    <!-- FEATURES BOX -->
    <div style="background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.25); border-radius:7px; padding:2.5mm 4mm; display:grid; grid-template-columns:1fr 1fr; gap:2mm 3.5mm; font-size:7.8pt; font-weight:700;">
      {features_html}
    </div>

    <!-- FOOTER -->
    <div style="display:flex; justify-content:space-between; align-items:center; border-top:1px solid rgba(255,255,255,0.25); padding-top:2mm; margin-top:1mm; font-size:7.5pt; color:rgba(255,255,255,0.95); font-weight:800;">
      <span>A6 Postcard Cardstock (148 × 105 mm)</span>
      <span style="color:#fde047;">Turn over for Deck Contents &amp; Checklist ➔</span>
      <span>masterfunctionalskills.co.uk</span>
    </div>
"""
    if is_quadrant:
        return f"""
  <div class="a6-quadrant">
    <div class="postcard-inner" style="background:{deck_meta['gradient']}; border-color:transparent; padding:4mm 6mm 3mm; box-sizing:border-box; color:#ffffff;">
      {inner_content}
    </div>
  </div>
"""
    else:
        return f"""
  <div class="a6-card" style="background:{deck_meta['gradient']}; color:#ffffff; display:flex; flex-direction:column; justify-content:space-between; padding:5mm 7mm 4mm; box-sizing:border-box;">
    {inner_content}
  </div>
"""

def render_cover_card_back_html(deck_meta, cards, is_quadrant=False):
    if len(cards) > 60:
        # Master All-In-One Deck: Comprehensive 6-Deck Curriculum Overview (266 Cards)
        contents_inner = f"""
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:2mm; font-size:5.8pt; color:#1e293b; margin-bottom:1.2mm;">
        <div style="background:#f0fdf4; border:1px solid #bbf7d0; border-radius:4px; padding:1.5mm;">
          <div style="font-weight:900; color:#065f46; font-size:6.4pt; margin-bottom:0.8mm;">📐 MATHEMATICS SUITE (88 Cards)</div>
          <div style="margin-bottom:0.5mm;"><strong>Deck 1: Maths Level 2</strong> • 50 Cards (#1–#50)</div>
          <div style="color:#047857; font-size:5.0pt; margin-bottom:0.8mm;">Number (1–18) • Measures &amp; Space (19–36) • Data (37–50)</div>
          <div style="margin-bottom:0.5mm;"><strong>Deck 2: Maths Level 1</strong> • 38 Cards (#1–#38)</div>
          <div style="color:#047857; font-size:5.0pt;">Number (1–14) • Shape &amp; Space (15–28) • Handling Data (29–38)</div>
        </div>
        <div style="background:#f5f3ff; border:1px solid #ddd6fe; border-radius:4px; padding:1.5mm;">
          <div style="font-weight:900; color:#4338ca; font-size:6.4pt; margin-bottom:0.8mm;">✍️ ENGLISH SUITE (98 Cards)</div>
          <div style="margin-bottom:0.5mm;"><strong>Deck 3: English Level 2</strong> • 52 Cards (#1–#52)</div>
          <div style="color:#4c1d95; font-size:5.0pt; margin-bottom:0.8mm;">Reading (1–18) • Writing (19–33) • SPaG (34–48) • SLC (49–52)</div>
          <div style="margin-bottom:0.5mm;"><strong>Deck 4: English Level 1</strong> • 46 Cards (#1–#46)</div>
          <div style="color:#4c1d95; font-size:5.0pt;">Reading (1–15) • Writing (16–28) • SPaG (29–42) • SLC (43–46)</div>
        </div>
      </div>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:2mm; font-size:5.8pt;">
        <div style="background:#fff7ed; border:1px solid #fed7aa; border-radius:4px; padding:1.5mm; color:#9a3412;">
          <div style="font-weight:900; color:#c2410c; font-size:6.2pt; margin-bottom:0.5mm;">💻 DIGITAL SKILLS (50 Cards)</div>
          <div style="font-size:5.0pt; color:#7c2d12; line-height:1.25;">
            Devices (1–10) • Creating &amp; Spreadsheets (11–24) • Communicating (25–32) • Transacting (33–40) • Security (41–50)
          </div>
        </div>
        <div style="background:#fffbeb; border:1px solid #fde68a; border-radius:4px; padding:1.5mm; color:#92400e;">
          <div style="font-weight:900; color:#b45309; font-size:6.2pt; margin-bottom:0.5mm;">🌟 ENTRY LEVEL 3 (30 Cards)</div>
          <div style="font-size:5.0pt; color:#78350f; line-height:1.25;">
            Entry 3 Maths Foundations (1–14) • Entry 3 English Reading, Writing, SPaG &amp; SLC (15–24) • Entry 3 Digital Skills (25–30)
          </div>
        </div>
      </div>
      <div style="margin-top:1.2mm; background:#f8fafc; border:1px solid #e2e8f0; border-radius:4px; padding:1.2mm 2mm; font-size:5.4pt; color:#475569; display:flex; justify-content:space-between;">
        <span><strong>Total Cards in Collection:</strong> {len(cards)} Dual-Coded Postcards</span>
        <span><strong>Standards:</strong> DfE Statutory Subject Content • Pearson Edexcel &amp; City &amp; Guilds</span>
      </div>
"""
    elif len(cards) <= 12:
        rows_html = ""
        for c in cards:
            rows_html += f"""
        <tr style="border-bottom:1px solid #f1f5f9; background:#ffffff;">
          <td style="padding:2.2px 4px; font-weight:800; color:#2563eb; text-align:center;">{c['number']}</td>
          <td style="padding:2.2px 4px; font-weight:700; color:#475569;">{c['dfe_code']}</td>
          <td style="padding:2.2px 4px; font-weight:700; color:#0f172a;">{c['title']}</td>
          <td style="padding:2.2px 4px; color:#64748b;">{c['strand_name']}</td>
          <td style="padding:2.2px 4px; text-align:center;"><span style="display:inline-block; width:10px; height:10px; border:1.2px solid #94a3b8; border-radius:2px;"></span></td>
          <td style="padding:2.2px 4px; text-align:center;"><span style="display:inline-block; width:10px; height:10px; border:1.2px solid #94a3b8; border-radius:2px;"></span></td>
        </tr>
"""
        contents_inner = f"""
      <table style="width:100%; border-collapse:collapse; font-size:6.8pt; line-height:1.25;">
        <thead>
          <tr style="background:#e2e8f0; color:#1e293b; text-align:left; font-weight:800;">
            <th style="padding:2.5px 4px; width:7%; text-align:center;">#</th>
            <th style="padding:2.5px 4px; width:17%;">DfE Code</th>
            <th style="padding:2.5px 4px; width:45%;">Topic &amp; Core Concept</th>
            <th style="padding:2.5px 4px; width:17%;">Strand</th>
            <th style="padding:2.5px 4px; width:7%; text-align:center;">Read</th>
            <th style="padding:2.5px 4px; width:7%; text-align:center;">Solved</th>
          </tr>
        </thead>
        <tbody>
          {rows_html}
        </tbody>
      </table>
"""
    else:
        mid = (len(cards) + 1) // 2
        col1 = cards[:mid]
        col2 = cards[mid:]
        
        row_font_size = "4.4pt" if len(cards) > 48 else ("4.7pt" if len(cards) > 40 else ("5.2pt" if len(cards) > 28 else "5.8pt"))
        row_padding = "0.35px 1px" if len(cards) > 48 else ("0.5px 1px" if len(cards) > 40 else ("0.8px 2px" if len(cards) > 28 else "1.2px 2px"))
        box_dim = "6.5px" if len(cards) > 40 else "7.5px"

        def render_col(col_cards):
            c_html = ""
            for c in col_cards:
                c_html += f"""
            <div style="display:flex; justify-content:space-between; align-items:center; padding:{row_padding}; border-bottom:1px solid #f1f5f9; font-size:{row_font_size};">
              <span style="white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:86%;"><strong>{c['number']}.</strong> {c['title']} <span style="color:#64748b;">({c['dfe_code']})</span></span>
              <span style="display:flex; gap:2.5px; flex-shrink:0;">
                <span style="display:inline-block; width:{box_dim}; height:{box_dim}; border:1px solid #94a3b8; border-radius:1.5px;"></span>
                <span style="display:inline-block; width:{box_dim}; height:{box_dim}; border:1px solid #94a3b8; border-radius:1.5px;"></span>
              </span>
            </div>
"""
            return c_html

        contents_inner = f"""
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:2.5mm;">
        <div>{render_col(col1)}</div>
        <div>{render_col(col2)}</div>
      </div>
"""


    inner_content = f"""
    <!-- HEADER -->
    <div style="background:#0f172a; color:#ffffff; padding:1.8mm 4mm; display:flex; justify-content:space-between; align-items:center;">
      <div style="font-size:7.8pt; font-weight:900; letter-spacing:0.3px;">
        📋 DECK CONTENTS &amp; REVISION CHECKLIST
      </div>
      <div style="font-size:6.8pt; font-weight:700; background:{deck_meta['accent']}; color:#0f172a; padding:1.5px 7px; border-radius:10px;">
        {len(cards)} Revision Cards
      </div>
    </div>

    <!-- INSTRUCTIONS -->
    <div style="background:#f1f5f9; border-bottom:1px solid #cbd5e1; padding:1.0mm 4mm; font-size:6.2pt; color:#334155; font-weight:700; display:flex; justify-content:space-between;">
      <span>Tick <strong>[✓] Read</strong> when you understand the rule, and <strong>[★] Solved</strong> when you answer the challenge!</span>
      <span style="color:#2563eb;">Pearson &amp; C&amp;G Aligned</span>
    </div>

    <!-- CONTENTS WRAP -->
    <div style="flex:1; padding:1.2mm 3.5mm; overflow:hidden;">
      {contents_inner}
    </div>

    <!-- TUTOR TIP -->
    <div style="background:#eff6ff; border-top:1px solid #bfdbfe; padding:1.2mm 4mm; font-size:6.0pt; color:#1e40af; line-height:1.2;">
      💡 <strong>Tutor Golden Tip (Abdul):</strong> Do not flip the card immediately! Attempt the Quick Challenge on the back using a dry-wipe pen or scratchpad first. Verify with the step-by-step model steps only after completing your working.
    </div>

    <!-- FOOTER -->
    <div class="card-footer" style="height:5.2mm; background:#f8fafc; border-top:1px solid #e2e8f0; padding:1px 4mm; display:flex; justify-content:space-between; align-items:center; font-size:6.5pt; color:#64748b; font-weight:700;">
      <span>masterfunctionalskills.co.uk • Free Interactive Web Deck</span>
      {FOOTER_LOGO_MICRO}
    </div>
"""

    if is_quadrant:
        return f"""
  <div class="a6-quadrant">
    <div class="postcard-inner" style="background:#ffffff; overflow:hidden;">
      {inner_content}
    </div>
  </div>
"""
    else:
        return f"""
  <div class="a6-card" style="background:#ffffff; color:#0f172a; display:flex; flex-direction:column; justify-content:space-between; box-sizing:border-box;">
    {inner_content}
  </div>
"""


def render_a6_individual_html(cards, deck_title="Functional Skills A6 Pocket Cards", deck_meta=None):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{deck_title} | Master Functional Skills</title>
  <style>
    @page {{
      size: 148mm 105mm;
      margin: 0;
    }}
    * {{
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}
    body {{
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      background: #ffffff;
      color: #0f172a;
    }}
    .a6-card {{
      width: 148mm;
      height: 105mm;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      overflow: hidden;
      page-break-after: always;
      position: relative;
      box-sizing: border-box;
      background: #ffffff;
    }}
    .card-header-bar {{
      padding: 0 6.5mm;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #ffffff;
      height: 9.5mm;
      flex-shrink: 0;
    }}
    .header-left {{
      font-size: 10.5pt;
      font-weight: 900;
      letter-spacing: -0.2px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 108mm;
    }}
    .header-right {{
      background: rgba(0, 0, 0, 0.3);
      padding: 2px 8px;
      border-radius: 999px;
      font-size: 8pt;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      white-space: nowrap;
    }}
    .card-content {{
      padding: 1.6mm 6.5mm 1.2mm;
      flex: 1;
      min-height: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 1.0mm;
      box-sizing: border-box;
      overflow: hidden;
    }}
    .rule-headline {{
      font-size: 11.4pt;
      font-weight: 900;
      color: #0f172a;
      line-height: 1.15;
      margin-bottom: 0.5mm;
    }}
    .rule-explanation {{
      font-size: 8.8pt;
      font-weight: 600;
      color: #1e293b;
      line-height: 1.24;
    }}
    .diagram-holder {{
      background: #f8fafc;
      border: 1.5px solid #cbd5e1;
      border-radius: 7px;
      flex: 1;
      min-height: 24mm;
      max-height: 43mm;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      padding: 2px 4px;
    }}
    .diagram-holder svg {{
      width: 100%;
      height: 100%;
      max-height: 100%;
    }}
    .golden-rule-pill {{
      background: #ecfdf5;
      border: 1.5px solid #10b981;
      border-radius: 6px;
      padding: 2px 8px;
      font-size: 8.3pt;
      font-weight: 700;
      color: #065f46;
      line-height: 1.2;
    }}
    .watch-out-pill {{
      background: #fff1f2;
      border: 1.5px solid #f43f5e;
      border-radius: 6px;
      padding: 2px 8px;
      font-size: 8.3pt;
      font-weight: 700;
      color: #9f1239;
      line-height: 1.2;
    }}
    .card-footer {{
      background: #f8fafc;
      border-top: 1.5px solid #e2e8f0;
      padding: 0 6.5mm;
      display: flex;
      justify-content: space-between;
      font-size: 8pt;
      color: #475569;
      font-weight: 800;
      height: 5.5mm;
      align-items: center;
      flex-shrink: 0;
    }}
    .back-content {{
      padding: 2mm 6.5mm 1.5mm;
      flex: 1;
      min-height: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 1.5mm;
      background: #fafaf9;
      box-sizing: border-box;
      overflow: hidden;
    }}
    .challenge-box {{
      background: #ffffff;
      border: 2px solid #2563eb;
      border-radius: 7px;
      padding: 2.2mm 3.5mm;
      flex-shrink: 0;
    }}
    .challenge-title {{
      font-size: 8.2pt;
      font-weight: 900;
      color: #1d4ed8;
      display: flex;
      justify-content: space-between;
      margin-bottom: 0.6mm;
    }}
    .challenge-q {{
      font-size: 10.5pt;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.3;
    }}
    .working-area {{
      background: #ffffff;
      border: 1.5px dashed #94a3b8;
      border-radius: 6px;
      padding: 1.2mm 3.5mm;
      height: 9mm;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 8pt;
      font-weight: 600;
      color: #64748b;
      flex-shrink: 0;
    }}
    .answer-box {{
      background: #ecfdf5;
      border: 2px solid #059669;
      border-radius: 8px;
      padding: 2.4mm 3.5mm;
      flex: 1;
      min-height: 0;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }}
    .answer-title {{
      font-size: 8.6pt;
      font-weight: 900;
      color: #065f46;
      margin-bottom: 1mm;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .answer-body {{
      font-size: 10pt;
      font-weight: 700;
      color: #064e3b;
      line-height: 1.34;
    }}
  </style>
</head>
<body>
"""
    if deck_meta:
        html += render_cover_card_front_html(deck_meta, is_quadrant=False)
        html += render_cover_card_back_html(deck_meta, cards, is_quadrant=False)

    for card in cards:
        theme = THEMES.get(card.get("strand_theme", "emerald"), THEMES["emerald"])
        # PAGE 1: FRONT
        html += f"""
  <div class="a6-card">
    <div class="card-header-bar" style="background:{theme['primary']};">
      <div class="header-left">{card['number']}. {card['title']}</div>
      <div class="header-right">{card['strand_name']}</div>
    </div>
    <div class="card-content">
      <div style="flex-shrink:0;">
        <div class="rule-headline">{card['rule_heading']}</div>
        <div class="rule-explanation">{card['rule_body']}</div>
      </div>
      <div class="diagram-holder">
        {card['svg_html']}
      </div>
      <div style="display:flex; flex-direction:column; gap:1.0mm; flex-shrink:0;">
        <div class="golden-rule-pill">★ <strong>Golden Rule:</strong> {card['golden_rule']}</div>
        <div class="watch-out-pill">⚠️ <strong>Watch Out:</strong> {card['watch_out']}</div>
      </div>
    </div>
    <div class="card-footer">
      <span>{card['dfe_code']} • {card['level_label']}</span>
      <span style="color:{theme['primary']};">Turn over for Practice Challenge ➔</span>
      <span>Card {card['number']} of {len(cards)}</span>
    </div>
  </div>

  <!-- PAGE 2: BACK -->
  <div class="a6-card">
    <div class="card-header-bar" style="background:#1e293b;">
      <div class="header-left">Challenge: {card['title']}</div>
      <div class="header-right" style="background:{theme['primary']};">{card['strand_name']}</div>
    </div>
    <div class="back-content">
      <div class="challenge-box">
        <div class="challenge-title">
          <span>🎯 QUICK EXAM CHALLENGE</span>
          <span>{card['dfe_code']}</span>
        </div>
        <div class="challenge-q">{card['challenge_prompt']}</div>
      </div>
      <div class="working-area">
        <span>✏️ Learner Scratchpad &amp; Calculations</span>
        <span style="font-size:7.5pt; color:#94a3b8;">Formula Working Area</span>
      </div>
      <div class="answer-box">
        <div class="answer-title">
          <span>✓ STEP-BY-STEP OFFICIAL MODEL ANSWER</span>
          <span style="font-size:8pt; background:#059669; color:#fff; padding:1.5px 6px; border-radius:4px; font-weight:800;">FULL MARKS</span>
        </div>
        <div class="answer-body">
          {card['answer_text']}
        </div>
      </div>
    </div>
    <div class="card-footer">
      <span>Card {card['number']} of {len(cards)} • {card['dfe_code']}</span>
      <span style="color:#059669; font-weight:800;">✓ Official Tutor Solution</span>
      <div class="card-footer-logo" style="display:inline-flex; align-items:center; gap:4px;">
        <svg viewBox="0 0 64 64" width="13" height="13" style="border-radius:2px; flex-shrink:0;">
          <rect x="2" y="2" width="60" height="60" rx="12" fill="#1d4ed8"/>
          <path d="M 32 10 L 48 17 L 32 24 L 16 17 Z" fill="#60a5fa"/>
          <path d="M 44 20.5 L 44 28 C 44 31 38 33 32 33 C 26 33 20 31 20 28 L 20 20.5" fill="none" stroke="#60a5fa" stroke-width="2.5"/>
          <path d="M 48 17 L 50 25" stroke="#f59e0b" stroke-width="2"/>
          <circle cx="50" cy="26" r="1.5" fill="#f59e0b"/>
          <path d="M 17 50 L 17 29 L 24 29 L 32 41 L 40 29 L 47 29 L 47 50 L 40 50 L 40 37 L 34 46 L 30 46 L 24 37 L 24 50 Z" fill="#ffffff"/>
        </svg>
        <span style="font-weight:900; color:#0f172a; font-size:7pt; letter-spacing:0.2px;">MASTER<span style="color:#2563eb;">FUNCTIONALSKILLS</span></span>
      </div>
    </div>
  </div>
"""
    html += "</body>\n</html>"
    return html

def render_a4_4up_imposition_html(cards, deck_title="Functional Skills A4 Printable Sheets (4-per-page A6)", deck_meta=None):
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{deck_title} | Master Functional Skills</title>
  <style>
    @page {{
      size: 297mm 210mm;
      margin: 0;
    }}
    * {{
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
    }}
    body {{
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      background: #e2e8f0;
      color: #0f172a;
    }}
    .sheet-page {{
      width: 297mm;
      height: 210mm;
      margin: 0 auto;
      background: #ffffff;
      padding: 0;
      display: grid;
      grid-template-columns: 148.5mm 148.5mm;
      grid-template-rows: 105mm 105mm;
      page-break-after: always;
      position: relative;
    }}
    @media print {{
      body {{ background: transparent; }}
      .sheet-page {{ margin: 0; }}
    }}
    .cut-line-v {{
      position: absolute;
      top: 0;
      bottom: 0;
      left: 148.5mm;
      width: 0;
      border-left: 1px dashed #94a3b8;
      pointer-events: none;
      z-index: 10;
    }}
    .cut-line-h {{
      position: absolute;
      left: 0;
      right: 0;
      top: 105mm;
      height: 0;
      border-top: 1px dashed #94a3b8;
      pointer-events: none;
      z-index: 10;
    }}
    .a6-quadrant {{
      width: 148.5mm;
      height: 105mm;
      padding: 1.5mm;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-sizing: border-box;
    }}
    .postcard-inner {{
      width: 100%;
      height: 100%;
      border: 1px solid #cbd5e1;
      border-radius: 9px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      background: #ffffff;
      box-sizing: border-box;
    }}
    .card-header-bar {{
      padding: 0 5.5mm;
      display: flex;
      justify-content: space-between;
      align-items: center;
      color: #ffffff;
      height: 9.2mm;
      flex-shrink: 0;
    }}
    .header-left {{
      font-size: 10.2pt;
      font-weight: 900;
      letter-spacing: -0.2px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
      max-width: 104mm;
    }}
    .header-right {{
      background: rgba(0, 0, 0, 0.3);
      padding: 2px 7.5px;
      border-radius: 999px;
      font-size: 7.8pt;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.4px;
      white-space: nowrap;
    }}
    .card-content {{
      padding: 1.5mm 5.5mm 1.1mm;
      flex: 1;
      min-height: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 0.9mm;
      box-sizing: border-box;
      overflow: hidden;
    }}
    .rule-headline {{
      font-size: 11pt;
      font-weight: 900;
      color: #0f172a;
      line-height: 1.15;
      margin-bottom: 0.4mm;
    }}
    .rule-explanation {{
      font-size: 8.6pt;
      font-weight: 600;
      color: #1e293b;
      line-height: 1.22;
    }}
    .diagram-holder {{
      background: #f8fafc;
      border: 1.5px solid #cbd5e1;
      border-radius: 7px;
      flex: 1;
      min-height: 23mm;
      max-height: 41mm;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      padding: 2px 4px;
    }}
    .diagram-holder svg {{
      width: 100%;
      height: 100%;
      max-height: 100%;
    }}
    .golden-rule-pill {{
      background: #ecfdf5;
      border: 1.5px solid #10b981;
      border-radius: 6px;
      padding: 1.8px 7px;
      font-size: 8.1pt;
      font-weight: 700;
      color: #065f46;
      line-height: 1.18;
    }}
    .watch-out-pill {{
      background: #fff1f2;
      border: 1.5px solid #f43f5e;
      border-radius: 6px;
      padding: 1.8px 7px;
      font-size: 8.1pt;
      font-weight: 700;
      color: #9f1239;
      line-height: 1.18;
    }}
    .card-footer {{
      background: #f8fafc;
      border-top: 1.5px solid #e2e8f0;
      padding: 0 5.5mm;
      display: flex;
      justify-content: space-between;
      font-size: 7.8pt;
      color: #475569;
      font-weight: 800;
      height: 5.2mm;
      align-items: center;
      flex-shrink: 0;
    }}
    .back-content {{
      padding: 1.8mm 5.5mm 1.2mm;
      flex: 1;
      min-height: 0;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      gap: 1.4mm;
      background: #fafaf9;
      box-sizing: border-box;
      overflow: hidden;
    }}
    .challenge-box {{
      background: #ffffff;
      border: 2px solid #2563eb;
      border-radius: 7px;
      padding: 2mm 3.2mm;
      flex-shrink: 0;
    }}
    .challenge-title {{
      font-size: 8pt;
      font-weight: 900;
      color: #1d4ed8;
      display: flex;
      justify-content: space-between;
      margin-bottom: 0.5mm;
    }}
    .challenge-q {{
      font-size: 10.2pt;
      font-weight: 800;
      color: #0f172a;
      line-height: 1.28;
    }}
    .working-area {{
      background: #ffffff;
      border: 1.5px dashed #94a3b8;
      border-radius: 6px;
      padding: 1.2mm 3.2mm;
      height: 8.5mm;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 7.8pt;
      font-weight: 600;
      color: #64748b;
      flex-shrink: 0;
    }}
    .answer-box {{
      background: #ecfdf5;
      border: 2px solid #059669;
      border-radius: 8px;
      padding: 2.2mm 3.2mm;
      flex: 1;
      min-height: 0;
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
    }}
    .answer-title {{
      font-size: 8.4pt;
      font-weight: 900;
      color: #065f46;
      margin-bottom: 0.8mm;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .answer-body {{
      font-size: 9.8pt;
      font-weight: 700;
      color: #064e3b;
      line-height: 1.32;
    }}
  </style>
</head>
<body>
"""
    if deck_meta:
        cover_item = {"is_cover": True, "deck_meta": deck_meta}
        deck_items = [cover_item] + list(cards)
    else:
        deck_items = list(cards)

    for i in range(0, len(deck_items), 4):
        chunk = deck_items[i:i+4]
        while len(chunk) < 4:
            chunk.append(None)

        # FRONT PAGE (Cards 0, 1, 2, 3)
        html += '<div class="sheet-page">\n  <div class="cut-line-v"></div><div class="cut-line-h"></div>\n'
        for item in chunk:
            if item and item.get("is_cover"):
                html += render_cover_card_front_html(deck_meta, is_quadrant=True)
            elif item:
                theme = THEMES.get(item.get("strand_theme", "emerald"), THEMES["emerald"])
                html += f"""
  <div class="a6-quadrant">
    <div class="postcard-inner">
      <div class="card-header-bar" style="background:{theme['primary']};">
        <div class="header-left">{item['number']}. {item['title']}</div>
        <div class="header-right">{item['strand_name']}</div>
      </div>
      <div class="card-content">
        <div style="flex-shrink:0;">
          <div class="rule-headline">{item['rule_heading']}</div>
          <div class="rule-explanation">{item['rule_body']}</div>
        </div>
        <div class="diagram-holder">
          {item['svg_html']}
        </div>
        <div style="display:flex; flex-direction:column; gap:0.9mm; flex-shrink:0;">
          <div class="golden-rule-pill">★ <strong>Golden Rule:</strong> {item['golden_rule']}</div>
          <div class="watch-out-pill">⚠️ <strong>Watch Out:</strong> {item['watch_out']}</div>
        </div>
      </div>
      <div class="card-footer">
        <span>{item['dfe_code']} • {item['level_label']}</span>
        <span style="color:{theme['primary']};">Turn over for Practice Challenge ➔</span>
        <span>A6 Pocket Card</span>
      </div>
    </div>
  </div>
"""
            else:
                html += '  <div class="a6-quadrant" style="visibility:hidden;"></div>\n'
        html += '</div>\n'

        # BACK PAGE (Duplex Swap: Cards 1, 0, 3, 2)
        back_chunk = [chunk[1], chunk[0], chunk[3], chunk[2]]
        html += '<div class="sheet-page">\n  <div class="cut-line-v"></div><div class="cut-line-h"></div>\n'
        for item in back_chunk:
            if item and item.get("is_cover"):
                html += render_cover_card_back_html(deck_meta, cards, is_quadrant=True)
            elif item:
                theme = THEMES.get(item.get("strand_theme", "emerald"), THEMES["emerald"])
                html += f"""
  <div class="a6-quadrant">
    <div class="postcard-inner">
      <div class="card-header-bar" style="background:#1e293b;">
        <div class="header-left">Challenge: {item['title']}</div>
        <div class="header-right" style="background:{theme['primary']};">{item['strand_name']}</div>
      </div>
      <div class="back-content">
        <div class="challenge-box">
          <div class="challenge-title">
            <span>🎯 QUICK EXAM CHALLENGE</span>
            <span>{item['dfe_code']}</span>
          </div>
          <div class="challenge-q">{item['challenge_prompt']}</div>
        </div>
        <div class="working-area">
          <span>✏️ Learner Scratchpad &amp; Calculations</span>
          <span style="font-size:7pt; color:#94a3b8;">Formula Working Area</span>
        </div>
        <div class="answer-box">
          <div class="answer-title">
            <span>✓ STEP-BY-STEP OFFICIAL MODEL ANSWER</span>
            <span style="font-size:7.5pt; background:#059669; color:#fff; padding:1.5px 5px; border-radius:3px; font-weight:800;">FULL MARKS</span>
          </div>
          <div class="answer-body">
            {item['answer_text']}
          </div>
        </div>
      </div>
      <div class="card-footer">
        <span>Card {item['number']} • {item['dfe_code']}</span>
        <span style="color:#059669; font-weight:800;">✓ Official Tutor Solution</span>
        <div class="card-footer-logo" style="display:inline-flex; align-items:center; gap:4px;">
          <svg viewBox="0 0 64 64" width="13" height="13" style="border-radius:2px; flex-shrink:0;">
            <rect x="2" y="2" width="60" height="60" rx="12" fill="#1d4ed8"/>
            <path d="M 32 10 L 48 17 L 32 24 L 16 17 Z" fill="#60a5fa"/>
            <path d="M 44 20.5 L 44 28 C 44 31 38 33 32 33 C 26 33 20 31 20 28 L 20 20.5" fill="none" stroke="#60a5fa" stroke-width="2.5"/>
            <path d="M 48 17 L 50 25" stroke="#f59e0b" stroke-width="2"/>
            <circle cx="50" cy="26" r="1.5" fill="#f59e0b"/>
            <path d="M 17 50 L 17 29 L 24 29 L 32 41 L 40 29 L 47 29 L 47 50 L 40 50 L 40 37 L 34 46 L 30 46 L 24 37 L 24 50 Z" fill="#ffffff"/>
          </svg>
          <span style="font-weight:900; color:#0f172a; font-size:6.8pt; letter-spacing:0.2px;">MASTER<span style="color:#2563eb;">FUNCTIONALSKILLS</span></span>
        </div>
      </div>
    </div>
  </div>
"""
            else:
                html += '  <div class="a6-quadrant" style="visibility:hidden;"></div>\n'
        html += '</div>\n'

    html += "</body>\n</html>"
    return html

def compile_pdf(html_content, output_pdf_path):
    tmp_html = tempfile.mktemp(suffix=".html", prefix="mfs_cards_")
    with open(tmp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    tmp_dir = tempfile.mkdtemp(prefix="chrome_pdf_")
    cmd = [
        "/usr/lib/chromium/chromium",
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--user-data-dir={tmp_dir}",
        f"--print-to-pdf={output_pdf_path}",
        f"file://{tmp_html}"
    ]
    try:
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
        if os.path.exists(output_pdf_path) and os.path.getsize(output_pdf_path) > 1000:
            print(f"✓ Created PDF: {os.path.basename(output_pdf_path)} ({os.path.getsize(output_pdf_path):,} bytes)")
            return True
        else:
            print(f"✗ Failed to create {output_pdf_path}: {res.stderr.decode('utf-8', errors='ignore')[:200]}")
            return False
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
        if os.path.exists(tmp_html):
            os.remove(tmp_html)

def main():
    local_base = os.path.dirname(os.path.abspath(__file__))
    nextcloud_base = "/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk"
    base_dirs = [local_base]
    if os.path.exists(nextcloud_base) and nextcloud_base != local_base:
        base_dirs.append(nextcloud_base)

    print("1. Validating all SVG assets...")
    validate_svgs()
    apply_tight_viewboxes()
    validate_svgs()
    print(f"✓ All {len(OVERHAULED_CARDS)} card SVGs validated cleanly!")

    print("2. Generating revision_cards_data.js...")
    generate_js()

    print("3. Generating Master A6 and A4 Imposition HTML...")
    # Master True A6 PDF (with Cover Card and 36-card Corbettmaths checklist)
    master_a6_html = render_a6_individual_html(OVERHAULED_CARDS, "Master Functional Skills A6 Pocket Revision Cards", DECK_METADATA["all_cards"])
    # Master A4 4-Up Imposition PDF (with Cover Card in Quadrant 0)
    master_a4_html = render_a4_4up_imposition_html(OVERHAULED_CARDS, "Master Functional Skills A4 Imposition Sheets (4 A6 Cards Per Page)", DECK_METADATA["all_cards"])

    for b_dir in base_dirs:
        os.makedirs(os.path.join(b_dir, "assets", "downloads"), exist_ok=True)
        with open(os.path.join(b_dir, "printable-a6-cards.html"), "w", encoding="utf-8") as f:
            f.write(master_a6_html)
        with open(os.path.join(b_dir, "printable-overhauled-cards.html"), "w", encoding="utf-8") as f:
            f.write(master_a4_html)
        with open(os.path.join(b_dir, "printable-all-cards.html"), "w", encoding="utf-8") as f:
            f.write(master_a4_html)

    print("4. Compiling Master PDF Packs...")
    primary_downloads = os.path.join(local_base, "assets", "downloads")
    
    # True A6 Master PDF
    master_a6_pdf = os.path.join(primary_downloads, "MasterFunctionalSkills_Visual_Postcard_Cards_A6.pdf")
    compile_pdf(master_a6_html, master_a6_pdf)

    # A4 4-up Master PDF
    master_a4_pdf = os.path.join(primary_downloads, "MasterFunctionalSkills_Visual_Postcard_Cards.pdf")
    compile_pdf(master_a4_html, master_a4_pdf)
    
    # Mirror into all_cards.pdf
    all_cards_pdf = os.path.join(primary_downloads, "MasterFunctionalSkills_Revision_Cards_all_cards.pdf")
    if os.path.exists(master_a4_pdf):
        shutil.copy2(master_a4_pdf, all_cards_pdf)

    print("5. Compiling Per-Subject / Level PDF Packs (Both A6 & A4 Imposition)...")
    subject_filters = [
        ("maths_l2", lambda c: c["subject"] == "maths" and c["level"] == "l2", "Maths Level 2 Revision Cards"),
        ("maths_l1", lambda c: c["subject"] == "maths" and c["level"] == "l1", "Maths Level 1 Revision Cards"),
        ("english_l2", lambda c: c["subject"] == "english" and c["level"] == "l2", "English Level 2 Revision Cards"),
        ("english_l1", lambda c: c["subject"] == "english" and c["level"] == "l1", "English Level 1 Revision Cards"),
        ("digital_skills", lambda c: c["subject"] == "digital" and c["level"] != "e3", "Digital Functional Skills Revision Cards"),
        ("entry_level_3", lambda c: c["level"] == "e3", "Entry Level 3 Revision Cards")
    ]

    for key, filter_fn, title in subject_filters:
        subset = [c for c in OVERHAULED_CARDS if filter_fn(c)]
        if not subset:
            continue
        
        deck_meta = DECK_METADATA.get(key)
        subset_a6_html = render_a6_individual_html(subset, f"{title} (A6)", deck_meta)
        subset_a4_html = render_a4_4up_imposition_html(subset, title, deck_meta)

        html_slug = f"printable-{key.replace('_', '-')}.html"
        for b_dir in base_dirs:
            with open(os.path.join(b_dir, html_slug), "w", encoding="utf-8") as f:
                f.write(subset_a4_html)

        # A6 PDF (Professional printer cardstock format with Cover Card & Contents)
        a6_pdf_name = f"MasterFunctionalSkills_Revision_Cards_{key}_A6.pdf"
        target_a6_pdf = os.path.join(primary_downloads, a6_pdf_name)
        compile_pdf(subset_a6_html, target_a6_pdf)

        # A4 4-up PDF (Home/Office A4 duplex cutting sheet with Cover Card in Quadrant 0)
        a4_pdf_name = f"MasterFunctionalSkills_Revision_Cards_{key}.pdf"
        target_a4_pdf = os.path.join(primary_downloads, a4_pdf_name)
        compile_pdf(subset_a4_html, target_a4_pdf)

    # Sync compiled PDFs to Nextcloud if present
    if os.path.exists(nextcloud_base) and nextcloud_base != local_base:
        nc_downloads = os.path.join(nextcloud_base, "assets", "downloads")
        os.makedirs(nc_downloads, exist_ok=True)
        for pdf_file in os.listdir(primary_downloads):
            if pdf_file.endswith(".pdf"):
                shutil.copy2(os.path.join(primary_downloads, pdf_file), os.path.join(nc_downloads, pdf_file))

    print("\n✓ ALL A6 AND A4 REVISION CARD PDFS COMPILED AND SYNCED SUCCESSFULLY!")

if __name__ == "__main__":
    main()