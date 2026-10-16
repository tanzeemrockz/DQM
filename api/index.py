import json
import random
import re
import string
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from engine import ENGINE_VERSION, is_compatible, traverse
from nodes import ALIASES, collapse_elongated

app = FastAPI(title="DQM Web Demo")

ROOT = Path(__file__).resolve().parent.parent
BRAIN_PATH = ROOT / "brains" / "main.tqm"

def normalize_query(raw: str) -> str:
    raw = raw.strip().lower()
    for sep in ["-", "/", "\\"]:
        raw = raw.replace(sep, " ")
    cleaned = "".join(char for char in raw if char not in "?!.,;:")
    words = cleaned.split()
    processed = []
    for word in words:
        squashed = collapse_elongated(word)
        processed.append(ALIASES.get(squashed, squashed))
    normalized = " ".join(processed)
    for punct in string.punctuation:
        normalized = normalized.replace(punct, "")
    return normalized.strip()

def load_web_brain():
    try:
        with BRAIN_PATH.open("r", encoding="utf-8") as f:
            brain = json.load(f)
    except FileNotFoundError:
        raise RuntimeError(f"Brain file not found: {BRAIN_PATH}")
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Brain JSON is invalid: {exc}")
    if not isinstance(brain.get("routes"), dict):
        raise RuntimeError("Brain must contain a 'routes' dictionary.")
    compatibility = brain.get("compatibility", "")
    if not is_compatible(ENGINE_VERSION, compatibility):
        raise RuntimeError(
            f"Brain requires engine {compatibility}; web engine is {ENGINE_VERSION}."
        )
    return brain

BRAIN = load_web_brain()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def health():
    return {
        "name": "DQM",
        "engine_version": ENGINE_VERSION,
        "brain_id": BRAIN.get("brain_id", "Unknown"),
        "brain_version": BRAIN.get("version", "Unknown"),
        "status": "ready",
    }

@app.post("/api/query")
def query_dqm(request: QueryRequest):
    raw_query = request.query.strip()
    if not raw_query:
        raise HTTPException(status_code=400, detail="Enter a query first.")
    if len(raw_query) > 500:
        raise HTTPException(status_code=413, detail="Query is too long (500 characters max).")
    normalized = normalize_query(raw_query)
    if not normalized:
        raise HTTPException(status_code=400, detail="That query has no searchable words.")
    answer = traverse(BRAIN["routes"], normalized)
    return {
        "query": raw_query,
        "normalized_query": normalized,
        "answer": answer,
        "brain_id": BRAIN.get("brain_id", "Unknown"),
        "engine_version": ENGINE_VERSION,
    }
