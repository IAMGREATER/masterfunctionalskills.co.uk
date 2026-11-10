/**
 * Master Functional Skills - Video Solution Modal Controller
 * Author: Master Functional Skills / DarkNight
 */

(function () {
  'use strict';

  // Available videos dictionary (slug/topic -> video details)
  // Available videos dictionary (slug/topic -> video details)
  const KNOWN_VIDEOS = {
    // Topic Masterclasses (Level 2 Maths)
    'numbers-and-place-value': {
      ytId: 'Ty9VhQvYT34',
      title: 'Numbers and Place Value • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Sonya',
      localVideo: 'assets/video/sonya-numbers-and-place-value-walkthrough.mp4',
      poster: 'assets/img/numbers-place-value-sonya-poster.png',
      companionSlug: 'ordering-numbers',
      companionLabel: 'Next: Ordering Numbers (Subi)'
    },
    'numbers and place value': {
      ytId: 'Ty9VhQvYT34',
      title: 'Numbers and Place Value • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Sonya',
      localVideo: 'assets/video/sonya-numbers-and-place-value-walkthrough.mp4',
      poster: 'assets/img/numbers-place-value-sonya-poster.png',
      companionSlug: 'ordering-numbers',
      companionLabel: 'Next: Ordering Numbers (Subi)'
    },
    'ordering-numbers': {
      ytId: '-6NY17_LDYg',
      title: 'Ordering Numbers • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Subi',
      localVideo: 'assets/video/subi-ordering-numbers-walkthrough.mp4',
      poster: 'assets/img/ordering-numbers-subi-poster.png',
      companionSlug: 'addition-and-subtraction',
      companionLabel: 'Next: Addition & Subtraction (Emma)'
    },
    'ordering numbers': {
      ytId: '-6NY17_LDYg',
      title: 'Ordering Numbers • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Subi',
      localVideo: 'assets/video/subi-ordering-numbers-walkthrough.mp4',
      poster: 'assets/img/ordering-numbers-subi-poster.png',
      companionSlug: 'addition-and-subtraction',
      companionLabel: 'Next: Addition & Subtraction (Emma)'
    },
    'addition-and-subtraction': {
      ytId: 'lZno-Cxkp80',
      title: 'Addition and Subtraction • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Emma',
      localVideo: 'assets/video/emma-addition-subtraction-walkthrough.mp4',
      poster: 'assets/img/addition-subtraction-emma-poster.png',
      companionSlug: 'multiplication',
      companionLabel: 'Next: Multiplication (Sonya)'
    },
    'addition and subtraction': {
      ytId: 'lZno-Cxkp80',
      title: 'Addition and Subtraction • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Emma',
      localVideo: 'assets/video/emma-addition-subtraction-walkthrough.mp4',
      poster: 'assets/img/addition-subtraction-emma-poster.png',
      companionSlug: 'multiplication',
      companionLabel: 'Next: Multiplication (Sonya)'
    },
    'multiplication': {
      ytId: 'JFnv0TXY8NE',
      title: 'Multiplication (Whole Numbers & Decimals) • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Sonya',
      localVideo: 'assets/video/sonya-multiplication-walkthrough.mp4',
      poster: 'assets/img/multiplication-sonya-poster.png',
      companionSlug: 'division',
      companionLabel: 'Next: Division (Subi)'
    },
    'functional-skills-multiplication': {
      ytId: 'JFnv0TXY8NE',
      title: 'Multiplication (Whole Numbers & Decimals) • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Sonya',
      localVideo: 'assets/video/sonya-multiplication-walkthrough.mp4',
      poster: 'assets/img/multiplication-sonya-poster.png',
      companionSlug: 'division',
      companionLabel: 'Next: Division (Subi)'
    },
    'division': {
      ytId: '8ZgpuneKalQ',
      title: 'Division & Remainders • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Subi',
      localVideo: 'assets/video/subi-division-and-remainders-walkthrough.mp4',
      poster: 'assets/img/division-subi-poster.png',
      companionSlug: 'bidmas',
      companionLabel: 'Next: BIDMAS (Emma)'
    },
    'functional-skills-division': {
      ytId: '8ZgpuneKalQ',
      title: 'Division & Remainders • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Subi',
      localVideo: 'assets/video/subi-division-and-remainders-walkthrough.mp4',
      poster: 'assets/img/division-subi-poster.png',
      companionSlug: 'bidmas',
      companionLabel: 'Next: BIDMAS (Emma)'
    },
    'bidmas': {
      ytId: '31-cHwQryVc',
      title: 'Order of Operations (BIDMAS) • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Emma',
      localVideo: 'assets/video/emma-bidmas-walkthrough.mp4',
      poster: 'assets/img/bidmas-emma-poster.png',
      companionSlug: 'division',
      companionLabel: 'Prev: Division (Subi)'
    },
    'functional-skills-bidmas': {
      ytId: '31-cHwQryVc',
      title: 'Order of Operations (BIDMAS) • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Emma',
      localVideo: 'assets/video/emma-bidmas-walkthrough.mp4',
      poster: 'assets/img/bidmas-emma-poster.png',
      companionSlug: 'division',
      companionLabel: 'Prev: Division (Subi)'
    },
    'order of operations': {
      ytId: '31-cHwQryVc',
      title: 'Order of Operations (BIDMAS) • Masterclass Walkthrough',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: 'Tutor Emma',
      localVideo: 'assets/video/emma-bidmas-walkthrough.mp4',
      poster: 'assets/img/bidmas-emma-poster.png',
      companionSlug: 'division',
      companionLabel: 'Prev: Division (Subi)'
    },

    
    // --- 33 NEW LEVEL 2 MATHS TOPIC MASTERCLASSES ---
    '3d-shapes-and-nets': {
      ytId: 'wHgk6CI99us',
      title: "3D Shapes, Nets and Plans \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-3d-shapes-and-nets-walkthrough.mp4',
      poster: 'assets/img/3d-shapes-and-nets-sonya-poster.png',
      companionSlug: '3d-shapes-and-nets',
      companionLabel: "3D Shapes and Nets"
    },
    "3d shapes and nets": {
      ytId: '',
      title: "3D Shapes, Nets and Plans \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-3d-shapes-and-nets-walkthrough.mp4',
      poster: 'assets/img/3d-shapes-and-nets-sonya-poster.png',
      companionSlug: '3d-shapes-and-nets',
      companionLabel: "3D Shapes and Nets"
    },
    'angles-bearings-pythagoras': {
      ytId: '-RQYqrfs3nE',
      title: "Angles, Bearings and Pythagoras \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-angles-bearings-pythagoras-walkthrough.mp4',
      poster: 'assets/img/angles-bearings-pythagoras-subi-poster.png',
      companionSlug: 'angles-bearings-pythagoras',
      companionLabel: "Angles, Bearings and Pythagoras"
    },
    "angles, bearings and pythagoras": {
      ytId: '',
      title: "Angles, Bearings and Pythagoras \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-angles-bearings-pythagoras-walkthrough.mp4',
      poster: 'assets/img/angles-bearings-pythagoras-subi-poster.png',
      companionSlug: 'angles-bearings-pythagoras',
      companionLabel: "Angles, Bearings and Pythagoras"
    },
    'area': {
      ytId: '2iZJuu0MUgs',
      title: "Area of 2D and Compound Shapes \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-area-walkthrough.mp4',
      poster: 'assets/img/area-subi-poster.png',
      companionSlug: 'area',
      companionLabel: "Area of 2D and Compound Shapes"
    },
    "area of 2d and compound shapes": {
      ytId: '',
      title: "Area of 2D and Compound Shapes \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-area-walkthrough.mp4',
      poster: 'assets/img/area-subi-poster.png',
      companionSlug: 'area',
      companionLabel: "Area of 2D and Compound Shapes"
    },
    'averages-and-spread': {
      ytId: 'sgvRdO8EIgU',
      title: "Averages and Spread \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-averages-and-spread-walkthrough.mp4',
      poster: 'assets/img/averages-and-spread-sonya-poster.png',
      companionSlug: 'averages-and-spread',
      companionLabel: "Averages and Spread (Mean, Median, Mode, Range)"
    },
    "averages and spread (mean, median, mode, range)": {
      ytId: '',
      title: "Averages and Spread \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-averages-and-spread-walkthrough.mp4',
      poster: 'assets/img/averages-and-spread-sonya-poster.png',
      companionSlug: 'averages-and-spread',
      companionLabel: "Averages and Spread (Mean, Median, Mode, Range)"
    },
    'bar-charts-and-pie-charts': {
      ytId: 'pvfhMZllArg',
      title: "Bar Charts and Pie Charts \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-bar-charts-and-pie-charts-walkthrough.mp4',
      poster: 'assets/img/bar-charts-and-pie-charts-emma-poster.png',
      companionSlug: 'bar-charts-and-pie-charts',
      companionLabel: "Bar Charts and Pie Charts"
    },
    "bar charts and pie charts": {
      ytId: '',
      title: "Bar Charts and Pie Charts \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-bar-charts-and-pie-charts-walkthrough.mp4',
      poster: 'assets/img/bar-charts-and-pie-charts-emma-poster.png',
      companionSlug: 'bar-charts-and-pie-charts',
      companionLabel: "Bar Charts and Pie Charts"
    },
    'bearings': {
      ytId: 'C9KA5RzKLfE',
      title: "Bearings and 3-Figure Directions \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-bearings-walkthrough.mp4',
      poster: 'assets/img/bearings-emma-poster.png',
      companionSlug: 'bearings',
      companionLabel: "Bearings and Navigation"
    },
    "bearings and navigation": {
      ytId: '',
      title: "Bearings and 3-Figure Directions \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-bearings-walkthrough.mp4',
      poster: 'assets/img/bearings-emma-poster.png',
      companionSlug: 'bearings',
      companionLabel: "Bearings and Navigation"
    },
    'coordinates-and-transformations': {
      ytId: 'tQY6G1i8hPc',
      title: "Coordinates and Transformations \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-coordinates-and-transformations-walkthrough.mp4',
      poster: 'assets/img/coordinates-and-transformations-sonya-poster.png',
      companionSlug: 'coordinates-and-transformations',
      companionLabel: "Coordinates and Transformations"
    },
    "coordinates and transformations": {
      ytId: '',
      title: "Coordinates and Transformations \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-coordinates-and-transformations-walkthrough.mp4',
      poster: 'assets/img/coordinates-and-transformations-sonya-poster.png',
      companionSlug: 'coordinates-and-transformations',
      companionLabel: "Coordinates and Transformations"
    },
    'currency-conversion': {
      ytId: 'WxhVrm3VsAU',
      title: "Currency Conversion & Exchange Rates \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-currency-conversion-walkthrough.mp4',
      poster: 'assets/img/currency-conversion-subi-poster.png',
      companionSlug: 'currency-conversion',
      companionLabel: "Currency Conversion & Exchange Rates"
    },
    "currency conversion and exchange rates": {
      ytId: '',
      title: "Currency Conversion & Exchange Rates \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-currency-conversion-walkthrough.mp4',
      poster: 'assets/img/currency-conversion-subi-poster.png',
      companionSlug: 'currency-conversion',
      companionLabel: "Currency Conversion & Exchange Rates"
    },
    'decimals': {
      ytId: '1yKdgKOIDn0',
      title: "Decimals Mastery \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-decimals-walkthrough.mp4',
      poster: 'assets/img/decimals-subi-poster.png',
      companionSlug: 'decimals',
      companionLabel: "Decimals (Arithmetic & Place Value)"
    },
    "decimals (arithmetic and place value)": {
      ytId: '',
      title: "Decimals Mastery \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-decimals-walkthrough.mp4',
      poster: 'assets/img/decimals-subi-poster.png',
      companionSlug: 'decimals',
      companionLabel: "Decimals (Arithmetic & Place Value)"
    },
    'density-mass-and-volume': {
      ytId: 'Jn4BMqg5yx4',
      title: "Density, Mass and Volume \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-density-mass-and-volume-walkthrough.mp4',
      poster: 'assets/img/density-mass-and-volume-sonya-poster.png',
      companionSlug: 'density-mass-and-volume',
      companionLabel: "Density, Mass and Volume"
    },
    "density, mass and volume": {
      ytId: '',
      title: "Density, Mass and Volume \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-density-mass-and-volume-walkthrough.mp4',
      poster: 'assets/img/density-mass-and-volume-sonya-poster.png',
      companionSlug: 'density-mass-and-volume',
      companionLabel: "Density, Mass and Volume"
    },
    'fdp-conversions': {
      ytId: 'k9D5oMouzvU',
      title: "FDP Conversions \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-fdp-conversions-walkthrough.mp4',
      poster: 'assets/img/fdp-conversions-subi-poster.png',
      companionSlug: 'fdp-conversions',
      companionLabel: "FDP Conversions (Fractions, Decimals, Percentages)"
    },
    "fdp conversions (fractions, decimals, percentages)": {
      ytId: '',
      title: "FDP Conversions \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-fdp-conversions-walkthrough.mp4',
      poster: 'assets/img/fdp-conversions-subi-poster.png',
      companionSlug: 'fdp-conversions',
      companionLabel: "FDP Conversions (Fractions, Decimals, Percentages)"
    },
    'formulas': {
      ytId: '39piKKg90OE',
      title: "Formulas and Substitution \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-formulas-walkthrough.mp4',
      poster: 'assets/img/formulas-subi-poster.png',
      companionSlug: 'formulas',
      companionLabel: "Formulas and Substitution"
    },
    "formulas and substitution": {
      ytId: '',
      title: "Formulas and Substitution \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-formulas-walkthrough.mp4',
      poster: 'assets/img/formulas-subi-poster.png',
      companionSlug: 'formulas',
      companionLabel: "Formulas and Substitution"
    },
    'fractions': {
      ytId: '74kfw27oSOE',
      title: "Fractions Arithmetic & Word Problems \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-fractions-walkthrough.mp4',
      poster: 'assets/img/fractions-sonya-poster.png',
      companionSlug: 'fractions',
      companionLabel: "Fractions (Arithmetic & Simplifying)"
    },
    "fractions (arithmetic and simplifying)": {
      ytId: '',
      title: "Fractions Arithmetic & Word Problems \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-fractions-walkthrough.mp4',
      poster: 'assets/img/fractions-sonya-poster.png',
      companionSlug: 'fractions',
      companionLabel: "Fractions (Arithmetic & Simplifying)"
    },
    'fractions-of-amounts': {
      ytId: 'JggjX4FDkqg',
      title: "Fractions of Amounts & Reverse Fractions \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-fractions-of-amounts-walkthrough.mp4',
      poster: 'assets/img/fractions-of-amounts-emma-poster.png',
      companionSlug: 'fractions-of-amounts',
      companionLabel: "Fractions of Amounts and Reverse Fractions"
    },
    "fractions of amounts and reverse fractions": {
      ytId: '',
      title: "Fractions of Amounts & Reverse Fractions \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-fractions-of-amounts-walkthrough.mp4',
      poster: 'assets/img/fractions-of-amounts-emma-poster.png',
      companionSlug: 'fractions-of-amounts',
      companionLabel: "Fractions of Amounts and Reverse Fractions"
    },
    'frequency-and-two-way-tables': {
      ytId: 'PzEL_FVXa7g',
      title: "Frequency & Two-Way Tables \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-frequency-and-two-way-tables-walkthrough.mp4',
      poster: 'assets/img/frequency-and-two-way-tables-subi-poster.png',
      companionSlug: 'frequency-and-two-way-tables',
      companionLabel: "Frequency & Two-Way Tables"
    },
    "frequency and two-way tables": {
      ytId: '',
      title: "Frequency & Two-Way Tables \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-frequency-and-two-way-tables-walkthrough.mp4',
      poster: 'assets/img/frequency-and-two-way-tables-subi-poster.png',
      companionSlug: 'frequency-and-two-way-tables',
      companionLabel: "Frequency & Two-Way Tables"
    },
    'percentages': {
      ytId: 'QXr9L_RKM1s',
      title: "Percentages of Amounts \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-percentages-walkthrough.mp4',
      poster: 'assets/img/percentages-sonya-poster.png',
      companionSlug: 'percentages',
      companionLabel: "Percentages of Amounts"
    },
    "percentages of amounts": {
      ytId: '',
      title: "Percentages of Amounts \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-percentages-walkthrough.mp4',
      poster: 'assets/img/percentages-sonya-poster.png',
      companionSlug: 'percentages',
      companionLabel: "Percentages of Amounts"
    },
    'percentages-and-percentage-change': {
      ytId: 'BsuBjE9ogZI',
      title: "Percentages & Percentage Change \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-percentages-and-percentage-change-walkthrough.mp4',
      poster: 'assets/img/percentages-and-percentage-change-sonya-poster.png',
      companionSlug: 'percentages-and-percentage-change',
      companionLabel: "Percentages & Percentage Change"
    },
    "percentages and percentage change": {
      ytId: '',
      title: "Percentages & Percentage Change \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-percentages-and-percentage-change-walkthrough.mp4',
      poster: 'assets/img/percentages-and-percentage-change-sonya-poster.png',
      companionSlug: 'percentages-and-percentage-change',
      companionLabel: "Percentages & Percentage Change"
    },
    'perimeter-area-and-composite-plans': {
      ytId: 'iN965C_11O0',
      title: "Perimeter, Area & Composite Plans \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-perimeter-area-and-composite-plans-walkthrough.mp4',
      poster: 'assets/img/perimeter-area-and-composite-plans-emma-poster.png',
      companionSlug: 'perimeter-area-and-composite-plans',
      companionLabel: "Perimeter, Area & Composite Plans"
    },
    "perimeter, area and composite plans": {
      ytId: '',
      title: "Perimeter, Area & Composite Plans \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-perimeter-area-and-composite-plans-walkthrough.mp4',
      poster: 'assets/img/perimeter-area-and-composite-plans-emma-poster.png',
      companionSlug: 'perimeter-area-and-composite-plans',
      companionLabel: "Perimeter, Area & Composite Plans"
    },
    'perimeter': {
      ytId: '07stUoCaETU',
      title: "Perimeter & Circumference \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-perimeter-walkthrough.mp4',
      poster: 'assets/img/perimeter-sonya-poster.png',
      companionSlug: 'perimeter',
      companionLabel: "Perimeter of 2D Shapes & Circumference"
    },
    "perimeter of 2d shapes and circumference": {
      ytId: '',
      title: "Perimeter & Circumference \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-perimeter-walkthrough.mp4',
      poster: 'assets/img/perimeter-sonya-poster.png',
      companionSlug: 'perimeter',
      companionLabel: "Perimeter of 2D Shapes & Circumference"
    },
    'probability-trees': {
      ytId: '-GY2jRSa5JE',
      title: "Probability Trees & Combined Events \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-probability-trees-walkthrough.mp4',
      poster: 'assets/img/probability-trees-emma-poster.png',
      companionSlug: 'probability-trees',
      companionLabel: "Probability Trees & Combined Events"
    },
    "probability trees and combined events": {
      ytId: '',
      title: "Probability Trees & Combined Events \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-probability-trees-walkthrough.mp4',
      poster: 'assets/img/probability-trees-emma-poster.png',
      companionSlug: 'probability-trees',
      companionLabel: "Probability Trees & Combined Events"
    },
    'probability-and-expected-frequency': {
      ytId: 'PD1CS1SLxSM',
      title: "Probability & Expected Frequency \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-probability-and-expected-frequency-walkthrough.mp4',
      poster: 'assets/img/probability-and-expected-frequency-subi-poster.png',
      companionSlug: 'probability-and-expected-frequency',
      companionLabel: "Probability & Expected Frequency"
    },
    "probability and expected frequency": {
      ytId: '',
      title: "Probability & Expected Frequency \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-probability-and-expected-frequency-walkthrough.mp4',
      poster: 'assets/img/probability-and-expected-frequency-subi-poster.png',
      companionSlug: 'probability-and-expected-frequency',
      companionLabel: "Probability & Expected Frequency"
    },
    'proportion': {
      ytId: 'qj-8nTsnO3I',
      title: "Direct & Inverse Proportion \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-proportion-walkthrough.mp4',
      poster: 'assets/img/proportion-sonya-poster.png',
      companionSlug: 'proportion',
      companionLabel: "Direct & Inverse Proportion"
    },
    "direct and inverse proportion": {
      ytId: '',
      title: "Direct & Inverse Proportion \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-proportion-walkthrough.mp4',
      poster: 'assets/img/proportion-sonya-poster.png',
      companionSlug: 'proportion',
      companionLabel: "Direct & Inverse Proportion"
    },
    'ratio': {
      ytId: 'jWoKhGQzOJI',
      title: "Ratio Mastery \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-ratio-walkthrough.mp4',
      poster: 'assets/img/ratio-emma-poster.png',
      companionSlug: 'ratio',
      companionLabel: "Ratio (Sharing & Simplifying)"
    },
    "ratio (sharing and simplifying)": {
      ytId: '',
      title: "Ratio Mastery \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-ratio-walkthrough.mp4',
      poster: 'assets/img/ratio-emma-poster.png',
      companionSlug: 'ratio',
      companionLabel: "Ratio (Sharing & Simplifying)"
    },
    'ratio-and-direct-proportion': {
      ytId: 'G-U7kCFwm-I',
      title: "Ratio & Direct Proportion \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-ratio-and-direct-proportion-walkthrough.mp4',
      poster: 'assets/img/ratio-and-direct-proportion-sonya-poster.png',
      companionSlug: 'ratio-and-direct-proportion',
      companionLabel: "Ratio and Direct Proportion Applications"
    },
    "ratio and direct proportion applications": {
      ytId: '',
      title: "Ratio & Direct Proportion \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-ratio-and-direct-proportion-walkthrough.mp4',
      poster: 'assets/img/ratio-and-direct-proportion-sonya-poster.png',
      companionSlug: 'ratio-and-direct-proportion',
      companionLabel: "Ratio and Direct Proportion Applications"
    },
    'rounding-and-estimating': {
      ytId: 'KxY8vBzGWKE',
      title: "Rounding and Estimating \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-rounding-and-estimating-walkthrough.mp4',
      poster: 'assets/img/rounding-and-estimating-emma-poster.png',
      companionSlug: 'rounding-and-estimating',
      companionLabel: "Rounding and Estimating"
    },
    "rounding and estimating": {
      ytId: '',
      title: "Rounding and Estimating \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-rounding-and-estimating-walkthrough.mp4',
      poster: 'assets/img/rounding-and-estimating-emma-poster.png',
      companionSlug: 'rounding-and-estimating',
      companionLabel: "Rounding and Estimating"
    },
    'scale-drawings': {
      ytId: 'KZWBNnfCNGw',
      title: "Maps and Scale Drawings \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-scale-drawings-walkthrough.mp4',
      poster: 'assets/img/scale-drawings-subi-poster.png',
      companionSlug: 'scale-drawings',
      companionLabel: "Maps and Scale Drawings"
    },
    "maps and scale drawings": {
      ytId: '',
      title: "Maps and Scale Drawings \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-scale-drawings-walkthrough.mp4',
      poster: 'assets/img/scale-drawings-subi-poster.png',
      companionSlug: 'scale-drawings',
      companionLabel: "Maps and Scale Drawings"
    },
    'scatter-graphs-and-correlation': {
      ytId: 'zOmrtdOj5dc',
      title: "Scatter Graphs and Correlation \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-scatter-graphs-and-correlation-walkthrough.mp4',
      poster: 'assets/img/scatter-graphs-and-correlation-sonya-poster.png',
      companionSlug: 'scatter-graphs-and-correlation',
      companionLabel: "Scatter Graphs and Correlation"
    },
    "scatter graphs and correlation": {
      ytId: '',
      title: "Scatter Graphs and Correlation \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Sonya",
      localVideo: 'assets/video/sonya-scatter-graphs-and-correlation-walkthrough.mp4',
      poster: 'assets/img/scatter-graphs-and-correlation-sonya-poster.png',
      companionSlug: 'scatter-graphs-and-correlation',
      companionLabel: "Scatter Graphs and Correlation"
    },
    'simple-and-compound-interest': {
      ytId: 'gsSLwcadZH0',
      title: "Simple and Compound Interest \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-simple-and-compound-interest-walkthrough.mp4',
      poster: 'assets/img/simple-and-compound-interest-subi-poster.png',
      companionSlug: 'simple-and-compound-interest',
      companionLabel: "Simple and Compound Interest"
    },
    "simple and compound interest": {
      ytId: '',
      title: "Simple and Compound Interest \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-simple-and-compound-interest-walkthrough.mp4',
      poster: 'assets/img/simple-and-compound-interest-subi-poster.png',
      companionSlug: 'simple-and-compound-interest',
      companionLabel: "Simple and Compound Interest"
    },
    'speed-distance-and-time': {
      ytId: 'ZUbm9S7_ySA',
      title: "Speed, Distance and Time \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-speed-distance-and-time-walkthrough.mp4',
      poster: 'assets/img/speed-distance-and-time-emma-poster.png',
      companionSlug: 'speed-distance-and-time',
      companionLabel: "Speed, Distance and Time"
    },
    "speed, distance and time": {
      ytId: '',
      title: "Speed, Distance and Time \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-speed-distance-and-time-walkthrough.mp4',
      poster: 'assets/img/speed-distance-and-time-emma-poster.png',
      companionSlug: 'speed-distance-and-time',
      companionLabel: "Speed, Distance and Time"
    },
    'symmetry-tessellation-and-2d-properties': {
      ytId: '0UOwW2sS_4k',
      title: "Symmetry, Tessellation & 2D Properties \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-symmetry-tessellation-and-2d-properties-walkthrough.mp4',
      poster: 'assets/img/symmetry-tessellation-and-2d-properties-emma-poster.png',
      companionSlug: 'symmetry-tessellation-and-2d-properties',
      companionLabel: "Symmetry, Tessellation & 2D Properties"
    },
    "symmetry, tessellation and 2d properties": {
      ytId: '',
      title: "Symmetry, Tessellation & 2D Properties \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-symmetry-tessellation-and-2d-properties-walkthrough.mp4',
      poster: 'assets/img/symmetry-tessellation-and-2d-properties-emma-poster.png',
      companionSlug: 'symmetry-tessellation-and-2d-properties',
      companionLabel: "Symmetry, Tessellation & 2D Properties"
    },
    'unit-conversions': {
      ytId: '0ZwUUWB76Dc',
      title: "Unit Conversions \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-unit-conversions-walkthrough.mp4',
      poster: 'assets/img/unit-conversions-emma-poster.png',
      companionSlug: 'unit-conversions',
      companionLabel: "Unit Conversions (Metric & Imperial)"
    },
    "unit conversions (metric and imperial)": {
      ytId: '',
      title: "Unit Conversions \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-unit-conversions-walkthrough.mp4',
      poster: 'assets/img/unit-conversions-emma-poster.png',
      companionSlug: 'unit-conversions',
      companionLabel: "Unit Conversions (Metric & Imperial)"
    },
    'volume': {
      ytId: 'gWgx6h77U6M',
      title: "Volume of Prisms and Cylinders \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-volume-walkthrough.mp4',
      poster: 'assets/img/volume-emma-poster.png',
      companionSlug: 'volume',
      companionLabel: "Volume of Prisms and Cylinders"
    },
    "volume of prisms and cylinders": {
      ytId: '',
      title: "Volume of Prisms and Cylinders \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Emma",
      localVideo: 'assets/video/emma-volume-walkthrough.mp4',
      poster: 'assets/img/volume-emma-poster.png',
      companionSlug: 'volume',
      companionLabel: "Volume of Prisms and Cylinders"
    },
    'volume-and-surface-area': {
      ytId: 'rYFoR1KywDk',
      title: "Surface Area & 3D Volumes \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-volume-and-surface-area-walkthrough.mp4',
      poster: 'assets/img/volume-and-surface-area-subi-poster.png',
      companionSlug: 'volume-and-surface-area',
      companionLabel: "Surface Area & Advanced 3D Volumes"
    },
    "surface area and advanced 3d volumes": {
      ytId: '',
      title: "Surface Area & 3D Volumes \u2022 Masterclass Walkthrough",
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      tutor: "Tutor Subi",
      localVideo: 'assets/video/subi-volume-and-surface-area-walkthrough.mp4',
      poster: 'assets/img/volume-and-surface-area-subi-poster.png',
      companionSlug: 'volume-and-surface-area',
      companionLabel: "Surface Area & Advanced 3D Volumes"
    },

// Past Paper 10
    'edexcel-maths-l2-past-paper-10-section-a': {
      ytId: 'muSRa0fEsSs',
      title: 'Past Paper 10 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-10-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'past paper 10 • section a: non-calculator': {
      ytId: 'muSRa0fEsSs',
      title: 'Past Paper 10 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-10-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'edexcel-maths-l2-past-paper-10-section-b': {
      ytId: 'b6Ma4VzxG8I',
      title: 'Past Paper 10 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-10-section-a',
      companionLabel: 'Section A: Non-Calculator (13m)'
    },
    'past paper 10 • section b: calculator': {
      ytId: 'b6Ma4VzxG8I',
      title: 'Past Paper 10 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp10',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-10-section-a',
      companionLabel: 'Section A: Non-Calculator (13m)'
    },

    // Past Paper 9
    'edexcel-maths-l2-past-paper-9-section-a': {
      ytId: '61c6xSMBz0I',
      title: 'Past Paper 9 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp9',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-9-section-b',
      companionLabel: 'Section B: Calculator (20m)'
    },
    'past paper 9 • section a: non-calculator': {
      ytId: '61c6xSMBz0I',
      title: 'Past Paper 9 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp9',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-9-section-b',
      companionLabel: 'Section B: Calculator (20m)'
    },
    'edexcel-maths-l2-past-paper-9-section-b': {
      ytId: 'how7uhzmyIQ',
      title: 'Past Paper 9 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp9',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-9-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },
    'past paper 9 • section b: calculator': {
      ytId: 'how7uhzmyIQ',
      title: 'Past Paper 9 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp9',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-9-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },

    // Past Paper 8
    'edexcel-maths-l2-past-paper-8-section-a': {
      ytId: 'nr8dqv5KIkI',
      title: 'Past Paper 8 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp8',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-8-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'past paper 8 • section a: non-calculator': {
      ytId: 'nr8dqv5KIkI',
      title: 'Past Paper 8 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp8',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-8-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'edexcel-maths-l2-past-paper-8-section-b': {
      ytId: 'KbPz2OxJRxc',
      title: 'Past Paper 8 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp8',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-8-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },
    'past paper 8 • section b: calculator': {
      ytId: 'KbPz2OxJRxc',
      title: 'Past Paper 8 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp8',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-8-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },

    // Past Paper 7
    'edexcel-maths-l2-past-paper-7-section-a': {
      ytId: 'bnxoprdRACk',
      title: 'Past Paper 7 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp7',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-7-section-b',
      companionLabel: 'Section B: Calculator (25m)'
    },
    'past paper 7 • section a: non-calculator': {
      ytId: 'bnxoprdRACk',
      title: 'Past Paper 7 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp7',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-7-section-b',
      companionLabel: 'Section B: Calculator (25m)'
    },
    'edexcel-maths-l2-past-paper-7-section-b': {
      ytId: 'IY2EjScrw4Y',
      title: 'Past Paper 7 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp7',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-7-section-a',
      companionLabel: 'Section A: Non-Calculator (12m)'
    },
    'past paper 7 • section b: calculator': {
      ytId: 'IY2EjScrw4Y',
      title: 'Past Paper 7 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp7',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-7-section-a',
      companionLabel: 'Section A: Non-Calculator (12m)'
    },
    // Past Paper 6
    'edexcel-maths-l2-past-paper-6-section-a': {
      ytId: 'TCwy_FiZ1eA',
      title: 'Past Paper 6 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp6',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-6-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'past paper 6 • section a: non-calculator': {
      ytId: 'TCwy_FiZ1eA',
      title: 'Past Paper 6 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp6',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-6-section-b',
      companionLabel: 'Section B: Calculator (22m)'
    },
    'edexcel-maths-l2-past-paper-6-section-b': {
      ytId: 'r4bU8USCWvs',
      title: 'Past Paper 6 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp6',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-6-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },
    'past paper 6 • section b: calculator': {
      ytId: 'r4bU8USCWvs',
      title: 'Past Paper 6 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp6',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-6-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },

    // Past Paper 5
    'edexcel-maths-l2-past-paper-5-section-a': {
      ytId: 'MtTl_qjpdIg',
      title: 'Past Paper 5 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp5',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-5-section-b',
      companionLabel: 'Section B: Calculator (18m)'
    },
    'past paper 5 • section a: non-calculator': {
      ytId: 'MtTl_qjpdIg',
      title: 'Past Paper 5 • Section A: Non-Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp5',
      activeSection: 'A',
      companionSlug: 'edexcel-maths-l2-past-paper-5-section-b',
      companionLabel: 'Section B: Calculator (18m)'
    },
    'edexcel-maths-l2-past-paper-5-section-b': {
      ytId: '5CqunL_1Pcw',
      title: 'Past Paper 5 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp5',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-5-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },
    'past paper 5 • section b: calculator': {
      ytId: '5CqunL_1Pcw',
      title: 'Past Paper 5 • Section B: Calculator (Full Walkthrough)',
      series: 'Pearson Edexcel Functional Skills Maths Level 2',
      paperGroup: 'edexcel-maths-l2-pp5',
      activeSection: 'B',
      companionSlug: 'edexcel-maths-l2-past-paper-5-section-a',
      companionLabel: 'Section A: Non-Calculator (10m)'
    },

    // SLC Task 1 & Task 2 Exemplar Walkthroughs
    'slc-task1-presentation-model': {
      ytId: 'l7VRzidsFno',
      title: 'SLC Task 1 • Presentation Model (Pass Benchmark)',
      series: 'Pearson Edexcel English Level 2 SLC',
      paperGroup: 'edexcel-english-l2-slc',
      activeSection: 'Task 1',
      companionSlug: 'slc-task2-discussion-model',
      companionLabel: 'Task 2: Discussion Model (4m)'
    },
    'slc task 1 • presentation model': {
      ytId: 'l7VRzidsFno',
      title: 'SLC Task 1 • Presentation Model (Pass Benchmark)',
      series: 'Pearson Edexcel English Level 2 SLC',
      paperGroup: 'edexcel-english-l2-slc',
      activeSection: 'Task 1',
      companionSlug: 'slc-task2-discussion-model',
      companionLabel: 'Task 2: Discussion Model (4m)'
    },
    'slc-task2-discussion-model': {
      ytId: 'labg8nxHII0',
      title: 'SLC Task 2 • Group Discussion Model (Pass Benchmark)',
      series: 'Pearson Edexcel English Level 2 SLC',
      paperGroup: 'edexcel-english-l2-slc',
      activeSection: 'Task 2',
      companionSlug: 'slc-task1-presentation-model',
      companionLabel: 'Task 1: Presentation Model (4m)'
    },
    'slc task 2 • discussion model': {
      ytId: 'labg8nxHII0',
      title: 'SLC Task 2 • Group Discussion Model (Pass Benchmark)',
      series: 'Pearson Edexcel English Level 2 SLC',
      paperGroup: 'edexcel-english-l2-slc',
      activeSection: 'Task 2',
      companionSlug: 'slc-task1-presentation-model',
      companionLabel: 'Task 1: Presentation Model (4m)'
    }
  };

  let modalOverlay = null;

  function initModalDom() {
    if (document.getElementById('mfsVideoModalOverlay')) {
      modalOverlay = document.getElementById('mfsVideoModalOverlay');
      return;
    }

    const overlay = document.createElement('div');
    overlay.id = 'mfsVideoModalOverlay';
    overlay.className = 'mfs-video-modal-overlay';
    overlay.setAttribute('role', 'dialog');
    overlay.setAttribute('aria-modal', 'true');
    overlay.setAttribute('aria-label', 'Video Solution Walkthrough');

    overlay.innerHTML = `
      <div class="mfs-video-modal-container" id="mfsModalContainer">
        <!-- Head -->
        <div class="mfs-video-modal-head">
          <div class="mfs-modal-branding">
            <div class="mfs-modal-logo-icon">
              <i class="fa-solid fa-play"></i>
            </div>
            <div class="mfs-modal-title-wrap">
              <span class="mfs-modal-series" id="mfsModalSeries">Pearson Edexcel Functional Skills</span>
              <h3 class="mfs-modal-title" id="mfsModalTitle">Topic Video Solution</h3>
            </div>
          </div>
          <button type="button" class="mfs-modal-close-btn" id="mfsModalCloseBtn" aria-label="Close modal">
            <i class="fa-solid fa-xmark"></i>
          </button>
        </div>

        <!-- Body -->
        <div class="mfs-video-modal-body">
          <div id="mfsModalSectionSwitcher" style="display:none; gap:10px; margin-bottom:12px; flex-wrap:wrap;"></div>
          <!-- Video Player Box -->
          <div class="mfs-player-ratio-box" id="mfsPlayerBox">
            <!-- Dynamic Content Injected Here -->
          </div>

          <!-- Metadata & Action Bar -->
          <div class="mfs-modal-meta-bar">
            <div class="mfs-meta-tutor-badge">
              <div class="mfs-tutor-avatar"><i class="fa-solid fa-graduation-cap"></i></div>
              <div class="mfs-tutor-details">
                <span class="mfs-tutor-name" id="mfsModalTutor">Your Functional Skills Tutor</span>
                <span class="mfs-tutor-role">Pearson Functional Skills Specialist</span>
              </div>
            </div>

            <div class="mfs-modal-actions">
              <a href="#" target="_blank" rel="noopener" class="btn-modal-sheet" id="mfsModalSheetBtn">
                <i class="fa-regular fa-file-pdf"></i> Question Worksheet
              </a>
              <a href="#" target="_blank" rel="noopener" class="btn-modal-answers" id="mfsModalAnswersBtn">
                <i class="fa-solid fa-circle-check"></i> Worked Answers [M1/A1]
              </a>
              <a href="https://www.youtube.com/@MasterFunctionalSkills" target="_blank" rel="noopener" class="btn-modal-yt" id="mfsModalYtBtn">
                <i class="fa-brands fa-youtube"></i> Watch on YouTube App
              </a>
            </div>
          </div>

          <!-- Features Cards -->
          <div class="mfs-modal-features-row">
            <div class="mfs-modal-feat-card">
              <i class="fa-solid fa-bullseye" style="color:#38bdf8;"></i>
              <div>
                <span class="mfs-feat-title">Method Marks (M1/A1)</span>
                <span class="mfs-feat-desc">Pearson mark criteria breakdown for every working step.</span>
              </div>
            </div>
            <div class="mfs-modal-feat-card">
              <i class="fa-solid fa-triangle-exclamation" style="color:#f59e0b;"></i>
              <div>
                <span class="mfs-feat-title">Examiner Trap Alerts</span>
                <span class="mfs-feat-desc">Identifies subtle exam traps and placeholder errors.</span>
              </div>
            </div>
            <div class="mfs-modal-feat-card">
              <i class="fa-solid fa-rotate-left" style="color:#10b981;"></i>
              <div>
                <span class="mfs-feat-title">Reverse Sanity Checks</span>
                <span class="mfs-feat-desc">Proofing checks to verify answers before moving on.</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);
    modalOverlay = overlay;

    // Attach Close Listeners
    document.getElementById('mfsModalCloseBtn').addEventListener('click', closeModal);
    overlay.addEventListener('click', function (e) {
      if (e.target === overlay) {
        closeModal();
      }
    });

    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && modalOverlay && modalOverlay.classList.contains('active')) {
        closeModal();
      }
    });
  }

  function openModal(options) {
    initModalDom();

    const topic = options.topic || 'Video Solution Walkthrough';
    const series = options.series || 'Pearson Edexcel Functional Skills';
    const tutor = options.tutor || 'Subi';
    const sheetUrl = options.sheetUrl || '#';
    const answersUrl = options.answersUrl || '#';
    
    // Detect YouTube ID from options or known dictionary
    let ytId = options.ytId || '';
    if (!ytId && options.videoSrc) {
      const m = options.videoSrc.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/))([a-zA-Z0-9_-]{11})/);
      if (m) ytId = m[1];
    }

    const normTopic = topic.trim().toLowerCase();
    const knownItem = KNOWN_VIDEOS[normTopic] || (options.slug && KNOWN_VIDEOS[options.slug]);
    if (!ytId && knownItem && knownItem.ytId) {
      ytId = knownItem.ytId;
    }

    // Set Header
    document.getElementById('mfsModalTitle').textContent = topic;
    document.getElementById('mfsModalSeries').textContent = series;
    document.getElementById('mfsModalTutor').textContent = tutor;

    // Section Switcher for Multi-Section Past Papers
    const switcherEl = document.getElementById('mfsModalSectionSwitcher');
    if (switcherEl) {
      if (knownItem && knownItem.companionSlug && KNOWN_VIDEOS[knownItem.companionSlug]) {
        const companion = KNOWN_VIDEOS[knownItem.companionSlug];
        const isSecB = knownItem.activeSection === 'B';
        const secA = isSecB ? companion : knownItem;
        const secB = isSecB ? knownItem : companion;
        switcherEl.style.display = 'flex';
        switcherEl.innerHTML = `
          <button type="button" id="mfsSwitchSecA" style="cursor:pointer; padding:8px 14px; border-radius:8px; font-weight:800; font-size:0.86rem; display:inline-flex; align-items:center; gap:6px; border:1.5px solid ${!isSecB ? '#3b82f6' : '#334155'}; background:${!isSecB ? '#2563eb' : '#1e293b'}; color:#ffffff;">
            <i class="fa-solid fa-circle-play"></i> Section A: Non-Calculator
          </button>
          <button type="button" id="mfsSwitchSecB" style="cursor:pointer; padding:8px 14px; border-radius:8px; font-weight:800; font-size:0.86rem; display:inline-flex; align-items:center; gap:6px; border:1.5px solid ${isSecB ? '#3b82f6' : '#334155'}; background:${isSecB ? '#2563eb' : '#1e293b'}; color:#ffffff;">
            <i class="fa-solid fa-calculator"></i> Section B: Calculator
          </button>
        `;
        document.getElementById('mfsSwitchSecA').onclick = function () {
          openModal({
            topic: secA.title,
            series: secA.series,
            tutor: tutor,
            sheetUrl: sheetUrl,
            answersUrl: answersUrl,
            ytId: secA.ytId,
            slug: secA.companionSlug ? secA.companionSlug : undefined
          });
        };
        document.getElementById('mfsSwitchSecB').onclick = function () {
          openModal({
            topic: secB.title,
            series: secB.series,
            tutor: tutor,
            sheetUrl: sheetUrl,
            answersUrl: answersUrl,
            ytId: secB.ytId,
            slug: secB.companionSlug ? secB.companionSlug : undefined
          });
        };
      } else {
        switcherEl.style.display = 'none';
        switcherEl.innerHTML = '';
      }
    }

    // Set Action Links
    const sheetBtn = document.getElementById('mfsModalSheetBtn');
    const answersBtn = document.getElementById('mfsModalAnswersBtn');
    const ytBtn = document.getElementById('mfsModalYtBtn');
    
    if (sheetUrl && sheetUrl !== '#') {
      sheetBtn.href = sheetUrl;
      sheetBtn.style.display = 'inline-flex';
    } else {
      sheetBtn.style.display = 'none';
    }

    if (answersUrl && answersUrl !== '#') {
      answersBtn.href = answersUrl;
      answersBtn.style.display = 'inline-flex';
    } else {
      answersBtn.style.display = 'none';
    }

    if (ytBtn) {
      if (ytId) {
        ytBtn.href = `https://youtu.be/${ytId}`;
        ytBtn.innerHTML = '<i class="fa-brands fa-youtube"></i> Watch on YouTube App';
      } else {
        ytBtn.href = 'https://www.youtube.com/@MasterFunctionalSkills';
        ytBtn.innerHTML = '<i class="fa-brands fa-youtube"></i> Visit MFS YouTube Channel';
      }
    }

    // Set Player Box
    const playerBox = document.getElementById('mfsPlayerBox');
    playerBox.innerHTML = '';

    if (ytId) {
      // Clean YouTube Embed (Never crashes mobile browsers with MIME type error)
      playerBox.innerHTML = `
        <iframe style="width:100%; height:100%; border:0; display:block;" src="https://www.youtube-nocookie.com/embed/${ytId}?autoplay=1&rel=0&playsinline=1" title="${escapeHtml(topic)}" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>
      `;
    } else {
      // In Production State / Channel Fallback
      playerBox.innerHTML = `
        <div class="mfs-video-placeholder-card">
          <div class="mfs-placeholder-icon-wrap" style="color:#ef4444; border-color:#ef4444; background:rgba(239,68,68,0.15);">
            <i class="fa-brands fa-youtube"></i>
          </div>
          <span class="mfs-placeholder-badge">
            <i class="fa-solid fa-circle-play"></i> Video Walkthrough on Master Functional Skills
          </span>
          <h4 class="mfs-placeholder-heading">${escapeHtml(topic)}</h4>
          <p class="mfs-placeholder-text">
            Watch our step-by-step video solutions with Pearson Edexcel method marks [M1/A1], examiner trap alerts, and reverse sanity checks directly on our YouTube channel.
          </p>
          <div style="display:flex; gap:12px; flex-wrap:wrap; justify-content:center; margin-top:8px;">
            <a href="https://www.youtube.com/@MasterFunctionalSkills" target="_blank" rel="noopener" class="btn-modal-yt" style="padding:10px 18px; font-size:0.92rem; background:#dc2626; color:#fff; border-radius:8px; text-decoration:none; font-weight:700; display:inline-flex; align-items:center; gap:8px;">
              <i class="fa-brands fa-youtube"></i> Open YouTube Channel
            </a>
            ${answersUrl && answersUrl !== '#' ? `<a href="${answersUrl}" target="_blank" rel="noopener" class="btn-modal-answers" style="padding:10px 18px; font-size:0.92rem;"><i class="fa-solid fa-circle-check"></i> Open Step-by-Step Worked Answers</a>` : ''}
            ${sheetUrl && sheetUrl !== '#' ? `<a href="${sheetUrl}" target="_blank" rel="noopener" class="btn-modal-sheet" style="padding:10px 18px; font-size:0.92rem;"><i class="fa-regular fa-file-pdf"></i> Open Question Worksheet</a>` : ''}
          </div>
        </div>
      `;
    }

    // Show Overlay
    modalOverlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    if (!modalOverlay) return;

    // Immediately stop iframe video/audio
    const playerBox = document.getElementById('mfsPlayerBox');
    if (playerBox) {
      playerBox.innerHTML = '';
    }

    modalOverlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  function escapeHtml(str) {
    return (str || '').replace(/[&<>"']/g, function (m) {
      return {
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        '"': '&quot;',
        "'": '&#39;'
      }[m];
    });
  }

  // Intercept all video buttons on page load
  function bindVideoButtons() {
    initModalDom();

    const videoButtons = document.querySelectorAll('.btn-mfs-video, .open-video-modal, .btn-paper-video');
    videoButtons.forEach(btn => {
      // Prevent double binding
      if (btn.getAttribute('data-mfs-video-bound') === 'true') return;
      btn.setAttribute('data-mfs-video-bound', 'true');

      btn.addEventListener('click', function (e) {
        const href = this.getAttribute('href') || '';
        // If link is a placeholder, do not open modal or navigate
        if (!href || href === '#' || href.startsWith('javascript:')) {
          e.preventDefault();
          return;
        }

        // If link points to video-solution.html, let browser navigate directly to the dedicated video app
        if (href.indexOf('video-solution.html') !== -1) {
          return;
        }

        // Check if link is an external non-YouTube URL
        if (/^https?:\/\//i.test(href) && !/(?:youtu\.be|youtube\.com)/i.test(href)) {
          return;
        }

        e.preventDefault();

        // Extract topic metadata from attributes or DOM context
        let topic = this.getAttribute('data-topic');
        let sheetUrl = this.getAttribute('data-sheet');
        let answersUrl = this.getAttribute('data-answers');
        let ytId = this.getAttribute('data-yt-id') || '';
        let series = this.getAttribute('data-series') || 'Pearson Edexcel Functional Skills';

        if (!ytId && href) {
          const m = href.match(/(?:youtu\.be\/|youtube\.com\/(?:watch\?v=|embed\/))([a-zA-Z0-9_-]{11})/);
          if (m) ytId = m[1];
        }

        // Auto-detect topic from parent row if missing
        if (!topic) {
          const row = this.closest('.topic-row, .past-paper-row, .revision-topic-card');
          if (row) {
            const titleEl = row.querySelector('.topic-title, .past-paper-title, h3, h4');
            if (titleEl) {
              topic = titleEl.textContent.trim();
            }
            if (!sheetUrl) {
              const sheetEl = row.querySelector('.btn-mfs-sheet, .btn-paper-qp');
              if (sheetEl) sheetUrl = sheetEl.getAttribute('href');
            }
            if (!answersUrl) {
              const answersEl = row.querySelector('a[href*="-answers.html"], .btn-paper-ms, .btn-paper-model');
              if (answersEl) answersUrl = answersEl.getAttribute('href');
            }
          }
        }

        openModal({
          topic: topic || 'Video Solution Walkthrough',
          sheetUrl: sheetUrl,
          answersUrl: answersUrl,
          ytId: ytId,
          series: series,
          tutor: 'Subi'
        });
      });
    });
  }

  // Expose global API
  window.MfsVideoModal = {
    open: openModal,
    close: closeModal,
    registerVideo: function (topicSlug, details) {
      KNOWN_VIDEOS[topicSlug.trim().toLowerCase()] = details;
    }
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bindVideoButtons);
  } else {
    bindVideoButtons();
  }
})();
