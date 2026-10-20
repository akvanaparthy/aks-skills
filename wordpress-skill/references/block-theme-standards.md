# Block theme standards

The rules that keep a theme compatible with WordPress, its review process, and future
versions. Read the section you need.

## 1. Files

```
my-theme/
├── style.css          # header is required; CSS optional
├── theme.json         # settings + styles
├── functions.php      # enqueue, pattern categories, block styles — nothing else
├── templates/         # index.html (required), front-page, single, archive, page, 404, search …
├── parts/             # header.html, footer.html … (flat, no subfolders)
├── patterns/          # PHP files with a header comment; theme-owned patterns
├── styles/            # style variations (*.json)
├── assets/fonts|images|css|js
├── screenshot.png     # 1200×900
└── readme.txt
```

`style.css` header: `Theme Name`, `Theme URI`, `Author`, `Author URI`, `Description`,
`Version`, `Requires at least`, `Tested up to`, `Requires PHP`, `License`
(`GPL-2.0-or-later`), `License URI`, `Text Domain`, `Tags`. Bump `Version` on every
release; hosts cache `theme.json` by version.

Pattern file header:

```php
<?php
/**
 * Title: Hero with image
 * Slug: my-theme/hero-image
 * Categories: my-theme-sections, featured
 * Keywords: hero, banner
 * Block Types: core/post-content
 * Viewport Width: 1400
 * Inserter: true
 */
?>
```

Register categories in `functions.php` with `register_block_pattern_category()`.
Use `esc_html_e()` / `esc_attr_e()` for strings and `esc_url( get_theme_file_uri() )`
for placeholder images.

## 2. Theme vs plugin ("plugin territory")

Belongs in a **plugin**, never in the theme: `register_post_type`, `register_taxonomy`,
`register_post_meta`/`register_meta`, `add_shortcode`, `register_block_type` (custom
blocks), `register_rest_route`, settings pages storing non-presentational data, analytics
or SEO output, email/CRM integrations, user roles. A theme may *recommend* plugins but
not bundle them.

A theme should still render if the companion plugin is deactivated (fall back to core
blocks; show nothing or a gentle notice where plugin blocks would be).

## 3. Showing structured data in templates

**Register meta so the editor and bindings can see it:**

```php
register_post_meta( 'book', '_mt_price', [
    'type'              => 'number',
    'single'            => true,
    'show_in_rest'      => [ 'schema' => [ 'type' => 'number' ] ],
    'sanitize_callback' => 'floatval',
    'auth_callback'     => fn() => current_user_can( 'edit_posts' ),
] );
```

**Block Bindings** (WP 6.5+): bind Paragraph/Heading `content`, Image `url`/`alt`,
Button `url`/`text` to `core/post-meta`:

```html
<!-- wp:paragraph {"metadata":{"bindings":{"content":{"source":"core/post-meta","args":{"key":"_mt_price"}}}}} --><p></p><!-- /wp:paragraph -->
```

For formatted output (currency, units, computed labels) register a custom source with
`register_block_bindings_source()` and `uses_context => ['postId']`. Return `''` for
empty values and hide the wrapper with a `render_block` filter adding a class.

**Lists**: Query Loop with `postType`, taxonomy query and a pattern as the inner
template. Server-side filtering via `pre_get_posts` on query vars keeps URLs crawlable.

**Interactivity** (WP 6.5+): `data-wp-interactive` directives + a store in a module
loaded through `viewScriptModule`. Always server-render the initial state so the page
works without JS and is indexable.

## 4. Internationalisation

- One text domain per package, matching the slug; load with `load_theme_textdomain()`.
- Every string through `__()`, `_e()`, `esc_html__()`, `_n()`, `_x()`; no concatenated
  sentences; placeholders with `sprintf()`.
- Generate `.pot` with `wp i18n make-pot .`.
- Fonts: include fallbacks with coverage for the site's scripts (e.g. Devanagari,
  Arabic, CJK) in the `font-family` stack.

## 5. Security

- Escape on output: `esc_html`, `esc_attr`, `esc_url`, `wp_kses_post`.
- Sanitize on input: `sanitize_text_field`, `absint`, `esc_url_raw`, `rest_sanitize_boolean`.
- Nonces + capability checks on anything that writes.
- No `eval`, `create_function`, `extract`, `shell_exec`; no remote code loading.
- No secrets in the repo; `.gitignore` `node_modules`, `vendor`, `*.zip`, `.env`.

## 6. Performance

- Self-host fonts as WOFF2, declare via `theme.json` `fontFace`, `font-display: swap`,
  preload the one or two used above the fold.
- Keep `style.css` small; prefer presets. No jQuery, no large slider libraries.
- Scripts only where their block is present (`viewScript`/`viewScriptModule`).
- Images: let WordPress generate `srcset`/`sizes` and modern formats; explicit
  width/height; first hero image gets `fetchpriority="high"`; no CSS background images
  for LCP content.
- Embeds (maps, videos) as click-to-load facades.
- Targets: LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 on a throttled mobile run.

## 7. Accessibility

- Semantic landmarks via core blocks (`header`, `nav`, `main`, `footer`); skip link.
- One `<h1>` per view in the template, logical heading order.
- Colour contrast ≥ 4.5:1 text, ≥ 3:1 UI, checked per palette pair actually used.
- Visible focus (`:focus-visible`), keyboard-operable menus/modals/tabs, no traps.
- `prefers-reduced-motion` honoured; carousels have controls and don't autoplay.
- `alt` on meaningful images; `alt=""` on decorative ones.
- Form fields labelled; errors described; status messages in `aria-live`.

## 8. Technical SEO that is the theme's responsibility

Crawlable server-rendered markup, one H1, breadcrumbs block where appropriate,
semantic HTML, fast loading, responsive images, `rel` attributes on pagination,
`noindex` on internal site search results, and **not** printing titles/meta/canonical/
schema that an active SEO plugin already prints. Anything beyond that (structured data,
metadata, robots/sitemap, snippet controls, AI-crawler policy) is handled by the
`seo-aeo-geo` skill — follow its priorities, and don't add FAQPage/HowTo schema or
`llms.txt` on your own initiative.

## 9. WordPress.org review essentials (if submitting)

Theme Check plugin passes; unique prefix on all functions/options/handles; no hard-coded
external URLs except theme/author URIs; links in content distinguishable; no admin-bar
removal; no paywalled core features; no CPTs/shortcodes/custom blocks; licenses for
bundled fonts/images declared in `readme.txt`; screenshot shows the actual theme.

## 10. Classic themes (only when required)

Template hierarchy in PHP (`header.php`, `index.php`, `single.php`…), `wp_head()`/
`wp_footer()`, `get_template_part()`, `add_theme_support()` for title-tag, post
thumbnails, html5, editor-styles, align-wide; `theme.json` still works for editor
settings in classic themes and is worth adding.
