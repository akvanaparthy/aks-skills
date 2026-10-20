#!/usr/bin/env node
/**
 * validate_theme.mjs — quick structural checks for a reusable WordPress block theme.
 *
 * Usage: node validate_theme.mjs <theme-dir> [--plugin <plugin-dir>] [--json]
 *
 * Checks (theme):
 *  - style.css header has required fields (Theme Name, Version, Text Domain, License, Requires PHP)
 *  - theme.json exists, parses, has "version"
 *  - templates/index.html exists; parts/ has no subdirectories
 *  - no raw hex colours in templates/, parts/, patterns/ (use presets)
 *  - no hard-coded Google Fonts / external font CDNs
 *  - functions.php has no plugin-territory code (register_post_type, register_taxonomy,
 *    add_shortcode, register_block_type, register_rest_route)
 *  - pattern PHP strings are wrapped in a translation function (heuristic)
 *  - text domain used in PHP matches style.css
 * Checks (plugin, optional):
 *  - main plugin file header present
 *  - every register_post_meta call includes show_in_rest
 *  - no secrets-looking strings committed (zoho client secret, oauth tokens)
 *
 * Exit code 1 on any ERROR; warnings don't fail.
 */
import fs from 'node:fs';
import path from 'node:path';

const args = process.argv.slice(2);
if (!args[0]) {
  console.error('Usage: node validate_theme.mjs <theme-dir> [--plugin <plugin-dir>] [--json]');
  process.exit(2);
}
const themeDir = path.resolve(args[0]);
const pluginIdx = args.indexOf('--plugin');
const pluginDir = pluginIdx > -1 ? path.resolve(args[pluginIdx + 1]) : null;
const asJson = args.includes('--json');

const errors = [];
const warnings = [];
const err = (file, msg) => errors.push({ file, msg });
const warn = (file, msg) => warnings.push({ file, msg });

function walk(dir, exts, acc = []) {
  if (!fs.existsSync(dir)) return acc;
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (['node_modules', 'vendor', '.git'].includes(entry.name)) continue;
      walk(full, exts, acc);
    } else if (exts.some((e) => entry.name.endsWith(e))) {
      acc.push(full);
    }
  }
  return acc;
}
const rel = (f) => path.relative(process.cwd(), f);

// ---------- theme ----------
const styleCss = path.join(themeDir, 'style.css');
let textDomain = null;
if (!fs.existsSync(styleCss)) {
  err('style.css', 'missing');
} else {
  const head = fs.readFileSync(styleCss, 'utf8').slice(0, 4000);
  const fields = ['Theme Name', 'Version', 'Text Domain', 'License', 'Requires PHP', 'Requires at least', 'Description', 'Author'];
  for (const f of fields) {
    if (!new RegExp(`^\\s*\\*?\\s*${f}:`, 'mi').test(head)) err('style.css', `header field "${f}" missing`);
  }
  const td = head.match(/Text Domain:\s*([\w-]+)/i);
  if (td) textDomain = td[1];
  if (/WordPress|Theme\b/i.test((head.match(/Theme Name:\s*(.+)/i) || [])[1] || '') && !/WordPress Theme Name/i.test(head)) {
    warn('style.css', 'Theme Name should not contain "WordPress" or "Theme" (directory rule)');
  }
}

const themeJsonPath = path.join(themeDir, 'theme.json');
if (!fs.existsSync(themeJsonPath)) {
  err('theme.json', 'missing');
} else {
  try {
    const tj = JSON.parse(fs.readFileSync(themeJsonPath, 'utf8'));
    if (!tj.version) err('theme.json', '"version" missing');
    if (tj.settings?.color?.defaultPalette !== false) warn('theme.json', 'settings.color.defaultPalette should be false for a branded theme');
    const palette = tj.settings?.color?.palette || [];
    for (const slug of ['base', 'contrast', 'primary']) {
      if (!palette.some((p) => p.slug === slug)) warn('theme.json', `palette lacks "${slug}" slug`);
    }
    const fams = tj.settings?.typography?.fontFamilies || [];
    for (const f of fams) {
      const src = JSON.stringify(f.fontFace || []);
      if (/fonts\.googleapis|fonts\.gstatic|use\.typekit/i.test(src)) err('theme.json', `font "${f.slug}" loads from an external CDN; self-host it`);
    }
  } catch (e) {
    err('theme.json', `invalid JSON: ${e.message}`);
  }
}

