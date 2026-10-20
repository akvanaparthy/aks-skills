# Real-estate SEO / AEO / GEO

Extends `seo-aeo-geo`. Its ground truth stands: AEO/GEO = SEO; no FAQPage/HowTo for
rich results; `llms.txt` is P3; don't present vendor heuristics as fact. This file adds
what is specific to property sites. Evidence is graded: **[G]** Google documentation,
**[D]** third-party data with disclosed method, **[V]** vendor claim, **[E]** practitioner
experience.

## 1. What the evidence says (2026)

- **AI Overviews rarely trigger for listing/agent queries, often for place and process
  queries.** One study of 8.2M tracked real-estate queries reports AI Overview trigger
  rates of ~4.5% overall, ~11% for agent discovery, ~26% for neighbourhood research,
  ~38% for local market intel and ~53% for process/how-to questions. [D — an AI-SEO
  agency's own data; directionally useful, don't quote the decimals]
- **Portals dominate what AI knows.** The same study estimates Zillow, Realtor.com,
  Redfin, Trulia and Homes.com account for ~61% of real-estate URLs in public LLM
  training data. [D/V] In India the equivalent is 99acres, MagicBricks, Housing.com,
  NoBroker; in the UK Rightmove, Zoopla, OnTheMarket.
- **Agent/brokerage sites are technically weak.** An audit of 65 live sites across 14
  platforms found crawler 403s for generic bots, partial initial HTML on JS-heavy
  builds, missing schema on sampled pages, and generic IDX setups. [D — small sample]
  Only ~6% of top-ranked agent sites had correct Person/RealEstateAgent schema. [V]
- **Hyper-local is the demand.** ~71% of buyer queries are hyper-local (place +
  intent). [V] Buyers increasingly ask assistants "best X in {city}" style questions
  and get a few named firms, not links. [E/V]
- **Freshness correlates with citation.** 70%+ of pages cited by ChatGPT in one
  sample were updated within 12 months. [V]
- **Google: no special schema or llms.txt is needed for AI features; AI surfaces are
  retrieval over the normal index.** [G] FAQ rich results are retired. [G]

Implication: the ranking and citation opportunity for a non-portal is **place content
with original data and a named expert**, served from fast, server-rendered pages, with
the business entity consistent everywhere. Listings are for converting visitors who
already arrived.

## 2. Page architecture and URLs (approve before building)

| Page type | URL pattern (example) | Indexable? | Why it exists |
|---|---|---|---|
| Home | `/` | yes | Entity home: RealEstateAgent/Organization + WebSite |
| Buy/Rent hub | `/buy/`, `/rent/` (or `/properties/`) | yes | Top of the inventory tree; intro + featured localities |
| City | `/buy/{city}/` | yes | Market overview, price trends, localities list |
| Locality | `/buy/{city}/{locality}/` | **yes — the money page** | Unique guide + live listings + prices + landmarks + the firm's own activity there |
| Type-in-place | `/buy/{city}/{locality}/{type}/` e.g. `/3-bhk-apartments/` | only whitelisted combos with demand and stock | Query-shaped landing page |
| Project / development | `/projects/{slug}/` | yes | Long-lived; configurations, status, documents |
| Listing | `/property/{slug}-{ref}/` | yes if unique to this site; `noindex` if syndicated/MLS/IDX feed | Conversion page |
| Agent | `/agents/{slug}/` | yes | ProfilePage → Person, worksFor the business |
| Guides / insights | `/guides/{slug}/` | yes | Process, finance, legal, "how to" — the highest AI-Overview trigger class |
| Search results with params | `/buy/?price_max=…&beds=3` | **no** (`noindex,follow`, canonical to nearest whitelisted page) | UX only |
| Sold/let archive | none (sold items stay at their URL, see §4) | — | — |

Rules: slugs ASCII, lowercase, hyphenated; no dates or IDs in locality/project URLs;
listing slugs carry the reference ID so renames don't create duplicates; never change
URL structure after launch without a redirect map.

