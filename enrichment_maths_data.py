# Enrichment blocks for Maths Data & Probability topics to guarantee >= 30 questions per worksheet.

ENRICHMENT_MATHS_DATA = {
    "bar-charts": [
        {
            "title": "Question 2: Reading Scale Intervals & Frequencies",
            "instruction": "Determine the value on the vertical frequency axis:",
            "items": [
                ("a", "Vertical scale: Major marks at 0, 10, 20. Bar reaches 3 small marks past 10 (each small mark = 2). Value?", "16"),
                ("b", "Vertical scale: Major marks at 0, 50, 100. Bar reaches halfway between 50 and 100. Value?", "75"),
                ("c", "Scale marked in 5s (0, 5, 10, 15...). Bar is 2 marks above 20. Value?", "30"),
                ("d", "Dual bar chart: Group A has 45, Group B has 60. Difference between groups?", "15 (60 - 45)"),
                ("e", "Component bar chart: Segment 1 is £120, Segment 2 is £80. Total bar height?", "£200.00"),
                ("f", "Frequency bar chart: 4 categories with values 12, 18, 15, 25. Total frequency?", "70 (12 + 18 + 15 + 25)"),
                ("g", "Highest bar in a survey has 85 votes, lowest has 25 votes. Range of votes?", "60 votes (85 - 25)"),
                ("h", "Category A has 40 responses out of 200 total responses. What fraction?", "1/5 (40/200)"),
                ("i", "What percentage of 200 is Category A (40 responses)?", "20%"),
                ("j", "What is the primary visual error in a truncated bar chart with broken axis?", "It exaggerates small differences between bars")
            ]
        },
        {
            "title": "Question 3: Dual Bars, Comparisons & Workplace Data Extraction",
            "instruction": "Extract values and perform comparative calculations:",
            "items": [
                ("a", "Sales: Q1 £14,000, Q2 £18,000, Q3 £22,000, Q4 £26,000. Total annual sales?", "£80,000.00"),
                ("b", "Increase in sales between Q1 (£14,000) and Q4 (£26,000)?", "£12,000.00"),
                ("c", "Staff attendance: Mon 95%, Tue 92%, Wed 88%, Thu 94%, Fri 86%. Lowest day?", "Friday (86%)"),
                ("d", "Difference between highest and lowest attendance days (95% - 86%)?", "9%"),
                ("e", "Dual bar chart: Male staff = 34, Female staff = 46. Total headcount?", "80 staff"),
                ("f", "Dual bar chart: Percentage of staff who are female (46 out of 80)?", "57.5% (46 ÷ 80 × 100)"),
                ("g", "Hospital wards: Ward 1 has 18 patients, Ward 2 has 24, Ward 3 has 22. Average per ward?", "21.3 patients (64 ÷ 3)"),
                ("h", "Target is 50 sales per week. Actual sales: 54, 48, 62, 56. Number of weeks meeting target?", "3 weeks (54, 62, 56)"),
                ("i", "Why must all bars on a standard discrete chart have equal widths and gaps?", "To ensure visual proportionality and avoid misleading the reader"),
                ("j", "Can a bar chart represent continuous data? (Yes / No)", "No (continuous data uses histograms or line graphs)")
            ]
        }
    ],
    "comparing-data-sets": [
        {
            "title": "Question 2: Comparing Two Groups Using Averages and Range",
            "instruction": "Calculate mean and range for both groups to draw conclusions:",
            "items": [
                ("a", "Group A scores: 12, 14, 16, 18. Mean = ?", "15.0 (60 ÷ 4)"),
                ("b", "Group B scores: 10, 15, 20, 25. Mean = ?", "17.5 (70 ÷ 4)"),
                ("c", "Which group scored higher on average (higher mean)?", "Group B (17.5 vs 15.0)"),
                ("d", "Group A range (18 - 12) = ?", "6"),
                ("e", "Group B range (25 - 10) = ?", "15"),
                ("f", "Which group had more consistent scores (smaller range)?", "Group A (range 6 is more consistent than 15)"),
                ("g", "Clinic 1 wait times: Mean 28 mins, Range 10 mins. Clinic 2: Mean 32 mins, Range 25 mins. Which clinic has faster average service?", "Clinic 1 (faster mean of 28 mins)"),
                ("h", "Which clinic has more predictable waiting times?", "Clinic 1 (lower range of 10 mins)"),
                ("i", "Two teams: Team X median = 45, Team Y median = 42. Which team has higher typical score?", "Team X (higher median)"),
                ("j", "Why does an extreme outlier make the median a better average than the mean?", "The median is not skewed by extreme values, giving a truer typical value")
            ]
        },
        {
            "title": "Question 3: Standard Functional Skills Comparison Statements",
            "instruction": "State the comparative conclusion covering average AND spread:",
            "items": [
                ("a", "Tutor A pass rate: Mean 82%, Range 8%. Tutor B: Mean 76%, Range 18%. Complete: Tutor A had higher...", "Higher average pass rate and more consistent results"),
                ("b", "Machine 1: Mean weight 500g, Range 4g. Machine 2: Mean 500g, Range 18g. Which machine is better calibrated?", "Machine 1 (much smaller range, higher precision)"),
                ("c", "Branch North sales: £12k, £14k, £16k (Mean £14k). Branch South: £8k, £14k, £20k (Mean £14k). Do they have identical performance?", "Same average sales (£14k), but Branch North is more consistent (Range £4k vs £12k)"),
                ("d", "Company A median salary: £26,000. Company B median: £31,000. Difference in typical salary?", "£5,000 higher in Company B"),
                ("e", "Delivery Fleet 1 on-time rate: 94%, Range 3%. Fleet 2: 91%, Range 9%. Which fleet is more reliable?", "Fleet 1 (higher rate and smaller range)"),
                ("f", "What two mathematical measures MUST be included in an exam comparison question?", "One average (mean, median or mode) AND one measure of spread (range)")
            ]
        }
    ],
    "conversion-graphs": [
        {
            "title": "Question 3: Reading Intermediate Values on Conversion Lines",
            "instruction": "Use the conversion line to convert between units:",
            "items": [
                ("a", "Line passes through (0, 0) and (5 miles, 8 km). Convert 10 miles to km", "16 km (8 × 2)"),
                ("b", "Convert 20 miles to km using the line", "32 km (8 × 4)"),
                ("c", "Convert 24 km to miles using the line", "15 miles (5 × 3)"),
                ("d", "Convert 40 km to miles using the line", "25 miles (5 × 5)"),
                ("e", "Line passes through (0, 0) and (£10, $13). Convert £50 to dollars", "$65.00 (13 × 5)"),
                ("f", "Convert $26 to pounds using the line", "£20.00 (10 × 2)"),
                ("g", "Convert £100 to dollars using the line", "$130.00 (13 × 10)"),
                ("h", "Line passes through (0 kg, 0 lbs) and (5 kg, 11 lbs). Convert 15 kg to lbs", "33 lbs (11 × 3)"),
                ("i", "Convert 55 lbs to kg using the line", "25 kg (5 × 5)"),
                ("j", "Convert 1 kg to lbs (estimate from 5 kg = 11 lbs)", "2.2 lbs (11 ÷ 5)")
            ]
        },
        {
            "title": "Question 4: Non-Zero Intercepts (Fixed Charges & Tariffs)",
            "instruction": "Read cost graphs featuring a fixed standing charge:",
            "items": [
                ("a", "Electricity graph starts at £15 on vertical axis (0 units). What is the fixed standing charge?", "£15.00"),
                ("b", "Total cost for 100 units is £35. Cost of 100 units excluding standing charge?", "£20.00 (£35 - £15)"),
                ("c", "Cost per unit (unit rate) = £20 ÷ 100 units = ?", "£0.20 (20p per unit)"),
                ("d", "Total cost for 200 units using graph (£15 + 200 × £0.20) = ?", "£55.00"),
                ("e", "Taxi graph starts at £3.50 (0 miles). 10 miles costs £21.50. Cost of the 10 miles travel alone?", "£18.00 (£21.50 - £3.50)"),
                ("f", "Taxi rate per mile (£18 ÷ 10 miles) = ?", "£1.80 per mile"),
                ("g", "Cost of a 5-mile taxi journey using graph?", "£12.50 (£3.50 + 5 × £1.80)"),
                ("h", "Hire car graph: £40 deposit + £25/day. Cost for 4 days?", "£140.00 (£40 + £100)"),
                ("i", "If customer paid £115 on hire car, how many days did they hire? ((115-40)÷25)", "3 days"),
                ("j", "What feature on a graph represents the unit rate or speed?", "The gradient (steepness) of the line")
            ]
        }
    ],
    "data-tables": [
        {
            "title": "Question 2: Completing Two-Way Frequency Tables",
            "instruction": "Find the missing cell values in two-way tables:",
            "items": [
                ("a", "Row: 24 Full-Time, 16 Part-Time. Row Total = ?", "40"),
                ("b", "Column: Men = 18, Total = 45. Women = ?", "27 (45 - 18)"),
                ("c", "Table has 60 adults and 40 children. Grand total = ?", "100"),
                ("d", "Of 60 adults, 35 chose tea and remaining chose coffee. Adults choosing coffee?", "25 (60 - 35)"),
                ("e", "Total choosing tea is 50 (35 adults + ? children). Children choosing tea?", "15 (50 - 35)"),
                ("f", "Of 40 children, 15 chose tea. Children choosing coffee?", "25 (40 - 15)"),
                ("g", "Total choosing coffee (25 adults + 25 children) = ?", "50"),
                ("h", "Check: Does Total Tea (50) + Total Coffee (50) equal Grand Total (100)?", "Yes (50 + 50 = 100)"),
                ("i", "Fraction of all participants who are adults choosing tea (35 out of 100)?", "7/20 (35%)"),
                ("j", "Percentage of children who chose coffee (25 out of 40)?", "62.5% (25 ÷ 40 × 100)")
            ]
        },
        {
            "title": "Question 3: Timetables, Delivery Matrices & Rate Tables",
            "instruction": "Look up information across rows and columns:",
            "items": [
                ("a", "Train timetable: Leaves Station A at 08:14, arrives Station B at 08:52. Journey time?", "38 minutes"),
                ("b", "Next train leaves at 08:44, arrives at 09:25. Journey time?", "41 minutes"),
                ("c", "Which train is faster: 08:14 (38m) or 08:44 (41m)?", "08:14 train (3 minutes faster)"),
                ("d", "Courier matrix: Zone 1 parcel up to 5kg costs £6.50. Cost for three 4kg parcels?", "£19.50 (3 × £6.50)"),
                ("e", "Zone 2 parcel up to 10kg costs £12.00. Surcharge for Saturday is £5.00. Total?", "£17.00"),
                ("f", "Swimming pool price table: Adult £6.50, Junior £4.00. Cost for 2 adults and 3 juniors?", "£25.00 (13 + 12)"),
                ("g", "Family pass is £22.00. How much is saved by buying the family pass (£25 - £22)?", "£3.00 saving"),
                ("h", "Parking rate table: Up to 2 hrs £3.00, 2-4 hrs £5.50, 4+ hrs £8.00. Arrive 10:15, leave 13:45 (3.5 hrs). Fee?", "£5.50 (2 to 4 hours bracket)"),
                ("i", "Hotel rate card: Single room £65, Double room £85. Breakfast £10/person. Cost for double room with 2 breakfasts?", "£105.00 (85 + 20)"),
                ("j", "Conference room matrix: Room A capacity 30, Room B 50. 42 delegates attending. Which room is required?", "Room B (Room A is too small)")
            ]
        }
    ],
    "estimating-the-mean": [
        {
            "title": "Question 2: Midpoints of Grouped Class Intervals",
            "instruction": "Find the exact midpoint of each group interval:",
            "items": [
                ("a", "Class interval: 0 < t ≤ 10. Midpoint = ?", "5 ((0 + 10) ÷ 2)"),
                ("b", "Class interval: 10 < t ≤ 20. Midpoint = ?", "15 ((10 + 20) ÷ 2)"),
                ("c", "Class interval: 20 < t ≤ 30. Midpoint = ?", "25"),
                ("d", "Class interval: 30 < t ≤ 50. Midpoint = ?", "40 ((30 + 50) ÷ 2)"),
                ("e", "Class interval: 50 < t ≤ 100. Midpoint = ?", "75 ((50 + 100) ÷ 2)"),
                ("f", "Class interval: 100 < t ≤ 200. Midpoint = ?", "150"),
                ("g", "Class interval: £20 to £40. Midpoint = ?", "£30.00"),
                ("h", "Class interval: 1.4 m to 1.6 m. Midpoint = ?", "1.5 m"),
                ("i", "Why do we use midpoints when estimating the mean from grouped data?", "The exact individual raw values are unknown, so the midpoint represents the group"),
                ("j", "Is the calculated mean from a grouped frequency table an exact value or an estimate?", "An estimate")
            ]
        },
        {
            "title": "Question 3: Frequency × Midpoint Products (Σfx ÷ Σf)",
            "instruction": "Calculate midpoint × frequency and find estimated mean:",
            "items": [
                ("a", "Midpoint 5, Frequency 4. Product fx = ?", "20"),
                ("b", "Midpoint 15, Frequency 6. Product fx = ?", "90"),
                ("c", "Midpoint 25, Frequency 10. Product fx = ?", "250"),
                ("d", "Total frequency Σf = 4 + 6 + 10 = ?", "20"),
                ("e", "Total fx Σfx = 20 + 90 + 250 = ?", "360"),
                ("f", "Estimated mean: Σfx ÷ Σf = 360 ÷ 20 = ?", "18.0"),
                ("g", "Midpoint 10, Frequency 5 (50); Midpoint 20, Frequency 15 (300). Total fx?", "350 (50 + 300)"),
                ("h", "Total frequency Σf = 5 + 15 = 20. Estimated mean = 350 ÷ 20 = ?", "17.5"),
                ("i", "Identify the modal group in a table where group 10-20 has highest frequency 15", "10 < t ≤ 20"),
                ("j", "What is the common error when calculating grouped mean?", "Dividing by the number of rows instead of the total frequency (Σf)")
            ]
        }
    ],
    "grouped-data": [
        {
            "title": "Question 2: Class Intervals, Boundaries & Modal Class",
            "instruction": "Identify the modal class, interval width, and frequencies:",
            "items": [
                ("a", "Intervals: 0-10 (freq 5), 10-20 (freq 14), 20-30 (freq 8). Modal class?", "10-20 (highest frequency of 14)"),
                ("b", "Class width of interval 10 < w ≤ 25 = ?", "15 (25 - 10)"),
                ("c", "Which group contains the value 10 in: 0 ≤ x < 10 or 10 ≤ x < 20?", "10 ≤ x < 20 (includes 10)"),
                ("d", "Total number of people surveyed: 5 + 14 + 8 = ?", "27"),
                ("e", "How many people had values greater than 10?", "22 (14 + 8)"),
                ("f", "What fraction of the total (27) is the modal class (14)?", "14/27"),
                ("g", "In which group does the median lie for 27 people? ((27+1)÷2 = 14th person)", "10-20 group (covers positions 6 to 19)"),
                ("h", "Difference between continuous and discrete grouped data", "Continuous data can take any decimal value (e.g. weight, time); discrete only whole units (e.g. books)")
            ]
        },
        {
            "title": "Question 3: Practical Frequency Polygon & Histogram Interpretations",
            "instruction": "Answer questions on grouped frequency charts:",
            "items": [
                ("a", "At what coordinate point are frequency polygons plotted horizontally?", "At the class midpoints"),
                ("b", "If modal class is £200-£300 with frequency 40, what does this tell an employer?", "The most common wage bracket is £200 to £300"),
                ("c", "Cumulative frequency for groups with frequencies 8, 12, 15, 5 at group 2?", "20 (8 + 12)"),
                ("d", "Cumulative frequency at group 3?", "35 (20 + 15)"),
                ("e", "Grand total cumulative frequency at group 4?", "40 (35 + 5)"),
                ("f", "How many workers earn less than the upper boundary of group 3?", "35 workers"),
                ("g", "Percentage of workers in group 1 (8 out of 40)?", "20% (8 ÷ 40 × 100)"),
                ("h", "Percentage of workers in group 3 (15 out of 40)?", "37.5%")
            ]
        }
    ],
    "line-graphs": [
        {
            "title": "Question 2: Reading Time-Series Trends on Line Graphs",
            "instruction": "Read data points over time and describe trends:",
            "items": [
                ("a", "Temperature at 09:00 was 12°C, at 14:00 was 20°C. Temperature change?", "8°C rise"),
                ("b", "Between 14:00 (20°C) and 18:00 (15°C). Temperature change?", "5°C drop"),
                ("c", "Peak temperature time if highest point on line is at 15:00", "15:00 (3:00 pm)"),
                ("d", "Overall trend: Line rises steadily from Monday to Friday. Trend description?", "Upward / Increasing trend"),
                ("e", "Overall trend: Line slopes downwards from January to June. Trend description?", "Downward / Decreasing trend"),
                ("f", "Line is flat horizontal between 11:00 and 13:00. Trend description?", "Constant / No change"),
                ("g", "Sales graph: Mon £300, Tue £450, Wed £400, Thu £550, Fri £700. Average daily sales?", "£480.00 (£2,400 ÷ 5)"),
                ("h", "Day with the biggest single-day increase in sales?", "Thursday to Friday (+£150)"),
                ("i", "Difference between Friday (£700) and Monday (£300)?", "£400.00"),
                ("j", "Estimate temperature at 10:30 if line passes through 10:00 (14°C) and 11:00 (18°C)", "16°C (halfway)")
            ]
        },
        {
            "title": "Question 3: Dual-Line Graph Comparisons",
            "instruction": "Compare two lines (e.g. Product A vs Product B):",
            "items": [
                ("a", "In June, Product A sold 400 units, Product B sold 250 units. Difference?", "150 units"),
                ("b", "At what month do the two lines intersect if they cross in August at 320 units?", "August (equal sales of 320)"),
                ("c", "Which product showed faster overall growth between January and December?", "Product with steeper upward slope"),
                ("d", "Patient pulse rate over 6 hours: 72, 75, 80, 85, 78, 70. Range of pulse rates?", "15 bpm (85 - 70)"),
                ("e", "Target range for patient is 60 to 80 bpm. Did pulse exceed target? At what value?", "Yes, peaked at 85 bpm"),
                ("f", "Why are line graphs particularly effective for showing changes over continuous time?", "They clearly show the rate of change and continuity between time intervals")
            ]
        }
    ],
    "lists": [
        {
            "title": "Question 2: Systematic Listing & Combinations (Outcomes)",
            "instruction": "List all possible combinations or outcomes systematically:",
            "items": [
                ("a", "Sandwich choice (Ham, Cheese) and Drink choice (Water, Juice). How many lunch deals?", "4 combos (2 × 2: HW, HJ, CW, CJ)"),
                ("b", "Starter (Soup, Salad), Main (Pasta, Fish, Steak). Total 2-course meal combinations?", "6 combos (2 × 3)"),
                ("c", "Shirt colours (Red, Blue, White) and Ties (Silk, Wool). Total combinations?", "6 combos (3 × 2)"),
                ("d", "Coin toss (H, T) and standard 6-sided die roll (1-6). Total possible outcomes?", "12 outcomes (2 × 6)"),
                ("e", "Passcode: 2 digits from 0 to 9 with repetition allowed. How many combinations?", "100 combos (10 × 10)"),
                ("f", "Passcode: 3 digits from 1 to 5 with NO repetition. How many combinations?", "60 combos (5 × 4 × 3)"),
                ("g", "4 runners in a race. How many different 1st and 2nd place orderings?", "12 orderings (4 × 3)"),
                ("h", "Team has 5 members. How many different pairs of 2 can be selected? (5×4÷2)", "10 pairs"),
                ("i", "Why is systematic listing essential in probability exams?", "It prevents accidental omissions or counting duplicates"),
                ("j", "What visual diagram can display all combinations branching out?", "Tree diagram")
            ]
        },
        {
            "title": "Question 3: Sorting, Filtering & Priority Lists",
            "instruction": "Filter and rank the items based on given criteria:",
            "items": [
                ("a", "List: [12, 45, 8, 23, 67, 34, 19]. Filter all numbers greater than 30", "45, 67, 34"),
                ("b", "List: [£1.20, £3.50, £0.85, £4.00, £2.10]. Filter prices under £2.00", "£1.20, £0.85"),
                ("c", "Rank in ascending order: [4.2, 4.05, 4.25, 4.15, 4.002]", "4.002, 4.05, 4.15, 4.2, 4.25"),
                ("d", "Urgent patient triage list: Red (immediate), Amber (10 mins), Green (60 mins). Which has highest priority?", "Red (immediate)"),
                ("e", "Job queue times: 15m, 45m, 20m, 30m. Total queue time?", "1 hour 50 minutes (110 mins)"),
                ("f", "Shortest job first rule on [40m, 15m, 25m]. Optimal order?", "15m, then 25m, then 40m")
            ]
        }
    ],
    "mean-median-mode-and-range": [
        {
            "title": "Question 5: Averages Selection & Reverse Mean Drills",
            "instruction": "Solve reverse average problems and select appropriate average:",
            "items": [
                ("a", "The mean of 4 numbers is 10. What is their total sum?", "40 (4 × 10)"),
                ("b", "Three numbers are 8, 12, 11 (sum 31). Mean of 4 numbers is 10 (sum 40). 4th number?", "9 (40 - 31)"),
                ("c", "Mean of 5 test scores is 70% (total 350). First 4 are 65, 75, 80, 60 (sum 280). 5th score?", "70% (350 - 280)"),
                ("d", "Average shoe size sold in a shop: Mean or Mode?", "Mode (shops order most common shoe sizes)"),
                ("e", "Average household income when CEO earns £5m and 99 staff earn £25k: Mean or Median?", "Median (unaffected by extreme executive salary)"),
                ("f", "Average exam score of 30 students: Mean or Mode?", "Mean (takes all student marks into account)")
            ]
        }
    ],
    "pie-charts": [
        {
            "title": "Question 2: Angles to Fractions & Proportions (360° Total)",
            "instruction": "Convert sector angles into simplified fractions of a 360° pie chart:",
            "items": [
                ("a", "Sector angle 90°. What fraction of the pie chart? (90/360)", "1/4 (25%)"),
                ("b", "Sector angle 180°. What fraction of the pie chart? (180/360)", "1/2 (50%)"),
                ("c", "Sector angle 60°. What fraction of the pie chart? (60/360)", "1/6"),
                ("d", "Sector angle 120°. What fraction of the pie chart? (120/360)", "1/3"),
                ("e", "Sector angle 45°. What fraction of the pie chart? (45/360)", "1/8 (12.5%)"),
                ("f", "Sector angle 36°. What fraction of the pie chart? (36/360)", "1/10 (10%)"),
                ("g", "Sector angle 72°. What fraction of the pie chart? (72/360)", "1/5 (20%)"),
                ("h", "Sector angle 270°. What fraction of the pie chart? (270/360)", "3/4 (75%)"),
                ("i", "A category represents 10% of total. What angle in degrees? (10% of 360°)", "36°"),
                ("j", "A category represents 40% of total. What angle in degrees? (0.4 × 360°)", "144°")
            ]
        },
        {
            "title": "Question 3: Calculating Frequencies from Angles",
            "instruction": "Work out actual frequencies given the total population:",
            "items": [
                ("a", "Total surveyed = 120 people. Sector angle = 90° (1/4). How many people?", "30 people (120 ÷ 4)"),
                ("b", "Total surveyed = 120 people. Sector angle = 180° (1/2). How many people?", "60 people"),
                ("c", "Total surveyed = 120 people. Sector angle = 60° (1/6). How many people?", "20 people (120 ÷ 6)"),
                ("d", "Total budget = £72,000. Sector angle for staffing = 150°. Staff budget? (150/360 × 72000)", "£30,000.00"),
                ("e", "Total budget = £72,000. Sector angle for rent = 90°. Rent budget?", "£18,000.00"),
                ("f", "Total 360 workers. Category has angle 45°. Number of workers?", "45 workers (1 degree = 1 worker)"),
                ("g", "Total 720 students. Category has angle 70°. Number of students? (2 per degree)", "140 students (70 × 2)"),
                ("h", "Total 200 cars. Red cars represent 72° (1/5). How many red cars?", "40 cars (200 ÷ 5)"),
                ("i", "Can two pie charts of different sizes be compared directly by sector angle without knowing total populations?", "No, because a larger angle in a smaller population can represent fewer people"),
                ("j", "What instrument is used to draw and measure pie chart sector angles accurately?", "Protractor")
            ]
        }
    ],
    "probability": [
        {
            "title": "Question 3: Single Event Probability (Fractions, Decimals, Percentages)",
            "instruction": "Express probability as a simplified fraction, decimal, and percentage:",
            "items": [
                ("a", "Rolling an even number on a 6-sided die (2, 4, 6 out of 6)", "1/2 (0.5 or 50%)"),
                ("b", "Rolling a number greater than 4 on a 6-sided die (5, 6 out of 6)", "1/3 (2/6 ÷ 2)"),
                ("c", "Rolling a prime number on a 6-sided die (2, 3, 5 out of 6)", "1/2"),
                ("d", "Rolling a 7 on a standard 6-sided die", "0 (Impossible)"),
                ("e", "Bag has 5 red, 3 blue, 2 green balls (10 total). P(Red)?", "1/2 (5/10)"),
                ("f", "P(Blue) from the bag of 10 balls?", "3/10 (0.3 or 30%)"),
                ("g", "P(Green) from the bag of 10 balls?", "1/5 (2/10)"),
                ("h", "P(Not Red) from the bag (1 - 5/10)?", "1/2 (5/10)"),
                ("i", "Drawing an Ace from a standard deck of 52 playing cards (4 Aces)", "1/13 (4/52)"),
                ("j", "Drawing a Heart from a standard deck of 52 cards (13 Hearts)", "1/4 (13/52)")
            ]
        },
        {
            "title": "Question 4: Expected Frequencies & The 'Not' Rule (P(Not A) = 1 - P(A))",
            "instruction": "Calculate expected occurrences (Probability × Number of Trials):",
            "items": [
                ("a", "P(Rain) = 0.2. What is P(No Rain)?", "0.8 (1 - 0.2)"),
                ("b", "P(Defective item) = 0.05. P(Non-defective)?", "0.95 (95%)"),
                ("c", "P(Winning raffle) = 1/50. P(Not winning)?", "49/50 (98%)"),
                ("d", "P(Late train) = 0.15. Out of 200 train journeys, expected number of late trains?", "30 trains (200 × 0.15)"),
                ("e", "P(Pass exam) = 0.85. Out of 40 students, expected passes?", "34 students (40 × 0.85)"),
                ("f", "Flip coin 100 times. Expected number of Heads? (0.5 × 100)", "50 Heads"),
                ("g", "Roll 6-sided die 60 times. Expected number of 6s? (1/6 × 60)", "10 times"),
                ("h", "Factory produces 10,000 chips. Defect rate is 2%. Expected defective chips?", "200 chips (10,000 × 0.02)"),
                ("i", "Probability of an event that is certain to occur", "1 (or 100%)"),
                ("j", "Can a probability ever be negative or greater than 1?", "No (always between 0 and 1)")
            ]
        }
    ],
    "probability-tables": [
        {
            "title": "Question 3: Missing Probability Calculations (Total = 1.0)",
            "instruction": "Find the missing probability so that all probabilities sum to 1.0:",
            "items": [
                ("a", "Outcomes: Red (0.3), Blue (0.4), Green (?). P(Green) = ?", "0.3 (1 - 0.7)"),
                ("b", "Outcomes: Win (0.55), Draw (0.25), Lose (?). P(Lose) = ?", "0.20 (1 - 0.80)"),
                ("c", "Outcomes: Walk (0.2), Bus (0.35), Car (0.3), Bike (?). P(Bike) = ?", "0.15 (1 - 0.85)"),
                ("d", "Outcomes: A (1/4), B (1/2), C (?). P(C) = ?", "1/4 (1 - 3/4)"),
                ("e", "Outcomes: 1 (0.1), 2 (0.15), 3 (0.25), 4 (0.2), 5 (?). P(5) = ?", "0.30 (1 - 0.70)"),
                ("f", "A spinner has 4 colours. Red and Blue are 0.3 each. Green and Yellow are equal. P(Green)?", "0.20 ((1 - 0.6) ÷ 2)"),
                ("g", "P(Yellow) on the same spinner?", "0.20"),
                ("h", "True or False: The sum of probabilities of all mutually exclusive outcomes is always 1.", "True"),
                ("i", "Outcomes: Small (0.45), Medium (0.35), Large (?). P(Large) = ?", "0.20 (1 - 0.80)"),
                ("j", "Outcomes: Morning (40%), Afternoon (35%), Evening (?). P(Evening) = ?", "25% (0.25)")
            ]
        },
        {
            "title": "Question 4: Two-Way Probability & Relative Frequency",
            "instruction": "Calculate probability from frequency tables:",
            "items": [
                ("a", "Survey of 50 people: 20 take bus. Probability of randomly picking bus rider?", "2/5 (20/50 = 0.4)"),
                ("b", "Out of 80 employees, 32 work night shifts. Probability of picking night worker?", "2/5 (32/80 = 0.4)"),
                ("c", "Out of 120 cars, 18 are electric. Probability of non-electric car? (102/120)", "17/20 (0.85 or 85%)"),
                ("d", "Medical trial: 45 recovered, 5 did not (50 total). Relative frequency of recovery?", "0.90 (45/50 = 90%)"),
                ("e", "If 500 patients tested, expected recoveries based on trial (0.90 × 500)?", "450 patients"),
                ("f", "Coin tossed 50 times landed on Heads 28 times. Experimental relative frequency?", "0.56 (28/50)"),
                ("g", "Theoretical probability of Heads (0.50). Why was experimental different?", "Small sample size / random variation (law of large numbers brings it closer over many trials)"),
                ("h", "How can experimental probability be made more reliable?", "Increase the number of trials / repeat experiment many times")
            ]
        }
    ],
    "scatter-graphs": [
        {
            "title": "Question 2: Types of Correlation & Relationship Identification",
            "instruction": "State whether correlation is Positive, Negative, or Zero (No correlation):",
            "items": [
                ("a", "Hours spent revising and Exam marks scored", "Positive correlation (more revision → higher marks)"),
                ("b", "Age of a used car and Market selling price", "Negative correlation (older car → lower price)"),
                ("c", "Height of a person and their Shoe size", "Positive correlation (taller person → larger feet)"),
                ("d", "Daily temperature and Sales of hot chocolate", "Negative correlation (warmer weather → fewer hot drinks)"),
                ("e", "Person's hair color and their IQ test score", "Zero / No correlation (unrelated variables)"),
                ("f", "Engine size of a car and Fuel consumption (miles per gallon)", "Negative correlation (larger engine → lower mpg)"),
                ("g", "Distance travelled in taxi and Fare charged", "Positive correlation (longer distance → higher fare)"),
                ("h", "Number of days absent and Annual salary", "Negative correlation (or zero, generally negative impact)"),
                ("i", "Points slope upwards from bottom-left to top-right on graph", "Positive correlation"),
                ("j", "Points slope downwards from top-left to bottom-right on graph", "Negative correlation")
            ]
        },
        {
            "title": "Question 3: Line of Best Fit, Outliers & Trend Interpolation",
            "instruction": "Interpret scatter points, outliers, and trend lines:",
            "items": [
                ("a", "A single point sits far away from the clustered line of best fit. What is this point called?", "An outlier (or anomaly)"),
                ("b", "What should generally be done with an obvious anomalous recording error when drawing a line of best fit?", "Ignore the outlier so it does not distort the line"),
                ("c", "Line of best fit passes through (2 hours revision, 40 marks) and (6 hours revision, 80 marks). Estimate mark for 4 hours revision", "60 marks (halfway)"),
                ("d", "Estimate mark for 5 hours revision using the line", "70 marks"),
                ("e", "Estimate mark for 1 hour revision using the line", "30 marks"),
                ("f", "What is estimating a value WITHIN the range of existing data points called?", "Interpolation (reliable)"),
                ("g", "What is estimating a value OUTSIDE the range of existing data points called?", "Extrapolation (unreliable / speculative)"),
                ("h", "Why is extrapolation risky in business sales forecasting?", "Trends may not continue linearly beyond known data boundaries"),
                ("i", "Does correlation prove that one variable causes the other (causation)?", "No (correlation does not imply causation)"),
                ("j", "How many points should ideally be above and below a well-balanced line of best fit?", "Approximately equal number of points on both sides")
            ]
        }
    ],
    "tables": [
        {
            "title": "Question 3: Multi-Column Workplace Spreadsheets & Invoices",
            "instruction": "Calculate missing row and column totals in structured tables:",
            "items": [
                ("a", "Row: Item A £45, Item B £65, Item C £120. Row Subtotal = ?", "£230.00"),
                ("b", "Row: 15 units at £8.00 per unit. Line Total = ?", "£120.00"),
                ("c", "Row: 24 units at £4.50 per unit. Line Total = ?", "£108.00"),
                ("d", "Row: 50 units at £1.20 per unit. Line Total = ?", "£60.00"),
                ("e", "Subtotal of rows: £120 + £108 + £60 = ?", "£288.00"),
                ("f", "Discount of 10% on £288.00 subtotal = ?", "£28.80"),
                ("g", "Net total after 10% discount (£288 - £28.80) = ?", "£259.20"),
                ("h", "Delivery surcharge £15.00 added to £259.20. Final Total Payable = ?", "£274.20"),
                ("i", "Column total check: Department A £1,450, Dept B £2,200, Dept C £850. Grand total?", "£4,500.00"),
                ("j", "Table sorting: What happens when a list of names is sorted alphabetically (A-Z)?", "Sorted in ascending alphabetical order")
            ]
        },
        {
            "title": "Question 4: Timetables & Scheduled Handover Windows",
            "instruction": "Extract time slots and verify durations from tabular schedules:",
            "items": [
                ("a", "Shift schedule: Clinic handover 07:30-08:00 (30m), Ward rounds 08:00-11:30. Ward round duration?", "3 hours 30 minutes"),
                ("b", "Break 11:30-12:15. Break duration?", "45 minutes"),
                ("c", "Clinic appointments: 12:15-16:00. Clinic duration?", "3 hours 45 minutes"),
                ("d", "Total working time in shift excluding 45m break (07:30 to 16:00 = 8h 30m total)?", "7 hours 45 minutes"),
                ("e", "Bus schedule: Bus leaves town every 20 mins starting at 06:10. List next 3 buses", "06:30, 06:50, 07:10"),
                ("f", "Arrive at bus stop at 07:02. How many minutes wait for 07:10 bus?", "8 minutes wait"),
                ("g", "Flight timetable: Departs London 13:25, Arrives Rome 16:55 local time (+1h zone). Actual flight time?", "2 hours 30 minutes"),
                ("h", "Cinema timetable: Film starts 19:40, runs for 115 minutes (1h 55m). Film ends at?", "21:35")
            ]
        }
    ],
    "tally-charts": [
        {
            "title": "Question 3: Tally Grouping & Frequency Verification",
            "instruction": "Convert tally marks into numbers and verify frequencies:",
            "items": [
                ("a", "Two full gates of tally (卌 卌) plus 3 single strokes = ?", "13 (5 + 5 + 3)"),
                ("b", "Four full gates of tally (卌 卌 卌 卌) = ?", "20 (4 × 5)"),
                ("c", "Three full gates of tally plus 4 strokes = ?", "19 (15 + 4)"),
                ("d", "Write 17 in tally format description", "3 full gates of 5, plus 2 individual marks"),
                ("e", "Write 26 in tally format description", "5 full gates of 5, plus 1 individual mark"),
                ("f", "Tally chart row: Car (18), Van (12), Lorry (6), Bus (4). Total vehicles?", "40 vehicles"),
                ("g", "Fraction of vehicles that were Vans (12 out of 40)?", "3/10 (30%)"),
                ("h", "Percentage of vehicles that were Cars (18 out of 40)?", "45% (18 ÷ 40 × 100)"),
                ("i", "Why are tally marks grouped in bundles of 5 with a diagonal slash?", "To make counting rapid and prevent miscounting individual lines"),
                ("j", "What is the frequency column in a tally chart?", "The numerical total count of tally marks for that category")
            ]
        },
        {
            "title": "Question 4: Creating Frequency Distributions from Raw Data",
            "instruction": "Tally and count the frequencies from raw survey data:",
            "items": [
                ("a", "Raw scores: [3, 4, 3, 5, 3, 2, 4, 3, 5, 3]. Frequency of score 3?", "5 times"),
                ("b", "Frequency of score 4?", "2 times"),
                ("c", "Frequency of score 5?", "2 times"),
                ("d", "Frequency of score 2?", "1 time"),
                ("e", "Check: Total frequencies sum (5 + 2 + 2 + 1) = ?", "10 (matches total items)"),
                ("f", "Modal score in this data set?", "3 (highest frequency of 5)"),
                ("g", "Range of scores (5 - 2) = ?", "3"),
                ("h", "Mean score: (3×5 + 4×2 + 5×2 + 2×1) ÷ 10 = (15 + 8 + 10 + 2) ÷ 10 = ?", "3.5")
            ]
        }
    ]
}
