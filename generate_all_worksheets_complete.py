#!/usr/bin/env python3
"""
Master Functional Skills - Complete Curriculum Worksheet & Answer Key Engine.
Generates 100% original, Pearson Edexcel aligned worksheets and examiner mark schemes
for all 100+ curriculum topics across Maths, English (Reading, Writing, SLC), and Digital Skills.
"""

import os, sys, re, json
from worksheet_templates import render_worksheet, render_answers

OUTPUT_DIR = "/home/subi/Projects/masterfunctionalskills.co.uk/worksheets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Helper for SVG diagrams
def get_svg_for_topic(slug):
    if "perimeter" in slug:
        return """<svg viewBox="0 0 340 180" width="340" height="180" xmlns="http://www.w3.org/2000/svg">
          <polygon points="40,30 280,30 280,90 180,90 180,150 40,150" fill="#e0f2fe" stroke="#0284c7" stroke-width="2.5" />
          <text x="160" y="24" font-size="12" font-weight="700" fill="#0369a1" text-anchor="middle">12.5 m</text>
          <text x="290" y="65" font-size="12" font-weight="700" fill="#0369a1">4.8 m</text>
          <text x="230" y="105" font-size="12" font-weight="700" fill="#0369a1" text-anchor="middle">5.5 m</text>
          <text x="190" y="125" font-size="12" font-weight="700" fill="#dc2626">a = ?</text>
          <text x="110" y="168" font-size="12" font-weight="700" fill="#dc2626">b = ?</text>
          <text x="10" y="95" font-size="12" font-weight="700" fill="#0369a1">10.2 m</text>
        </svg>"""
    elif "area" in slug:
        return """<svg viewBox="0 0 340 180" width="340" height="180" xmlns="http://www.w3.org/2000/svg">
          <polygon points="40,30 280,30 280,80 160,80 160,150 40,150" fill="#fef3c7" stroke="#d97706" stroke-width="2.5" />
          <line x1="40" y1="80" x2="160" y2="80" stroke="#b45309" stroke-dasharray="4,4" stroke-width="1.5" />
          <text x="160" y="22" font-size="12" font-weight="700" fill="#b45309" text-anchor="middle">14.0 m</text>
          <text x="290" y="60" font-size="12" font-weight="700" fill="#b45309">3.5 m</text>
          <text x="100" y="60" font-size="12" font-weight="700" fill="#92400e" text-anchor="middle">Area A</text>
          <text x="100" y="120" font-size="12" font-weight="700" fill="#92400e" text-anchor="middle">Area B</text>
          <text x="10" y="95" font-size="12" font-weight="700" fill="#b45309">9.0 m</text>
        </svg>"""
    elif "circle" in slug:
        return """<svg viewBox="0 0 300 160" width="300" height="160" xmlns="http://www.w3.org/2000/svg">
          <circle cx="150" cy="80" r="60" fill="#eff6ff" stroke="#2563eb" stroke-width="2.5" />
          <line x1="90" y1="80" x2="210" y2="80" stroke="#1d4ed8" stroke-width="2" />
          <circle cx="150" cy="80" r="3" fill="#1d4ed8" />
          <text x="150" y="72" font-size="12" font-weight="700" fill="#1e40af" text-anchor="middle">Diameter = 14.0 m</text>
        </svg>"""
    elif "triangle" in slug or "angles-in-2d" in slug:
        return """<svg viewBox="0 0 300 160" width="300" height="160" xmlns="http://www.w3.org/2000/svg">
          <polygon points="50,130 250,130 180,40" fill="#ecfdf5" stroke="#059669" stroke-width="2.5" />
          <text x="75" y="125" font-size="12" font-weight="700" fill="#047857">48°</text>
          <text x="215" y="125" font-size="12" font-weight="700" fill="#047857">67°</text>
          <text x="180" y="65" font-size="12" font-weight="700" fill="#dc2626" text-anchor="middle">x = ?</text>
        </svg>"""
    elif "volume" in slug:
        return """<svg viewBox="0 0 320 170" width="320" height="170" xmlns="http://www.w3.org/2000/svg">
          <polygon points="50,70 180,70 240,40 110,40" fill="#e0e7ff" stroke="#4338ca" stroke-width="2" />
          <polygon points="50,70 180,70 180,140 50,140" fill="#c7d2fe" stroke="#4338ca" stroke-width="2" />
          <polygon points="180,70 240,40 240,110 180,140" fill="#a5b4fc" stroke="#4338ca" stroke-width="2" />
          <text x="115" y="158" font-size="12" font-weight="700" fill="#3730a3" text-anchor="middle">Length = 2.4 m</text>
          <text x="225" y="135" font-size="12" font-weight="700" fill="#3730a3">Width = 1.2 m</text>
          <text x="35" y="110" font-size="12" font-weight="700" fill="#3730a3">Height = 0.9 m</text>
        </svg>"""
    elif "scatter" in slug or "line-graph" in slug:
        return """<svg viewBox="0 0 340 180" width="340" height="180" xmlns="http://www.w3.org/2000/svg">
          <line x1="50" y1="140" x2="300" y2="140" stroke="#334155" stroke-width="2" />
          <line x1="50" y1="140" x2="50" y2="20" stroke="#334155" stroke-width="2" />
          <circle cx="80" cy="120" r="4" fill="#2563eb" />
          <circle cx="120" cy="105" r="4" fill="#2563eb" />
          <circle cx="160" cy="90" r="4" fill="#2563eb" />
          <circle cx="200" cy="70" r="4" fill="#2563eb" />
          <circle cx="240" cy="55" r="4" fill="#2563eb" />
          <circle cx="280" cy="35" r="4" fill="#2563eb" />
          <line x1="60" y1="130" x2="290" y2="30" stroke="#dc2626" stroke-width="2" stroke-dasharray="4,4" />
          <text x="175" y="165" font-size="11" font-weight="700" fill="#475569" text-anchor="middle">Experience (Years)</text>
          <text x="15" y="80" font-size="11" font-weight="700" fill="#475569" transform="rotate(-90,15,80)" text-anchor="middle">Hourly Pay (£)</text>
        </svg>"""
    elif "pie-chart" in slug:
        return """<svg viewBox="0 0 280 160" width="280" height="160" xmlns="http://www.w3.org/2000/svg">
          <circle cx="100" cy="80" r="60" fill="#e2e8f0" stroke="#475569" stroke-width="1.5" />
          <path d="M 100,80 L 100,20 A 60,60 0 0,1 160,80 Z" fill="#3b82f6" />
          <path d="M 100,80 L 160,80 A 60,60 0 0,1 100,140 Z" fill="#10b981" />
          <path d="M 100,80 L 100,140 A 60,60 0 0,1 100,20 Z" fill="#f59e0b" />
          <rect x="180" y="40" width="12" height="12" fill="#3b82f6" /><text x="200" y="51" font-size="11" fill="#1e293b">Admin (25%)</text>
          <rect x="180" y="65" width="12" height="12" fill="#10b981" /><text x="200" y="76" font-size="11" fill="#1e293b">Nursing (25%)</text>
          <rect x="180" y="90" width="12" height="12" fill="#f59e0b" /><text x="200" y="101" font-size="11" fill="#1e293b">Care (50%)</text>
        </svg>"""
    return None

print("Helper SVG module ready.")
