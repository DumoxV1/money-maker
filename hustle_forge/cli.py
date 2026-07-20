#!/usr/bin/env python3
"""hustle_forge CLI — generate a business kit, optionally AI-authored.

Examples
--------
  python -m hustle_forge list
  python -m hustle_forge gen ai-resume-rewrite
  python -m hustle_forge gen --random --out my_kit
  python -m hustle_forge gen ai-seo-affiliate-boring --ai     # force AI/LLM
  python -m hustle_forge gen ai-resume-rewrite --template     # force template
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from hustle_forge import core  # noqa: E402


def main(argv=None):
    p = argparse.ArgumentParser(
        prog="hustle_forge",
        description="0-budget AI side-hustle toolkit. Generate a full "
        "business kit — by default the plans are AI-authored.",
    )
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("list", help="List all available niches")

    g = sub.add_parser("gen", help="Generate a business kit for a niche")
    g.add_argument("niche", nargs="?", help="Niche id (see 'list')")
    g.add_argument("--random", action="store_true", help="Pick a random niche")
    g.add_argument("--ai", action="store_true",
                   help="Force AI/LLM generation (needs HUSTLE_LLM_BASE_URL)")
    g.add_argument("--template", action="store_true",
                   help="Force the offline template (no LLM)")
    g.add_argument("--out", default="output", help="Output directory")

    args = p.parse_args(argv)

    if args.cmd == "list":
        print("Available niches:\n" + core.list_niches())
        return 0

    if args.cmd == "gen":
        if args.ai and args.template:
            p.error("--ai and --template are mutually exclusive")
        use_ai = None
        if args.ai:
            use_ai = True
        if args.template:
            use_ai = False

        niche_id = args.niche
        if args.random and not niche_id:
            niche_id = core.random_niche()
        if not niche_id:
            p.error("provide a niche id or --random")
        try:
            plan, social = core.generate(niche_id, args.out, use_ai=use_ai)
        except SystemExit as e:
            print(str(e), file=sys.stderr)
            return 1
        mode = "AI-authored" if (use_ai is not False) else "template"
        print(f"✅ Kit ({mode}) generated for '{niche_id}':")
        print(f"   • {plan}")
        print(f"   • {social}")
        print("\nNext: read the plan, pick your channel, ship the first post.")
        return 0

    p.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