if (!fs.existsSync(path.join(themeDir, 'templates', 'index.html'))) err('templates/index.html', 'missing (required for a block theme)');

const partsDir = path.join(themeDir, 'parts');
if (fs.existsSync(partsDir)) {
  for (const e of fs.readdirSync(partsDir, { withFileTypes: true })) {
    if (e.isDirectory()) err(`parts/${e.name}`, 'template parts cannot be in subdirectories');
  }
}

// raw colours / external fonts in markup
const markupFiles = [
  ...walk(path.join(themeDir, 'templates'), ['.html']),
  ...walk(path.join(themeDir, 'parts'), ['.html']),
  ...walk(path.join(themeDir, 'patterns'), ['.php']),
];
const hexRe = /#(?:[0-9a-f]{3}){1,2}\b/gi;
for (const f of markupFiles) {
  const src = fs.readFileSync(f, 'utf8');
  const hexes = (src.match(hexRe) || []).filter((h) => !/^#(fff|ffffff|000|000000)$/i.test(h));
  if (hexes.length) warn(rel(f), `raw hex colour(s) ${[...new Set(hexes)].slice(0, 5).join(', ')} — use theme.json presets`);
  if (/fonts\.googleapis\.com|fonts\.gstatic\.com/i.test(src)) err(rel(f), 'external Google Fonts reference');
  if (/https?:\/\/(?!schema\.org|www\.w3\.org)[^"'\s)]+\.(?:png|jpe?g|webp|svg|avif)/i.test(src) && !/get_(?:template|theme)_(?:directory|file)_uri|get_stylesheet_directory_uri/.test(src)) {
    warn(rel(f), 'absolute image URL; use get_theme_file_uri() placeholders');
  }
}

// generated-page tells (design-quality.md §3) — warnings only
const allMarkup = markupFiles.map((f) => [f, fs.readFileSync(f, 'utf8')]);
const tells = [
  [/[→➜➔]\s*<\/(a|button|span|div)>/g, 'arrow glued to link/button text'],
  [/\s·\s[^<]{1,40}\s·\s/g, 'middle-dot meta strings (A · B · C)'],
  [/"textTransform":"uppercase"[^}]{0,80}"letterSpacing"/g, 'tracked-out all-caps label (eyebrow)'],
  [/\b0[1-3]\s*<\/(span|p|div|h[1-6])>/g, 'numbered 01/02/03 markers — only if content is a sequence'],
  [/#(?:0b0b0b|111111|111)\b/gi, 'tinted near-black standing in for black'],
  [/rgba\(0,\s*0,\s*0,\s*0?\.1\)/g, 'the generic soft grey card shadow'],
  [/[\u{1F300}-\u{1FAFF}]/gu, 'emoji used as icons'],
];
const tellCounts = new Map();
for (const [f, src] of allMarkup) {
  for (const [re, label] of tells) {
    const n = (src.match(re) || []).length;
    if (n) tellCounts.set(label, (tellCounts.get(label) || 0) + n);
  }
}
for (const [label, n] of tellCounts) warn('design', `${label} ×${n} — a choice or a default? (design-quality.md §3)`);
const hexAll = new Set(allMarkup.flatMap(([, s]) => (s.match(hexRe) || []).map((h) => h.toLowerCase())));
if (['#f4f1ea', '#d97757'].some((h) => hexAll.has(h))) warn('design', 'cream + terracotta palette is the most common generated default');

// pattern translation heuristic + text domain
const patternFiles = walk(path.join(themeDir, 'patterns'), ['.php']);
for (const f of patternFiles) {
  const src = fs.readFileSync(f, 'utf8');
  if (!/^\s*<\?php\s*\/\*\*[\s\S]*?Title:/m.test(src)) err(rel(f), 'pattern header (Title:) missing');
  // text between > and < that contains letters and isn't inside PHP
  const stripped = src.replace(/<\?php[\s\S]*?\?>/g, '');
  const plain = stripped.match(/>\s*([A-Za-z][^<>{}]{3,})\s*</g) || [];
  const suspicious = plain.map((m) => m.replace(/^>\s*|\s*<$/g, '').trim()).filter((t) => !/^(wp:|\/wp:)/.test(t) && /[a-z]{3,}\s[a-z]{3,}/i.test(t));
  if (suspicious.length) warn(rel(f), `possible untranslated text: "${suspicious[0].slice(0, 50)}"${suspicious.length > 1 ? ` (+${suspicious.length - 1})` : ''}`);
  if (textDomain) {
    const wrongTd = [...src.matchAll(/(?:__|_e|esc_html__|esc_html_e|esc_attr__|esc_attr_e|_x)\(\s*'[^']*'\s*,\s*'([^']+)'/g)].map((m) => m[1]).filter((d) => d !== textDomain);
    if (wrongTd.length) err(rel(f), `text domain "${wrongTd[0]}" ≠ style.css Text Domain "${textDomain}"`);
  }
}

// plugin-territory in theme PHP
const themePhp = walk(themeDir, ['.php']).filter((f) => !f.includes(`${path.sep}patterns${path.sep}`));
const territory = ['register_post_type', 'register_taxonomy', 'add_shortcode', 'register_block_type', 'register_rest_route', 'register_post_meta', 'register_meta'];
for (const f of themePhp) {
  const src = fs.readFileSync(f, 'utf8');
  for (const fn of territory) {
    if (new RegExp(`\\b${fn}\\s*\\(`).test(src)) err(rel(f), `${fn}() is plugin territory — move to property-core`);
  }
  if (/wp_enqueue_script\([^)]*jquery/i.test(src)) warn(rel(f), 'enqueues jQuery');
  if (textDomain) {
    const wrongTd = [...src.matchAll(/(?:__|_e|esc_html__|esc_html_e|esc_attr__|esc_attr_e|_x)\(\s*'[^']*'\s*,\s*'([^']+)'/g)].map((m) => m[1]).filter((d) => d !== textDomain);
    if (wrongTd.length) err(rel(f), `text domain "${wrongTd[0]}" ≠ "${textDomain}"`);
  }
}

// ---------- plugin (optional) ----------
if (pluginDir) {
  const phpFiles = walk(pluginDir, ['.php']);
  const main = phpFiles.find((f) => /Plugin Name:/.test(fs.readFileSync(f, 'utf8').slice(0, 3000)));
  if (!main) err('plugin', 'no file with a "Plugin Name:" header found');
  for (const f of phpFiles) {
    const src = fs.readFileSync(f, 'utf8');
    for (const m of src.matchAll(/register_(?:post_)?meta\s*\(([\s\S]*?)\);/g)) {
      if (!/show_in_rest/.test(m[1])) err(rel(f), 'register_meta without show_in_rest (Block Bindings / REST need it)');
      if (!/sanitize_callback/.test(m[1])) warn(rel(f), 'register_meta without sanitize_callback');
    }
    if (/\$_(GET|POST|REQUEST)\[[^\]]+\]/.test(src) && !/sanitize_|wp_unslash|absint|intval|rest_sanitize/.test(src)) warn(rel(f), 'superglobal used without obvious sanitization');
    if (/(1000\.[0-9a-f]{32}\.[0-9a-f]{32})|client_secret\s*=>\s*'[^']{10,}'/i.test(src)) err(rel(f), 'looks like a committed Zoho token/secret');
  }
}

// ---------- report ----------
if (asJson) {
  console.log(JSON.stringify({ errors, warnings }, null, 2));
} else {
  for (const w of warnings) console.log(`WARN  ${w.file}: ${w.msg}`);
  for (const e of errors) console.log(`ERROR ${e.file}: ${e.msg}`);
  console.log(`\n${errors.length} error(s), ${warnings.length} warning(s)`);
}
process.exit(errors.length ? 1 : 0);
