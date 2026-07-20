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
    # every niche must declare a diversification basket + competition
    for n in niches:
        assert "basket" in n, f"{n.get('id')} missing basket"
        assert "competition" in n, f"{n.get('id')} missing competition"
        assert "source" in n, f"{n.get('id')} missing source"
    listing = core.list_niches()
    assert "dumpster-rental" in listing

    with tempfile.TemporaryDirectory() as d:
        plan, social = core.generate("dumpster-rental", d)
        assert plan.exists() and social.exists()
        text = plan.read_text(encoding="utf-8")
        assert "Business Kit" in text
        assert "Diversification Note" in text  # new basket section present
        assert "Twitter" in social.read_text(encoding="utf-8")

    baskets = {n["basket"] for n in niches}
    assert len(baskets) >= 5, f"expected diversified baskets, got {baskets}"
    print(f"OK — {len(niches)} niches across {len(baskets)} baskets: {sorted(baskets)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
