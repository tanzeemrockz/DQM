import json
import random

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