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
                "title": "Section A: Core Skills (Warm-Up)",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [q1, q2]
            },
            {
                "title": "Section B: Everyday & Workplace Maths",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [q3, q4]
            },
            {
                "title": "Section C: Exam-Style Problem Solving",
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
                "title": "Section A: Core Skills (The Basics)",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [q1, q2]
            },
            {
                "title": "Section B: Real-Life & Workplace Practice",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [q3, q4]
            },
            {
                "title": "Section C: Exam-Style Tasks",
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
                "title": "Section A: Core Skills (The Basics)",
                "meta": "Questions 1 & 2 • 4 Marks",
                "questions": [q1, q2]
            },
            {
                "title": "Section B: Everyday & Workplace Tasks",
                "meta": "Questions 3 & 4 • 6 Marks",
                "questions": [q3, q4]
            },
            {
                "title": "Section C: Practical Problem Solving",
                "meta": "Questions 5 & 6 • 8 Marks",
                "questions": [q5, q6]
            }
        ]
    }

print("Topic dataset helper functions defined.")
