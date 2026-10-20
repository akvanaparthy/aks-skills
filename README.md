# aks-skills

My own Claude Code / agent skills. Each folder is one skill (`SKILL.md` + optional
`references/`, `scripts/`, and a `CLAUDE.md` template).

| Skill | What it does |
|---|---|
| [`wordpress-skill`](wordpress-skill/) | Build or modify modern WordPress block themes (and companion plugins) to current standards, matching reference images, without the generated-page look. |
| [`seo-aeo-geo-skill`](seo-aeo-geo-skill/) | Technical SEO + AI-search visibility (AEO/GEO) engineering for an existing codebase: indexability, crawler access, metadata, JSON-LD, CWV, with verification. Modes: `audit`, `implement`, `review`. |
| [`real-estate-web-skill`](real-estate-web-skill/) | Domain layer for property sites, loaded on top of the two above: data model and lifecycle, faceted search indexing, locality/project page strategy, listing schema, lead capture, plus India / US / UK-EU market rules. |

How they fit: `wordpress-skill` builds the site, `seo-aeo-geo` handles search and AI
visibility, and `real-estate-web` adds only what is different about property sites.
Other industries get their own layer the same way (`<industry>-web-skill/`).

## Install

Project-level (recommended, committed with the repo):

```
git clone https://github.com/akvanaparthy/aks-skills.git /tmp/aks-skills
mkdir -p .claude/skills
cp -r /tmp/aks-skills/wordpress-skill .claude/skills/wordpress-skill
cp -r /tmp/aks-skills/seo-aeo-geo-skill .claude/skills/seo-aeo-geo
cp -r /tmp/aks-skills/real-estate-web-skill .claude/skills/real-estate-web   # property sites only
cp .claude/skills/wordpress-skill/CLAUDE.md ./CLAUDE.md   # then fill in the braces
```

Global (all projects):

```
cp -r /tmp/aks-skills/wordpress-skill ~/.claude/skills/wordpress-skill
cp -r /tmp/aks-skills/seo-aeo-geo-skill ~/.claude/skills/seo-aeo-geo
```

Or with the skills CLI: `npx skills add akvanaparthy/aks-skills --skill wordpress-skill seo-aeo-geo-skill`.

Restart Claude Code after installing so it picks the skill up.

## Pairs well with

- [WordPress/agent-skills](https://github.com/WordPress/agent-skills) — official skills
  for WordPress APIs (`wp-block-themes`, `wp-interactivity-api`, `wp-plugin-development`…).
  `npx skills add WordPress/agent-skills --skill wp-block-themes`
