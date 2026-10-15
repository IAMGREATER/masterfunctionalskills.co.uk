#!/usr/bin/env python3
"""Maths Domain 3: Measures, Instruments & Compound Units (7 Core Topics)"""

TOPICS_DOMAIN3 = [
    {
        'filename': 'functional-skills-time.html',
        'clean_topic': 'Time, 24-Hour Clocks & Timetables',
        'intro_lead': 'Convert between 12-hour and 24-hour time, calculate elapsed time across day boundaries, read complex healthcare and transport timetables, and schedule clinical appointments.',
        'next_file': 'functional-skills-speed.html',
        'next_name': 'Speed, Distance & Time',
        'spec_points': [
            ('L1.16 / L2.18', 'Calculate with time in 12-hour and 24-hour clocks, including time intervals across hours and days.'),
            ('L1.17', 'Read, interpret and use information from complex timetables and schedules.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-clock',
                'title': 'Golden Rule 1: Time is Base-60, NOT Base-100',
                'desc': 'There are 60 minutes in an hour, not 100. 1 hour and 45 minutes is 1.75 hours (45/60 = 0.75), NOT 1.45 hours!',
                'badge': '15 mins = 0.25 hrs | 30 mins = 0.5 hrs | 45 mins = 0.75 hrs'
            },
            {
                'icon': 'fa-calendar-days',
                'title': 'Golden Rule 2: The Timeline Bridge for Elapsed Time',
                'desc': 'When calculating time elapsed (e.g. from 09:45 to 13:20), jump forward to the next whole hour first (09:45 to 10:00 = 15m), count whole hours (10:00 to 13:00 = 3h), then add remaining minutes (13:00 to 13:20 = 20m). Total = 3h 35m.',
                'badge': 'Jump to Next Hour → Count Whole Hours → Add Remaining Minutes'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Converting Between 12-Hour (AM/PM) and 24-Hour Clock Formats',
                'summary': 'The +12 rule for afternoon/evening hours and handling 12:00 midnight/noon.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Time Period</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">12-Hour Clock</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">24-Hour Clock (4 Digits)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Conversion Rule</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Midnight Hour</td><td style="padding:6px; border:1px solid #cbd5e1;">12:25 am</td><td style="padding:6px; border:1px solid #cbd5e1;">00:25</td><td style="padding:6px; border:1px solid #cbd5e1;">Replace 12 am with 00</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Morning (AM)</td><td style="padding:6px; border:1px solid #cbd5e1;">8:40 am</td><td style="padding:6px; border:1px solid #cbd5e1;">08:40</td><td style="padding:6px; border:1px solid #cbd5e1;">Add leading zero if under 10</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Noon Hour</td><td style="padding:6px; border:1px solid #cbd5e1;">12:30 pm</td><td style="padding:6px; border:1px solid #cbd5e1;">12:30</td><td style="padding:6px; border:1px solid #cbd5e1;">Keep 12 unchanged</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Afternoon / Evening (PM)</td><td style="padding:6px; border:1px solid #cbd5e1;">4:15 pm</td><td style="padding:6px; border:1px solid #cbd5e1;">16:15</td><td style="padding:6px; border:1px solid #cbd5e1;">Add 12 to the hour (4 + 12 = 16)</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Skill 2: Converting Decimal Hours to Hours & Minutes (and Vice Versa)',
                'summary': 'Avoiding the #1 time calculation error in Functional Skills.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Decimal Hours to Minutes (× 60):</strong> Multiply the decimal part by 60: <em>2.4 hours = 2 hours + (0.4 × 60) = 2 hours 24 minutes.</em></li>
                    <li><strong>Minutes to Decimal Hours (÷ 60):</strong> Divide the minutes by 60: <em>1 hour 36 minutes = 1 + (36 ÷ 60) = 1.6 hours.</em></li>
                    <li><strong>Common Benchmarks:</strong> <code>15 mins = 0.25 h</code> &bull; <code>20 mins = 1/3 h</code> &bull; <code>30 mins = 0.5 h</code> &bull; <code>45 mins = 0.75 h</code>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 3: Working Backwards from Arrival Deadlines (Latest Departure Timetables)',
                'summary': 'How to select the right bus or train and work backwards to home departure time.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Find the Latest Arrival at Station/Stop:</strong> Subtract the walking time from the final appointment deadline (e.g. Appointment <code>09:30</code> minus <code>12 mins</code> walk = must arrive at station by <code>09:18</code>).</li>
                    <li><strong>Select the Correct Train/Bus Column:</strong> Scan the destination row on the timetable and pick the latest service that arrives <strong>on or before</strong> <code>09:18</code> (e.g. arrives <code>09:12</code>; an arrival at <code>09:22</code> is too late!).</li>
                    <li><strong>Read Up the Same Column:</strong> Trace up that exact column to find the departure time from the starting station.</li>
                  </ol>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Hospital Community Midwife Home Visit Timetable',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Community Health Nursing Travel Schedule',
                'question': "A community midwife departs the clinic at <strong>08:35</strong>. She drives for <strong>40 minutes</strong> to Patient A, spends <strong>55 minutes</strong> conducting a post-natal examination, and drives for <strong>25 minutes</strong> to Patient B.<br>At what time in 24-hour format does she arrive at Patient B's home?",
                'steps': [
                    ('Step 1', 'Sum total elapsed travel and appointment time', '40 mins drive + 55 mins appointment + 25 mins drive = 120 minutes.', 'M1: Total minutes summation'),
                    ('Step 2', 'Convert 120 minutes into hours', '120 ÷ 60 = exactly 2 hours.', 'M1: Conversion to hours'),
                    ('Step 3', 'Add 2 hours to departure time (08:35)', '08:35 + 2 hours = 10:35.', 'A1: Accurate 24-hour arrival time')
                ],
                'final_answer': 'Arrival Time = 10:35',
                'tutor_tip': 'Notice how 40 + 55 + 25 = 120 minutes = exactly 2 hours. Adding whole hours to 08:35 is immediate.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Surgical Sterilisation Autoclave Cycle & Shift Finish Check',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Sterile Services Department Operations',
                'question': 'A sterile services technician starts loading instrument trays at <strong>13:45</strong>.<br>• Loading takes <strong>25 minutes</strong>.<br>• The autoclave sterilisation cycle runs for <strong>1.4 hours</strong>.<br>• Cooling and unloading takes <strong>35 minutes</strong>.<br>• The technician must also take a mandatory <strong>30-minute break</strong> after unloading before clocking off.<br><br>The technician\'s shift ends at <strong>5:15 pm</strong>. Will she finish everything (including her break) before her shift ends?',
                'steps': [
                    ('Step 1', 'Convert 1.4 hours into hours and minutes', '0.4 × 60 = 24 minutes → 1.4 hours = 1 hour 24 minutes (84 minutes).', 'M1: Accurate decimal hour conversion (84 mins)'),
                    ('Step 2', 'Sum all task durations in minutes', '25 mins (load) + 84 mins (cycle) + 35 mins (unload) + 30 mins (break) = 174 minutes.', 'M1: Total minutes summation'),
                    ('Step 3', 'Convert 174 minutes to hours/minutes and add to 13:45 start time', '174 mins = 2 hours 54 minutes.<br>13:45 + 2 hrs = 15:45; 15:45 + 54 mins = 16:39 (4:39 pm).', 'M1: Accurate finish time calculation'),
                    ('Step 4', 'Compare against 5:15 pm (17:15) shift end', '16:39 is 36 minutes before 17:15 (5:15 pm). Yes, she will finish with 36 minutes to spare.', 'A1: Correct decision with 16:39 / 4:39 pm finish time')
                ],
                'final_answer': 'Yes (She finishes at 16:39 / 4:39 pm, which is 36 minutes before her 17:15 / 5:15 pm shift ends).',
                'tutor_tip': 'Watch out for 1.4 hours! 1.4 hours is 1 hour 24 minutes (0.4 × 60), NOT 1 hour 40 minutes!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Entering 1.35 on a Calculator to Represent 1 Hour 35 Minutes',
                'desc': 'Calculators treat 1.35 as 1 and 35/100 (1 hr 21 mins), whereas 35 minutes is 35/60 = 0.583 hours.',
                'fix': 'Always convert minutes to fractions of 60 before using a calculator.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A staff training seminar starts at <strong>14:45</strong> and finishes at <strong>17:20</strong>. How long did the seminar last in hours and minutes?',
                'solution_steps': '1. 14:45 to 15:00 = 15 minutes.<br>2. 15:00 to 17:00 = 2 hours.<br>3. 17:00 to 17:20 = 20 minutes.<br>4. Total = 2 hours and 35 minutes.',
                'correct_answer': '2 hours and 35 minutes',
                'tutor_tip': 'Use the timeline bridge method to avoid subtraction errors across 60-minute thresholds.'
            },
            {
                'marks': '2 Marks',
                'question': 'A night nurse clocks on at <strong>21:30</strong> on Tuesday and clocks off at <strong>06:15</strong> on Wednesday morning. She has an unpaid break of <strong>45 minutes</strong>. For how many paid hours does she work?',
                'solution_steps': '1. 21:30 to 24:00 (midnight) = 2 hours 30 minutes.<br>2. 00:00 to 06:15 = 6 hours 15 minutes &rarr; Total shift = 8 hours 45 minutes.<br>3. Subtract 45 mins unpaid break = exactly 8 paid hours.',
                'correct_answer': '8 hours',
                'tutor_tip': 'Bridge through midnight (24:00 / 00:00) in two steps when calculating overnight shifts.'
            },
            {
                'marks': '3 Marks',
                'question': 'A train timetable shows departures from Oxford at <strong>07:42, 08:12, and 08:42</strong>. The journey to London Paddington takes <strong>56 minutes</strong>, followed by a <strong>18-minute</strong> underground transfer to a hospital appointment at <strong>09:45</strong>. Which is the latest train from Oxford the patient can catch?',
                'solution_steps': '1. Total travel time from Oxford departure to hospital = 56 + 18 = 74 minutes (1 hour 14 minutes).<br>2. Work backwards from 09:45: 09:45 - 1 hr 14 mins = 08:31 latest departure.<br>3. Compare trains: 08:42 is too late (arrives 09:56). The 08:12 train arrives at hospital at 09:26.<br>4. Latest train = 08:12.',
                'correct_answer': 'The 08:12 train (arrives at hospital at 09:26)',
                'tutor_tip': 'Always test your chosen train forward to confirm arrival is before 09:45 (08:12 + 1h 14m = 09:26).'
            }
        ]
    },
    {
        'filename': 'functional-skills-speed.html',
        'clean_topic': 'Speed, Distance & Time',
        'intro_lead': 'Apply the speed-distance-time triangle to calculate vehicle journey times, average driving speeds, delivery ETAs, and speed limit compliance in logistics and transport.',
        'next_file': 'functional-skills-density.html',
        'next_name': 'Density & Compound Units',
        'spec_points': [
            ('L2.19', 'Calculate speed, distance, and time using compound measures and convert between compound units.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-gauge',
                'title': 'Golden Rule 1: Speed, Distance & Time Formula Triangle',
                'desc': 'Cover what you want to find with your thumb:<br>• <strong>Distance = Speed × Time</strong><br>• <strong>Speed = Distance ÷ Time</strong><br>• <strong>Time = Distance ÷ Speed</strong>',
                'badge': 'Distance = Speed × Time | Speed = Distance ÷ Time | Time = Distance ÷ Speed'
            },
            {
                'icon': 'fa-stopwatch',
                'title': 'Golden Rule 2: Divide Minutes by 60 to Get Decimal Hours',
                'desc': 'Never write 45 minutes as 0.45! To turn minutes into decimal hours, divide by 60 (15 mins = 0.25 hrs, 30 mins = 0.5 hrs, 45 mins = 0.75 hrs). To turn decimal hours back into minutes, multiply by 60 (0.4 hrs × 60 = 24 mins).',
                'badge': 'Decimal Hours = Minutes ÷ 60 | Minutes = Decimal Hours × 60'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: The Speed, Distance & Time Formula Triangle (S-D-T)',
                'summary': 'Use the big triangle to find Speed, Distance, or Time with complete confidence.',
                'content_html': """
    <div class="big-formula-diagram-container" style="background:#ffffff; border:2px solid #cbd5e1; border-radius:14px; padding:24px 20px; margin:20px 0; box-shadow:0 6px 18px rgba(15, 23, 42, 0.08);">
      <div style="text-align:center; margin-bottom:16px;">
        <span style="display:inline-block; background:#eff6ff; color:#1e40af; border:1px solid #bfdbfe; font-size:0.82rem; font-weight:800; padding:5px 16px; border-radius:999px; text-transform:uppercase; letter-spacing:0.05em;">
          <i class="fa-solid fa-gauge" style="margin-right:6px; color:#2563eb;"></i> Master Formula Triangle
        </span>
        <h3 style="margin:10px 0 6px 0; color:#0f172a; font-size:1.45rem; font-weight:900;">The Speed, Distance &amp; Time (S-D-T) Triangle</h3>
        <p style="margin:0; color:#64748b; font-size:0.98rem; max-width:620px; margin:0 auto; line-height:1.5;">
          Place your finger or thumb over the letter you want to find. The remaining letters give you the exact calculation formula.
        </p>
      </div>

      <div style="display:flex; justify-content:center; width:100%;">
        <svg viewBox="0 0 700 350" width="100%" style="max-width:720px; height:auto; display:block; font-family:system-ui, -apple-system, sans-serif;" xmlns="http://www.w3.org/2000/svg">
          <!-- Background glow for triangle -->
          <polygon points="160,18 15,295 305,295" fill="#f8fafc" stroke="#0f172a" stroke-width="4.5" stroke-linejoin="round"/>
          
          <!-- Dividing Horizontal Bar -->
          <line x1="68" y1="175" x2="252" y2="175" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Division indicators -->
          <circle cx="48" cy="175" r="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
          <text x="48" y="181" font-size="16" font-weight="900" fill="#1d4ed8" text-anchor="middle">÷</text>
          <circle cx="272" cy="175" r="14" fill="#eff6ff" stroke="#3b82f6" stroke-width="1.5"/>
          <text x="272" y="181" font-size="16" font-weight="900" fill="#1d4ed8" text-anchor="middle">÷</text>

          <!-- Vertical Dividing Line between S and T -->
          <line x1="160" y1="175" x2="160" y2="295" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Multiplication indicator -->
          <circle cx="160" cy="245" r="15" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
          <text x="160" y="251" font-size="16" font-weight="900" fill="#b45309" text-anchor="middle">×</text>

          <!-- Top Chamber: Distance (D) -->
          <circle cx="160" cy="98" r="44" fill="#dbeafe" stroke="#2563eb" stroke-width="3.5"/>
          <text x="160" y="108" font-size="38" font-weight="900" fill="#1e40af" text-anchor="middle">D</text>
          <text x="160" y="128" font-size="11" font-weight="900" fill="#1d4ed8" text-anchor="middle">DISTANCE</text>
          <text x="160" y="141" font-size="9" font-weight="700" fill="#3b82f6" text-anchor="middle">(miles, km, m)</text>

          <!-- Bottom Left Chamber: Speed (S) -->
          <circle cx="95" cy="235" r="40" fill="#fef3c7" stroke="#d97706" stroke-width="3.5"/>
          <text x="95" y="246" font-size="34" font-weight="900" fill="#b45309" text-anchor="middle">S</text>
          <text x="95" y="264" font-size="11" font-weight="900" fill="#92400e" text-anchor="middle">SPEED</text>
          <text x="95" y="277" font-size="8.5" font-weight="700" fill="#b45309" text-anchor="middle">(mph, km/h)</text>

          <!-- Bottom Right Chamber: Time (T) -->
          <circle cx="225" cy="235" r="40" fill="#dcfce7" stroke="#16a34a" stroke-width="3.5"/>
          <text x="225" y="246" font-size="34" font-weight="900" fill="#15803d" text-anchor="middle">T</text>
          <text x="225" y="264" font-size="11" font-weight="900" fill="#166534" text-anchor="middle">TIME</text>
          <text x="225" y="277" font-size="8.5" font-weight="700" fill="#15803d" text-anchor="middle">(hours, mins)</text>

          <!-- Right: Clear Operational Explanations Panel -->
          <g transform="translate(330, 18)">
            <rect x="0" y="0" width="355" height="295" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="177" y="26" font-size="12.5" font-weight="900" fill="#0f172a" text-anchor="middle" letter-spacing="0.05em">HOW TO READ THE TRIANGLE</text>
            
            <!-- Box 1: Distance -->
            <rect x="14" y="38" width="327" height="56" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
            <text x="26" y="60" font-size="11" font-weight="900" fill="#1d4ed8">1. COVER DISTANCE (D)</text>
            <text x="26" y="80" font-size="13.5" font-weight="900" fill="#0f172a">Distance = Speed × Time</text>
            <rect x="238" y="50" width="92" height="30" rx="6" fill="#2563eb"/>
            <text x="284" y="70" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">D = S × T</text>

            <!-- Box 2: Speed -->
            <rect x="14" y="102" width="327" height="56" rx="8" fill="#fffbeb" stroke="#fde68a" stroke-width="1.5"/>
            <text x="26" y="124" font-size="11" font-weight="900" fill="#b45309">2. COVER SPEED (S)</text>
            <text x="26" y="144" font-size="13.5" font-weight="900" fill="#0f172a">Speed = Distance ÷ Time</text>
            <rect x="238" y="114" width="92" height="30" rx="6" fill="#d97706"/>
            <text x="284" y="134" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">S = D ÷ T</text>

            <!-- Box 3: Time -->
            <rect x="14" y="166" width="327" height="56" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1.5"/>
            <text x="26" y="188" font-size="11" font-weight="900" fill="#15803d">3. COVER TIME (T)</text>
            <text x="26" y="208" font-size="13.5" font-weight="900" fill="#0f172a">Time = Distance ÷ Speed</text>
            <rect x="238" y="178" width="92" height="30" rx="6" fill="#16a34a"/>
            <text x="284" y="198" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">T = D ÷ S</text>

            <!-- Decimal Time Banner -->
            <rect x="14" y="230" width="327" height="52" rx="8" fill="#fef2f2" stroke="#fca5a5" stroke-width="1.2"/>
            <text x="177" y="249" font-size="11" font-weight="900" fill="#991b1b" text-anchor="middle">⏱️ DECIMAL TIME RULE (DIVIDE MINS BY 60):</text>
            <text x="177" y="268" font-size="11" font-weight="800" fill="#b91c1c" text-anchor="middle">15m = 0.25h &bull; 30m = 0.5h &bull; 45m = 0.75h (NEVER 0.45!)</text>
          </g>
        </svg>
      </div>
    </div>
    """
            },
            {
                'title': 'Skill 2: Converting Minutes & Decimal Hours in Speed Calculations',
                'summary': 'Preventing the classic decimal time trap when given minutes.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Hours &amp; Minutes</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Fraction of an Hour</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Decimal Hours (Use in Formula)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1 hour 15 mins</td><td style="padding:6px; border:1px solid #cbd5e1;">1 and 15/60 = 1 1/4</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700; color:#166534;">1.25 hours</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">2 hours 30 mins</td><td style="padding:6px; border:1px solid #cbd5e1;">2 and 30/60 = 2 1/2</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700; color:#166534;">2.5 hours</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1 hour 45 mins</td><td style="padding:6px; border:1px solid #cbd5e1;">1 and 45/60 = 1 3/4</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700; color:#166534;">1.75 hours</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">36 minutes</td><td style="padding:6px; border:1px solid #cbd5e1;">36/60 = 6/10</td><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700; color:#166534;">0.6 hours</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Skill 3: Two-Stage Journeys & Overall Average Speed',
                'summary': 'Why overall average speed is Total Distance ÷ Total Time (NEVER the average of two speeds).',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">To find the overall average speed of a multi-leg delivery journey:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Total Distance:</strong> Add the distances of Leg 1 and Leg 2.</li>
                    <li><strong>Total Time:</strong> Add the driving times of Leg 1 and Leg 2 (in decimal hours).</li>
                    <li><strong>Overall Average Speed:</strong> <code>Total Distance ÷ Total Time</code>.</li>
                  </ol>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1/2 Foundation): Ambulance Inter-Hospital Emergency Transfer',
                'marks': '3 Marks (Pearson Edexcel Level 2)',
                'context': 'Emergency Patient Transport Services',
                'question': 'An emergency transfer ambulance travels <strong>84 miles</strong> between two regional specialist hospitals. The journey takes <strong>1 hour and 45 minutes</strong>.<br>(a) Calculate the average speed of the ambulance in miles per hour (mph).<br>(b) The driver was instructed not to exceed an average speed of 50 mph. Was this instruction followed?',
                'steps': [
                    ('Step 1', 'Convert time into decimal hours', '45 minutes = 45 ÷ 60 = 0.75 hours.<br>Total time = 1.75 hours.', 'M1: Time conversion to decimal hours'),
                    ('Step 2', 'Calculate average speed (Distance ÷ Time)', 'Speed = 84 miles ÷ 1.75 hours = 48 mph.', 'M1: Speed formula calculation'),
                    ('Step 3', 'Compare with instruction threshold and conclude', '48 mph is less than 50 mph. Yes, the driver followed the speed instruction.', 'A1: Accurate speed and valid comparative conclusion')
                ],
                'final_answer': '(a) Average Speed = 48 mph | (b) Yes, 48 mph complies with the 50 mph limit.',
                'tutor_tip': 'If you divided 84 by 1.45, you would get 57.9 mph — an error that forfeits both marks! Always convert 45 mins to 0.75 hrs.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Blood Bank Courier ETA & Cold-Chain Deadline',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Urgent Medical Logistics',
                'question': 'A blood bank courier leaves the regional hub at <strong>10:15 am</strong> to deliver plasma <strong>117 miles</strong> away.<br>• For the first <strong>72 miles</strong> on the motorway, he drives at an average speed of <strong>60 mph</strong>.<br>• For the remaining <strong>45 miles</strong> on A-roads, he drives at an average speed of <strong>36 mph</strong>.<br>• He also stops for a <strong>15-minute</strong> roadworks delay.<br><br>The plasma must arrive before <strong>1:00 pm (13:00)</strong>. Does the courier arrive on time?',
                'steps': [
                    ('Step 1', 'Calculate driving time for the motorway leg (72 miles @ 60 mph)', 'Time 1 = 72 ÷ 60 = 1.2 hours = 1 hour 12 minutes (72 minutes).', 'M1: First leg time calculation'),
                    ('Step 2', 'Calculate driving time for the A-road leg (45 miles @ 36 mph)', 'Time 2 = 45 ÷ 36 = 1.25 hours = 1 hour 15 minutes (75 minutes).', 'M1: Second leg time calculation'),
                    ('Step 3', 'Sum total journey time including roadworks delay and add to 10:15', 'Total minutes = 72 + 75 + 15 (delay) = 162 minutes = 2 hours 42 minutes.<br>Arrival time = 10:15 + 2 hours 42 mins = 12:57 pm.', 'M1: Total duration and arrival time'),
                    ('Step 4', 'Compare against 1:00 pm (13:00) deadline', '12:57 pm is 3 minutes before 1:00 pm. Yes, the courier arrives on time with 3 minutes to spare.', 'A1: Accurate arrival time (12:57 pm) and clear conclusion')
                ],
                'final_answer': 'Yes (Arrives at 12:57 pm, which is 3 minutes before the 1:00 pm deadline).',
                'tutor_tip': 'Notice how converting 1.2 hours (72 mins) and 1.25 hours (75 mins) into minutes makes adding the 15-minute delay super easy!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Dividing by 1.45 Instead of 1.75',
                'desc': 'Treating 1 hour 45 minutes as 1.45 hours is the single most common error in Level 2 speed questions.',
                'fix': 'Never use minutes as decimals directly: 45 mins = 45/60 = 0.75.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A freight delivery lorry travels <strong>165 miles</strong> at an average speed of <strong>55 mph</strong>. How long does the journey take in hours?',
                'solution_steps': '1. Time = Distance ÷ Speed = 165 ÷ 55 = 3 hours.<br>2. Journey duration = 3 hours.',
                'correct_answer': '3 hours',
                'tutor_tip': 'Distance ÷ Speed = 165 ÷ 55 = 3.'
            },
            {
                'marks': '2 Marks',
                'question': 'A district nurse drives at an average speed of <strong>36 mph</strong> for <strong>40 minutes</strong>. How many miles does she travel?',
                'solution_steps': '1. Convert 40 minutes into hours: 40/60 = 2/3 hour.<br>2. Distance = Speed × Time = 36 × (2/3) = (36 ÷ 3) × 2 = 24 miles.',
                'correct_answer': '24 miles',
                'tutor_tip': 'When minutes are 20 or 40, use fractions (1/3 or 2/3 of an hour) to avoid recurring decimals!'
            },
            {
                'marks': '3 Marks',
                'question': 'A train travels <strong>210 km</strong> between <strong>09:20 and 11:05</strong>. Calculate the average speed of the train in <strong>km/h</strong>.',
                'solution_steps': '1. Elapsed time from 09:20 to 11:05 = 1 hour 45 minutes = 1.75 hours.<br>2. Speed = Distance ÷ Time = 210 ÷ 1.75 = 120 km/h.',
                'correct_answer': '120 km/h',
                'tutor_tip': '1 hour 45 minutes = 1.75 hours; 210 ÷ 1.75 = 120 km/h.'
            }
        ]
    },
    {
        'filename': 'functional-skills-density.html',
        'clean_topic': 'Density & Compound Units',
        'intro_lead': 'Calculate material density, mass, and volume using the density triangle (D = M ÷ V), understand pressure (P = F ÷ A), and solve warehouse storage weight capacity problems.',
        'next_file': 'functional-skills-unit-conversions.html',
        'next_name': 'Unit Conversions',
        'spec_points': [
            ('L2.19', 'Calculate density, mass, and volume using compound measures in vocational contexts.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-cube',
                'title': 'Golden Rule 1: Density, Mass & Volume Formula Triangle',
                'desc': 'Mass is at the top of the triangle:<br>• <strong>Mass = Density × Volume</strong><br>• <strong>Density = Mass ÷ Volume</strong><br>• <strong>Volume = Mass ÷ Density</strong>',
                'badge': 'Mass = Density × Volume | Density = Mass ÷ Volume | Volume = Mass ÷ Density'
            },
            {
                'icon': 'fa-weight-hanging',
                'title': 'Golden Rule 2: Ensure Mass and Volume Units Match Density',
                'desc': 'If density is given in g/cm³, mass MUST be in grams and volume in cm³. If density is kg/m³, convert mass to kg and volume to m³.',
                'badge': 'g/cm³ → g and cm³ | kg/m³ → kg and m³'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: The Mass, Density & Volume Formula Triangle (M-D-V)',
                'summary': 'Mass is always on top. Use the big triangle to find Mass, Density, or Volume.',
                'content_html': """
    <div class="big-formula-diagram-container" style="background:#ffffff; border:2px solid #cbd5e1; border-radius:14px; padding:24px 20px; margin:20px 0; box-shadow:0 6px 18px rgba(15, 23, 42, 0.08);">
      <div style="text-align:center; margin-bottom:16px;">
        <span style="display:inline-block; background:#f5f3ff; color:#5b21b6; border:1px solid #ddd6fe; font-size:0.82rem; font-weight:800; padding:5px 16px; border-radius:999px; text-transform:uppercase; letter-spacing:0.05em;">
          <i class="fa-solid fa-cube" style="margin-right:6px; color:#7c3aed;"></i> Master Formula Triangle
        </span>
        <h3 style="margin:10px 0 6px 0; color:#0f172a; font-size:1.45rem; font-weight:900;">The Mass, Density &amp; Volume (M-D-V) Triangle</h3>
        <p style="margin:0; color:#64748b; font-size:0.98rem; max-width:620px; margin:0 auto; line-height:1.5;">
          Remember: <strong>Mass is always on top (M)</strong>. Cover the quantity you need to find with your finger.
        </p>
      </div>

      <div style="display:flex; justify-content:center; width:100%;">
        <svg viewBox="0 0 700 350" width="100%" style="max-width:720px; height:auto; display:block; font-family:system-ui, -apple-system, sans-serif;" xmlns="http://www.w3.org/2000/svg">
          <!-- Background glow for triangle -->
          <polygon points="160,18 15,295 305,295" fill="#f8fafc" stroke="#0f172a" stroke-width="4.5" stroke-linejoin="round"/>
          
          <!-- Dividing Horizontal Bar -->
          <line x1="68" y1="175" x2="252" y2="175" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Division indicators -->
          <circle cx="48" cy="175" r="14" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
          <text x="48" y="181" font-size="16" font-weight="900" fill="#6d28d9" text-anchor="middle">÷</text>
          <circle cx="272" cy="175" r="14" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.5"/>
          <text x="272" y="181" font-size="16" font-weight="900" fill="#6d28d9" text-anchor="middle">÷</text>

          <!-- Vertical Dividing Line between D and V -->
          <line x1="160" y1="175" x2="160" y2="295" stroke="#0f172a" stroke-width="4.5"/>
          <!-- Multiplication indicator -->
          <circle cx="160" cy="245" r="15" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
          <text x="160" y="251" font-size="16" font-weight="900" fill="#0369a1" text-anchor="middle">×</text>

          <!-- Top Chamber: Mass (M) -->
          <circle cx="160" cy="98" r="44" fill="#ede9fe" stroke="#7c3aed" stroke-width="3.5"/>
          <text x="160" y="108" font-size="38" font-weight="900" fill="#5b21b6" text-anchor="middle">M</text>
          <text x="160" y="128" font-size="11" font-weight="900" fill="#4c1d95" text-anchor="middle">MASS</text>
          <text x="160" y="141" font-size="9" font-weight="700" fill="#7c3aed" text-anchor="middle">(grams, kg, tonnes)</text>

          <!-- Bottom Left Chamber: Density (D) -->
          <circle cx="95" cy="235" r="40" fill="#e0f2fe" stroke="#0284c7" stroke-width="3.5"/>
          <text x="95" y="246" font-size="34" font-weight="900" fill="#0369a1" text-anchor="middle">D</text>
          <text x="95" y="264" font-size="11" font-weight="900" fill="#075985" text-anchor="middle">DENSITY</text>
          <text x="95" y="277" font-size="8.5" font-weight="700" fill="#0284c7" text-anchor="middle">(g/cm³, kg/m³)</text>

          <!-- Bottom Right Chamber: Volume (V) -->
          <circle cx="225" cy="235" r="40" fill="#dcfce7" stroke="#16a34a" stroke-width="3.5"/>
          <text x="225" y="246" font-size="34" font-weight="900" fill="#15803d" text-anchor="middle">V</text>
          <text x="225" y="264" font-size="11" font-weight="900" fill="#166534" text-anchor="middle">VOLUME</text>
          <text x="225" y="277" font-size="8.5" font-weight="700" fill="#15803d" text-anchor="middle">(cm³, m³, litres)</text>

          <!-- Right: Clear Operational Explanations Panel -->
          <g transform="translate(330, 18)">
            <rect x="0" y="0" width="355" height="295" rx="12" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.8"/>
            <text x="177" y="26" font-size="12.5" font-weight="900" fill="#0f172a" text-anchor="middle" letter-spacing="0.05em">HOW TO READ THE TRIANGLE</text>
            
            <!-- Box 1: Mass -->
            <rect x="14" y="38" width="327" height="56" rx="8" fill="#f5f3ff" stroke="#ddd6fe" stroke-width="1.5"/>
            <text x="26" y="60" font-size="11" font-weight="900" fill="#5b21b6">1. COVER MASS (M)</text>
            <text x="26" y="80" font-size="13.5" font-weight="900" fill="#0f172a">Mass = Density × Volume</text>
            <rect x="238" y="50" width="92" height="30" rx="6" fill="#7c3aed"/>
            <text x="284" y="70" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">M = D × V</text>

            <!-- Box 2: Density -->
            <rect x="14" y="102" width="327" height="56" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5"/>
            <text x="26" y="124" font-size="11" font-weight="900" fill="#0369a1">2. COVER DENSITY (D)</text>
            <text x="26" y="144" font-size="13.5" font-weight="900" fill="#0f172a">Density = Mass ÷ Volume</text>
            <rect x="238" y="114" width="92" height="30" rx="6" fill="#0284c7"/>
            <text x="284" y="134" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">D = M ÷ V</text>

            <!-- Box 3: Volume -->
            <rect x="14" y="166" width="327" height="56" rx="8" fill="#f0fdf4" stroke="#bbf7d0" stroke-width="1.5"/>
            <text x="26" y="188" font-size="11" font-weight="900" fill="#15803d">3. COVER VOLUME (V)</text>
            <text x="26" y="208" font-size="13.5" font-weight="900" fill="#0f172a">Volume = Mass ÷ Density</text>
            <rect x="238" y="178" width="92" height="30" rx="6" fill="#16a34a"/>
            <text x="284" y="198" font-size="12" font-weight="900" fill="#ffffff" text-anchor="middle">V = M ÷ D</text>

            <!-- Units Matching Banner -->
            <rect x="14" y="230" width="327" height="52" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.2"/>
            <text x="177" y="249" font-size="11" font-weight="900" fill="#166534" text-anchor="middle">⚖️ CHECK MATCHING UNITS BEFORE CALCULATING:</text>
            <text x="177" y="268" font-size="10.5" font-weight="800" fill="#15803d" text-anchor="middle">g with cm³ &rarr; g/cm³  |  kg with m³ &rarr; kg/m³ (1 L water = 1 kg)</text>
          </g>
        </svg>
      </div>
    </div>
    """
            },
            {
                'title': 'Skill 2: Combining 3D Volume Formulas with Density to Find Mass',
                'summary': 'How to solve two-stage geometry + density questions in Section B.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Stage 1 (Find 3D Volume):</strong> Calculate the volume of the cuboid (<code>L × W × H</code>) or cylinder (<code>3.14 × r² × h</code>) making sure all dimensions match the density unit (all in <code>cm</code> or all in <code>m</code>).</li>
                    <li><strong>Stage 2 (Multiply by Density):</strong> Multiply Volume by Density (<code>M = D × V</code>).</li>
                    <li><strong>Stage 3 (Convert Mass if Required):</strong> Divide grams by <code>1,000</code> to get kilograms, or divide kilograms by <code>1,000</code> to get tonnes.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 3: Pressure, Force & Area Compound Measures (P = F ÷ A)',
                'summary': 'Applying compound unit reasoning to floor loading and clinical pressure.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Pressure Formula:</strong> <code>Pressure (N/m² or kg/m²) = Force / Weight ÷ Contact Area</code>.</li>
                    <li><strong>Finding Maximum Force:</strong> <code>Force = Pressure × Area</code>.</li>
                    <li><strong>Rates of Flow / Population Density:</strong> Follow the exact unit label! E.g. <code>patients per km² = Patients ÷ Area in km²</code>; <code>litres per minute = Litres ÷ Minutes</code>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 2 Foundation): Hospital Facility Concrete Foundation Pier Density & Weight',
                'marks': '3 Marks (Pearson Edexcel Level 2)',
                'context': 'Healthcare Construction Engineering',
                'question': 'A concrete footing for an MRI machine foundation is a cuboid measuring <strong>1.5 m long, 0.8 m wide, and 0.5 m deep</strong>. The reinforced concrete has a density of <strong>2,400 kg/m³</strong>.<br>Calculate the total mass of the footing in kilograms.',
                'steps': [
                    ('Step 1', 'Calculate the volume of the cuboid footing', 'Volume = length × width × depth = 1.5 × 0.8 × 0.5 = 0.6 m³.', 'M1: Cuboid volume calculation'),
                    ('Step 2', 'Apply Mass = Density × Volume formula', 'Mass = 2,400 kg/m³ × 0.6 m³ = 1,440 kg.', 'M1: Density triangle multiplication'),
                    ('Step 3', 'State final mass with correct units', 'Total Mass = 1,440 kg (or 1.44 tonnes).', 'A1: Accurate mass with unit')
                ],
                'final_answer': 'Total Mass = 1,440 kg',
                'tutor_tip': 'Notice the units matched: volume was in m³ and density was in kg/m³, so the answer is directly in kg.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Steel Medical Gas Cylinder Rack Crane Lift Safety Check',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Industrial Engineering & Lifting Compliance',
                'question': 'A hospital engineering team needs to lift a solid steel counterweight block onto a roof plant room.<br>• The block is a cuboid measuring <strong>50 cm long, 40 cm wide, and 25 cm high</strong>.<br>• Steel has a density of <strong>7.8 g/cm³</strong>.<br>• The portable hoist has a maximum Safe Working Load (SWL) of <strong>400 kg</strong>.<br><br>Can the portable hoist safely lift the steel block? Show full working.',
                'steps': [
                    ('Step 1', 'Calculate the volume of the cuboid in cm³', 'Volume = 50 cm × 40 cm × 25 cm = 50,000 cm³.', 'M1: Cuboid volume in cm³'),
                    ('Step 2', 'Calculate mass in grams using Mass = Density × Volume', 'Mass = 7.8 g/cm³ × 50,000 cm³ = 390,000 grams.', 'M1: Mass calculation in grams'),
                    ('Step 3', 'Convert mass from grams to kilograms', '390,000 g ÷ 1,000 = 390 kg.', 'M1: Conversion to kg'),
                    ('Step 4', 'Compare against 400 kg Safe Working Load', '390 kg < 400 kg (10 kg below maximum limit). Yes, the hoist can safely lift the block.', 'A1: Accurate mass (390 kg) and justified safety confirmation')
                ],
                'final_answer': 'Yes, safe to lift (Block mass is 390 kg, which is 10 kg under the 400 kg hoist limit).',
                'tutor_tip': 'Because density is in g/cm³, keep dimensions in cm first to get grams (390,000 g), then divide by 1,000 at the end to get 390 kg!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Multiplying Instead of Dividing for Density',
                'desc': 'Doing Mass × Volume to find density is a common error. Remember that Mass is at the top of the triangle (D = M ÷ V).',
                'fix': 'Sketch the triangle: M at the top, D and V at the bottom.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A metal component has a volume of <strong>80 cm³</strong> and a mass of <strong>632 grams</strong>. Calculate the density of the metal in <strong>g/cm³</strong>.',
                'solution_steps': '1. Density = Mass ÷ Volume = 632 ÷ 80.<br>2. 632 ÷ 80 = 7.9 g/cm³.',
                'correct_answer': '7.9 g/cm³',
                'tutor_tip': 'Divide 632 by 80 to obtain 7.9 g/cm³.'
            },
            {
                'marks': '2 Marks',
                'question': 'A bottle of surgical spirit has a mass of <strong>640 grams</strong>. Surgical spirit has a density of <strong>0.8 g/cm³</strong>. Calculate the volume of the surgical spirit in <strong>cm³</strong>.',
                'solution_steps': '1. Volume = Mass ÷ Density = 640 ÷ 0.8.<br>2. 640 ÷ 0.8 = 6,400 ÷ 8 = 800 cm³.',
                'correct_answer': '800 cm³',
                'tutor_tip': 'Cover V in the M-D-V triangle: Volume = Mass ÷ Density.'
            },
            {
                'marks': '3 Marks',
                'question': 'An oak timber beam is a cuboid measuring <strong>2 m long, 0.2 m wide, and 0.15 m thick</strong>. Oak has a density of <strong>750 kg/m³</strong>. Calculate the mass of <strong>4 identical oak beams</strong> in kilograms.',
                'solution_steps': '1. Volume of 1 beam = 2 × 0.2 × 0.15 = 0.06 m³.<br>2. Mass of 1 beam = 0.06 × 750 = 45 kg.<br>3. Mass of 4 beams = 4 × 45 kg = 180 kg.',
                'correct_answer': '180 kg',
                'tutor_tip': 'Check units: all lengths are in metres and density is in kg/m³.'
            }
        ]
    },
    {
        'filename': 'functional-skills-unit-conversions.html',
        'clean_topic': 'Metric & Imperial Unit Conversions',
        'intro_lead': 'Convert seamlessly between metric units (mm, cm, m, km; ml, cl, l; g, kg, tonnes) and handle common imperial conversions (inches, feet, miles; ounces, pounds, stone; pints, gallons).',
        'next_file': 'functional-skills-length.html',
        'next_name': 'Length & Dimensions',
        'spec_points': [
            ('L1.18 / L2.20', 'Convert between metric units of length, weight, and capacity.'),
            ('L2.21', 'Convert between metric and common imperial units using given conversion factors.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-stairs',
                'title': 'Golden Rule 1: Big Unit to Small Unit = MULTIPLY',
                'desc': 'When going from a larger unit to a smaller unit (e.g. metres to centimetres), MULTIPLY (1 m = 100 cm, so 4.5 m = 450 cm). Smaller unit to larger = DIVIDE.',
                'badge': 'Big to Small → Multiply | Small to Big → Divide'
            },
            {
                'icon': 'fa-arrows-split-up-and-left',
                'title': 'Golden Rule 2: Benchmark Metric-to-Imperial Conversion Factors',
                'desc': '5 miles ≈ 8 km • 1 inch ≈ 2.5 cm • 1 kg ≈ 2.2 lbs • 1 gallon ≈ 4.5 litres • 1 foot = 12 inches.',
                'badge': '5 miles ≈ 8 km | 1 kg ≈ 2.2 lbs | 1 gallon ≈ 4.5 L'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: The Metric Conversion Staircase (Length, Mass & Capacity)',
                'summary': 'Powers of 10, 100, and 1,000 for metric conversions.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:left;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Measure Type</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Core Equivalences</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Exam Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Length</td><td style="padding:8px; border:1px solid #cbd5e1;"><code>1 km = 1,000 m</code> &bull; <code>1 m = 100 cm</code> &bull; <code>1 cm = 10 mm</code></td><td style="padding:8px; border:1px solid #cbd5e1;"><code>2.4 m = 240 cm = 2,400 mm</code></td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Mass / Weight</td><td style="padding:8px; border:1px solid #cbd5e1;"><code>1 tonne = 1,000 kg</code> &bull; <code>1 kg = 1,000 g</code> &bull; <code>1 g = 1,000 mg</code></td><td style="padding:8px; border:1px solid #cbd5e1;"><code>850 g = 0.85 kg</code></td></tr>
                      <tr><td style="padding:8px; border:1px solid #cbd5e1; font-weight:700;">Capacity</td><td style="padding:8px; border:1px solid #cbd5e1;"><code>1 L = 1,000 ml</code> &bull; <code>1 L = 100 cl</code> &bull; <code>1 cl = 10 ml</code></td><td style="padding:8px; border:1px solid #cbd5e1;"><code>75 cl = 750 ml = 0.75 L</code></td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Skill 2: Metric-to-Imperial & Imperial-to-Metric Conversions',
                'summary': 'Using conversion factors and two-step bridges (e.g. 5 miles = 8 km).',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Miles to Kilometres (<code>÷ 5 × 8</code>):</strong> <em>45 miles &rarr; 45 ÷ 5 = 9; 9 × 8 = 72 km.</em></li>
                    <li><strong>Kilometres to Miles (<code>÷ 8 × 5</code>):</strong> <em>64 km &rarr; 64 ÷ 8 = 8; 8 × 5 = 40 miles.</em></li>
                    <li><strong>Kilograms &amp; Pounds (<code>1 kg = 2.2 lbs</code>):</strong> kg to lbs = <code>× 2.2</code>; lbs to kg = <code>÷ 2.2</code>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 3: Compound Imperial Units (Feet & Inches; Stone & Pounds)',
                'summary': 'Converting compound imperial measurements into a single unit first.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">Never write <strong>5 feet 6 inches</strong> as <code>5.6 feet</code> (there are 12 inches in a foot, not 10!):</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Feet &amp; Inches to Total Inches (<code>1 ft = 12 in</code>):</strong> <code>5 ft 6 in = (5 × 12) + 6 = 66 inches</code>.</li>
                    <li><strong>Stone &amp; Pounds to Total Pounds (<code>1 stone = 14 lbs</code>):</strong> <code>11 stone 4 lbs = (11 × 14) + 4 = 158 lbs</code>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1/2 Foundation): NHS Patient Medication Weight Dosage Conversion',
                'marks': '3 Marks (Pearson Edexcel Level 2)',
                'context': 'Clinical Medication Administration',
                'question': "A patient's medical chart lists their weight in imperial as <strong>11 stone 4 lbs</strong>. Hospital clinical dosage guidelines for an intravenous antibiotic require the weight in kilograms.<br>Use: <strong>1 stone = 14 lbs</strong> and <strong>1 kg = 2.2 lbs</strong>.<br>Calculate the patient's weight in kilograms to the nearest whole kg.",
                'steps': [
                    ('Step 1', 'Convert stone into pounds', '11 stone × 14 lbs = 154 lbs.<br>Total weight in lbs = 154 + 4 = 158 lbs.', 'M1: Imperial weight conversion to lbs'),
                    ('Step 2', 'Convert pounds into kilograms (divide by 2.2)', '158 lbs ÷ 2.2 = 71.818... kg.', 'M1: Metric conversion division'),
                    ('Step 3', 'Round to nearest whole kilogram', '71.818... rounds UP to 72 kg.', 'A1: Accurate rounded mass (72 kg)')
                ],
                'final_answer': 'Patient Weight = 72 kg (to nearest whole kg)',
                'tutor_tip': 'Always check that the answer is sensible: 11 stone is around 70 kg, so 72 kg is realistic.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): European Continental Freight Bridge Clearance Check',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'International Transport Logistics',
                'question': 'A UK HGV driver is transporting medical imaging equipment in France. His lorry has a height of <strong>13 feet 6 inches</strong>.<br>He approaches a low railway bridge in France marked with a maximum height limit of <strong>4.0 metres</strong>.<br>Use: <strong>1 foot = 12 inches</strong> and <strong>1 inch = 2.54 cm</strong>.<br>Can the lorry safely pass under the bridge? Show full working.',
                'steps': [
                    ('Step 1', 'Convert lorry height from feet and inches into total inches', '13 feet × 12 inches = 156 inches.<br>Total height = 156 + 6 = 162 inches.', 'M1: Total height in inches (162 in)'),
                    ('Step 2', 'Convert inches to centimetres', '162 inches × 2.54 cm = 411.48 cm.', 'M1: Conversion to centimetres'),
                    ('Step 3', 'Convert centimetres to metres (or convert 4.0 m to 400 cm)', '411.48 cm ÷ 100 = 4.1148 metres.', 'M1: Metric conversion to metres'),
                    ('Step 4', 'Compare against 4.0 m bridge limit and state decision', '4.11 m > 4.0 m (11.48 cm too tall). No, the lorry cannot safely pass under the bridge.', 'A1: Clear decision supported by 4.11 m / 411.48 cm')
                ],
                'final_answer': 'No (Lorry height is 4.11 m / 411.48 cm, which exceeds the 4.0 m / 400 cm bridge limit by 11.48 cm).',
                'tutor_tip': 'Remember: 13 feet 6 inches is 13.5 feet (162 inches), NOT 13.6 feet!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Dividing by 10 or 100 Instead of 1,000 for Grams/Kilograms',
                'desc': 'Assuming 1 kg = 100 g instead of 1,000 g causes factor-of-ten errors in medication or postal problems.',
                'fix': "Remember 'kilo' always means 1,000: 1 kilometre = 1,000 m; 1 kilogram = 1,000 g."
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'Convert <strong>3.45 metres</strong> into millimetres (mm).',
                'solution_steps': '1. 1 m = 1,000 mm (100 cm × 10 mm).<br>2. 3.45 × 1,000 = 3,450 mm.',
                'correct_answer': '3,450 mm',
                'tutor_tip': 'To convert metres to millimetres, multiply by 1,000.'
            },
            {
                'marks': '2 Marks',
                'question': 'A road sign in Spain shows the distance to the nearest hospital is <strong>56 km</strong>. Using <strong>5 miles = 8 km</strong>, calculate this distance in miles.',
                'solution_steps': '1. Divide km by 8: 56 ÷ 8 = 7.<br>2. Multiply by 5: 7 × 5 = 35 miles.',
                'correct_answer': '35 miles',
                'tutor_tip': 'Kilometres are shorter than miles, so the number of miles (35) must be smaller than the number of km (56).'
            },
            {
                'marks': '3 Marks',
                'question': 'A catering water urn holds <strong>4.5 gallons</strong>. Using <strong>1 gallon = 4.54 litres</strong>, how many <strong>250 ml</strong> cups of tea can be filled from one full urn?',
                'solution_steps': '1. Capacity in litres = 4.5 × 4.54 = 20.43 litres.<br>2. Convert to millilitres = 20.43 × 1,000 = 20,430 ml.<br>3. Divide by 250 ml cup: 20,430 ÷ 250 = 81.72 &rarr; 81 full cups.',
                'correct_answer': '81 full cups',
                'tutor_tip': 'Alternatively, 250 ml = 0.25 L (4 cups per litre): 20.43 L × 4 = 81.72 &rarr; 81 full cups.'
            }
        ]
    },
    {
        'filename': 'functional-skills-length.html',
        'clean_topic': 'Length & Dimensions',
        'intro_lead': 'Measure, estimate, and calculate lengths, heights, widths, and perimeters in construction, interior decorating, and clinical patient positioning.',
        'next_file': 'functional-skills-weight.html',
        'next_name': 'Weight & Mass',
        'spec_points': [
            ('L1.18 / L2.20', 'Estimate and measure length and solve problems involving dimensions.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-ruler',
                'title': 'Golden Rule 1: Always Align with 0 on Measuring Tools',
                'desc': 'When reading a ruler or tape measure, check whether measurement starts at the 0 mark or at the physical end of the tool.',
                'badge': 'Start at 0, NOT the edge of the ruler'
            },
            {
                'icon': 'fa-tape',
                'title': 'Golden Rule 2: Convert All Dimensions to the Same Unit Before Calculating',
                'desc': 'If room length is 4.2 m and skirting board is sold in 240 cm lengths, convert both to centimetres (420 cm and 240 cm) or both to metres (4.2 m and 2.4 m).',
                'badge': 'Never add or divide metres and centimetres directly'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Length Measurement Benchmarks & Unit Selection',
                'summary': 'Real-world physical benchmarks for rapid estimation and unit checking.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Millimetres (mm):</strong> Precision engineering, timber thickness, tablet diameters (<code>10 mm = 1 cm</code>).</li>
                    <li><strong>Centimetres (cm):</strong> Furniture dimensions, shelving, clothing sizes (<code>100 cm = 1 m</code>).</li>
                    <li><strong>Metres (m):</strong> Room dimensions, garden fencing, corridor lengths (<code>1,000 m = 1 km</code>).</li>
                    <li><strong>Kilometres (km):</strong> Road transport distances and courier routes.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 2: Cutting Lengths from Timber / Pipe Stock (No-Joining Rule)',
                'summary': 'Why you must divide each stock length individually when offcuts cannot be glued together.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">Suppose you need <strong>10 shelves</strong> each measuring <strong>90 cm</strong>, and timber planks are sold in <strong>240 cm</strong> lengths:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Check how many full shelves fit into 1 plank:</strong> <code>240 cm ÷ 90 cm = 2.66... &rarr; 2 full shelves per plank</code> (with a 60 cm offcut that is too short for a 3rd shelf).</li>
                    <li><strong>Divide required shelves by shelves per plank:</strong> <code>10 shelves ÷ 2 per plank = 5 planks needed</code>.</li>
                  </ol>
                </div>
                """
            },
            {
                'title': 'Skill 3: Spacing Items with Gaps Along a Wall or Fence',
                'summary': 'Calculating posts, shelving brackets, or hospital bed bays with mandatory clearance gaps.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">When placing <strong>4 lockers</strong> (each <code>60 cm</code> wide) along a <strong>3.5 m (350 cm)</strong> wall with a <code>15 cm</code> gap between each locker:</p>
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>4 lockers have 3 internal gaps</strong> between them (<code>Gaps = Items - 1</code>).</li>
                    <li><strong>Total width used:</strong> <code>(4 × 60 cm) + (3 × 15 cm) = 240 cm + 45 cm = 285 cm</code>.</li>
                    <li><strong>Remaining wall space:</strong> <code>350 cm - 285 cm = 65 cm</code>.</li>
                  </ul>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Ward Corridor Handrail Installation Dimensions',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Hospital Facilities Maintenance',
                'question': 'A hospital corridor handrail is <strong>14.4 metres</strong> long. Timber rails are sold in sections of <strong>240 cm</strong> each.<br>(a) How many sections are needed to cover the entire handrail length?<br>(b) If each section costs <strong>£18.50</strong>, calculate the total cost.',
                'steps': [
                    ('Step 1', 'Convert dimensions to common units (metres to cm)', '14.4 m × 100 = 1,440 cm.', 'M1: Unit conversion to centimetres'),
                    ('Step 2', 'Divide total length by section length', '1,440 cm ÷ 240 cm = 6 sections.', 'A1: Accurate section count'),
                    ('Step 3', 'Calculate total expenditure', '6 sections × £18.50 = £111.00.', 'A1: Accurate cost calculation')
                ],
                'final_answer': '(a) 6 sections needed | (b) Total cost = £111.00',
                'tutor_tip': 'Dividing 14.4 by 240 without converting gives 0.06 — always ensure units match before dividing!'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Pharmacy Shelving Cut-List & Timber Plank Order',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Commercial Joinery & Fit-Out',
                'question': 'A carpenter is building dispensary shelving and needs <strong>12 solid timber shelves</strong>, each measuring <strong>85 cm</strong> long.<br>• Timber boards are sold in <strong>3.0 metre</strong> lengths at <strong>£22.00 per board</strong>.<br>• Offcuts cannot be joined together to make a shelf.<br><br>Calculate the minimum number of 3.0 m boards the carpenter must buy, and the total cost.',
                'steps': [
                    ('Step 1', 'Convert board length to centimetres and find shelves per board', '3.0 m = 300 cm.<br>300 cm ÷ 85 cm = 3.529... → 3 full shelves can be cut from each board (3 × 85 = 255 cm, leaving a 45 cm offcut).', 'M1: Finding whole shelves per single board (3)'),
                    ('Step 2', 'Calculate number of 3.0 m boards needed for 12 shelves', '12 shelves ÷ 3 shelves per board = 4 boards.', 'M1: Dividing total shelves by shelves per board'),
                    ('Step 3', 'Calculate total cost of the boards', '4 boards × £22.00 = £88.00.', 'M1: Cost multiplication'),
                    ('Step 4', 'State final answer clearly', '4 boards are required at a total cost of £88.00.', 'A1: Accurate board count (4) and cost (£88.00)')
                ],
                'final_answer': '4 boards required | Total Cost = £88.00',
                'tutor_tip': 'If you added 12 × 85 cm = 1,020 cm and divided by 300 cm (= 3.4 → 4 boards), you would get lucky here, but in many exam questions joining offcuts gives the wrong board count! Always check how many fit in ONE board first.'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Mixing Units in Division or Joining Unjoinable Offcuts',
                'desc': 'Dividing metres by centimetres directly, or assuming small wood offcuts can be glued together to form a structural shelf.',
                'fix': 'Convert all lengths to cm first and check how many whole pieces fit into 1 stock length.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A roll of medical fabric tape is <strong>5 metres</strong> long. A nurse cuts <strong>8 strips</strong> measuring <strong>35 cm</strong> each. How many centimetres of tape remain on the roll?',
                'solution_steps': '1. 5 m = 500 cm.<br>2. 8 strips × 35 cm = 280 cm used.<br>3. Remaining = 500 - 280 = 220 cm (or 2.2 m).',
                'correct_answer': '220 cm (or 2.2 m)',
                'tutor_tip': 'Convert 5 metres to 500 cm first.'
            },
            {
                'marks': '2 Marks',
                'question': 'A picture framer needs to make a rectangular frame measuring <strong>65 cm long by 45 cm high</strong>. Allowing an extra <strong>15 cm</strong> in total for corner mitre cuts, what total length of moulding is needed in metres?',
                'solution_steps': '1. Frame perimeter = 2 × (65 + 45) = 2 × 110 = 220 cm.<br>2. Add cutting allowance = 220 + 15 = 235 cm.<br>3. Convert to metres: 235 ÷ 100 = 2.35 metres.',
                'correct_answer': '2.35 m',
                'tutor_tip': 'Check the unit requested in the final sentence (metres).'
            },
            {
                'marks': '3 Marks',
                'question': 'An office wall is <strong>4.6 metres</strong> long. The facilities manager places a filing cabinet (<strong>80 cm wide</strong>) in the corner, followed by <strong>3 identical desks</strong> (each <strong>115 cm wide</strong>). How much spare wall length remains in centimetres?',
                'solution_steps': '1. Wall length = 4.6 m = 460 cm.<br>2. 3 desks = 3 × 115 cm = 345 cm.<br>3. Total furniture width = 80 cm + 345 cm = 425 cm.<br>4. Remaining wall length = 460 - 425 = 35 cm.',
                'correct_answer': '35 cm',
                'tutor_tip': 'Convert 4.6 m to 460 cm right at the start.'
            }
        ]
    },
    {
        'filename': 'functional-skills-weight.html',
        'clean_topic': 'Weight & Mass',
        'intro_lead': 'Measure and calculate mass in grams, kilograms, and tonnes, solve postal package and baggage allowance limits, and convert between metric and imperial weight.',
        'next_file': 'functional-skills-capacity.html',
        'next_name': 'Capacity & Volume Units',
        'spec_points': [
            ('L1.18 / L2.20', 'Calculate and convert with units of weight and mass in practical contexts.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-scale-balanced',
                'title': 'Golden Rule 1: The 1,000 Factor for Mass',
                'desc': '1 tonne = 1,000 kg • 1 kg = 1,000 g • 1 g = 1,000 mg. Always multiply by 1,000 to go down a unit and divide by 1,000 to go up.',
                'badge': 'Tonnes × 1000 → Kilograms × 1000 → Grams'
            },
            {
                'icon': 'fa-truck-ramp-box',
                'title': 'Golden Rule 2: Gross Weight vs Net Weight vs Tare Weight',
                'desc': 'Gross Weight = Total weight (packaging + goods). Tare Weight = Weight of empty container/vehicle. Net Weight = Goods only (Gross - Tare).',
                'badge': 'Gross Weight = Net Goods + Tare Packaging'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Metric Mass Conversions (mg, g, kg, tonnes)',
                'summary': 'Moving seamlessly across powers of 1,000.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">From Unit</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">To Unit</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Operation</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Worked Example</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Tonnes (t)</td><td style="padding:6px; border:1px solid #cbd5e1;">Kilograms (kg)</td><td style="padding:6px; border:1px solid #cbd5e1;"><code>× 1,000</code></td><td style="padding:6px; border:1px solid #cbd5e1;"><code>1.8 tonnes = 1,800 kg</code></td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Kilograms (kg)</td><td style="padding:6px; border:1px solid #cbd5e1;">Grams (g)</td><td style="padding:6px; border:1px solid #cbd5e1;"><code>× 1,000</code></td><td style="padding:6px; border:1px solid #cbd5e1;"><code>3.4 kg = 3,400 g</code></td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Grams (g)</td><td style="padding:6px; border:1px solid #cbd5e1;">Kilograms (kg)</td><td style="padding:6px; border:1px solid #cbd5e1;"><code>÷ 1,000</code></td><td style="padding:6px; border:1px solid #cbd5e1;"><code>250 g = 0.25 kg</code></td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">Milligrams (mg)</td><td style="padding:6px; border:1px solid #cbd5e1;">Grams (g)</td><td style="padding:6px; border:1px solid #cbd5e1;"><code>÷ 1,000</code></td><td style="padding:6px; border:1px solid #cbd5e1;"><code>500 mg = 0.5 g</code></td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Skill 2: Vehicle Payload, Tare Weight & Safe Working Loads (SWL)',
                'summary': 'Checking lift and van weight limits including pallets, cages, and drivers.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>Total Loaded Pallet Weight:</strong> <code>(Number of Boxes × Weight per Box) + Empty Wooden Pallet Weight</code>.</li>
                    <li><strong>Maximum Number of Crates on a Lift:</strong> <code>(Max Safe Load − Operator/Cage Weight) ÷ Weight of 1 Crate</code> (always round <strong>DOWN</strong> to whole crates for safety!).</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 3: Weight-Based Dosage & Catering Portion Calculations',
                'summary': 'Applying mg/kg clinical rules and per-kilogram cooking times.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <p style="color:#334155; line-height:1.7;">Two high-frequency exam applications of weight:</p>
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>Clinical Dosage by Body Mass:</strong> If a drug requires <code>15 mg per kg</code> of body weight for a <code>64 kg</code> patient: <code>64 × 15 = 960 mg</code>.</li>
                    <li><strong>Roasting Time Rules:</strong> "Cook for 20 minutes per 500 g plus 25 minutes extra." For a <code>2.5 kg (2,500 g)</code> joint: there are five 500 g blocks &rarr; <code>(5 × 20) + 25 = 125 mins (2 hrs 5 mins)</code>.</li>
                  </ol>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Depot Freight Pallet Gross Weight Compliance',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Logistics & Freight Transport',
                'question': 'A wooden freight pallet weighs <strong>24 kg</strong> when empty. It is loaded with <strong>45 boxes</strong> of clinical supplies. Each box has a mass of <strong>800 grams</strong>.<br>(a) Calculate the total gross weight of the loaded pallet in kilograms.<br>(b) The tail-lift has a safe working load of <strong>75 kg</strong>. Can this pallet be safely lifted?',
                'steps': [
                    ('Step 1', 'Calculate total weight of boxes in grams', '45 boxes × 800 g = 36,000 grams.', 'M1: Multi-item mass multiplication'),
                    ('Step 2', 'Convert box mass to kilograms', '36,000 g ÷ 1,000 = 36 kg.', 'M1: Grams to kilograms conversion'),
                    ('Step 3', 'Calculate gross pallet weight and evaluate limit', 'Gross weight = 36 kg (boxes) + 24 kg (pallet) = 60 kg.<br>60 kg < 75 kg. Yes, the tail-lift can safely lift the pallet.', 'A1: Accurate gross weight and safety confirmation')
                ],
                'final_answer': '(a) Gross Weight = 60 kg | (b) Yes, 60 kg is within the 75 kg safe working load.',
                'tutor_tip': 'Notice how converting 36,000 g to 36 kg first makes adding the 24 kg pallet effortless.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Hospital Service Lift Trips for Laundry Cage Transfer',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Hospital Portering Operations',
                'question': 'A hospital porter needs to take <strong>32 bags</strong> of soiled linen down in a service lift.<br>• Each linen bag weighs <strong>12.5 kg</strong>.<br>• The porter uses a metal roll-cage that weighs <strong>35 kg</strong> when empty.<br>• The porter himself weighs <strong>82 kg</strong> and rides in the lift with the cage.<br>• The service lift has a maximum weight limit of <strong>0.35 tonnes</strong>.<br><br>Can the porter transport all 32 bags in just <strong>2 lift trips</strong>? Show full working.',
                'steps': [
                    ('Step 1', 'Convert maximum lift limit from tonnes to kilograms', '0.35 tonnes × 1,000 = 350 kg maximum per trip.', 'M1: Tonnes to kg conversion (350 kg)'),
                    ('Step 2', 'Subtract porter and empty roll-cage weight to find max linen weight per trip', 'Porter + Cage = 82 kg + 35 kg = 117 kg.<br>Max linen weight per trip = 350 kg - 117 kg = 233 kg.', 'M1: Subtracting tare/operator weight'),
                    ('Step 3', 'Calculate maximum bags per trip (or weight of 16 bags per trip)', '16 bags per trip × 12.5 kg = 200 kg of linen per trip (or 233 ÷ 12.5 = 18.64 → max 18 bags per trip).', 'M1: Bag weight comparison per trip'),
                    ('Step 4', 'Conclude whether 2 trips are sufficient', 'Since 200 kg ≤ 233 kg (or 2 × 18 = 36 bags ≥ 32 bags), yes, he can transport all 32 bags in 2 trips (e.g. 16 bags per trip = 317 kg total weight).', 'A1: Correct conclusion supported by exact figures')
                ],
                'final_answer': 'Yes (16 bags per trip weighs 200 kg + 117 kg porter/cage = 317 kg per trip, which is under the 350 kg limit).',
                'tutor_tip': 'Always remember to subtract the weight of the porter and the empty cage on EVERY trip!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Adding Grams and Kilograms Directly',
                'desc': 'Adding 24 kg + 36,000 g = 36,024 is an error caused by failing to convert to common units.',
                'fix': 'Always convert to the same unit before adding.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A parcel courier van can carry a maximum payload of <strong>1.2 tonnes</strong>. The driver has loaded <strong>950 kg</strong> of parcels. Can a further <strong>320 kg</strong> parcel be loaded without exceeding the limit?',
                'solution_steps': '1. Max payload = 1.2 tonnes = 1,200 kg.<br>2. Current + new parcel = 950 + 320 = 1,270 kg.<br>3. 1,270 kg > 1,200 kg. No, it exceeds the limit by 70 kg.',
                'correct_answer': 'No, it exceeds the payload limit by 70 kg (1,270 kg > 1,200 kg).',
                'tutor_tip': 'Convert 1.2 tonnes to 1,200 kg before comparing.'
            },
            {
                'marks': '2 Marks',
                'question': 'A catering pack contains <strong>2.4 kg</strong> of grated cheese. A chef uses <strong>65 grams</strong> of cheese on each pizza. How many pizzas can the chef top from one pack?',
                'solution_steps': '1. Convert 2.4 kg to grams: 2.4 × 1,000 = 2,400 g.<br>2. Divide by 65 g: 2,400 ÷ 65 = 36.92... &rarr; 36 full pizzas.',
                'correct_answer': '36 full pizzas',
                'tutor_tip': 'Round down to 36 because there is not enough cheese left for a 37th pizza.'
            },
            {
                'marks': '3 Marks',
                'question': 'A veterinary antibiotic is prescribed at a daily dose of <strong>20 mg per kg</strong> of body weight, split into <strong>2 equal doses</strong> (morning and evening). Calculate the mass of a single evening dose in <strong>grams</strong> for a dog weighing <strong>35 kg</strong>.',
                'solution_steps': '1. Total daily dose = 35 kg × 20 mg = 700 mg.<br>2. Single evening dose = 700 mg ÷ 2 = 350 mg.<br>3. Convert mg to grams: 350 ÷ 1,000 = 0.35 grams.',
                'correct_answer': '0.35 g (350 mg)',
                'tutor_tip': 'Read carefully: the question asks for a SINGLE dose in GRAMS (divide mg by 1,000).'
            }
        ]
    },
    {
        'filename': 'functional-skills-capacity.html',
        'clean_topic': 'Capacity & Liquid Volume Units',
        'intro_lead': 'Measure and convert liquid capacity in millilitres, centilitres, and litres, calculate container capacities, and solve clinical medication fluid dosage problems.',
        'next_file': 'functional-skills-perimeter.html',
        'next_name': 'Perimeter',
        'spec_points': [
            ('L1.18 / L2.20', 'Calculate and convert with metric units of capacity and volume.')
        ],
        'golden_rules': [
            {
                'icon': 'fa-glass-water',
                'title': 'Golden Rule 1: 1 Litre = 1,000 Millilitres = 1,000 cm³',
                'desc': 'To convert litres to millilitres, multiply by 1,000. To convert millilitres to litres, divide by 1,000. Remember the 3D volume bridge: 1 cm³ holds 1 ml, and 1 m³ holds 1,000 litres.',
                'badge': '1 Litre = 1,000 ml = 1,000 cm³ | 1 m³ = 1,000 Litres'
            },
            {
                'icon': 'fa-droplet',
                'title': 'Golden Rule 2: 1 Centilitre (cl) = 10 Millilitres',
                'desc': 'Catering and beverage bottles often use centilitres: 75 cl = 750 ml = 0.75 litres.',
                'badge': '1 cl = 10 ml | 100 cl = 1 Litre'
            }
        ],
        'skills': [
            {
                'title': 'Skill 1: Converting Between Millilitres (ml), Centilitres (cl) & Litres (L)',
                'summary': 'Instant reference chart for liquid capacity conversions.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <table style="width:100%; border-collapse:collapse; text-align:center;">
                    <thead>
                      <tr style="background:#0284c7; color:#fff;">
                        <th style="padding:8px; border:1px solid #cbd5e1;">Litres (L)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Centilitres (cl)</th>
                        <th style="padding:8px; border:1px solid #cbd5e1;">Millilitres (ml)</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">1 L</td><td style="padding:6px; border:1px solid #cbd5e1;">100 cl</td><td style="padding:6px; border:1px solid #cbd5e1;">1,000 ml</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">0.75 L</td><td style="padding:6px; border:1px solid #cbd5e1;">75 cl</td><td style="padding:6px; border:1px solid #cbd5e1;">750 ml</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">0.33 L</td><td style="padding:6px; border:1px solid #cbd5e1;">33 cl</td><td style="padding:6px; border:1px solid #cbd5e1;">330 ml</td></tr>
                      <tr><td style="padding:6px; border:1px solid #cbd5e1; font-weight:700;">2.5 L</td><td style="padding:6px; border:1px solid #cbd5e1;">250 cl</td><td style="padding:6px; border:1px solid #cbd5e1;">2,500 ml</td></tr>
                    </tbody>
                  </table>
                </div>
                """
            },
            {
                'title': 'Skill 2: Bridging 3D Geometric Volume (cm³ and m³) to Liquid Litres',
                'summary': 'How to convert tank dimensions in cm or m into litres of water or fuel.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ul style="padding-left:20px; line-height:1.8; color:#334155;">
                    <li><strong>From <code>cm³</code> to Litres (<code>÷ 1,000</code>):</strong> A fish tank measuring <code>60 cm × 30 cm × 40 cm = 72,000 cm³</code> holds <code>72,000 ÷ 1,000 = 72 litres</code>.</li>
                    <li><strong>From <code>m³</code> to Litres (<code>× 1,000</code>):</strong> A rainwater harvesting tank with volume <code>2.4 m³</code> holds <code>2.4 × 1,000 = 2,400 litres</code>.</li>
                  </ul>
                </div>
                """
            },
            {
                'title': 'Skill 3: Clinical Fluid Balance Charts & IV Drip Flow Rates',
                'summary': 'Tracking fluid intake vs output and calculating ml/hour infusion durations.',
                'content_html': """
                <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; padding:18px; margin:16px 0;">
                  <ol style="padding-left:22px; line-height:1.8; color:#334155;">
                    <li><strong>IV Infusion Rate:</strong> <code>Rate (ml/hr) = Total Volume (ml) ÷ Time (hours)</code>. For example, <code>1.5 litres (1,500 ml)</code> over <code>6 hours</code> = <code>1,500 ÷ 6 = 250 ml/hr</code>.</li>
                    <li><strong>Fluid Balance:</strong> <code>Net Balance = Total Fluid Intake (ml) − Total Fluid Output (ml)</code>.</li>
                  </ol>
                </div>
                """
            }
        ],
        'worked_models': [
            {
                'title': 'Model 1 (Level 1 Foundation): Hospital Ward Oral Rehydration Fluid Dispensing',
                'marks': '3 Marks (Pearson Edexcel Level 1/2)',
                'context': 'Clinical Ward Fluid Administration',
                'question': "A care home nurse prepares a <strong>2-litre jug</strong> of oral rehydration fluid. She pours <strong>150 ml</strong> into each resident's cup.<br>(a) How many full cups can she pour from the jug?<br>(b) How many millilitres of fluid remain in the jug?",
                'steps': [
                    ('Step 1', 'Convert jug capacity from litres to millilitres', '2 litres × 1,000 = 2,000 ml.', 'M1: Litres to ml conversion'),
                    ('Step 2', 'Divide total volume by single cup volume', '2,000 ml ÷ 150 ml = 13.333... (13 remainder 50).', 'M1: Division setup and execution'),
                    ('Step 3', 'State whole cups and remaining volume', 'Full cups = 13 cups.<br>Volume used = 13 × 150 ml = 1,950 ml.<br>Remaining = 2,000 - 1,950 = 50 ml.', 'A1: Accurate cups and remainder in ml')
                ],
                'final_answer': '(a) 13 full cups | (b) 50 ml remains in the jug.',
                'tutor_tip': 'Notice you cannot pour 13.33 cups; you round down to 13 full cups and 50 ml left over.'
            },
            {
                'title': 'Model 2 (Level 2 Decision): Commercial Greenhouse Water Tank & Pump Filling Time',
                'marks': '4 Marks (Pearson Edexcel Level 2 Problem Solving)',
                'context': 'Horticultural Irrigation Engineering',
                'question': 'A commercial nursery has a rectangular water storage tank measuring <strong>2.5 m long, 1.2 m wide, and 0.8 m deep</strong>.<br>• The tank is currently completely empty.<br>• The manager needs to fill the tank to <strong>80% of its maximum capacity</strong>.<br>• A water hose fills the tank at a rate of <strong>32 litres per minute</strong>.<br>• Use: <strong>1 m³ = 1,000 litres</strong>.<br><br>Will the tank reach 80% capacity within <strong>1 hour</strong>?',
                'steps': [
                    ('Step 1', 'Calculate full tank volume in m³ and convert to litres', 'Volume = 2.5 × 1.2 × 0.8 = 2.4 m³.<br>Full capacity in litres = 2.4 × 1,000 = 2,400 litres.', 'M1: Tank volume in litres (2,400 L)'),
                    ('Step 2', 'Calculate 80% target volume', '80% of 2,400 L = 0.80 × 2,400 = 1,920 litres.', 'M1: 80% capacity calculation'),
                    ('Step 3', 'Divide required litres by flow rate (32 L/min)', 'Time = 1,920 litres ÷ 32 L/min = 60 minutes.', 'M1: Division by flow rate'),
                    ('Step 4', 'Compare against 1-hour (60-minute) limit', '60 minutes = exactly 1 hour. Yes, the tank will reach 80% capacity in exactly 1 hour (60 minutes).', 'A1: Accurate time (60 mins) and justified conclusion')
                ],
                'final_answer': 'Yes (80% capacity is 1,920 litres, which takes 1,920 ÷ 32 = 60 minutes = exactly 1 hour).',
                'tutor_tip': 'Remember the golden bridge: 1 m³ = 1,000 litres, whereas 1,000 cm³ = 1 litre!'
            }
        ],
        'examiner_traps': [
            {
                'title': 'Dividing 2 by 150 Without Converting to Millilitres',
                'desc': 'Doing 2 ÷ 150 gives 0.0133 — always convert litres to millilitres first!',
                'fix': 'Both numbers must be in millilitres (or both in litres) before dividing.'
            }
        ],
        'practice_questions': [
            {
                'marks': '2 Marks',
                'question': 'A bottle of cough linctus contains <strong>300 ml</strong>. The recommended adult dose is <strong>15 ml three times daily</strong>. How many full days will this bottle last?',
                'solution_steps': '1. Daily dose = 15 ml × 3 = 45 ml per day.<br>2. Total days = 300 ÷ 45 = 6.666... days.<br>3. It will last for 6 full days (with 30 ml left over for day 7).',
                'correct_answer': '6 full days',
                'tutor_tip': 'Calculate the total daily dose (45 ml) first before dividing the bottle volume.'
            },
            {
                'marks': '2 Marks',
                'question': 'A catering team needs <strong>18 litres</strong> of orange juice for a conference. Orange juice is sold in cartons of <strong>75 cl</strong>. How many cartons must they buy?',
                'solution_steps': '1. Convert both to millilitres (or litres): 18 L = 18,000 ml; 75 cl = 750 ml (0.75 L).<br>2. Divide: 18,000 ÷ 750 (or 18 ÷ 0.75) = 24 cartons.',
                'correct_answer': '24 cartons',
                'tutor_tip': '75 cl = 750 ml = 0.75 L.'
            },
            {
                'marks': '3 Marks',
                'question': 'A hospital patient is prescribed <strong>1.8 litres</strong> of intravenous saline to be infused at a constant rate of <strong>240 ml per hour</strong>. If the infusion starts at <strong>08:15</strong>, at what time will it finish?',
                'solution_steps': '1. Convert 1.8 L to ml: 1.8 × 1,000 = 1,800 ml.<br>2. Duration = 1,800 ÷ 240 = 7.5 hours = 7 hours 30 minutes.<br>3. Finish time = 08:15 + 7 hours 30 minutes = 15:45 (3:45 pm).',
                'correct_answer': '15:45 (or 3:45 pm)',
                'tutor_tip': '0.5 hours = 30 minutes; 08:15 + 7h 30m = 15:45.'
            }
        ]
    }
]
