"""Continuous niche research — runs with zero external API keys.

Uses plain curl + DuckDuckGo HTML + Wikipedia to surface NEW, quiet,
AI-executable side-hustle niches. Appends any candidate not already in
the database to data/niche_research.json for later human/AI review.

Designed to run on a schedule (cron) so the project keeps finding
stille geldverdieners without being asked.
"""
import json
import re
import subprocess
import html
import urllib.parse
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "hustle_forge" / "data" / "niches.json"
OUT = ROOT / "hustle_forge" / "data" / "niche_research.json"

SEED_QUERIES = [
    "AI generated digital product sells passively",
    "quiet forgotten money claim assistance service",
    "white label AI service resell agencies",
    "API arbitrage micro saas profitable",
    "automated content publishing api money",
    "royalty free AI generated asset marketplace",
    "unclaimed government money finder",
    "AI ghostwriting retainer service",
]


def ddg(query, n=8):
    try:
        out = subprocess.run(
            ["curl", "-sS", "-m", "25", "-A", "Mozilla/5.0",
             "--data-urlencode", f"q={query}",
             "https://html.duckduckgo.com/html/"],
            capture_output=True, text=True, timeout=35)
        text = out.stdout
        titles = re.findall(r'result__a"[^>]*>(.*?)</a>', text, re.S)
        snips = re.findall(r'result__snippet"[^>]*>(.*?)</a>', text, re.S)

        def clean(s):
            s = re.sub(r'<[^>]+>', '', s)
            return html.unescape(s).strip()

        return [{"title": clean(t), "snippet": clean(s)}
                for t, s in zip(titles, snips)][:n]
    except Exception as e:
        return [{"error": str(e)}]


def keywords_of(text):
    # crude but dependency-free signal extraction
    hits = set()
    for kw in ["AI", "API", "royalty", "white label", "unclaimed", "ghostwrite",
               "automated", "passive", "resell", "arbitrage", "KDP", "sample pack",
               "newsletter", "audit", "generator"]:
        if kw.lower() in text.lower():
            hits.add(kw)
    return hits


def main():
    db = json.loads(DB.read_text(encoding="utf-8"))
    known = {n["id"] for n in db["niches"]}
    known_names = {n["name"].lower() for n in db["niches"]}

    candidates = []
    for q in SEED_QUERIES:
        for r in ddg(q):
            blob = f"{r.get('title','')} {r.get('snippet','')}"
            kws = keywords_of(blob)
            # only keep results that look like a quiet, AI-executable angle
            if len(kws) >= 1 and "error" not in r:
                title = r.get("title", "")[:80]
                if title.lower() not in known_names:
                    candidates.append({
                        "source_query": q,
                        "title": title,
                        "snippet": r.get("snippet", "")[:200],
                        "signals": sorted(kws),
                        "found_at": datetime.now().isoformat(timespec="seconds"),
                    })

    # de-dupe by title
    seen = set()
    uniq = []
    for c in candidates:
        if c["title"].lower() not in seen:
            seen.add(c["title"].lower())
            uniq.append(c)

    existing = []
    if OUT.exists():
        try:
            existing = json.loads(OUT.read_text(encoding="utf-8"))
        except Exception:
            existing = []
    merged = existing + uniq
    OUT.write_text(json.dumps(merged, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"Researched {len(SEED_QUERIES)} queries -> "
          f"{len(uniq)} new candidates logged to {OUT.name} "
          f"(db already has {len(known)} niches).")
    for c in uniq[:5]:
        print(f"  • [{','.join(c['signals'])}] {c['title']}")


if __name__ == "__main__":
    main()
