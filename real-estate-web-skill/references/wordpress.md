# Real estate on WordPress

Extends `wordpress-skill`. All of this lives in the companion plugin (data, blocks,
leads); the theme only displays it.

## 1. Entities

Pick the primary entity from the business type (SKILL.md "Decisions"):

| Entity (CPT) | Use when | Key relations |
|---|---|---|
| `property` | Every site: a unit, house, plot, office… that can be bought or rented | belongs to a `project` (optional), has an `agent`, has a `location` term |
| `project` | Developers/builders; new-launch and under-construction stock; also "building/community" pages for brokerages | has many `property` (unit configurations), `location`, `developer` |
| `agent` | Brokerages with a team; optional for a solo agent (use the author) | has many `property` |
| `developer` | Portals or brokerages listing other builders' projects | has many `project` |
| `enquiry` (private) | Always — local copy of every lead | links to property/project/agent |

Taxonomies (all `show_in_rest`, with admin columns):

| Taxonomy | Hierarchical | Notes |
|---|---|---|
| `property_type` | no | Apartment/Flat, House/Villa, Townhouse, Plot/Land, Office, Retail, Warehouse… market-specific list in `markets.md` |
| `listing_status` | no | For Sale, For Rent, Under Offer, Sold, Let, Withdrawn — drives lifecycle (§3) |
| `location` | **yes** | Country › State/Region › City › Locality/Neighbourhood (› Sub-locality). The spine of the SEO architecture. |
| `feature` | no | Amenities: pool, gym, parking, lift, security, garden… |
| `possession` / `availability` | no | Ready / Under construction / New launch (sales); Available now / From date (rentals) |
| `furnishing` | no | Unfurnished / Part / Fully (rentals mostly) |

Meta (prefix with the plugin slug; `register_post_meta` with schema, sanitize, auth):

- Pricing: `price` (integer, minor units avoided — store whole currency units),
  `price_currency`, `price_on_request` (bool), `rent_period` (`month|week|year`),
  `deposit`, `maintenance`, `price_per_area` (computed), `price_suffix` (e.g. "+ taxes")
- Size: `bedrooms` (number, allow 0 and .5), `bedroom_label` ("3 BHK", "Studio"),
  `bathrooms`, `area_primary` + `area_primary_type` (`carpet|net internal|living|built-up|super built-up|gross`),
  `area_secondary` (+type), `area_unit` (`sqft|sqm|sqyd|acre|ha|…`), `plot_area`, `plot_unit`
- Building: `floor` (int; 0 = ground), `total_floors`, `year_built`, `orientation/facing`,
  `parking` (text), `furnishing` (taxonomy)
- Timeline: `availability_date`, `possession_date` (YYYY-MM), `listed_at`, `sold_at`
- Legal/compliance (market-specific, see `markets.md`): `rera_number` + `rera_state`
  + `rera_url`; `mls_number`; `epc_rating` + `epc_url`; `council_tax_band`
- Location: `lat`, `lng`, `address_line`, `postcode`, `landmarks` (array of {name, distance, unit, type})
- Media: `gallery` (attachment IDs), `floor_plans`, `brochure_id`, `video_url`, `tour_url`
- Relations: `project_id`, `agent_id`, `developer_id`
- Flags: `featured`, `verified`, `exclusive`, `reference_id` (public ref like `HYD-0231`)

Project adds: `price_min`, `price_max`, `configurations` (array of {label, area, price_from}),
`units_total`, `towers`, `launch_date`, `completion_date`, `master_plan_id`,
`approvals`/`documents` (array), plus the same legal/location/media fields.

## 2. Editor experience

