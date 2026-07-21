"""Launch-content generator — turns any niche into ready-to-post assets.

Outputs a markdown file with platform-specific copy (Reddit, LinkedIn,
Twitter/X, cold DM, ProductHunt, email) built purely from the niche data.
No network, no API keys.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "hustle_forge" / "data" / "niches.json"


def load(id_):
    db = json.loads(DB.read_text(encoding="utf-8"))
    n = next((x for x in db["niches"] if x["id"] == id_), None)
    if not n:
        raise SystemExit(f"Unknown niche '{id_}'. Run 'python -m hustle_forge list'.")
    return n


TPL = """# Launch Content — {name}

> Auto-generated from niche data. Tweak, then ship.

## Reddit (value-first, no spam)
"If you're dealing with [{problem}], here's the play I'd use:
{offer}. The angle that makes it quiet is [{basket}] — low competition,
steady demand. Happy to share the exact steps if useful."

Subreddits: r/Entrepreneur, r/SideProject, r/passive_income, r/beermoney

## LinkedIn (founder POV)
Most people chase crowded niches. We run {name} — {offer}.
The edge is {basket}: thin competition, recurring demand.
First euros land in {time_to_first_euro}. What boring vertical are you ignoring?

## Twitter / X (thread hook)
🧵 {pitch}

The bottleneck everyone complains about? Already solved.

1/ {problem}
2/ {offer}
3/ {price}
4/ Live in {time_to_first_euro}
5/ DM "START" and I'll send the first step.

## Cold DM (personalized)
Hi {{first_name}}, saw you're in [{audience}] — quick Q:
are you struggling with {problem}?

I help with {offer} (usually {price}).
Want a free 10-min teardown of your setup?

## ProductHunt / BetaList (if software)
"🚀 {name} — {pitch}
We automated {problem} so you don't have to. {basket} angle, €0 to start."

## Welcome email (first lead)
Subject: the quiet way to start {name}
Body: Most people overcomplicate this. Here's the 1-step version:
{offer}. Reply with your biggest blocker — I'll send the fix free.
"""


def render(n):
    return TPL.format(
        name=n["name"], problem=n["problem"], offer=n["offer"],
        basket=n["basket"], price=n["price"],
        time_to_first_euro=n["time_to_first_euro"],
        audience=n["audience"], pitch=n["pitch"],
    )


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Usage: python scripts/launch_content.py <niche_id>")
    n = load(sys.argv[1])
    out = ROOT / "output" / f"{n['id']}_launch_content.md"
    out.parent.mkdir(exist_ok=True)
    out.write_text(render(n), encoding="utf-8")
    print(f"✅ Launch content for '{n['id']}' -> {out}")


if __name__ == "__main__":
    main()
