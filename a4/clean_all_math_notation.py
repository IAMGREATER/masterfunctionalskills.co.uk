"""
books/a4/clean_all_math_notation.py
Cleans and converts all corrupted LaTeX and math notation in:
- books/a4/specialist_suite_reference.py
- books/a4/generate_specialist_reference.py
into clear, simple, plain English and standard HTML formatting.
"""

from pathlib import Path
import re

FILES = [
    Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/books/a4/specialist_suite_reference.py"),
    Path("/home/subi/Nextcloud/Projects/masterfunctionalskills.co.uk/books/a4/generate_specialist_reference.py"),
]

def clean_math_text(s: str) -> str:
    # 1. Fix broken form feed \x0c or \f that came from \frac
    s = s.replace("\x0crac", "frac").replace("\x0c", "")
    
    # 2. Fix broken LaTeX fractions: \frac{a{b or \frac{a}{b} -> a/b
    s = re.sub(r'\\frac\{([^}]+)\{([^}]+)', r'\1/\2', s)
    s = re.sub(r'\\frac\{([^}]+)\}\{([^}]+)\}', r'\1/\2', s)
    s = re.sub(r'\\frac\{([^}]+)\}', r'\1', s)
    s = s.replace(r'\frac', '')

    # 3. Fix \text{...} -> ...
    s = re.sub(r'\\text\{([^}]+)\}', r'\1', s)
    s = re.sub(r'\\mathbf\{([^}]+)\}', r'<b>\1</b>', s)

    # 4. Fix broken square roots &radic;{... or \sqrt{...
    s = re.sub(r'&radic;\{([^=]+)=', r'√(\1) =', s)
    s = re.sub(r'&radic;\{([^<\s]+)', r'√(\1)', s)
    s = re.sub(r'\\sqrt\{([^}]+)\}', r'√(\1)', s)
    s = s.replace(r'&radic;', '√')

    # 5. Fix \times -> ×, \div / &divide; -> ÷, \pm / &plusmn; -> ±, \approx / &asymp; -> ≈
    s = s.replace(r'\times', '×').replace(r'\div', '÷').replace(r'\pm', '±').replace(r'\approx', '≈')
    s = s.replace(r'\rightarrow', '→')
    s = s.replace(r'\pi', 'π').replace('&pi;', 'π')

    # 6. Clean dangling $ signs used in LaTeX inline math
    # But preserve normal currency £ and code syntax
    s = re.sub(r'\$([0-9A-Za-z\s\.,\+\-\*/÷×=_\(\)]+)\$', r'\1', s)
    # Remove remaining standalone unescaped single $ that aren't currency
    s = re.sub(r'(?<![0-9A-Za-z£])\$(?![0-9])', '', s)

    # 7. Clean exponents like ^2 -> ², ^3 -> ³
    s = s.replace('^2', '²').replace('^3', '³')
    s = s.replace('{2}', '²').replace('{3}', '³')

    # 8. Clean broken fraction strings like 4\frac{1{6 -> 4 1/6
    s = re.sub(r'(\d+)\s*frac\s*\{?(\d+)\{?(\d+)', r'\1 \2/\3', s)
    s = re.sub(r'(\d+)\s*\\?\s*(\d+)/(\d+)', r'\1 \2/\3', s)

    # 9. Clean specific mangled lines
    s = s.replace("2\\frac{2{4", "2 2/4").replace("1\\frac{2{3", "1 2/3").replace("4\\frac{1{6", "4 1/6")
    s = s.replace("2\\frac{3{4", "2 3/4").replace("4\\frac{5{12", "4 5/12")
    s = s.replace("2\\frac{1{4", "2 1/4").replace("3\\frac{11{12", "3 11/12")
    s = s.replace("1\\frac{3{4", "1 3/4").replace("3\\frac{1{2", "3 1/2").replace("1\\frac{4{5", "1 4/5")
    s = s.replace("1\\frac{7{10", "1 7/10").replace("1\\frac{1{3", "1 1/3")
    s = s.replace("4\\frac{1{4", "4 1/4")

    # Clean formula box
    s = s.replace(r"Triangle: $A = \frac{1{2 b h$", "Triangle: Area = (Base × Height) ÷ 2")
    s = s.replace(r"Trapezium: $A = \frac{a + b}{2 h$", "Trapezium: Area = ((a + b) ÷ 2) × Height")
    s = s.replace(r"$\text{Speed} = \frac{\text{Distance}}{\text{Time}}$", "Speed = Distance ÷ Time")
    s = s.replace(r"$\text{Distance} = \text{Speed} \times \text{Time}$", "Distance = Speed × Time")
    s = s.replace(r"$\text{Time} = \frac{\text{Distance}}{\text{Speed}}$", "Time = Distance ÷ Speed")
    s = s.replace(r"$\text{Density} = \frac{\text{Mass}}{\text{Volume}}$", "Density = Mass ÷ Volume")
    s = s.replace(r"$\text{Mass} = \text{Density} \times \text{Volume}$", "Mass = Density × Volume")
    s = s.replace(r"Percentage Change: $\frac{\text{Actual Change}}{\text{Original Value}} \times 100%$", "Percentage Change = (Actual Change ÷ Original Value) × 100%")
    s = s.replace(r"Reverse Percentage: $\text{Original} = \frac{\text{New Value}}{\text{Decimal Multiplier}}$", "Reverse Percentage: Original = New Value ÷ Decimal Multiplier")
    s = s.replace(r"Estimated Mean: $\frac{&Sigma; (\text{midpoint} \times \text{frequency})}{&Sigma; \text{frequency}}$", "Estimated Mean = Total of (Midpoint × Frequency) ÷ Total Frequency")

    return s

def process():
    for fpath in FILES:
        if not fpath.exists():
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        
        cleaned = clean_math_text(content)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"Cleaned math and formula notation in: {fpath.name}")

if __name__ == "__main__":
    process()
