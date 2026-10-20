# Market specifics

Read the section for the project's country. These affect fields, formatting,
compliance blocks, and which portals/feeds matter. Not legal advice — confirm with the
client's counsel where it matters.

## India

**Regulation — RERA (Real Estate (Regulation and Development) Act, 2016).** Each state/UT
has its own authority and portal (MahaRERA, TG RERA, K-RERA, UP RERA, Gujarat RERA,
HARERA, WBRERA, TN RERA…). Promoters must display the project's registration number
and the RERA website address in every advertisement and prospectus (Section 11(2));
authorities such as WBRERA have ordered that it be clearly visible. Treat the website as
advertising: a RERA block on every project and project-linked listing, linking to the
state portal; the firm's **agent** registration number in the footer. Formats are
state-specific (e.g. Maharashtra `P5190000XXXX`, Telangana `P0240000XXXX`, Karnataka
`PRM/KA/RERA/…`); store raw, validate loosely, warn on mismatch. Small plots/projects can
be exempt — allow "Not applicable" rather than blank. **Carpet area** is the
RERA-defined headline figure; show it first, built-up / super built-up second.

**Units and formatting.** Prices: Indian numbering — `₹ 45,000` below 1 lakh,
`₹ 85 L` / `₹ 85 Lakh` from 1 lakh, `₹ 1.25 Cr` from 1 crore; store integer rupees;
offer an "international" display (`₹ 12,500,000`) for NRI audiences. Price per sq ft is
a standard comparison metric. Area units: sq ft default; sq yd (plots, north/west),
sq m, acre, cent (south), guntha (MH/KA), bigha (north; varies by state — show as
entered). Configuration vocabulary is **BHK** (1 RK, 1–5+ BHK, allow .5).
Possession: Ready to Move / Under Construction (month-year) / New Launch. Facing
(Vastu) matters. Floor "7th of 18"; 0 = Ground. Phones: 10 digits starting 6–9,
display `+91 98765 43210`. Timezone Asia/Kolkata. Prices for under-construction stock
are often quoted "+ GST"; make the suffix a setting.

**Behaviour and trust.** Traffic is mostly mobile (mid-range Android, 4G): sticky
Call / WhatsApp / Enquire bar, filter drawer, map as opt-in. WhatsApp
(`https://wa.me/91…?text=`) is the preferred contact channel. Trust signals buyers
look for: RERA, developer track record, bank loan approvals (logos from settings),
possession timeline, approvals/legal documents list (OC/CC, title), Vastu compliance,
Google reviews, verified badge, EMI calculator (default ~8.5 %, 20 years), nearby
landmarks with distances (metro, IT parks, schools, hospitals, airport). Locality pages
often include transliterated names in Hindi/Telugu/Kannada script — fonts need
Devanagari/regional fallbacks.

**SEO.** Portals: 99acres, MagicBricks, Housing.com, NoBroker, Square Yards. Query
shapes: `{type} in {locality}` ("3 BHK flats in Gachibowli"), `{locality} + budget`
("flats in Thane under 1 crore"), `{project name} price/possession/reviews`,
`{locality} property rates`. Locale `en_IN`; Hindi content optional, no RTL. Locality
+ project pages are the money pages; price-trend and RERA/documentation guides earn
citations.

**Privacy.** Digital Personal Data Protection Act 2023: collect only what's needed,
unticked consent line, deletion on request. Advertising: avoid "guaranteed returns";
"*T&C apply" where prices are "starting at".

## United States

**MLS / IDX.** Most brokerage sites display shared MLS inventory through an IDX
vendor. That stock is duplicated across every agent site in the market, often rendered
client-side, and must be displayed as provided (little room for unique text). Treat IDX
pages as a visitor tool: `noindex` unless the vendor provides crawlable, canonical pages
and the firm is the listing broker; put SEO effort into neighbourhood, community/
building and guide pages, and into the firm's **own** listings (full pages, unique
copy, `Offer` with `InStock`). Watch listing-status churn (active → pending → sold)
and MLS rules on displaying sold data.

**Compliance.** Fair Housing: no language implying preference by protected class
(e.g. "perfect for families", "safe neighbourhood", "walking distance to church"); add
the Equal Housing Opportunity logo; MLS attribution and broker licence number per state;
TCPA consent language on lead forms (express written consent for calls/texts); some
states require agent licence numbers in advertising.

**Units and formatting.** `$1,250,000`; sq ft; lot size in acres or sq ft; `3 bd · 2 ba`;
HOA fees; property tax; year built; ZIP; `tel:` with E.164; mortgage calculator with
rate/term/down payment and taxes/insurance.

**Portals / entities.** Zillow, Realtor.com, Redfin, Trulia, Homes.com dominate AI
training data and citations; neighbourhood guides, school/commute data, "best
neighbourhoods in {city} for {need}", market reports, and the agent's own transaction
record are what differentiate. Google Business Profile per office and per agent where
allowed.

## United Kingdom / EU

**UK.** Portals: Rightmove, Zoopla, OnTheMarket; agents usually push listings via a
feed (BLM/RTDF) from their CRM — the website may import the same feed (mark `source`).
Required/expected on listings: **EPC** rating (and link), council tax band, tenure
(freehold/leasehold with remaining lease years), ground rent/service charge for
leaseholds, floor plan, material information (NTSELAT Parts A–C). Prices: `£450,000`
or `Guide price`/`Offers over`; rent `pcm`/`pw`; sq ft and sq m; "2 bed, 1 bath".
Redress scheme and company registration in the footer; GDPR consent on forms.
"Sold STC" / "Let agreed" statuses are standard and should stay visible.

**EU (general).** EPC/energy label is mandatory in listings in most member states;
prices in EUR with local separators; sq m; agency licence numbers per country (e.g.
Spain, Italy); GDPR. Multilingual sites are common — this is where `hreflang` is
actually needed (e.g. `es`, `en`, `de` on a Spanish coast site).

## Adding another market

Capture: currency/number format; area units and the legally defined area; room
vocabulary; mandatory identifiers and where they must appear; sale-status vocabulary;
preferred contact channel; dominant portals (for feeds and for the citation
landscape); privacy and advertising rules. Put all of it in plugin settings and
formatting callbacks — never in the theme.
