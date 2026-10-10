import os
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
}

def uinput(cmsg='DQM $> '):
    raw = input(cmsg).strip().lower()
    if not raw:
        return ''
    clean_chars = [char for char in raw if char not in "?!.,;:"]
    cleaned = ''.join(clean_chars)
    words = cleaned.split()
    expanded_words = [ALIASES.get(word, word) for word in words]
    normalized_query = ' '.join(expanded_words)
    for punct in string.punctuation:
        normalized_query = normalized_query.replace(punct, '')
        return normalized_query.strip()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')