## 3. Facet indexing

Property search is the canonical faceted-navigation problem. Apply:

- **Whitelist** facet combinations that (a) match real query demand and (b) have stock:
  typically `location`, `location × type`, `location × beds`, `location × intent`.
  Give each a pretty URL, unique title/H1/intro, self-canonical, sitemap entry, and
  internal links from the parent locality page. Maintain the whitelist in plugin
  settings; generate pages from it, not from every possible combination.
- **Everything else** (price ranges, area ranges, furnishing, features, sort, page
  size, stacked filters): query parameters only, `noindex,follow`, canonical to the
  nearest whitelisted page, one fixed parameter order, excluded from sitemaps. If crawl
  volume becomes a problem, add `robots.txt` disallows for the parameter patterns — but
  only after the noindex has been processed for anything already indexed. [G guidance
  as summarised by practitioners]
- **Empty results on a whitelisted URL → 404** (or temporarily `noindex`), never an
  empty 200. [G: soft-404]
- **Pagination**: crawlable, sequentially linked, self-canonical per page; no
  `view-all` unless small.
- **Internal site search** (`?s=`) results: `noindex`.
- Before adding a facet to the whitelist, check Search Console for the query pattern;
  after adding, watch "Crawled – currently not indexed" and "Duplicate without
  user-selected canonical" reports.

## 4. Expired, sold and let listings

The decision depends on value and links, not habit:

- **Has inbound links or steady traffic** → keep the page live with a clear
  "Sold/Let" state, price history if allowed, links to similar stock and the locality
  page; keep indexable for a period, then `noindex`. Mark `Offer.availability` as
  `SoldOut`. Keep out of archives and sitemaps from day one.
- **No links, no traffic** → `noindex` immediately; return **410** after ~30 days.
- **Redirect only to a genuinely similar page** (same project, same locality + type);
  redirecting to the home page or a broad archive is a soft-404 in Google's eyes.
- **Syndicated/IDX stock** that was never unique: `noindex` from the start, so expiry
  needs no handling at all.
- If you know the expiry date (rental availability, auction), use `unavailable_after`
  in the robots meta.

## 5. Structured data per page type

Google has **no rich result for property listings** (no price/beds display from
`RealEstateListing`) [G/E]; markup still helps entity understanding and is harmless.
Use JSON-LD, one `@graph` per page, site-wide entities emitted once, values identical
to visible content, numbers without separators or symbols.

| Page | Types | Notes |
|---|---|---|
| Site-wide | `RealEstateAgent` (+ `Organization`) with `@id`, logo, `sameAs`, `areaServed`, `telephone`, address, licence as `identifier`; `WebSite` with `SearchAction` | Emit in one place only; coordinate with Yoast/Rank Math/AIOSEO (they already emit Organization/WebSite — hook into their graph rather than duplicate) |
| Listing | `RealEstateListing` → `about`: `Apartment` / `House` / `SingleFamilyResidence` / `Place` (plots, commercial) with `numberOfBedrooms`, `numberOfBathroomsTotal`, `floorSize` (`QuantitativeValue` + `unitCode`), `address`, `geo`, `amenityFeature`, `image`; `offers`: `Offer` with `price`, `priceCurrency`, `availability`, `businessFunction` (`Sell`/`LeaseOut`), `priceSpecification.unitText: MONTH` for rentals; `datePosted`; `BreadcrumbList` | Availability lives on `Offer`, not on the listing [E — common error]; only on the listing page itself |
| Project | `ApartmentComplex` (or `Place` for mixed/plots) with `numberOfAccommodationUnits`, `petsAllowed` if relevant; `AggregateOffer` (`lowPrice`, `highPrice`, `priceCurrency`); `BreadcrumbList`; `ImageObject`/`VideoObject` | Status/possession as visible text; don't invent dates |
| Locality / city | `Place` (`name`, `geo`, `containedInPlace`), `BreadcrumbList`, `ItemList` of the listings shown (≤ 20), `Article` if the page has an authored guide with author + dates, `Dataset` only for a real downloadable dataset | The authored guide is what gets cited; mark the author as a `Person` |
| Agent | `ProfilePage` → `mainEntity: Person` (`jobTitle`, `worksFor` → the business `@id`, `knowsAbout`, licence as `identifier`, `sameAs`) | |
| Guides | `Article`/`BlogPosting` with real author, `datePublished`, `dateModified`, `image` | |
| Open house / launch event | `Event` only for a real, dated event | |
| Reviews | `AggregateRating` only from first-party reviews that are visible and genuine | Fabricated ratings are a spam-policy violation |

