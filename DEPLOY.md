# Deploy — exact commands (copy/paste)

Everything is built and committed locally. The only step I can't run for
you is the GitHub push (no GitHub auth in this environment). Run these in
**Git Bash** from `C:\Dev\Money Maker`:

## 1. Login to GitHub (one time)
```bash
gh auth login
```
Pick: GitHub.com → HTTPS → paste the browser code → authorize.

## 2. Create the repo + push
Replace `money-maker` if you want another name. This creates a **private
or public** repo on *your* account and pushes the commit.

```bash
gh repo create money-maker --public --source=. --remote=origin --push
```

If you already made the repo on github.com, instead run:
```bash
git remote add origin https://github.com/<YOUR_USERNAME>/money-maker.git
git branch -M main
git push -u origin main
```

## 3. Turn on the free website (GitHub Pages)
```bash
gh repo deploy-key  # not needed; just go to Settings below
```
In your browser: **repo → Settings → Pages → Source: Deploy from a branch
→ Branch: `main` → folder `/ (root)** → Save.

Your site goes live at:
`https://<YOUR_USERNAME>.github.io/money-maker/`

## 4. Fill in the money links (do this before sharing)
Open `index.html` and replace every `REPLACE_YOU` with your handles:
- Gumroad → `https://REPLACE_YOU.gumroad.com`
- Ko-fi    → `https://ko-fi.com/REPLACE_YOU`
- GitHub   → `https://github.com/REPLACE_YOU/money-maker`

Free accounts: http://gumroad.com  ·  https://ko-fi.com

## 5. Verify the tool still works
```bash
python -m hustle_forge list
python -m hustle_forge gen ai-resume-rewrite --out output
```

## 6. (Re)commit the link edits
```bash
git add -A && git commit -m "Add real monetization links" && git push
```

---
Done. You now have a free, live side-hustle funnel. Next moves (optional,
I can do them): write 5 launch posts, set up the Gumroad products, or
expand the niche database.
