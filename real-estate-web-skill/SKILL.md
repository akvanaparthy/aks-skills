---
name: real-estate-web
description: Real-estate domain layer for building property websites — listings, projects/developments, agents, locality/neighbourhood pages, property search, lead capture — on top of the wordpress-skill and seo-aeo-geo skills. Use whenever the project is a real-estate, property, realtor, broker, developer/builder, rental, or listings site, in any country, even if the user doesn't say "real estate" (words like listings, properties, BHK, MLS, IDX, RERA, locality, neighbourhood, open house, floor plan, EMI/mortgage calculator are the tell). Load it after the base skill it extends.
compatibility: Extends wordpress-skill (theme + companion plugin) and seo-aeo-geo (technical SEO / AI-search). Works without them but assumes their rules.
---

# Real-estate web layer

What is actually different about property sites, and only that. Everything generic —
how to build a block theme, how to do technical SEO — stays in the base skills. This
layer answers the questions those skills can't: what the data model is, which pages
rank, what to do with sold listings, how search facets should be indexed, what schema
means for a listing, and how leads move.

## What is different (the short version)

1. **Inventory churns.** Listings appear, go pending, sell, expire. The site needs an
   explicit lifecycle (`active → under offer → sold/let → archived`) with a URL policy
   for every state. Most SEO damage on property sites comes from ignoring this.
2. **The money pages are not the listings.** Individual listings are near-duplicates of
   what portals already show (shared inventory, syndication, MLS/IDX). Locality /
   neighbourhood, project / development, and market-insight pages are where a
   brokerage or developer can rank and be cited. Listings convert; localities rank.
3. **Search is faceted.** Price × beds × type × area × status explodes into millions of
   URLs. Index only a whitelist; keep everything else crawl-controlled.
4. **Data has domain shape.** Price (sale vs rent, per-period), area in several
   definitions and units, bedrooms (BHK, studio), floor level, orientation, possession /
   availability date, legal identifiers (RERA, MLS number, EPC), geo, gallery, floor
   plans, documents. Model it once, in a plugin, with formatted bindings.
5. **Conversion is a phone call.** Call, WhatsApp/SMS, "book a viewing", "download
   brochure", "get price". Every listing and project page needs those above the fold
   and sticky on mobile, and every lead needs attribution (which property, which
   campaign) before it reaches the CRM.
6. **Trust is regulated.** Licence / registration numbers (RERA in India, MLS and
   state licence in the US, EPC rating in the UK/EU) must be displayed; advertising rules
   exist. Treat compliance fields as first-class, not footnotes.
7. **AI search cares about places and process, not listings.** Data from 2026 (vendor
   studies, graded in the SEO reference) shows AI Overviews trigger far more for
   "neighbourhood research", "local market" and "how does X work" queries than for
   agent or listing queries, and that portals dominate citations. The win is original
   local data and named-expert content, not schema tricks.

## How to use this layer

- **Building the site (theme + plugin):** follow `wordpress-skill`, then read
  `references/wordpress.md` for the data model, search/filters, lifecycle, lead capture
  and performance patterns specific to property sites.
- **SEO / AEO / GEO work:** follow `seo-aeo-geo`'s priorities and ground truth, then read
  `references/seo-aeo-geo.md` for page architecture, facet indexing, expired-listing
  policy, schema per page type, and what the evidence says about AI visibility in
  real estate.
- **Market rules:** `references/markets.md` for India (RERA, ₹ lakh/crore, BHK, carpet
  area), US (MLS/IDX, Fair Housing), UK/EU (EPC, Rightmove/Zoopla feeds) — read the
  section for the project's country.

## Decisions to confirm with the user early

Ask these once, up front; they are expensive to change later:

- Country/market → units, currency display, legal identifiers, portal feeds.
- Inventory source: hand-entered in WordPress, imported feed (MLS/IDX, CRM, XML/CSV from
  a portal), or both. Imported feeds usually mean listing pages should be `noindex`
  and the SEO effort goes into locality/project pages.
- Business type: brokerage/agent (many listings, short-lived) vs developer/builder (few
  projects, long-lived, unit configurations) vs rental operator vs portal. This decides
  whether `project` is the primary entity or `property` is.
- URL structure (see SEO reference §2) — approve before building anything.
- CRM/destination for leads and what fields it needs.

## Guardrails

- Don't let listing pages become the SEO plan. If the user asks to "rank our listings",
  explain the shared-inventory problem and propose locality/project pages instead.
- Don't generate hundreds of near-identical locality or "type-in-city" pages from a
  template. Google's doorway-page and scaled-content policies apply; each indexable page
  needs content that only exists for that place (prices, supply, landmarks, commute,
  schools, the firm's own transactions there).
- Don't add FAQPage/HowTo schema for rich results, `llms.txt` as a priority, or
  "GEO score" claims — the base `seo-aeo-geo` skill's ground truth holds here too.
- Don't fabricate figures in schema or on pages (price, rating, review counts, dates,
  area). Everything machine-readable must match what is visible.
- Don't hard-code a brand, licence number, phone, or city in the theme; all of it is
  settings or content.

## References

- `references/wordpress.md` — entities and fields, lifecycle, search/filters (Interactivity
  API + URL params), map/list UX, lead capture + attribution + CRM provider pattern,
  performance on image-heavy pages
- `references/seo-aeo-geo.md` — page architecture that ranks, URL design, facet indexing
  rules, expired/sold listing policy, schema per page type, AI-search evidence (graded)
- `references/markets.md` — India, US, UK/EU specifics
