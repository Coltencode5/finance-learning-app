"""Shared helpers for sector-financials dossier extraction scripts."""
from __future__ import annotations

import re

BIBLIO_RE = re.compile(
    r"Journal of|Law Journal|Review of|Working [Pp]aper|University,|"
    r"Georgetown|Stanford|Cambridge|Oxford University|ISBN|Bibliography|"
    r"References|OceanofPDF|Dow Jones|Financial Times|"
    r"et al\.|Working paper|Spee(?:ch)?\b|"
    r"discussed (?:again )?in Chapter \d+|"
    r"See also Chapter \d+|as discussed in Chapter",
    re.I,
)

YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")
AUTHOR_LIST_RE = re.compile(r"[A-Z][a-z]+,\s+[A-Z][a-z]")


def is_bibliography_snippet(snippet: str) -> bool:
    """Heuristic: snippet looks like a citation, cross-ref, or footnote — not definitional prose."""
    if not snippet or len(snippet) < 25:
        return True
    if BIBLIO_RE.search(snippet):
        return True
    if len(YEAR_RE.findall(snippet)) >= 2:
        return True
    if len(AUTHOR_LIST_RE.findall(snippet)) >= 2:
        return True
    # Mid-word fragment from PDF column wrap (e.g. "paration of ING's")
    lead = snippet.lstrip("“\"'(")
    if lead and lead[0].islower() and not lead.startswith(("the ", "a ", "an ", "in ", "of ")):
        return True
    # TOC / figure-caption debris
    if re.match(r"^(Figure|Table|Exhibit|Chapter \d+:|Provisions Chapter)", snippet, re.I):
        return True
    if snippet.count("Chapter ") >= 2:
        return True
    return False


def score_definition_snippet(snippet: str) -> int:
    score = 0
    if re.search(r"\b(is|are|means|refers to|defined as|represents|denotes|called)\b", snippet, re.I):
        score += 4
    if re.search(r"\b(important|function|measure|ratio|concept)\b", snippet, re.I):
        score += 1
    lead = snippet.lstrip("“\"'(")
    if lead and (lead[0].isupper() or lead.startswith('"')):
        score += 1
    if re.search(r"[.!?]", snippet):
        score += 1
    return score


def definition_snippets(text: str, term: str, window: int = 220, max_len: int = 300) -> str:
    """Return best-effort definitional context for term, skipping bibliography-adjacent hits."""
    if not text or not term:
        return ""
    rx = re.compile(re.escape(term), re.I)
    candidates: list[tuple[int, int, str]] = []

    for m in rx.finditer(text):
        start = max(0, m.start() - 40)
        end = min(len(text), m.end() + window)
        snippet = re.sub(r"\s+", " ", text[start:end]).strip()
        if len(snippet) < 30:
            continue
        if is_bibliography_snippet(snippet):
            continue
        candidates.append((score_definition_snippet(snippet), len(snippet), snippet))

    if candidates:
        candidates.sort(key=lambda x: (-x[0], -x[1]))
        return candidates[0][2][:max_len]

    # Fallback: any match, still prefer non-bib if possible
    for m in rx.finditer(text):
        start = max(0, m.start() - 40)
        end = min(len(text), m.end() + window)
        snippet = re.sub(r"\s+", " ", text[start:end]).strip()
        if snippet and not is_bibliography_snippet(snippet):
            return snippet[:max_len]

    m = rx.search(text)
    if not m:
        return ""
    start = max(0, m.start() - 40)
    end = min(len(text), m.end() + window)
    return re.sub(r"\s+", " ", text[start:end]).strip()[:max_len]
