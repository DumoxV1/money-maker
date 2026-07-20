"""Core generation logic for hustle_forge.

Pure standard library — no pip installs, no API keys, no budget.
"""
import json
import os
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent
DATA = BASE / "data" / "niches.json"
TPL_PLAN = BASE / "templates" / "business_plan.md"
TPL_SOCIAL = BASE / "templates" / "social_posts.md"


def load_niches():
    with open(DATA, encoding="utf-8") as f:
        return json.load(f)["niches"]


def list_niches():
    rows = []
    for n in load_niches():
        rows.append(
            f"  [{n['id']}] {n['name']}  —  {n['category']}  "
            f"(diff: {n['difficulty']}, first €: {n['time_to_first_euro']})"
        )
    return "\n".join(rows)


def _bullets(items):
    return "\n".join(f"- {i}" for i in items)


def generate(niche_id, out_dir="output"):
    niches = load_niches()
    niche = next((n for n in niches if n["id"] == niche_id), None)
    if niche is None:
        raise SystemExit(
            f"Unknown niche '{niche_id}'.\nAvailable:\n{list_niches()}"
        )

    from . import __version__

    ts = datetime.now().strftime("%Y-%m-%d %H:%M")

    plan = (
        TPL_PLAN.read_text(encoding="utf-8")
        .replace("{version}", __version__)
        .replace("{name}", niche["name"])
        .replace("{category}", niche["category"])
        .replace("{difficulty}", niche["difficulty"])
        .replace("{time_to_first_euro}", niche["time_to_first_euro"])
        .replace("{problem}", niche["problem"])
        .replace("{audience}", niche["audience"])
        .replace("{offer}", niche["offer"])
        .replace("{price}", niche["price"])
        .replace("{channels_bullets}", _bullets(niche["channels"]))
        .replace("{tools_bullets}", _bullets(niche["tools"]))
        .replace("{pitch}", niche["pitch"])
        .replace("{timestamp}", ts)
    )

    social = (
        TPL_SOCIAL.read_text(encoding="utf-8")
        .replace("{version}", __version__)
        .replace("{name}", niche["name"])
        .replace("{problem}", niche["problem"])
        .replace("{audience}", niche["audience"])
        .replace("{offer}", niche["offer"])
        .replace("{price}", niche["price"])
        .replace("{time_to_first_euro}", niche["time_to_first_euro"])
        .replace("{pitch}", niche["pitch"])
        .replace("{first_name}", "there")
    )

    out = Path(out_dir)
    out.mkdir(exist_ok=True)
    plan_path = out / f"{niche_id}_business_plan.md"
    social_path = out / f"{niche_id}_social_posts.md"
    plan_path.write_text(plan, encoding="utf-8")
    social_path.write_text(social, encoding="utf-8")
    return plan_path, social_path


def random_niche():
    import random

    return random.choice(load_niches())["id"]
