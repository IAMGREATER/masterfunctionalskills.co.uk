#!/usr/bin/env python3
"""
Master Functional Skills - Comprehensive Topic Registry.
Generates structured original questions and solutions for all Functional Skills standards.
"""

def make_maths_topic(slug, title, spec_codes, formula_hint, q1, q2, q3, q4, q5, q6):
    return {
        "slug": slug,
        "title": title,
        "subject": "Mathematics",
        "spec_codes": f"Pearson Edexcel: {spec_codes}",
        "formula_hint": formula_hint,
        "back_url": f"../functional-skills-{slug}.html",
        "total_marks": 18,
        "sections": [
            {
                "title": "Section A: Procedural Fluency Check",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [q1, q2]
            },
            {
                "title": "Section B: Workplace & Functional Scenarios",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [q3, q4]
            },
            {
                "title": "Section C: Pearson Edexcel Problem Solving & Justification",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [q5, q6]
            }
        ]
    }

def make_english_topic(slug, title, category, spec_codes, golden_rule, q1, q2, q3, q4, q5, q6):
    prefix = "Reading" if category == "reading" else ("Writing" if category == "writing" else "SLC")
    back_url = f"../{slug}.html"
    return {
        "slug": slug,
        "title": title,
        "subject": f"English {prefix}",
        "spec_codes": f"Pearson Edexcel: {spec_codes}",
        "formula_hint": golden_rule,
        "back_url": back_url,
        "total_marks": 18,
        "sections": [
            {
                "title": "Section A: Foundational Concept Check",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [q1, q2]
            },
            {
                "title": "Section B: Functional Workplace Application",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [q3, q4]
            },
            {
                "title": "Section C: Pearson Edexcel Exam-Style Analysis & Evaluation",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [q5, q6]
            }
        ]
    }

def make_digital_topic(slug, title, spec_codes, golden_rule, q1, q2, q3, q4, q5, q6):
    return {
        "slug": slug,
        "title": title,
        "subject": "Digital Functional Skills",
        "spec_codes": f"Ofqual / Pearson Edexcel: {spec_codes}",
        "formula_hint": golden_rule,
        "back_url": f"../{slug}.html",
        "total_marks": 18,
        "sections": [
            {
                "title": "Section A: Core Technical Skills",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [q1, q2]
            },
            {
                "title": "Section B: Digital Workplace Tasks",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [q3, q4]
            },
            {
                "title": "Section C: Problem Solving, Cybersecurity & Verification",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [q5, q6]
            }
        ]
    }

print("Topic dataset helper functions defined.")
