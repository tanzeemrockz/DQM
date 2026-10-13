import os
import re
import string

ALIASES = {
    # --- Interrogatives & Contractions ---
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
    "when's": "when is",
    "whens": "when is",
    "which's": "which is",
    "whichs": "which is",
    "that's": "that is",
    "thats": "that is",
    "it's": "it is",
    "its": "it is",
    "there's": "there is",
    "theres": "there is",
    "here's": "here is",
    "heres": "here is",

    # --- Verb Contractions & Negations ---
    "can't": "cannot",
    "cant": "cannot",
    "won't": "will not",
    "wont": "will not",
    "don't": "do not",
    "dont": "do not",
    "doesn't": "does not",
    "doesnt": "does not",
    "didn't": "did not",
    "didnt": "did not",
    "isn't": "is not",
    "isnt": "is not",
    "aren't": "are not",
    "arent": "are not",
    "wasn't": "was not",
    "wasnt": "was not",
    "weren't": "were not",
    "werent": "were not",

    # --- Pronoun Contractions ---
    "i'm": "i am",
    "im": "i am",
    "you're": "you are",
    "youre": "you are",
    "we're": "we are",
    "they're": "they are",
    "theyre": "they are",
    "i've": "i have",
    "ive": "i have",
    "you've": "you have",
    "youve": "you have",
    "we've": "we have",
    "weve": "we have",
    "i'll": "i will",
    "ill": "i will",
    "you'll": "you will",
    "youll": "you will",

    # --- Informal Greetings & Openers ---
    "heyya": "hey",
    "heya": "hey",
    "hiya": "hi",
    "yo": "hi",
    "howdy": "hello",
    "greetings": "hello",
    "salutations": "hello",
    "sup": "what is up",
    "wassup": "what is up",
    "wazzup": "what is up",
    "waddup": "what is up",

    # --- Chat Slang & Conversational Fillers ---
    "wbu": "what about you",
    "hbu": "how about you",
    "idk": "i do not know",
    "tbh": "to be honest",
    "btw": "by the way",
    "fr": "for real",
    "pls": "please",
    "plz": "please",
    "bc": "because",
    "cuz": "because",

    # --- Gratitude & Partings ---
    "thx": "thanks",
    "thnx": "thanks",
    "thanx": "thanks",
    "ty": "thank you",
    "tysm": "thank you",
    "cya": "goodbye",
    "bye": "goodbye",
    "byebye": "goodbye",
    "peace": "goodbye",
    "gn": "good night",
    "gm": "good morning",

    # --- Intent Shortcuts ---
    "meaning": "define",
    "definition": "define",
    "loc": "where is",
    "location": "where is",
    "diff": "difference",
    "calc": "convert"
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