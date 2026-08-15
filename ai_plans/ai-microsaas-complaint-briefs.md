===PLAN===
# Business Kit: AI Micro-SaaS Complaint Validation Briefs

## Problem
Solo builders are surrounded by generic micro-SaaS idea lists, model-generated opportunity scores, and surveys that invite confirmation bias. The useful evidence is messier: repeated complaints, quantified losses, improvised workarounds, switching objections, abandoned tools, and comments showing that a problem is rare or already solved. Those signals sit across permitted public communities, issue trackers, reviews, support discussions, and open datasets. Finding them, separating repetition from copied noise, and preserving the evidence trail can consume the same week the founder hoped to spend validating a product.

## Audience
Bootstrapped developers, no-code founders, product studios, and small SaaS agencies choosing whether one narrowly defined problem and buyer segment deserves a build or customer-discovery sprint. Start with non-regulated B2B or prosumer workflows whose users discuss operational pain publicly. The service supports research; it does not replace direct customer conversations or make investment, legal, employment, credit, health, or other consequential decisions.

## Offer
A self-serve, versioned validation brief for one customer-defined problem, audience, geography, and timeframe. Each delivery contains:
- The exact hypothesis, inclusion/exclusion rules, search terms, source manifest, retrieval window, and coverage limitations
- Deduplicated complaint clusters with short verified excerpts, canonical source links, capture times, and per-source counts
- Separate signals for pain, quantified time or cost, repeated workarounds, existing spend, switching friction, requested outcomes, and abandoned attempts
- An alternatives map showing named incumbent categories and recurring gaps without copying proprietary reviews or claiming a complete market census
- A counter-evidence section covering praise for current tools, free substitutes, low urgency, one-off edge cases, contradictory jobs-to-be-done, and weak or stale coverage
- Deterministic tables by source, date, cluster, and declared segment, with repost and near-duplicate counts exposed rather than inflated
- A bounded MVP and interview-test plan derived from supported clusters, plus questions designed to falsify the hypothesis
- A confidence and provenance appendix stating what the sources can and cannot establish

The report never converts post counts into market size, invents revenue, labels anonymous commenters as buyers, or promises product-market fit.

## Pricing
Charge €59 for a quick brief covering a small allowlist of sources and one recent window, €149 for a deeper brief with alternatives and counter-evidence, or €199/month for a three-hypothesis watchlist that reports only newly verified signals and cluster changes. Publish a fictional or openly licensed sample with its source manifest and quality checklist. Put source limits, refresh cadence, retention, and refund conditions on the checkout page so fulfillment remains bounded.

## Channels
- Useful methodology and redacted sample posts in Indie Hackers and bootstrapped-founder communities where promotion is allowed
- Personalized, low-volume outreach to builders publicly documenting an early product hypothesis
- Product-management, validation, no-code, and micro-SaaS communities
- Upwork jobs for product discovery, review analysis, voice-of-customer research, or market validation
- Narrow SEO pages for “evidence-based SaaS validation,” “complaint research for micro-SaaS,” and workflow-specific pain research

## Tool Stack
- Hermes for hypothesis normalization, source-query planning, constrained extraction, cluster labeling, report writing, and support triage
- Official APIs, RSS feeds, open-data exports, and public datasets whose current terms allow the intended access and analysis
- Examples such as the Stack Exchange API, GitHub API for relevant public issues, Hacker News Algolia API, and customer-authorized exports; use each only within its current policy
- Playwright only for explicitly permitted public pages that lack a supported feed, with robots and rate-limit controls
- Python plus DuckDB or SQLite for canonical records, exact counts, deduplication, date windows, manifests, and reproducible tables
- Text embeddings and locality-sensitive hashes for candidate clustering, followed by evidence-preserving verification rules
- JSON Schema, immutable content hashes, link/excerpt checks, and a reproducible HTML-to-PDF plus CSV renderer
- Lemon Squeezy or Stripe payment links, object storage, and a self-serve intake, export, correction, and deletion portal

