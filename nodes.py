import os
import re
import string

ALIASES = {
    "who's": "who is",
    "whos": "who is",
    "what's": "what is",
    "whats": "what is",
    "how's": "how is",
    "hows": "how is",
    "where's": "where is",
    "wheres": "where is",
    "why's": "why is",
    "whys": "why is",
    "heyya": "hey",
    "heya": "hey",
    "hiya": "hi",
    "sup": "what is up",
    "wassup": "what is up"
}

def collapse_elongated(word):
    collapsed = re.sub(r'(.)\1{2,}', r'\1', word)
    if collapsed.startswith("hi") and set(collapsed) == {"h", "i"}:
        return "hi"
    if collapsed.startswith("yo") and set(collapsed) == {"y", "o"}:
        return "yo"
    return collapsed

def uinput(cmsg='DQM $> '):
    raw = input(cmsg).strip().lower()
    if not raw:
        return ""

    for sep in ["-", "/", "\\"]:
        raw = raw.replace(sep, " ")

    clean_chars = [char for char in raw if char not in "?!.,;:"]
    cleaned = "".join(clean_chars)
    words = cleaned.split()
    processed_words = []
    for word in words:
        squashed = collapse_elongated(word)
        aliased = ALIASES.get(squashed, squashed)
        processed_words.append(aliased)

    normalized_query = " ".join(processed_words)
    for punct in string.punctuation:
        normalized_query = normalized_query.replace(punct, "")

    return normalized_query.strip()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')