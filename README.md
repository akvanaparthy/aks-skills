# aks-skills

My own Claude Code / agent skills. Each folder is one skill (`SKILL.md` + optional
`references/`, `scripts/`, and a `CLAUDE.md` template).

| Skill | What it does |
|---|---|
| [`wordpress-skill`](wordpress-skill/) | Build or modify modern WordPress block themes (and companion plugins) to current standards, matching reference images, without the generated-page look. |
| [`seo-aeo-geo-skill`](seo-aeo-geo-skill/) | Technical SEO + AI-search visibility (AEO/GEO) engineering for an existing codebase: indexability, crawler access, metadata, JSON-LD, CWV, with verification. Modes: `audit`, `implement`, `review`. |

The two are designed to work together: `wordpress-skill` handles the theme's own technical
SEO share and defers everything else to `seo-aeo-geo`.

## Install

Project-level (recommended, committed with the repo):

```
git clone https://github.com/akvanaparthy/aks-skills.git /tmp/aks-skills
mkdir -p .claude/skills
cp -r /tmp/aks-skills/wordpress-skill .claude/skills/wordpress-skill
cp -r /tmp/aks-skills/seo-aeo-geo-skill .claude/skills/seo-aeo-geo
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
