===PLAN===
# Business Kit: AI Micro-Vertical Procurement Renewal Briefs

## Problem
Small specialist suppliers face a poor choice: manually inspect thousands of public-procurement records or buy a broad alert platform that still sends an inbox full of loosely related tenders. By the time a live notice appears, the supplier may know little about the buyer, prior awards, incumbent, contract period, or likely renewal cycle. Official award data contains those clues, but it is fragmented across notices, amendments, languages, codes, dates, and document formats.

## Audience
Small EU suppliers and bid advisers that repeatedly sell one narrow service or product category in a defined region—for example laboratory calibration, archival digitization, accessibility testing, industrial inspection software, specialist translation, or another legitimate micro-vertical with enough official notices to analyze.

## Offer
A versioned weekly intelligence product for one CPV/category and geography, delivered as a readable PDF plus analysis-ready CSV. Each issue contains:
- New and amended notices that pass the subscriber's declared fit rules
- Recent awards with buyer, supplier, value, procedure, and contract-period fields when officially stated
- Buyer, incumbent, award-value, seasonality, and competition summaries grounded in cited records
- Stated contract end dates and separately labeled estimated renewal windows, each with its derivation and confidence
- A deterministic fit score based on customer-set geography, value, capability, deadline, and exclusion rules
- Direct official-record links, notice identifiers, capture timestamps, source language, and a methodology/change log

The product informs market research and opportunity discovery; it does not promise a renewal, interpret procurement law, write a bid, or submit anything to a contracting authority.

## Pricing
Charge €49/month for one category and region, €99/month for three adjacent categories, or €149/month for a small team edition with rule-specific CSV views. Sell a €249 one-off 12-month market map to prospects that are not ready for recurring delivery. Publish a redacted or historical sample issue so buyers can inspect coverage, citations, and limitations before paying.

## Channels
- Narrow SEO pages targeting a CPV code, region, and supplier problem rather than generic “tender alerts”
- Personalized, low-volume LinkedIn or email outreach to relevant supplier owners and bid managers
- Trade-association and permitted supplier-directory listings
- Procurement, export, and SME communities where research resources may be shared
- Beehiiv or Ghost for a free sample digest and Lemon Squeezy for automated checkout and delivery

## Tool Stack
- Hermes for vertical selection, extraction orchestration, bounded summaries, copy, support triage, and release reporting
- Official TED Search API and TED Open Data, with other official sources added only when their access and reuse terms permit it
- Python with SQLite or DuckDB for canonical records, joins, date logic, deterministic calculations, and versioned snapshots
- JSON Schema and fixture-based tests for notice, award, amendment, and subscriber-rule validation
- A reproducible HTML-to-PDF renderer plus CSV generation and checksum tooling
- Beehiiv or Ghost API for publishing and Lemon Squeezy or another supported storefront API for checkout and digital fulfillment

## 7-Day Launch Plan
- **Day 1** — Select one quiet beachhead with a single category/CPV family and region. Use historical official records to require adequate recurring volume, identifiable supplier language, and a useful award trail; reject categories where the source data is too sparse or sensitive. Define a written scope that excludes legal advice, bid submission, and unsupported predictions.
- **Day 2** — Build an API-first collector that stores raw responses, source URLs, notice identifiers, retrieval times, source language, reuse metadata, and content hashes. Add pagination, rate limits, retries, backoff, and immutable snapshots. Do not bypass authentication, CAPTCHAs, paid documents, or technical controls.
- **Day 3** — Normalize notices and awards into a tested schema. Join corrections and amendments to their parent records, preserve original values beside normalized ones, flag cancellations, record currency and date semantics, and retain exact source excerpts for every extracted fact.
- **Day 4** — Implement subscriber-declared fit rules and the renewal model. Treat an official end date or duration as stated evidence; treat every calculated window as an estimate, expose the formula and inputs, lower confidence for missing or contradictory data, and suppress records that cannot be supported.
- **Day 5** — Generate the first PDF/CSV issue and run release gates: schema validity, duplicate and amendment checks, official-link checks, arithmetic reconciliation, currency/date labels, source coverage, translation traceability, estimate labeling, CSV safety, clean rendering, and deterministic archive checks. Fail closed instead of publishing an incomplete issue.
- **Day 6** — Create the storefront, sample issue, transparent methodology, coverage table, limitation statement, refund terms, self-serve rules form, billing, delivery, archive, unsubscribe, export, and deletion flows. Test checkout and fulfillment with a sandbox transaction where supported.
- **Day 7** — Publish one evidence-led market snapshot, create narrow landing pages from aggregate non-personal findings, and send a small number of relevant, truthful sample invitations with a clear opt-out. Record suppression requests and let engagement plus coverage quality—not bulk volume—choose the next micro-vertical.

