import os, sys, re, ast, json

PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def generate_maths_content():
    print("Generating Maths Suite Content...")
    
    # 1. Parse L2 Core Guide
    l2_core_path = os.path.join(PROJECT_DIR, "generate_maths_l2_core_guide.py")
    with open(l2_core_path, "r", encoding="utf-8") as f:
        l2_core_txt = f.read()

    calls_l2 = re.findall(r'practice_page\(\s*\"([^\"]+)\",\s*\"([^\"]+)\",\s*(\d+),\s*([a-zA-Z0-9_]+),\s*\"([^\"]+)\",\s*\"([^\"]+)\",\s*\"([^\"]+)\"', l2_core_txt)
    
    topic_l2_questions = {}
    for i, (title, std, page, scaf, q1, q2, q3) in enumerate(calls_l2, 1):
        topic_l2_questions[i] = [
            {"q": f"<b>Question 1 (Foundation):</b> {q1}", "marks": 2},
            {"q": f"<b>Question 2 (Workplace Problem):</b> {q2}", "marks": 3, "weight": 1.2},
            {"q": f"<b>Question 3 (Exam Challenge):</b> {q3}", "marks": 4, "weight": 1.4}
        ]

    tree_l2 = ast.parse(l2_core_txt)
    chk_dict_l2 = {}
    mock_dict_l2 = {}
    for node in ast.walk(tree_l2):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if target.id.startswith('chk'):
                        chk_dict_l2[target.id] = ast.literal_eval(node.value)
                    elif target.id.startswith('mock_p'):
                        mock_dict_l2[target.id] = ast.literal_eval(node.value)

    checkpoint_l2_questions = {}
    # 3 checkpoints x 4 pages
    chk_map = [
        [("chk1_p1", 1), ("chk1_p2", 4), ("chk1_p3", 7), ("chk1_p4", 10)],
        [("chk2_p1", 1), ("chk2_p2", 4), ("chk2_p3", 7), ("chk2_p4", 10)],
        [("chk3_p1", 1), ("chk3_p2", 4), ("chk3_p3", 7), ("chk3_p4", 10)]
    ]
    for c_idx in range(3):
        for cp_p in range(4):
            var_name, start_q = chk_map[c_idx][cp_p]
            raw_items = chk_dict_l2.get(var_name, [])
            q_list = []
            for item in raw_items:
                q_num, marks, q_text = item[0], item[1], item[2]
                q_list.append({"q": f"<b>Question {q_num}:</b> {q_text}", "marks": marks, "weight": 1.2 if marks >= 3 else 1.0})
            checkpoint_l2_questions[(c_idx, cp_p)] = q_list

    # Mock 1 from L2 Core Guide (mock_p73 to mock_p78)
    # Sec A: mock_p73 (3q), mock_p74 (3q) -> 3 pages x 2q
    sec_a_all = []
    for item in mock_dict_l2.get("mock_p73", []):
        sec_a_all.append({"q": f"<b>Question {item[0]}:</b> {item[2]}", "marks": item[1], "weight": 1.2 if item[1]>=3 else 1.0})
    for item in mock_dict_l2.get("mock_p74", []):
        sec_a_all.append({"q": f"<b>Question {item[0]}:</b> {item[2]}", "marks": item[1], "weight": 1.2 if item[1]>=3 else 1.0})

    mock1_sec_a = [
        sec_a_all[0:2],
        sec_a_all[2:4],
        sec_a_all[4:6]
    ]

    sec_b_all = []
    for p_var in ["mock_p75", "mock_p76", "mock_p77", "mock_p78"]:
        for item in mock_dict_l2.get(p_var, []):
            sec_b_all.append({"q": f"<b>Question {item[0]}:</b> {item[2]}", "marks": item[1], "weight": 1.3 if item[1]>=4 else 1.0})
    
    mock1_sec_b = [
        sec_b_all[0:2],
        sec_b_all[2:4],
        sec_b_all[4:6],
        sec_b_all[6:8],
        sec_b_all[8:10]
    ]

    # Mock 2 from build_mock_maths_l2.py (Paper 2: Logistics & Fleet)
    mock_maths_path = os.path.join(PROJECT_DIR, "books", "publish", "build_mock_maths_l2.py")
    with open(mock_maths_path, "r", encoding="utf-8") as f:
        mock_maths_txt = f.read()

    tree_mock = ast.parse(mock_maths_txt)
    papers_data = []
    for node in ast.walk(tree_mock):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "papers_data":
                    papers_data = ast.literal_eval(node.value)

    p2 = papers_data[1] # Paper 2
    p3 = papers_data[2] # Paper 3
    p2_sec_a = []
    for item in p2[1]: # 4 questions
        m_val = int(re.search(r'\d+', item[1]).group(0)) if re.search(r'\d+', item[1]) else 4
        p2_sec_a.append({"q": f"<b>{item[0]}:</b> {item[2]}", "marks": m_val, "weight": 1.2})
    for item in p3[1][:2]: # 2 questions from Paper 3
        m_val = int(re.search(r'\d+', item[1]).group(0)) if re.search(r'\d+', item[1]) else 4
        p2_sec_a.append({"q": f"<b>{item[0]}:</b> {item[2]}", "marks": m_val, "weight": 1.2})

    mock2_sec_a = [
        p2_sec_a[0:2],
        p2_sec_a[2:4],
        p2_sec_a[4:6]
    ]

    p2_sec_b = []
    for item in p2[2]: # 10 questions
        m_val = int(re.search(r'\d+', item[1]).group(0)) if re.search(r'\d+', item[1]) else 5
        p2_sec_b.append({"q": f"<b>{item[0]}:</b> {item[2]}", "marks": m_val, "weight": 1.3})

    mock2_sec_b = [
        p2_sec_b[0:2],
        p2_sec_b[2:4],
        p2_sec_b[4:6],
        p2_sec_b[6:8],
        p2_sec_b[8:10]
    ]

    mock_maths_l2_data = [
        {"sec_a": mock1_sec_a, "sec_b": mock1_sec_b},
        {"sec_a": mock2_sec_a, "sec_b": mock2_sec_b}
    ]

    # Parse L2 Workbook drills (generate_maths_l2_companion_workbook.py)
    l2_wb_path = os.path.join(PROJECT_DIR, "generate_maths_l2_companion_workbook.py")
    with open(l2_wb_path, "r", encoding="utf-8") as f:
        l2_wb_txt = f.read()

    wb_matches = re.findall(r'<div class=\"q-card\">\s*<div class=\"q-header\"><span class=\"q-num\">(.*?)</span><span class=\"q-marks\">(.*?)</span></div>\s*<p>(.*?)</p>', l2_wb_txt, re.DOTALL)
    workbook_l2_drills = {}
    for d_idx in range(34):
        idx1 = d_idx * 3
        idx2 = d_idx * 3 + 1
        idx3 = d_idx * 3 + 2
        
        # Take task 2 (context) and task 3 (exam challenge) or task 1 & task 2
        m1 = wb_matches[idx1 % len(wb_matches)]
        m2 = wb_matches[idx2 % len(wb_matches)]
        
        num1 = m1[0].strip()
        num2 = m2[0].strip()
        q1_text = m1[2].strip().replace("\n", " ")
        q2_text = m2[2].strip().replace("\n", " ")
        
        m_val1 = int(re.search(r'\d+', m1[1]).group(0)) if re.search(r'\d+', m1[1]) else 3
        m_val2 = int(re.search(r'\d+', m2[1]).group(0)) if re.search(r'\d+', m2[1]) else 4

        workbook_l2_drills[d_idx + 1] = [
            {"q": f"<b>{num1}:</b> {q1_text}", "marks": m_val1, "weight": 1.0},
            {"q": f"<b>{num2}:</b> {q2_text}", "marks": m_val2, "weight": 1.3}
        ]

    # 2. Parse L1 Core Guide
    l1_core_path = os.path.join(PROJECT_DIR, "generate_maths_l1_core_guide.py")
    with open(l1_core_path, "r", encoding="utf-8") as f:
        l1_core_txt = f.read()

    calls_l1 = re.findall(r'practice_page\(\s*\"([^\"]+)\",\s*\"([^\"]+)\",\s*(\d+),\s*([a-zA-Z0-9_]+),\s*\"([^\"]+)\",\s*\"([^\"]+)\",\s*\"([^\"]+)\"', l1_core_txt)
    topic_l1_questions = {}
    for i, (title, std, page, scaf, q1, q2, q3) in enumerate(calls_l1, 1):
        topic_l1_questions[i] = [
            {"q": f"<b>Question 1 (Foundation):</b> {q1}", "marks": 2},
            {"q": f"<b>Question 2 (Workplace Problem):</b> {q2}", "marks": 3, "weight": 1.2},
            {"q": f"<b>Question 3 (Exam Challenge):</b> {q3}", "marks": 4, "weight": 1.4}
        ]

    tree_l1 = ast.parse(l1_core_txt)
    chk_dict_l1 = {}
    mock_dict_l1 = {}
    for node in ast.walk(tree_l1):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if target.id.startswith('chk'):
                        chk_dict_l1[target.id] = ast.literal_eval(node.value)
                    elif target.id.startswith('mock_p'):
                        mock_dict_l1[target.id] = ast.literal_eval(node.value)

    checkpoint_l1_questions = {}
    for c_idx in range(3):
        for cp_p in range(4):
            var_name, start_q = chk_map[c_idx][cp_p]
            raw_items = chk_dict_l1.get(var_name, [])
            q_list = []
            for item in raw_items:
                q_num, marks, q_text = item[0], item[1], item[2]
                q_list.append({"q": f"<b>Question {q_num}:</b> {q_text}", "marks": marks, "weight": 1.2 if marks >= 3 else 1.0})
            checkpoint_l1_questions[(c_idx, cp_p)] = q_list

    # L1 Mocks
    sec_a_l1_all = []
    for item in mock_dict_l1.get("mock_p73", []):
        sec_a_l1_all.append({"q": f"<b>Question {item[0]}:</b> {item[2]}", "marks": item[1], "weight": 1.0})
    for item in mock_dict_l1.get("mock_p74", []):
        sec_a_l1_all.append({"q": f"<b>Question {item[0]}:</b> {item[2]}", "marks": item[1], "weight": 1.0})

    mock1_l1_sec_a = [
        sec_a_l1_all[0:2],
        sec_a_l1_all[2:4],
        sec_a_l1_all[4:6]
    ]

    sec_b_l1_all = []
    for p_var in ["mock_p75", "mock_p76", "mock_p77", "mock_p78"]:
        for item in mock_dict_l1.get(p_var, []):
            sec_b_l1_all.append({"q": f"<b>Question {item[0]}:</b> {item[2]}", "marks": item[1], "weight": 1.2 if item[1]>=4 else 1.0})

    mock1_l1_sec_b = [
        sec_b_l1_all[0:2],
        sec_b_l1_all[2:4],
        sec_b_l1_all[4:6],
        sec_b_l1_all[6:8],
        sec_b_l1_all[8:10]
    ]

    mock_maths_l1_data = [
        {"sec_a": mock1_l1_sec_a, "sec_b": mock1_l1_sec_b},
        {"sec_a": mock1_l1_sec_a, "sec_b": mock1_l1_sec_b} # secondary mock copy / variants
    ]

    # Parse L1 Workbook drills
    l1_wb_path = os.path.join(PROJECT_DIR, "generate_maths_l1_companion_workbook.py")
    with open(l1_wb_path, "r", encoding="utf-8") as f:
        l1_wb_txt = f.read()

    wb1_matches = re.findall(r'<div class=\"q-card\">\s*<div class=\"q-header\"><span class=\"q-num\">(.*?)</span><span class=\"q-marks\">(.*?)</span></div>\s*<p>(.*?)</p>', l1_wb_txt, re.DOTALL)
    workbook_l1_drills = {}
    for d_idx in range(34):
        idx1 = d_idx * 3
        idx2 = d_idx * 3 + 1
        m1 = wb1_matches[idx1 % len(wb1_matches)]
        m2 = wb1_matches[idx2 % len(wb1_matches)]
        num1 = m1[0].strip()
        num2 = m2[0].strip()
        q1_text = m1[2].strip().replace("\n", " ")
        q2_text = m2[2].strip().replace("\n", " ")
        m_val1 = int(re.search(r'\d+', m1[1]).group(0)) if re.search(r'\d+', m1[1]) else 2
        m_val2 = int(re.search(r'\d+', m2[1]).group(0)) if re.search(r'\d+', m2[1]) else 3
        workbook_l1_drills[d_idx + 1] = [
            {"q": f"<b>{num1}:</b> {q1_text}", "marks": m_val1, "weight": 1.0},
            {"q": f"<b>{num2}:</b> {q2_text}", "marks": m_val2, "weight": 1.2}
        ]

    # 3. Parse E3 Core Guide
    e3_core_path = os.path.join(PROJECT_DIR, "generate_maths_e3_core_guide.py")
    with open(e3_core_path, "r", encoding="utf-8") as f:
        e3_core_txt = f.read()

    calls_e3 = re.findall(r'practice_page\(\s*\"([^\"]+)\",\s*\"([^\"]+)\",\s*(\d+),\s*([a-zA-Z0-9_]+),\s*\"([^\"]+)\",\s*\"([^\"]+)\",\s*\"([^\"]+)\"', e3_core_txt)
    topic_e3_questions = {}
    for i, (title, std, page, scaf, q1, q2, q3) in enumerate(calls_e3, 1):
        topic_e3_questions[i] = [
            {"q": f"<b>Task 1 (Visual Model):</b> {q1}", "marks": 2},
            {"q": f"<b>Task 2 (Practical Application):</b> {q2}", "marks": 2, "weight": 1.1},
            {"q": f"<b>Task 3 (Workplace Problem):</b> {q3}", "marks": 3, "weight": 1.3}
        ]

    tree_e3 = ast.parse(e3_core_txt)
    chk_dict_e3 = {}
    mock_dict_e3 = {}
    for node in ast.walk(tree_e3):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if target.id.startswith('chk'):
                        chk_dict_e3[target.id] = ast.literal_eval(node.value)
                    elif target.id.startswith('mock_p'):
                        mock_dict_e3[target.id] = ast.literal_eval(node.value)

    checkpoint_e3_questions = {}
    for c_idx in range(3):
        for cp_p in range(4):
            var_name, start_q = chk_map[c_idx][cp_p]
            raw_items = chk_dict_e3.get(var_name, [])
            q_list = []
            for item in raw_items:
                q_num, marks, q_text = item[0], item[1], item[2]
                q_list.append({"q": f"<b>Question {q_num}:</b> {q_text}", "marks": marks, "weight": 1.0})
            checkpoint_e3_questions[(c_idx, cp_p)] = q_list

    # E3 Mocks
    sec_a_e3_all = []
    for item in mock_dict_e3.get("mock_p73", []):
        sec_a_e3_all.append({"q": f"<b>Question {item[0]}:</b> {item[2]}", "marks": item[1], "weight": 1.0})
    for item in mock_dict_e3.get("mock_p74", []):
        sec_a_e3_all.append({"q": f"<b>Question {item[0]}:</b> {item[2]}", "marks": item[1], "weight": 1.0})

    mock1_e3_sec_a = [
        sec_a_e3_all[0:2],
        sec_a_e3_all[2:4],
        sec_a_e3_all[4:6]
    ]

    sec_b_e3_all = []
    for p_var in ["mock_p75", "mock_p76", "mock_p77", "mock_p78"]:
        for item in mock_dict_e3.get(p_var, []):
            sec_b_e3_all.append({"q": f"<b>Question {item[0]}:</b> {item[2]}", "marks": item[1], "weight": 1.1})

    mock1_e3_sec_b = [
        sec_b_e3_all[0:2],
        sec_b_e3_all[2:4],
        sec_b_e3_all[4:6],
        sec_b_e3_all[6:8],
        sec_b_e3_all[8:10]
    ]

    mock_maths_e3_data = [
        {"sec_a": mock1_e3_sec_a, "sec_b": mock1_e3_sec_b},
        {"sec_a": mock1_e3_sec_a, "sec_b": mock1_e3_sec_b}
    ]

    out_file = os.path.join(PROJECT_DIR, "books", "a4", "maths_suite_content.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write("# -*- coding: utf-8 -*-\n")
        f.write('"""\nMaths Suite Real Question Bank & Data Module.\n')
        f.write('Contains authentic Pearson Edexcel questions for L2, L1, and Entry 3.\n"""\n\n')
        f.write(f"TOPIC_L2_QUESTIONS = {repr(topic_l2_questions)}\n\n")
        f.write(f"CHECKPOINT_L2_QUESTIONS = {repr(checkpoint_l2_questions)}\n\n")
        f.write(f"MOCK_MATHS_L2_DATA = {repr(mock_maths_l2_data)}\n\n")
        f.write(f"WORKBOOK_L2_DRILLS = {repr(workbook_l2_drills)}\n\n")
        f.write(f"TOPIC_L1_QUESTIONS = {repr(topic_l1_questions)}\n\n")
        f.write(f"CHECKPOINT_L1_QUESTIONS = {repr(checkpoint_l1_questions)}\n\n")
        f.write(f"MOCK_MATHS_L1_DATA = {repr(mock_maths_l1_data)}\n\n")
        f.write(f"WORKBOOK_L1_DRILLS = {repr(workbook_l1_drills)}\n\n")
        f.write(f"TOPIC_E3_QUESTIONS = {repr(topic_e3_questions)}\n\n")
        f.write(f"CHECKPOINT_E3_QUESTIONS = {repr(checkpoint_e3_questions)}\n\n")
        f.write(f"MOCK_MATHS_E3_DATA = {repr(mock_maths_e3_data)}\n\n")

    print(f"Generated {out_file} successfully! Size: {os.path.getsize(out_file)} bytes")

if __name__ == "__main__":
    generate_maths_content()