## 7-Day Launch Plan
- **Day 1** — Fix one beachhead, such as bootstrapped B2B workflow tools, and define the supported output schema. Create an allowlist of source types and record each source's access method, reuse terms, quote limits, attribution rules, quotas, deletion behavior, and prohibited uses. Exclude private groups, paywalled content, sensitive-person research, and any source that cannot be used lawfully and reliably.
- **Day 2** — Build structured intake for the proposed user, problem, job, geography, language, timeframe, known alternatives, exclusions, source preferences, and falsification threshold. Reject broad prompts such as “find me a profitable SaaS” and require one testable hypothesis; never infer a sensitive trait or target population from free text.
- **Day 3** — Implement API/feed-first collectors. Save canonical URL or stable ID, source, author field only when necessary, publication and retrieval times, allowed excerpt, access-policy version, and content hash. Add quotas, retries, backoff, robots checks where applicable, deletion/takedown handling, and defenses against prompt injection in fetched text.
- **Day 4** — Build reproducible deduplication and clustering. Normalize obvious reposts, preserve every source record, expose cluster membership, and separate model-proposed labels from deterministic counts. Add structured signal fields for problem, context, workaround, consequence, alternative, urgency, willingness evidence, contradiction, and uncertainty; require an exact excerpt for each extracted claim.
- **Day 5** — Generate the brief and run release gates: hypothesis-scope check, source-policy check, URL re-open, excerpt match, duplicate accounting, date and segment validation, table reconciliation, minimum source diversity, stale-data warning, counter-evidence coverage, unsupported-claim scan, CSV neutralization, and clean PDF rendering. Fail closed or issue an explicit “insufficient evidence” report rather than padding the result.
- **Day 6** — Wire sandbox checkout, bounded tiers, intake validation, job queue, tenant-isolated storage, encrypted secrets, report delivery, watchlist diffs, billing, correction requests, opt-out, export, retention, deletion, and an audit log. Test with owned fixtures containing copied posts, dead links, sarcasm, praise, vague complaints, source outages, adversarial instructions, and a hypothesis that deserves rejection.
- **Day 7** — Publish the transparent sample and methodology. Identify a small number of founders with a specific public build hypothesis, send truthful opt-out invitations to inspect the sample, and let qualified buyers purchase and receive a report without a call. Use report failures and buyer corrections—not invented demand claims—to refine the source scope.

## AI Execution
After checkout, the agent validates the customer's bounded hypothesis and converts it into explicit inclusion, exclusion, synonym, timeframe, geography, language, and counter-signal rules. It selects only sources on the maintained policy allowlist, prefers supported APIs and feeds, applies per-source quotas, and records the access-policy version used. Every fetched item is treated as untrusted data: active content is never executed, embedded instructions cannot alter the workflow, and unsupported files or fields are quarantined. The agent stores a stable source reference, retrieval time, content hash, minimum necessary metadata, and only the excerpt needed to substantiate a report claim.

The agent identifies candidate duplicates with hashes and embeddings, but deterministic rules preserve an auditable canonical record and disclose every merged item. A constrained model extracts problem context, workaround, consequence, alternative, urgency, requested outcome, and contradiction into a schema, with an exact source span and an abstain state for each field. Code—not the model—calculates frequencies, source diversity, time distributions, duplicate rates, and threshold results. A commenter, upvote, issue, or review is never silently treated as a unique company, customer, purchase, or unit of market demand.

Before delivery, a separate verification pass reopens available sources, checks that each excerpt matches, confirms dates and declared segments, reconciles all tables to canonical records, and scans every narrative statement for evidence. It specifically searches for counterexamples, strong existing alternatives, free workarounds, low urgency, stale clusters, and source concentration. Missing or removed evidence is omitted or marked unavailable. If coverage is weak, the system returns a useful insufficiency brief with the searched scope and gaps; it does not fabricate more signals or require the operator to research manually.

Passing reports are rendered, checksummed, delivered, and archived according to the declared retention period. A scheduled watchlist retrieves only permitted new material, deduplicates it against prior versions, reports meaningful cluster changes, and preserves a change log. The same agent handles qualified public prospect research, compliant outreach, checkout, intake corrections, billing events, delivery, exports, deletions, takedown propagation, and support answers grounded in tenant-isolated logs. No operator conducts interviews, browses forums, cleans spreadsheets, writes reports, joins calls, or performs recurring or physical fulfillment.

