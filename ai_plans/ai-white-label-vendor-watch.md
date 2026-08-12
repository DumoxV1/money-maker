===PLAN===
# Business Kit: AI White-Label Vendor Change Monitor

## Problem
Small AI, automation, and marketing agencies increasingly resell third-party software under their own brand. Their client promises and margins depend on upstream pricing, partner terms, branding controls, API behavior, security documentation, and availability. Those details live across scattered pages and can change quietly; discovering a change after a client complains creates emergency work, margin loss, and reputational damage.

## Audience
Small agencies and fractional operations leads that resell or bundle several white-label AI/SaaS vendors but do not have a dedicated vendor-management or product-operations team.

## Offer
A self-serve upstream change monitor for an agency's approved vendor portfolio. The agency supplies public or authorized URLs and a simple product/margin/escalation matrix. The service versions source pages, removes cosmetic noise, verifies substantive changes, maps each one to affected agency offers, and sends an evidence-linked alert with a recommended check, repricing task, client-message draft, or migration brief. A branded monthly risk digest documents what changed and what stayed stable.

## Pricing
Charge €79/month for five vendors, €149/month for 12, or €249/month for 25, with a €299 one-off portfolio baseline for agencies not ready to subscribe. Count monitored vendors and check frequency rather than raw pages so pricing is predictable. Offer a free report on one publicly documented vendor as the proof product.

## Channels
- Personalized, low-volume cold email to agencies publicly advertising white-label AI or SaaS packages
- LinkedIn agency owners, product-operations leads, and fractional COOs
- White-label SaaS, MSP, automation, and no-code communities where promotion is permitted
- Upwork jobs involving vendor comparisons, SaaS operations, documentation monitoring, or margin reporting

## Tool Stack
- Hermes for qualification, onboarding, semantic change classification, impact mapping, report generation, and support triage
- Vendor APIs, RSS feeds, changelogs, and status webhooks where offered
- Playwright plus changedetection.io for permitted public pages without a reliable feed
- SQLite or Git-backed immutable snapshots with content hashes, timestamps, and source URLs
- Email and Slack/Teams webhooks for alerts
- Stripe payment links and a self-serve client portal

## 7-Day Launch Plan
- **Day 1** — Fix the beachhead: agencies reselling 3-15 white-label AI tools. Define the accepted source types and explicitly exclude authenticated scraping without permission, license circumvention, and legal-compliance guarantees.
- **Day 2** — Build a machine-readable intake schema for vendor URLs, agency offer names, current cost and price bands, critical capabilities, alert recipients, materiality thresholds, and escalation rules.
- **Day 3** — Implement API/RSS-first collection, Playwright fallback for permitted public pages, canonical text extraction, versioned snapshots, content hashes, retries, and per-domain rate limits.
- **Day 4** — Add semantic diffing that suppresses timestamps, navigation, rotating testimonials, and other cosmetic noise. Require every alert to include old/new excerpts, source URL, capture times, confidence, and affected agency rules.
- **Day 5** — Create bounded alert classes: price/margin, partner terms, feature/API, branding, security/privacy document, outage, and unknown. Generate action checklists and message drafts, but label legal or contractual interpretation for qualified review.
- **Day 6** — Wire checkout, URL validation, self-serve onboarding, email/Slack delivery, monthly digests, pause/delete controls, billing, and an audit log. Test against owned fixtures that simulate both meaningful and cosmetic edits.
- **Day 7** — Publish one transparent sample report using public historical changelog data, identify a small set of agencies with a visible white-label offer, and send compliant personalized invitations to monitor one vendor free with a clear opt-out.

## AI Execution
After checkout, the agency submits only public or explicitly authorized source URLs and a structured map of vendor dependencies, pricing thresholds, critical features, and recipients. A scheduled agent prefers official APIs, feeds, changelogs, and status webhooks, then uses rate-limited browser checks only where permitted. It canonicalizes each capture, records an immutable timestamped snapshot, detects differences, filters known cosmetic regions, and rechecks the live source before treating a change as real. The AI classifies verified changes, quotes exact before/after evidence, applies only the agency's declared impact rules, drafts a bounded action or migration brief, and routes low-confidence or legal questions for external review rather than guessing. It deduplicates alerts, retries failures, produces branded digests, handles billing and deletion requests, and triages support from logs. Prospecting through recurring delivery is digital and scheduled, so no operator must browse pages, interpret every diff, meet clients, or perform physical work.

## Legal and Quality Guardrails
- Monitor only public pages or resources the client is authorized to access. Prefer official feeds and APIs; obey terms, robots directives, rate limits, authentication boundaries, and takedown requests.
- Never bypass CAPTCHAs, paywalls, access controls, license restrictions, or technical protections. Do not republish full proprietary documents; store the minimum snapshot needed for evidence and client-authorized comparison.
- Describe the product as change detection and operational triage, not legal, security, privacy, or regulatory advice. Contractual or compliance conclusions must be labeled for qualified review.
- Every substantive alert must carry a source URL, capture timestamps, exact old/new excerpts, confidence, and the rule that made it material. A failed fetch is an availability warning, not evidence that a policy changed.
- Recheck before alerting, suppress cosmetic churn, deduplicate repeated edits, expose false-positive feedback, and preserve an audit trail and rollback-safe parser versions.
- Encrypt client configuration and webhook secrets, use least privilege, minimize retention, separate tenants, support export/deletion, and never ingest end-customer personal data for the standard offer.
- Do not auto-accept new terms, change client pricing, publish claims, or trigger migrations. The agent may draft bounded actions; the agency controls consequential account and client decisions.
- Use truthful, opt-out outreach based on relevant public business signals and respect anti-spam law, community rules, and every suppression request.

## One-Line Pitch
Know which upstream AI-vendor change threatens your margin before your client does.

===SOCIAL===
## Twitter / X
🧵 White-label AI agencies have a quiet single point of failure: upstream vendors.

1/ Pricing pages change
2/ Partner terms move
3/ APIs deprecate behavior
4/ Branding controls disappear
5/ Clients notice after the promise breaks

This monitor verifies the diff, maps it to your offers, and sends the evidence plus the next check. From €79/month.

## LinkedIn
Reselling AI software creates recurring revenue—and recurring upstream risk. Our monitor watches approved vendor pricing, partner terms, API docs, branding controls, security pages, changelogs, and status feeds. It suppresses cosmetic noise, verifies meaningful changes against timestamped evidence, maps them to your product rules, and sends a branded action brief before the issue reaches a client.

## Reddit
"I am testing a vendor-change monitor specifically for small white-label AI agencies. It prefers official feeds/APIs, versions permitted public pages, removes cosmetic churn, and only alerts after a recheck with exact before/after excerpts. The useful layer is mapping the verified change to an agency's margin and feature rules—not pretending an LLM can give legal advice. Which upstream page has surprised your agency most often?"

## IG/TikTok
Vendor page changed → AI verifies the diff → affected offer identified → evidence-linked action brief sent. 🔎🤖📈

#whitelabel #saasops #agencyautomation #vendorRisk #ai

## Cold Email
Subject: upstream-change check for {agency_name}

Hi {first_name}, I noticed {specific_public_signal_that_the_agency_resells_or_bundles_ai_software}. I built a small monitor for the quiet risk behind that model: upstream pricing, partner terms, API docs, branding controls, security pages, and status changes.

It verifies changes, quotes the source, and maps them to your own margin and feature rules instead of sending raw page-diff noise. May I send a free one-vendor sample report? If not, reply "no" and I will not contact you again.
