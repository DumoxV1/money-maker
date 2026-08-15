===PLAN===
# Business Kit: AI B2B SaaS Release Enablement Kits

## Problem
Small B2B SaaS teams can ship a feature in days and then spend another week explaining it. The approved specification, release ticket, changelog note, help article, customer email, sales deck, short explainer, FAQ, and onboarding quiz often live with different owners. Facts and terminology drift between formats, old screenshots survive, support receives avoidable questions, and sales either ignores the release or overstates it. Generic repurposing tools make more content, but they rarely prove that every statement is supported by the approved release source.

## Audience
Bootstrapped and vertical B2B SaaS companies with regular product releases but no dedicated release-communications or customer-education team. A second beachhead is small product or customer-success agencies that need a repeatable white-label deliverable for several SaaS clients. Start with ordinary workflow software and exclude medical, legal, financial, safety-critical, or other high-impact product claims.

## Offer
A source-grounded enablement kit generated from one client-approved release bundle. Each release can produce:
- A concise changelog entry and long-form help-center draft
- A segmented customer email plus in-app announcement variants
- A sales one-pager and short branded slide deck
- A narrated micro-explainer assembled from client-approved screens or neutral graphics
- A support FAQ, internal objection sheet, and optional non-certifying knowledge quiz
- Social and community copy adapted from the same canonical facts
- A claim-to-source matrix, cross-format consistency report, render previews, and delivery manifest

The client selects channels, audiences, terminology, forbidden claims, and draft-versus-publish permissions through a structured intake. The standard service transforms approved material; it does not discover unreleased features, operate the product as an end user, or invent positioning and performance claims.

## Pricing
Charge €99 for a one-release pilot, €199/month for two release kits, €399/month for five, or €699/month for eight with additional audience variants. Include a fixed number of formats and one machine-readable rules update per tier; price extra languages or unusually long source bundles separately. Offer agencies a white-label tier with their own templates and client workspaces rather than open-ended manual revisions.

## Channels
- Personalized, low-volume email to bootstrapped and vertical SaaS teams with a visible but inconsistent public changelog
- LinkedIn outreach to product marketing, customer education, customer success, and product operations leads
- SaaS founder, product-led-growth, technical-writing, and customer-success communities where service posts are allowed
- Upwork jobs involving release notes, knowledge-base updates, product explainers, decks, or content repurposing
- Narrow SEO pages for searches such as “release communication checklist” and “turn release notes into customer education”
- A free sample built from the seller's own fictional demo release, showing the claim-to-source matrix and QA report

## Tool Stack
- Hermes for prospect qualification, structured intake, orchestration, source-bounded writing, report generation, and support triage
- A retrieval pipeline with page-level or section-level citations and schema-constrained outputs
- A source-to-podcast, video, deck, infographic, or quiz API whose current terms permit the intended commercial use
- Marp or Slidev for reproducible decks; FFmpeg and a commercially licensed text-to-speech provider for explainers
- Client-authorized help-center, CMS, changelog, email, and scheduling APIs
- Playwright for preview rendering, link checks, screenshot-diff checks, and draft verification
- JSON Schema, deterministic terminology and claim checks, an encrypted object store, and a versioned audit log
- Stripe payment links and a self-serve source, authorization, export, and deletion portal

## 7-Day Launch Plan
- **Day 1** — Choose one beachhead such as bootstrapped vertical SaaS with two to eight releases per month. Define accepted source types, output formats, turnaround, languages, and exclusions. Create a fictional demo product and release so the proof asset contains no borrowed claims or confidential material.
- **Day 2** — Build a machine-readable intake for approved source files, release/version identifiers, audiences, terminology, required and forbidden statements, brand tokens, approved media, pronunciation, channel limits, publication mode, approvers, retention, and deletion. Refuse incomplete or contradictory bundles instead of filling gaps.
- **Day 3** — Implement the canonical fact table. Extract atomic facts with exact source excerpts and locations, separate fact from requested positioning, preserve dates and units, flag contradictions, and require every generated factual sentence to map to at least one approved fact ID.
- **Day 4** — Add format generators for changelog, help article, email, one-pager, deck, FAQ, quiz, and a 60-90 second explainer. Use shared terminology and audience rules while keeping format-specific templates deterministic and versioned.
- **Day 5** — Build release gates: schema checks, source coverage, unsupported-claim detection, names/version/date consistency, broken links, stale or unapproved media, slide overflow, caption and transcript alignment, pronunciation, audio clipping, quiz-answer grounding, metadata completeness, and clean archive extraction. Block the whole affected asset when a material check fails.
- **Day 6** — Wire sandbox checkout, tenant-isolated upload, malware and active-content scanning, draft previews, scoped OAuth, explicit publish permissions, rollback records, usage caps, billing, status messages, export, retention, deletion, and a kill switch. Test the pipeline end to end with the fictional release and deliberately contradictory fixtures.
- **Day 7** — Publish the demo kit and evidence report, identify a small set of relevant SaaS teams from permitted public business pages, and send truthful opt-out invitations for a paid or low-cost pilot. Let qualified customers purchase, submit sources, receive drafts, and manage delivery without a call.

## AI Execution
After checkout, the agent verifies that the customer controls or is authorized to use the submitted material and that the bundle is explicitly approved for transformation. It treats files, links, metadata, and embedded instructions as untrusted input, scans and normalizes supported formats, and extracts a canonical table of atomic release facts. Every fact stores its exact excerpt, location, source hash, release identifier, and status. Contradictions, missing audience rules, unsupported media, and ambiguous publication permissions stop processing and generate a self-serve correction request rather than a guessed answer.