Editors won't use raw custom fields. Give `property` a plugin sidebar panel with grouped
controls (Price, Size, Building, Timeline, Legal, Location with map pin picker, Media,
Relations) via `PluginDocumentSettingPanel` + `useEntityProp`. Validate on save:
price present unless `price_on_request`; `location` term required; legal identifier
required when the market mandates it (warn, don't block, for exempt stock).

Bulk entry/import: a CSV/XML importer with field mapping (portal and MLS feeds vary) and
a dry-run report; mark imported listings with `source` + `source_id` so re-imports
update instead of duplicating, and so the SEO layer can `noindex` syndicated stock.

## 3. Lifecycle (this is where property sites rot)

| Status | Front end | Index policy | Schema `availability` |
|---|---|---|---|
| For Sale / For Rent | full page, all CTAs | per SEO reference (indexable only if the listing is unique to this site) | `InStock` |
| Under Offer / Reserved | full page, badge, CTA "register interest" | unchanged | `LimitedAvailability` (or `InStock` with a visible notice) |
| Sold / Let | page stays, badge, price shown as "Sold at"/"Let", CTA → similar properties + locality page; removed from archives and sitemaps | keep indexable 30–90 days if it has links/traffic, then `noindex`; delete (410) only if it never earned traffic | `SoldOut` |
| Withdrawn / expired | same as sold but with "no longer available" | `noindex` immediately; 410 after 30 days unless linked | `Discontinued` |

Implement as a scheduled job: on status change, set the index flag, drop from
archives (`pre_get_posts`), regenerate sitemaps, and queue a re-check at +30/+90 days.
Never redirect a sold listing to the home page or a generic archive (soft-404); if you
redirect at all, redirect to the same project or the locality page.

Projects/developments persist across phases; keep their URL forever and update
configurations and status (New launch → Under construction → Ready → Sold out).

## 4. Search and filters

- One block, Interactivity API, server-rendered form that works without JS.
- Facets: location (hierarchical, type-ahead), type, status/intent (buy/rent toggle),
  price range (market-aware formatting), beds, baths, area range, possession,
  furnishing, features, keyword, sort. Everything maps to query vars; the archive's
  Query Loop is filtered server-side via `pre_get_posts`; the Interactivity store
  mirrors state to the URL (`history.replaceState`) and fetches a REST endpoint for
  live updates. Pagination and location drill-down stay as real `<a href>` links.
- REST `GET /<plugin>/v1/search`: sanitized params, `WP_Query` with numeric meta
  queries, `include_children` on location, transient cache keyed by normalized args,
  per-IP rate limit, facet counts in the response, and card payloads (not full posts).
- Index-only-what-is-whitelisted: see the SEO reference §3 for which facet URLs get
  pretty paths, titles and self-canonicals.
- Empty result sets return 200 with suggestions on the main archive but **404** on
  whitelisted landing URLs that no longer have stock (otherwise they become soft-404s).
- Map: optional half-map layout; marker clustering; bounding-box search updates the
  list; click-to-load the map library on mobile; price labels on pins. Draw-to-search
  is a nice-to-have, not a default.
- Saved searches / alerts: only if the business will act on them (they create
  expectations); store as a private CPT with a cron digest.

## 5. Listing and project page anatomy (what converts)

Above the fold: gallery (first image is the LCP element — explicit dimensions,
`fetchpriority="high"`), title with reference ID, price (+ per-area), key facts strip
(beds · baths · area · status/possession), primary CTAs (Call, WhatsApp/SMS, Enquire /
Book a viewing), agent card. Then: description, features, floor plans, location map +
landmarks with distances, project details (if any), compliance block (licence/RERA/EPC
with link to the official portal), calculator (EMI/mortgage — default rate and tenure
from settings), similar properties (same locality ± price band), locality page link.
Mobile: sticky bottom bar with the three CTAs; tabs or accordions for the long sections.

## 6. Leads

Enquiry form block (Interactivity API, no-JS fallback) → `POST /<plugin>/v1/leads` with
nonce, honeypot, time-to-submit check, optional Turnstile, phone validation per market,
consent checkbox → store `enquiry` post first → email the assigned agent immediately →
queue CRM push via Action Scheduler (fallback WP-Cron) with 3 retries → admin list with
status, retry, CSV export, delete (privacy requests).

Attribution captured on first visit into a first-party cookie and attached to every
lead: UTM set, `gclid`/`fbclid`, landing page, referrer; plus the property/project ref,
URL, locality, price and bed count at submission. Also log call and WhatsApp clicks as
"activity" leads and push a `dataLayer` event so ads platforms can optimise.

CRM layer is a provider interface (`push_lead(array): Result`, `test(): bool`) with an
email provider always on and a generic webhook provider (Zoho Flow, HubSpot, Make,
n8n). Vendor-specific providers (Zoho CRM, HubSpot, Salesforce, LeadSquared) are
added per client; tokens encrypted at rest; never logged.

## 7. Performance on image-heavy pages

- Galleries: WordPress-generated sizes + `sizes` attributes; first slide eager, others
  lazy; a lightbox that loads only on interaction; limit thumbnails to the first 12 and
  paginate the rest.
- Card grids: `loading="lazy"` except the first row; fixed aspect ratio boxes to kill CLS.
- Maps and video tours: facades until clicked.
- Search: cache the REST results; don't run facet counts on every keystroke (debounce,
  and cache counts separately).
- Listing archives with thousands of posts: index the meta keys you filter on (add
  a custom table or `meta_key`+`meta_value` composite indexes) before it gets slow.

## 8. Theme responsibilities (the only things the theme owns here)

Templates `single-property`, `archive-property`, `taxonomy-location`,
`single-project`, `archive-project`, `single-agent`; a `property-card` pattern; style
tokens for status badges (sale/rent/sold) and the key-facts strip; a `mobile-cta`
template part; sensible defaults for the compliance block. All values arrive via
Block Bindings (`core/post-meta` raw, `<plugin>/field` formatted).
