"""Core generation logic for hustle_forge.

Pure standard library. Two generation modes:
- template  (default fallback, 0 deps, 0 budget): fills business_plan.md / social_posts.md
- ai        (when HUSTLE_LLM_BASE_URL is set, or a pre-authored AI plan exists):
             an LLM authors the plan + posts, so the output is purely AI-generated.

A pre-authored AI plan shipped in ai_plans/<id>.md always wins, so the
delivered plans are genuinely "made by an AI" even with no network.
"""
import json
import os
import re
import urllib.request
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent
DATA = BASE / "data" / "niches.json"
TPL_PLAN = BASE / "templates" / "business_plan.md"
TPL_SOCIAL = BASE / "templates" / "social_posts.md"
TPL_PROMPT = BASE / "templates" / "ai_prompt.md"
AI_PLANS = ROOT / "ai_plans"

SYSTEM = (
    "You are a concise, pragmatic business strategist for 0-budget side "
    "hustles that an AI agent can run autonomously. Write tight, specific, "
    "actionable plans. No fluff, no illegal tactics."
)


def load_niches():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)["niches"]


def list_niches():
    rows = []
    for n in load_niches():
        rows.append(
            f"  [{n['id']}] {n['name']}  —  {n['basket']}  "
            f"(diff: {n['difficulty']}, first €: {n['time_to_first_euro']})"
        )
    return "\n".join(rows)


def _bullets(items):
    return "\n".join(f"- {i}" for i in items)


def llm_configured():
    return bool(os.environ.get("HUSTLE_LLM_BASE_URL"))


def call_llm(prompt, system=SYSTEM, timeout=90):
    """Call an OpenAI-compatible chat endpoint. Returns text or None."""
    base = os.environ.get("HUSTLE_LLM_BASE_URL")
    if not base:
        return None
    key = os.environ.get("HUSTLE_LLM_KEY")
    model = os.environ.get("HUSTLE_LLM_MODEL", "gpt-4o-mini")
    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.7,
    }
    url = base.rstrip("/") + "/chat/completions"
    headers = {"Content-Type": "application/json"}
    if key:
        headers["Authorization"] = f"Bearer {key}"
    req = urllib.request.Request(
        url, data=json.dumps(body).encode(), headers=headers, method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.load(r)
        return data["choices"][0]["message"]["content"]
    except Exception:
        return None


def build_prompt(niche):
    p = TPL_PROMPT.read_text(encoding="utf-8")
    return (
        p.replace("{name}", niche["name"])
        .replace("{problem}", niche["problem"])
        .replace("{audience}", niche["audience"])
        .replace("{offer}", niche["offer"])
        .replace("{price}", niche["price"])
        .replace("{channels}", _bullets(niche["channels"]))
        .replace("{tools}", _bullets(niche["tools"]))
        .replace("{ai_execution}", niche.get("ai_execution", ""))
        .replace("{pitch}", niche["pitch"])
    )


def parse_llm(text):
    """Split LLM output into (plan, social) using ===PLAN===/===SOCIAL===."""
    m = re.search(r"===PLAN===(.*?)===SOCIAL===", text, re.S)
    s = re.search(r"===SOCIAL===(.*)", text, re.S)
    if m and s:
        return m.group(1).strip(), s.group(1).strip()
    return text.strip(), ""


def _render_template(tpl_path, niche, ts):
    return (
        tpl_path.read_text(encoding="utf-8")
        .replace("{version}", __version__)
        .replace("{name}", niche["name"])
        .replace("{category}", niche["category"])
        .replace("{basket}", niche.get("basket", niche.get("category", "")))
        .replace("{difficulty}", niche["difficulty"])
        .replace("{time_to_first_euro}", niche["time_to_first_euro"])
        .replace("{competition}", niche.get("competition", "varies"))
        .replace("{source}", niche.get("source", "internal research"))
        .replace("{problem}", niche["problem"])
        .replace("{audience}", niche["audience"])
        .replace("{offer}", niche["offer"])
        .replace("{price}", niche["price"])
        .replace("{channels_bullets}", _bullets(niche["channels"]))
        .replace("{tools_bullets}", _bullets(niche["tools"]))
        .replace("{ai_execution}", niche.get("ai_execution", ""))
        .replace("{pitch}", niche["pitch"])
        .replace("{timestamp}", ts)
    )


def generate(niche_id, out_dir="output", use_ai=None):
    niches = load_niches()
    niche = next((n for n in niches if n["id"] == niche_id), None)
    if niche is None:
        raise SystemExit(f"Unknown niche '{niche_id}'.\nAvailable:\n{list_niches()}")

    from . import __version__

    ts = datetime.now().strftime("%Y-%m-%d %H:%M")

    if use_ai is None:
        use_ai = True  # prefer AI-made plans by default

    # 1) Pre-authored AI plan (shipped in repo) — purely AI-made, no network.
    pre = AI_PLANS / f"{niche_id}.md"
    if use_ai and pre.exists():
        plan_txt, social_txt = parse_llm(pre.read_text(encoding="utf-8"))
        plan_txt = _append_diversification(plan_txt, niche)
        if not social_txt:
            social_txt = _render_template(TPL_SOCIAL, niche, ts)
        return _write(out_dir, niche_id, plan_txt, social_txt)

    # 2) Live LLM call (requires HUSTLE_LLM_BASE_URL).
    if use_ai and llm_configured():
        out = call_llm(build_prompt(niche))
        if out:
            plan_txt, social_txt = parse_llm(out)
            plan_txt = _append_diversification(plan_txt, niche)
            if not social_txt:
                social_txt = _render_template(TPL_SOCIAL, niche, ts)
            return _write(out_dir, niche_id, plan_txt, social_txt)

    # 3) Template fallback (0 deps, 0 budget).
    plan_txt = _render_template(TPL_PLAN, niche, ts)
    social_txt = _render_template(TPL_SOCIAL, niche, ts)
    return _write(out_dir, niche_id, plan_txt, social_txt)


def _append_diversification(plan_txt, niche):
    """Add the basket reminder to AI-authored plans for consistency."""
    if "Diversification Note" in plan_txt:
        return plan_txt
    basket = niche.get("basket", niche.get("category", ""))
    note = (
        "\n\n---\n\n## Diversification Note\n"
        f"This niche belongs to the **{basket}** basket. To de-risk, run at "
        "least one niche from a *different* basket in parallel — the baskets "
        "don't correlate, so one slowdown never sinks you."
    )
    return plan_txt + note


def _write(out_dir, niche_id, plan_txt, social_txt):
    out = Path(out_dir)
    out.mkdir(exist_ok=True)
    plan_path = out / f"{niche_id}_business_plan.md"
    social_path = out / f"{niche_id}_social_posts.md"
    plan_path.write_text(plan_txt, encoding="utf-8")
    social_path.write_text(social_txt, encoding="utf-8")
    return plan_path, social_path


def random_niche():
    import random

    return random.choice(load_niches())["id"]
