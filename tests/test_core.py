"""Self-test for hustle_forge — no external deps, no network."""
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from hustle_forge import core

ROOT = Path(__file__).resolve().parent.parent
AI_PLANS = ROOT / "ai_plans"


def run():
    niches = core.load_niches()
    assert len(niches) == 12, f"expected 12 niches, got {len(niches)}"
    for n in niches:
        assert "basket" in n, f"{n.get('id')} missing basket"
        # every niche must be AI-executable (no physical body required)
        assert "ai_execution" in n and n["ai_execution"], f"{n.get('id')} not AI-executable"
        # every niche must have a pre-authored AI plan shipped in the repo
        plan = AI_PLANS / f"{n['id']}.md"
        assert plan.exists(), f"missing shipped AI plan: {plan}"
        txt = plan.read_text(encoding="utf-8")
        assert "===PLAN===" in txt and "===SOCIAL===" in txt, f"{n['id']} plan malformed"

    listing = core.list_niches()
    assert "ai-seo-affiliate-boring" in listing

    # generate using the shipped AI plan (no network) and confirm AI authorship
    with tempfile.TemporaryDirectory() as d:
        plan, social = core.generate("ai-resume-rewrite", d)
        assert plan.exists() and social.exists()
        text = plan.read_text(encoding="utf-8")
        assert "Business Kit" in text
        assert "AI Execution" in text  # new section present
        assert "Diversification Note" in text
        assert "Twitter" in social.read_text(encoding="utf-8")

    baskets = {n["basket"] for n in niches}
    assert len(baskets) >= 5, f"expected diversified baskets, got {baskets}"
    print(f"OK — {len(niches)} AI-executable niches across {len(baskets)} baskets; "
          f"all 12 AI plans shipped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
