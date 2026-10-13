import os
import json
import random

ENGINE_VERSION = "2.1.0"

def parse_version(ver_str):
    try:
        clean = ver_str.replace(">=", "").replace("<=", "").replace(">", "").replace("<", "").replace("v", "").strip()
        return tuple(map(int, clean.split(".")))
    except Exception:
        return (0, 0, 0)

def is_compatible(engine_ver, required_ver_rule):
    if not required_ver_rule or required_ver_rule == "*":
        return True
    eng_tuple = parse_version(engine_ver)
    req_tuple = parse_version(required_ver_rule)

    if ">=" in required_ver_rule:
        return eng_tuple >= req_tuple
    elif "<=" in required_ver_rule:
        return eng_tuple <= req_tuple
    elif ">" in required_ver_rule:
        return eng_tuple > req_tuple
    elif "<" in required_ver_rule:
        return eng_tuple < req_tuple
    else:
        return eng_tuple == req_tuple

def list_brains(brains_dir="brains"):
    if not os.path.exists(brains_dir):
        os.makedirs(brains_dir)
        return []
    return [f for f in os.listdir(brains_dir) if f.endswith(".tqm")]

def load_brains(filepath):
    try:
        with open(filepath, "r", encoding="utf8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found!")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to parse '{filepath}'! Check JSON formatting.")
        return None

    if "routes" not in data or not isinstance(data["routes"], dict):
        print(f"Error: Brain '{filepath}' is missing a valid 'routes' dictionary.")
        return None

    compat_rule = data.get("compatibility", "")
    if not is_compatible(ENGINE_VERSION, compat_rule):
        print(f"\n[WARNING] Brain '{data.get('brain_id')}' requires engine {compat_rule}.")
        print(f"Current engine version is v{ENGINE_VERSION}. Route traversal might fail.\n")

    brain_licence = data.get("licence", "")
    if brain_licence != "CC-BY-NC-SA-4.0":
        print(f"[Notice] Brain '{data.get('brain_id')}' uses licence '{brain_licence}'. Expected 'CC-BY-NC-SA-4.0'")

    return data

def init_brain(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        data = json.load(f)
    return data

def traverse(routes, prompt):
    words = prompt.split()
    if not words:
        return ""
    current = routes
    for word in words:
        if isinstance(current, dict) and word in current:
            current = current[word]
        else:
            return "Path not found."
    if isinstance(current, list):
        return random.choice(current)
    elif isinstance(current, str):
        return current
    else:
        return "Incomplete query. Give me more details."