## AI Execution
A scheduled agent queries supported official procurement APIs for a fixed category, geography, and time window. It versions every response; resolves parent, amendment, correction, award, and cancellation relationships; normalizes multilingual fields; and deduplicates records without discarding the original evidence. Deterministic code computes counts, totals, distributions, contract intervals, and subscriber-rule scores. The language model may classify ambiguous descriptions and explain patterns only within a constrained schema, with notice-level citations and an abstain state. Renewal entries are generated only from documented dates or an exposed formula and are visibly separated into stated and estimated fields.

Before release, automated checks reopen source links, reconcile every table to the canonical dataset, verify excerpts, detect stale or contradictory records, neutralize spreadsheet-formula injection, render the report, validate links and checksums, and block publication if required evidence is absent. Passing editions are packaged, listed, sold, delivered, archived, and announced by API. The agent handles customer rule changes, routine source-linked questions, billing events, opt-outs, deletion requests, and failure reports from structured logs. Prospecting, checkout, research, analysis, QA, publishing, recurring fulfillment, and support triage are digital and schedulable; no operator has to watch portals, write reports, attend calls, or perform physical work.

## Legal and Quality Guardrails
- Use only official public records and other sources whose current access and reuse terms permit the intended product. Prefer APIs and open-data exports, observe quotas and attribution requirements, retain license/version records, and honor corrections or takedowns.
- Never bypass access controls, scrape restricted tender documents, republish confidential material, or imply affiliation with TED, the EU, a contracting authority, or any supplier.
- Attach an official URL, stable identifier, retrieval time, source language, and exact supporting excerpt to material facts. If a fact cannot be cited, omit it; never invent an award, incumbent, budget, deadline, contact, or buyer intention.
- Label inferred dates as estimates—not “upcoming tenders”—and show the inputs, method, confidence, and last-checked time. A contract end date does not prove that a buyer will renew, re-tender, or use the same scope.
- Present factual market intelligence, not legal, financial, procurement, or bid advice. Do not auto-submit bids, contact authorities as a customer, certify eligibility, predict awards, or make consequential decisions for the subscriber.
- Preserve original currency and date fields, state conversion dates and rates where conversions are offered, reconcile arithmetic with deterministic code, and distinguish estimated, ceiling, and awarded values.
- Link amendments and cancellations, recheck records before each issue, publish corrections visibly, version every report, and provide a machine-readable change log.
- Minimize personal data. Do not enrich private individuals or compile personal contact lists; process any public business-contact data only with a documented lawful basis, limited retention, export/deletion controls, and applicable privacy notices.
- Use truthful, low-volume, opt-out outreach and obey anti-spam law, robots directives, platform terms, community rules, rate limits, and suppression requests.
- Sanitize CSV cells, PDFs, links, filenames, and imported text; isolate tenants and secrets; scan generated archives; and never execute code or active content found in source documents.

## One-Line Pitch
See the next quiet public-sector sales window before it becomes another noisy tender alert.

===SOCIAL===
## Twitter / X
🧵 A live tender alert is often the last signal, not the first.

1/ Follow one micro-vertical, not every keyword
2/ Join notices, amendments, awards, and cancellations
3/ Cite the buyer, value, incumbent, and stated contract period
4/ Label renewal estimates as estimates
5/ Deliver one clean PDF + CSV each week

Evidence-linked procurement renewal briefs from €49/month—built for specialist suppliers, not inbox volume.

## LinkedIn
Broad tender alerts optimize for how many notices they can send. A specialist supplier needs something narrower: what changed in its exact category and region, who bought previously, what was actually awarded, which contract dates are stated, and which renewal windows are only estimates. These weekly AI-built briefs join official notices and awards into a cited PDF and CSV, apply the subscriber's own fit rules, and expose every inference. It is market intelligence, not automated bidding or procurement advice.

## Reddit / Community Post
Title: I built a source-linked renewal brief for one public-procurement micro-vertical

“I am testing a narrow alternative to generic tender alerts. It collects permitted official notice and award data for one category and region, links amendments and cancellations, and publishes a weekly PDF/CSV with exact record IDs and source links. Stated contract dates and estimated renewal windows are kept in separate fields, with the estimate formula exposed. No auto-bidding and no claims that an inferred window is a future tender. Which fields would make a historical sample genuinely useful rather than another alert feed?”

## IG / TikTok / Pinterest
Official notices + awards → amendments joined → dates verified → renewal estimates labeled → one cited weekly brief. 🔎📊🤖

#publicprocurement #b2bdata #sme #marketintelligence #automation

## Cold Email
Subject: a narrow procurement map for {category} in {region}

Hi {first_name}, I noticed {specific_public_signal_that_the_business_serves_the_selected_category}. I built a sample brief that filters official procurement notices and awards to {category} in {region}, then shows cited buyer, award, contract-period, amendment, and renewal-window fields in one PDF and CSV.

Estimated windows are clearly labeled and linked to their source dates; it is research, not a promise of a tender or a bid service. May I send the historical sample and coverage table? If it is not relevant, reply “no” and I will not contact you again.
