"""Self-test for hustle_forge — no external deps, no network."""
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from hustle_forge import core


def run():
    niches = core.load_niches()
    assert len(niches) >= 12, f"expected >=12 niches, got {len(niches)}"
    assert len({n["id"] for n in niches}) == len(niches), "duplicate niche ids"
    expected_keys = {"id", "name", "category", "problem", "audience",
                     "offer", "price", "channels", "tools", "difficulty",
                     "time_to_first_euro", "pitch"}
    for n in niches:
        assert expected_keys <= set(n), f"niche {n.get('id')} missing keys"
    listing = core.list_niches()
    assert "ai-resume-rewrite" in listing

    with tempfile.TemporaryDirectory() as d:
        plan, social = core.generate("ai-resume-rewrite", d)
        assert plan.exists() and social.exists()
        assert "Business Kit" in plan.read_text(encoding="utf-8")
        assert "Twitter" in social.read_text(encoding="utf-8")

    print(f"OK — {len(niches)} niches, kit generation works.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
