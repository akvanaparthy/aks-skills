# aks-skills

My own Claude Code / agent skills. Each folder is one skill (`SKILL.md` + optional
`references/`, `scripts/`, and a `CLAUDE.md` template).

| Skill | What it does |
|---|---|
| [`wordpress-skill`](wordpress-skill/) | Build or modify modern WordPress block themes (and companion plugins) to current standards, matching reference images. |

## Install

Project-level (recommended, committed with the repo):

```
git clone https://github.com/akvanaparthy/aks-skills.git /tmp/aks-skills
mkdir -p .claude/skills
cp -r /tmp/aks-skills/wordpress-skill .claude/skills/wordpress-skill
cp .claude/skills/wordpress-skill/CLAUDE.md ./CLAUDE.md   # then fill in the braces
```

Global (all projects):

```
cp -r /tmp/aks-skills/wordpress-skill ~/.claude/skills/wordpress-skill
```

Or with the skills CLI: `npx skills add akvanaparthy/aks-skills --skill wordpress-skill`.

Restart Claude Code after installing so it picks the skill up.

## Pairs well with

- [WordPress/agent-skills](https://github.com/WordPress/agent-skills) — official skills
  for WordPress APIs (`wp-block-themes`, `wp-interactivity-api`, `wp-plugin-development`…).
  `npx skills add WordPress/agent-skills --skill wp-block-themes`
