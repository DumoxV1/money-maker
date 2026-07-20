hustle_forge
=============

0-budget AI side-hustle toolkit. Generate a **complete business kit**
(business plan + social posts) from a single command — fully offline,
no API key, no cost.

Built for the `Money Maker` project: autonomous income with €0 budget.

Install
-------
No dependencies. Just Python 3.8+.

    git clone https://github.com/<you>/money-maker.git
    cd money-maker
    python -m hustle_forge list

Usage
-----
    # List every niche you can launch
    python -m hustle_forge list

    # Generate a kit for a specific niche
    python -m hustle_forge gen ai-resume-rewrite

    # Surprise me
    python -m hustle_forge gen --random --out my_kit

This writes two files into `output/` (or your `--out` dir):

- `<niche>_business_plan.md` — problem, audience, offer, pricing,
  7-day launch plan.
- `<niche>_social_posts.md` — ready-to-post Twitter/LinkedIn/Reddit/
  IG/TikTok/cold-DM copy.

How it makes money
------------------
1. **Free** — the CLI and landing page build trust and an audience.
2. **Lead magnet** — the "50 0-budget AI side hustles" PDF (see `site/`).
3. **Paid** — premium prompt packs, templates, and the "Forge Club"
   on Gumroad / Ko-fi (links in the site).

Philosophy
----------
Done beats perfect. Every kit ends with a 7-day launch plan. Ship the
first paid pilot before you polish anything.

License
-------
MIT
