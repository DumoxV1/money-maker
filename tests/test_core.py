"""Self-test for hustle_forge — no external deps, no network."""
import os
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from hustle_forge import core


def run():
    niches = core.load_niches()
    assert len(niches) == 12, f"expected 12 niches, got {len(niches)}"
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