The agent then creates each selected asset through a constrained schema. Generated factual clauses must reference approved fact IDs, while customer-supplied positioning is labeled separately and checked against the forbidden-claim rules. Shared dictionaries keep feature names, version numbers, dates, limitations, calls to action, and support links consistent across the changelog, article, email, deck, narration, FAQ, and quiz. Deterministic code validates schemas, citations, links, numbers, terminology, required disclosures, media provenance, archive contents, and output limits. Render tests inspect slide overflow, responsive article drafts, caption timing, audio levels, missing images, and link destinations. Any unsupported statement is deleted or the asset is regenerated; a language model cannot waive a failed factual gate.

Passing assets are packaged with the source matrix, checksums, previews, and a versioned QA report. By default they are delivered as drafts. If the customer's machine-readable policy explicitly authorizes a channel, the agent publishes or schedules through a least-privilege API, reopens the resulting draft or page, verifies the expected version, and stores a rollback record. It handles relevant prospecting, opt-outs, checkout, intake validation, production, QA, delivery, authorized publication, billing events, deletion requests, and log-grounded support triage. No side-hustle operator needs to write copy, edit slides or audio, join meetings, click through a product, or perform recurring or physical fulfillment.

## Legal and Quality Guardrails
- Process only material the customer owns or is authorized to transform. Record source hashes, submitted approval, media provenance, provider/model versions, and applicable commercial-use terms; never expose confidential release material between tenants.
- Do not infer an unreleased capability, roadmap promise, compatibility, price, benchmark, security property, legal status, customer result, or availability date. If the approved source does not support a claim, omit it and report the gap.
- The standard offer excludes regulated and high-impact claims, incident communications, security advisories, legal notices, financial guidance, medical or safety instructions, and emergency messaging. It is content production, not legal, compliance, accessibility, security, or product advice.
- Default to drafts. Publish only to a customer-controlled destination through explicit channel-level authorization, least-privilege credentials, rate and spend limits, an audit trail, rollback where supported, and a kill switch. Never send to imported customer lists without a compliant client-owned consent process.
- Use only customer-approved screenshots, recordings, logos, fonts, music, voices, and brand assets. Do not clone a person's voice without documented consent, imitate third-party styles, or fabricate product footage, reviews, quotes, users, or endorsements. Follow current channel AI-disclosure rules.
- Treat generated captions, alt text, translations, and quizzes as drafts unless objective checks establish their stated scope. Do not claim accessibility certification, training completion, or competence from an automatically generated asset.
- Scan uploads, reject active content and unsupported archives, sanitize HTML/Markdown/URLs/filenames, isolate renderers, encrypt secrets and stored sources, minimize retention, and provide export and deletion controls.
- Preserve exact units, dates, versions, limits, and source wording where precision matters. Verify all links just before delivery, expose the tested source version, and issue visible corrections when an approved source changes.
- Use relevant, truthful, low-volume outreach with a clear opt-out. Respect anti-spam law, community rules, platform terms, robots directives, rate limits, and suppression requests.

## One-Line Pitch
One approved release bundle in; every customer and sales enablement asset out — consistent, cited, and ready to publish.

===SOCIAL===
## Twitter / X
🧵 A feature is not fully shipped when every team explains it differently.

1/ Upload the approved release bundle
2/ Extract a cited fact table
3/ Generate the changelog, help article, email, deck, explainer, FAQ, and quiz
4/ Reject unsupported or inconsistent claims
5/ Deliver drafts plus one evidence report

Source-grounded SaaS release enablement from €99 per release.

## LinkedIn
Release communication is a quiet post-production problem. Product has the specification, support needs an FAQ, customers need a help article, sales needs a deck, and marketing needs an email and short explainer. This AI pipeline turns one approved release bundle into the complete kit, maps factual claims back to exact source excerpts, and checks every format for consistency before delivery. It is not generic content multiplication; it is a versioned enablement release with evidence.

## Reddit / Community Post
Title: Testing a source-grounded release kit for small B2B SaaS teams

“I am building a pipeline that takes an approved release specification and produces a changelog draft, help article, customer email, one-pager, deck, short explainer, FAQ, and quiz. Every factual clause has to map to an exact source excerpt, and deterministic checks compare names, versions, dates, limits, links, and media across formats. It defaults to drafts and refuses contradictory source bundles. Which release asset is usually still missing when support tickets start arriving?”

## IG / TikTok / YouTube Shorts
Approved release bundle → cited fact table → article + email + deck + explainer + FAQ → consistency gate → publish-ready drafts. 🚀📚🤖

#saas #productmarketing #customereducation #releasenotes #contentoperations

## Cold Email
Subject: one release, one consistent enablement kit for {company_name}

Hi {first_name}, I noticed {specific_public_signal_about_a_recent_release_or_changelog}. I built a source-grounded post-production pipeline for small SaaS teams: one approved release bundle becomes the changelog, help article, customer email, sales deck, short explainer, FAQ, and quiz, with every factual claim mapped back to the source.

It defaults to drafts and includes a cross-format evidence report rather than an open-ended writing retainer. May I send the fictional demo kit and its QA checklist? If it is not relevant, reply “no” and I will not contact you again.