Validate with the Rich Results Test (for the types Google does feature: breadcrumbs,
article, organisation logo, events) and the Schema Markup Validator (for the rest).

## 6. Content that ranks and gets cited

**Locality page (the template that matters).** Required unique content per page:
- A 40–80-word direct answer under the H1 ("{Locality} is a {description}; typical
  {type} prices run {range} as of {month year}") — written by a human or generated
  from the firm's own data, dated, with an author.
- Original numbers: current asking-price range and per-area figure from the site's
  own stock; rental yields if known; supply counts (how many on this site);
  month-over-month change if tracked. Present in a table.
- Specifics only true of this place: landmarks with distances, commute times to
  named hubs, schools, transit, upcoming infrastructure, micro-areas within the locality.
- The firm's own footprint: transactions closed here, agents who cover it, client
  stories.
- Live listings (Query Loop) and whitelisted sub-pages (type × locality).
- Last-updated date visible and honoured (regenerate numbers on a schedule).

Twenty well-made locality pages beat two hundred templated ones; the latter risk the
doorway/scaled-content policies [G].

**Guides** phrased as the questions people ask assistants ("How does the home-buying
process work in {city}?", "Stamp duty in {state} in {year}"), each with the answer in
the first sentence under its H2, key facts early, tables for comparable numbers, named
author with credentials, dates. These are the pages most likely to appear in AI
Overviews/AI Mode and assistant answers [D].

**Entity consistency.** Same business name, address, phone, licence number and
service-area list on the site, Google Business Profile, portals, directories and
social profiles. Put quotable plain-language facts on the About page ("{Firm} has
closed {n} transactions in {city} since {year}").

**Reviews.** Earn first-party and Google reviews; display them with attribution. Vendor
data associates review volume across several platforms with assistant mentions [V];
genuine reviews are also simply trust.

**Multi-modal.** Property video tours and locality walk-throughs with transcripts and
captions give assistants text to cite and give Google video results [V/E].

## 7. Crawling and rendering checklist for property sites

- Listing and locality content present in the initial HTML (Interactivity API is
  fine; client-only fetched listings are not).
- Googlebot, Bingbot and search-indexing AI bots allowed (`OAI-SearchBot`,
  `Claude-SearchBot`, `PerplexityBot`, `Applebot`); training bots are a business
  decision; CDN/WAF rules don't 403 verified crawlers (test with a non-browser UA).
- Image sitemap or image entries for listing galleries; `alt` text that names the
  room/view and place.
- XML sitemaps: localities, projects, agents, guides, unique listings; never
  parameter URLs, sold/withdrawn, or imported-feed stock.
- Core Web Vitals on `single-property` and the locality template measured on a
  throttled mobile run; galleries and maps are the usual LCP/INP offenders.
- `hreflang` only if the site truly has language variants; `en-IN` vs `en-US` alone is
  not a reason.

## 8. Measurement

Search Console: filter queries by locality names; use the Search generative AI
performance report where available. GA4: segment referrals from chatgpt.com,
perplexity.ai, gemini.google.com, copilot. Re-run a fixed set of buyer prompts monthly
across assistants and log which firms are named. Tie enquiries to landing page type
(locality vs listing vs guide) so the content investment can be judged on leads, not
sessions.