## Legal and Quality Guardrails
- Access only public or customer-authorized material through methods allowed by each source's current terms. Prefer official APIs, feeds, and open datasets; obey robots directives, quotas, attribution, quote, caching, retention, and deletion requirements. Never bypass authentication, CAPTCHAs, paywalls, private-group controls, or technical protections.
- Keep a versioned source-policy registry and stop collection when permission is unclear or terms change. A page being viewable does not automatically permit bulk extraction, storage, resale, or model training.
- Quote only the minimum excerpt needed for analysis, link and attribute it as required, do not republish review corpora or proprietary datasets, and propagate removals or corrections into future report versions.
- Minimize personal data. Prefer aggregate workflow evidence, stable source IDs, and redacted handles; do not infer demographics, health, finances, identity, employability, or other sensitive traits, and do not build dossiers or contact lists from individual complainants.
- Treat public text, URLs, files, and metadata as untrusted. Strip active content, neutralize CSV formulas, isolate parsers, reject embedded instructions, scan outputs, and never expose secrets or one tenant's evidence to another.
- Every extracted signal requires a source link or stable ID, retrieval time, exact supporting span, and confidence. Reopen links before delivery, expose dead or removed records, and distinguish direct statements from model labels.
- Use deterministic code for counts, windows, duplicate handling, thresholds, and tables. Disclose reposts, source concentration, search limits, language limits, stale periods, and community-selection bias.
- Never equate mentions, votes, reviews, issue comments, or complaint frequency with unique buyers, willingness to pay, market size, revenue, causality, or product-market fit. Label all MVP and messaging suggestions as hypotheses to test.
- Search for disconfirming evidence and show it beside supporting evidence. An “insufficient evidence” or “do not build yet” result is a valid paid deliverable, not a pipeline failure.
- Do not make investment, legal, financial, employment, health, credit, housing, insurance, or other consequential recommendations. The buyer controls product and business decisions and should conduct direct customer discovery before relying on the brief.
- Use truthful, relevant, low-volume outreach with a clear opt-out. Honor anti-spam law, platform and community rules, suppression requests, and source-user takedowns; never message people merely because they appeared in the research corpus.

## One-Line Pitch
Before you build the micro-SaaS, see the complaints, workarounds, and counter-evidence—not another AI idea score.

===SOCIAL===
## Twitter / X
🧵 An AI idea score is not market validation.

1/ Define one buyer + problem hypothesis
2/ Search only permitted, attributable sources
3/ Deduplicate reposts and copied complaints
4/ Verify every excerpt and count with code
5/ Show counter-evidence and weak coverage too

Source-linked micro-SaaS complaint briefs from €59.

## LinkedIn
Most AI validation tools are optimized to produce an encouraging answer. This service is optimized to preserve evidence. It turns one narrow micro-SaaS hypothesis into a versioned brief of verified complaints, workarounds, alternatives, and counter-signals. Every narrative point links to a source; deterministic code handles counts and duplicates; an insufficient-evidence result is allowed. It is a research starting point, not a promise of product-market fit.

## Reddit / Community Post
Title: Testing a complaint-evidence brief that is allowed to say “do not build yet”

“I am building a narrow alternative to generic SaaS idea scores. You submit one user/problem hypothesis; the pipeline checks permitted public sources, preserves links and short excerpts, deduplicates copied signals, and reports supporting pain alongside alternatives and counter-evidence. Counts are not presented as market size or willingness to pay, and weak coverage produces an insufficiency report. What would make the provenance useful enough to guide your next customer interview?”

## IG / TikTok / YouTube Shorts
Generic idea score → confidence theater.

Bounded hypothesis → permitted sources → verified excerpts → duplicates removed → counter-evidence shown → next test. 🔎🤖

#microsaas #buildinpublic #productdiscovery #voiceofcustomer #bootstrapped

## Cold Email
Subject: evidence check for {public_product_hypothesis}

Hi {first_name}, I noticed {specific_public_signal_that_the_founder_is_testing_a_narrow_problem}. I built a self-serve research brief that looks for attributable complaints, workarounds, alternatives, and counter-signals across permitted public sources, then verifies the excerpts and deduplicates the counts.

It does not claim post volume equals market size, and it can conclude that evidence is insufficient. May I send the transparent sample and source checklist? If it is not relevant, reply “no” and I will not contact you again.
