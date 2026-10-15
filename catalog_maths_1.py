#!/usr/bin/env python3
"""
Catalog Maths 1: Number & Number Systems (19 Topics).
"""
from build_topic_dataset import make_maths_topic

CATALOG_MATHS_1 = [
    # 1. Rounding and Estimating
    make_maths_topic(
        slug="rounding-and-estimating",
        title="Rounding & Estimating",
        spec_codes="E3.6 • L1.10 • L2.12",
        formula_hint="Look at the deciding digit immediately to the right of your target place. If it is 5 or more (5, 6, 7, 8, 9), round UP. If it is 4 or less (0, 1, 2, 3, 4), round DOWN. For estimating, round numbers to 1 significant figure.",
        q1={
            "title": "Question 1 (Level 1 Rounding to Nearest 100)",
            "marks": 2,
            "stem": "Round <strong>4,758</strong> to the nearest hundred.",
            "lines": 2,
            "ans_label": "Rounded value =",
            "choice_box": "____________________",
            "step_rows": [
                ("1. Identify hundreds place (7) and deciding digit in tens place (5)", "[M1]"),
                ("2. Since 5 ≥ 5, round UP to 4,800", "[A1]")
            ],
            "final_answer": "4,800",
            "pitfall": "Rounding to the nearest 10 instead of 100 (writing 4,760).",
            "reverse_check": "4,758 is closer to 4,800 than to 4,700."
        },
        q2={
            "title": "Question 2 (Level 2 Rounding to 2 Decimal Places)",
            "marks": 2,
            "stem": "Round <strong>14.8362</strong> to <strong>two decimal places</strong>.",
            "lines": 2,
            "ans_label": "Rounded value =",
            "choice_box": "____________________",
            "step_rows": [
                ("1. Identify second decimal place (3) and deciding digit (6)", "[M1]"),
                ("2. Round UP: 14.84", "[A1]")
            ],
            "final_answer": "14.84",
            "pitfall": "Truncating without rounding (writing 14.83).",
            "reverse_check": "14.8362 is closer to 14.84 than 14.83."
        },
        q3={
            "title": "Question 3 (Level 1 Estimating Supermarket Bill)",
            "marks": 3,
            "stem": "A catering assistant purchases three supplies for a lunch event:<br>• 18 cases of water at <strong>£4.95</strong> per case<br>• 22 platters of sandwiches at <strong>£9.85</strong> per platter<br>• 48 fruit snack boxes at <strong>£1.95</strong> per box<br><br>Estimate the total cost by rounding each quantity and price to <strong>1 significant figure</strong>.",
            "lines": 4,
            "ans_label": "Estimated Total =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Round water: 20 × £5 = £100", "[M1]"),
                ("2. Round sandwiches: 20 × £10 = £200. Round fruit: 50 × £2 = £100", "[P1]"),
                ("3. Sum estimated costs: £100 + £200 + £100 = £400", "[A1]")
            ],
            "final_answer": "£400",
            "pitfall": "Calculating exact values instead of estimates when the question explicitly asks to estimate.",
            "reverse_check": "Exact total is £89.10 + £216.70 + £93.60 = £399.40. £400 is an excellent estimate."
        },
        q4={
            "title": "Question 4 (Level 2 Apprentice Fuel Estimation)",
            "marks": 3,
            "stem": "A delivery fleet driver covers <strong>385 miles</strong> per week.<br>The van does <strong>38 miles per gallon</strong>.<br>Diesel costs <strong>£6.85 per gallon</strong>.<br><br>Use suitable approximations to estimate the driver's weekly fuel cost.",
            "lines": 4,
            "ans_label": "Estimated Fuel Cost =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Round miles and mpg: 400 miles ÷ 40 mpg = 10 gallons", "[M1]"),
                ("2. Round diesel price to 1 sig fig: £7 per gallon", "[P1]"),
                ("3. Multiply: 10 gallons × £7 = £70", "[A1]")
            ],
            "final_answer": "£70 (Accept £68.50 using £6.85)",
            "pitfall": "Dividing mpg by miles (38 ÷ 385) instead of miles ÷ mpg.",
            "reverse_check": "Exact: 385 ÷ 38 = 10.13 gallons × £6.85 = £69.40. £70 is highly accurate."
        },
        q5={
            "title": "Question 5 (Level 2 Hospital Renovation Estimate)",
            "marks": 4,
            "stem": "An estates team estimates the total cost of installing new LED fixtures across <strong>48 consultation rooms</strong>.<br>• Each room requires <strong>6 fixtures</strong> at <strong>£28.75</strong> each.<br>• Electrician installation labour is estimated at <strong>1.8 hours per room</strong> at <strong>£32.50 per hour</strong>.<br><br>Calculate an estimated total cost using values rounded to 1 significant figure.",
            "lines": 5,
            "ans_label": "Estimated Total Cost =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Estimate rooms: 50. Fixtures: 6 × £30 = £180 per room (or round to £200)", "[P1]"),
                ("2. Fixtures total: 50 × £180 = £9,000", "[P1]"),
                ("3. Labour estimate: 2 hours × £30 = £60 per room; 50 × £60 = £3,000", "[M1]"),
                ("4. Total estimate: £9,000 + £3,000 = £12,000", "[A1]")
            ],
            "final_answer": "£12,000 (Accept £11,000 to £13,000 depending on rounding strategy)",
            "pitfall": "Calculating exact decimals and rounding only the final answer.",
            "reverse_check": "Exact: 48 × (6 × £28.75 + 1.8 × £32.50) = 48 × (£172.50 + £58.50) = 48 × £231.00 = £11,088."
        },
        q6={
            "title": "Question 6 (Level 2 Budget Justification Check)",
            "marks": 4,
            "stem": "A project manager has a contingency budget of <strong>£15,000</strong>.<br>The manager quickly estimates: <em>'Since the exact cost of £11,088 is well under our £12,000 estimate, our budget has at least £3,500 surplus remaining.'</em><br><br>Is the manager correct?<br>Show the exact budget surplus and state a clear conclusion.",
            "lines": 5,
            "ans_label": "Conclusion & Exact Surplus =",
            "choice_box": "Correct / Incorrect: Surplus is £ ____________",
            "step_rows": [
                ("1. Calculate exact surplus: £15,000 - £11,088", "[M1]"),
                ("2. Accurate subtraction: £3,912.00", "[P1]"),
                ("3. Compare with claim: £3,912 > £3,500", "[M1]"),
                ("4. Conclude: <strong>Yes, the manager is correct</strong>. The actual surplus is £3,912, which exceeds £3,500.", "[A1]")
            ],
            "final_answer": "Correct (Actual surplus is £3,912, which exceeds £3,500)",
            "pitfall": "Subtracting £12,000 estimate instead of the exact cost £11,088.",
            "reverse_check": "£11,088 + £3,912 = £15,000."
        }
    ),
    # 2. Fractions, Decimals and Percentages (FDP)
    make_maths_topic(
        slug="fractions-decimals-and-percentages",
        title="FDP Conversions",
        spec_codes="L1.12 • L2.13",
        formula_hint="Fractions to decimals: divide top by bottom. Decimals to percentages: multiply by 100. Percentages to fractions: put over 100 and simplify.",
        q1={
            "title": "Question 1 (Level 1 Fraction to Percentage)",
            "marks": 2,
            "stem": "Convert <strong>3/8</strong> to a decimal and to a percentage.",
            "lines": 3,
            "ans_label": "Decimal & Percentage =",
            "choice_box": "Decimal: _____ | Percentage: _____ %",
            "step_rows": [
                ("1. Divide 3 by 8: 3 ÷ 8 = 0.375", "[M1]"),
                ("2. Multiply by 100: 0.375 × 100 = 37.5%", "[A1]")
            ],
            "final_answer": "0.375 and 37.5%",
            "pitfall": "Confusing 3/8 with 3/5 (thinking it is 0.60 or 60%).",
            "reverse_check": "37.5 / 100 = 375 / 1000 = 3/8."
        },
        q2={
            "title": "Question 2 (Level 2 Recurring Decimal to Fraction)",
            "marks": 2,
            "stem": "Write <strong>0.85</strong> as a fraction in its simplest form.",
            "lines": 3,
            "ans_label": "Simplest Fraction =",
            "choice_box": "____________________",
            "step_rows": [
                ("1. Place over 100: 85/100", "[M1]"),
                ("2. Divide numerator and denominator by 5: 17/20", "[A1]")
            ],
            "final_answer": "17/20",
            "pitfall": "Stopping at 85/100 without simplifying.",
            "reverse_check": "17 ÷ 20 = 0.85."
        },
        q3={
            "title": "Question 3 (Level 1 Comparing FDP Values)",
            "marks": 3,
            "stem": "Arrange the following values in order from <strong>smallest</strong> to <strong>largest</strong>:<br><strong>35% &nbsp;|&nbsp; 0.32 &nbsp;|&nbsp; 3/10 &nbsp;|&nbsp; 0.305</strong>",
            "lines": 4,
            "ans_label": "Ordered values =",
            "choice_box": "Smallest: ________________ to Largest: ________________",
            "step_rows": [
                ("1. Convert all to decimals: 35% = 0.35; 0.32; 3/10 = 0.30; 0.305", "[M1]"),
                ("2. Compare decimals: 0.30 < 0.305 < 0.32 < 0.35", "[P1]"),
                ("3. Write in original format: 3/10, 0.305, 0.32, 35%", "[A1]")
            ],
            "final_answer": "3/10,  0.305,  0.32,  35%",
            "pitfall": "Thinking 0.305 is larger than 0.32 because 305 looks bigger than 32.",
            "reverse_check": "30% < 30.5% < 32% < 35%."
        },
        q4={
            "title": "Question 4 (Level 2 Clinical Trial Recovery Rates)",
            "marks": 3,
            "stem": "Three patient rehabilitation programmes report their success rates:<br>• Clinic A: <strong>14 out of 20</strong> patients make a full recovery.<br>• Clinic B: <strong>68%</strong> recovery rate.<br>• Clinic C: <strong>0.72</strong> recovery rate.<br><br>Which clinic achieved the highest recovery rate?",
            "lines": 4,
            "ans_label": "Highest Clinic =",
            "choice_box": "Clinic _____",
            "step_rows": [
                ("1. Clinic A: 14 ÷ 20 = 0.70 = 70%", "[M1]"),
                ("2. Compare all three in same format: Clinic A = 70%, Clinic B = 68%, Clinic C = 72%", "[P1]"),
                ("3. State highest clinic: Clinic C (72%)", "[A1]")
            ],
            "final_answer": "Clinic C (72%)",
            "pitfall": "Comparing 14 directly with 68 without converting to a common standard.",
            "reverse_check": "72% (C) > 70% (A) > 68% (B)."
        },
        q5={
            "title": "Question 5 (Level 2 NHS Energy Reduction Multi-Tier)",
            "marks": 4,
            "stem": "An NHS Trust reduces energy consumption across three hospital wings:<br>• North Wing reduced consumption by <strong>1/8</strong>.<br>• South Wing reduced consumption by <strong>14%</strong>.<br>• East Wing reduced consumption by <strong>0.115</strong>.<br><br>Work out the difference in percentage points between the wing with the <strong>greatest</strong> reduction and the wing with the <strong>least</strong> reduction.",
            "lines": 5,
            "ans_label": "Difference in percentage points =",
            "choice_box": "_____________ % points",
            "step_rows": [
                ("1. North Wing: 1/8 = 0.125 = 12.5%", "[P1]"),
                ("2. South Wing: 14%. East Wing: 0.115 = 11.5%", "[P1]"),
                ("3. Identify extremes: Greatest = South (14%), Least = East (11.5%)", "[M1]"),
                ("4. Subtract: 14% - 11.5% = 2.5 percentage points", "[A1]")
            ],
            "final_answer": "2.5 percentage points",
            "pitfall": "Selecting North Wing (12.5%) as least, overlooking East Wing (11.5%).",
            "reverse_check": "11.5% + 2.5% = 14.0%."
        },
        q6={
            "title": "Question 6 (Level 2 Discount Comparison Justification)",
            "marks": 4,
            "stem": "An equipment distributor offers two pricing promotions on an endoscopy trolley priced at <strong>£2,400</strong>:<br>• Deal 1: <strong>1/5 off</strong> the normal price.<br>• Deal 2: <strong>18% discount</strong> plus an extra <strong>£30 voucher</strong> deducted at checkout.<br><br>A procurement officer states: <em>'Deal 1 is better because it saves at least £20 more than Deal 2.'</em><br><br>Is the procurement officer correct?<br>Show your calculations clearly and state a definitive conclusion.",
            "lines": 5,
            "ans_label": "Conclusion & Savings Comparison =",
            "choice_box": "Correct / Incorrect: Deal 1 saves £ _____ vs Deal 2 saves £ _____",
            "step_rows": [
                ("1. Deal 1 saving: 1/5 of £2,400 = £2,400 ÷ 5 = £480.00", "[P1]"),
                ("2. Deal 2 saving: 18% of £2,400 = £432.00 + £30 = £462.00", "[P1]"),
                ("3. Difference in savings: £480.00 - £462.00 = £18.00", "[M1]"),
                ("4. Conclude: <strong>No / Incorrect</strong>; Deal 1 is indeed cheaper, but it only saves £18 more, NOT 'at least £20 more'.", "[A1]")
            ],
            "final_answer": "Incorrect (Deal 1 saves £18 more, which is less than the claimed £20)",
            "pitfall": "Agreeing simply because Deal 1 is cheaper, failing to check the 'at least £20' threshold.",
            "reverse_check": "£480 - £462 = £18 < £20."
        }
    ),
    # 3. Simple & Compound Interest
    make_maths_topic(
        slug="interest-and-compound-interest",
        title="Simple & Compound Interest",
        spec_codes="L1.13 • L2.14",
        formula_hint="Simple interest: Starting Money × Interest Rate × Number of Years. Compound interest: Year 1 interest is added to the balance, then Year 2 interest is calculated on the new combined balance (Starting Balance × Multiplier × Multiplier).",
        q1={
            "title": "Question 1 (Level 1 Simple Interest)",
            "marks": 2,
            "stem": "Calculate the simple interest on an investment of <strong>£4,500</strong> for <strong>3 years</strong> at an interest rate of <strong>4% per annum</strong>.",
            "lines": 3,
            "ans_label": "Simple Interest =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. 1 year interest: 4% of £4,500 = £180", "[M1]"),
                ("2. 3 years: 3 × £180 = £540", "[A1]")
            ],
            "final_answer": "£540",
            "pitfall": "Calculating compound interest or stating the total balance (£5,040) instead of just the interest.",
            "reverse_check": "£540 ÷ 3 = £180; £180 ÷ £4,500 = 0.04 = 4%."
        },
        q2={
            "title": "Question 2 (Level 2 Compound Multiplier)",
            "marks": 2,
            "stem": "An emergency reserve fund of <strong>£12,000</strong> is deposited in a savings account paying <strong>3.5% compound interest per year</strong>.<br>Write down the single multiplier used to calculate the balance after 1 year, and calculate the interest earned in year 1.",
            "lines": 3,
            "ans_label": "Multiplier & Year 1 Interest =",
            "choice_box": "Multiplier: _____ | Interest: £ _____ ",
            "step_rows": [
                ("1. State multiplier: 1 + 0.035 = 1.035", "[M1]"),
                ("2. Calculate interest: £12,000 × 0.035 = £420.00", "[A1]")
            ],
            "final_answer": "Multiplier: 1.035; Year 1 Interest: £420.00",
            "pitfall": "Using 1.35 (which represents 35% interest).",
            "reverse_check": "£12,000 × 1.035 = £12,420; £12,420 - £12,000 = £420."
        },
        q3={
            "title": "Question 3 (Level 2 Two-Year Compound Growth)",
            "marks": 3,
            "stem": "A social enterprise invests <strong>£25,000</strong> in a green energy community bond.<br>The bond pays <strong>4% compound interest per year</strong>.<br><br>Work out the total value of the investment at the end of <strong>2 years</strong>.",
            "lines": 4,
            "ans_label": "Total Value =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Year 1: £25,000 × 1.04 = £26,000", "[M1]"),
                ("2. Year 2: £26,000 × 1.04 = £27,040", "[P1]"),
                ("3. State final balance: £27,040", "[A1]")
            ],
            "final_answer": "£27,040",
            "pitfall": "Treating as simple interest: 2 × (4% of £25k) = £2,000, giving £27,000 (missing the £40 interest on interest).",
            "reverse_check": "£25,000 × (1.04)² = £25,000 × 1.0816 = £27,040."
        },
        q4={
            "title": "Question 4 (Level 2 Loan Repayment APR Comparison)",
            "marks": 3,
            "stem": "A medical training consultancy borrows <strong>£8,000</strong> over 1 year.<br>• Bank A charges <strong>6% simple interest</strong> plus a <strong>£120 arrangement fee</strong>.<br>• Bank B charges <strong>7.5% simple interest</strong> with <strong>no arrangement fee</strong>.<br><br>Which bank loan is cheaper overall, and by how much?",
            "lines": 4,
            "ans_label": "Cheaper Bank & Saving =",
            "choice_box": "Bank _____ is cheaper by £ ____________",
            "step_rows": [
                ("1. Bank A: 6% of £8,000 = £480. Total cost: £480 + £120 = £600", "[M1]"),
                ("2. Bank B: 7.5% of £8,000 = £600. Total cost: £600", "[P1]"),
                ("3. Compare: Both cost exactly £600.00 (Difference: £0)", "[A1]")
            ],
            "final_answer": "Both loans cost exactly the same (£600 total finance cost)",
            "pitfall": "Forgetting the arrangement fee for Bank A.",
            "reverse_check": "Bank A: £480 + £120 = £600. Bank B: £600. Equal."
        },
        q5={
            "title": "Question 5 (Level 2 Three-Year Compound Interest Difference)",
            "marks": 4,
            "stem": "An NHS Trust legacy donation of <strong>£50,000</strong> is invested for <strong>3 years</strong>.<br>Account X pays <strong>5% simple interest per year</strong>.<br>Account Y pays <strong>5% compound interest per year</strong>.<br><br>Work out the extra interest earned by choosing Account Y instead of Account X over the 3 years.",
            "lines": 5,
            "ans_label": "Extra Interest =",
            "choice_box": "£ ____________________",
            "step_rows": [
                ("1. Account X (Simple): 3 × (0.05 × £50,000) = 3 × £2,500 = £7,500 interest", "[P1]"),
                ("2. Account Y (Compound): £50,000 × (1.05)³ = £50,000 × 1.157625 = £57,881.25", "[M1]"),
                ("3. Compound interest earned: £57,881.25 - £50,000 = £7,881.25", "[P1]"),
                ("4. Difference: £7,881.25 - £7,500.00 = £381.25", "[A1]")
            ],
            "final_answer": "£381.25 extra interest",
            "pitfall": "Subtracting final balance from interest (£57,881.25 - £7,500).",
            "reverse_check": "Yr 1: £2,500 / £2,500. Yr 2: £2,500 / £2,625 (+£125). Yr 3: £2,500 / £2,756.25 (+£256.25). £125 + £256.25 = £381.25."
        },
        q6={
            "title": "Question 6 (Level 2 Financial Growth Justification)",
            "marks": 4,
            "stem": "A community nursery invests <strong>£15,000</strong> in a growth bond earning <strong>6% compound interest annually</strong>.<br>The treasurer claims: <em>'At 6% compound interest, our investment will have grown by more than £2,800 by the end of Year 3.'</em><br><br>Is the treasurer correct?<br>Show your calculations year-by-year or with multipliers and state a clear conclusion.",
            "lines": 5,
            "ans_label": "Conclusion & Year 3 Interest =",
            "choice_box": "Correct / Incorrect: Total growth is £ ____________",
            "step_rows": [
                ("1. Year 1: £15,000 × 1.06 = £15,900", "[P1]"),
                ("2. Year 2: £15,900 × 1.06 = £16,854", "[P1]"),
                ("3. Year 3: £16,854 × 1.06 = £17,865.24", "[M1]"),
                ("4. Calculate total growth: £17,865.24 - £15,000 = £2,865.24. Compare: £2,865.24 > £2,800. Conclude: <strong>Yes, the treasurer is correct</strong> (growth exceeds £2,800 by £65.24).", "[A1]")
            ],
            "final_answer": "Correct (Total growth is £2,865.24, which exceeds £2,800)",
            "pitfall": "Calculating simple interest: 3 × £900 = £2,700, which would lead to the wrong conclusion 'No'.",
            "reverse_check": "£15,000 × (1.06)³ = £17,865.24; £17,865.24 - £15,000 = £2,865.24."
        }
    )
]

print(f"Loaded {len(CATALOG_MATHS_1)} topics in catalog_maths_1.py")
