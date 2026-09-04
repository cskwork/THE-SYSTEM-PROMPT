# THE-SYSTEM-PROMPT

The operating contract I hand every coding agent. One file, `AGENTS.md`: stance, an
evidence rule, and a seven-step loop from orient to report. Plan confirmation is the
last human gate — after it the agent runs to completion on its own.

It is written to sit on top of a harness prompt, not replace it, so it carries only the
rules that change default behaviour: give three ranked options before coding, verify
claims against running code rather than docs, sort verification output into passed /
pre-existing / regression / skipped, and report in a fixed section order.

## Install

Keep one canonical copy and link it into each agent's config directory:

```bash
mkdir -p ~/.agents
curl -fsSL https://raw.githubusercontent.com/cskwork/THE-SYSTEM-PROMPT/main/AGENTS.md \
  -o ~/.agents/AGENTS.md

ln -sfn ~/.agents/AGENTS.md ~/.claude/CLAUDE.md
ln -sfn ~/.agents/AGENTS.md ~/.codex/AGENTS.md
ln -sfn ~/.agents/AGENTS.md ~/.gemini/GEMINI.md            # Gemini CLI reads GEMINI.md
ln -sfn ~/.agents/AGENTS.md ~/.config/opencode/AGENTS.md
ln -sfn ~/.agents/AGENTS.md ~/.pi/agent/AGENTS.md
```

Move any target that is a regular file to a timestamped backup before you replace it.
Skip the directories whose agent you have not installed. On Windows, symlinks need
Developer Mode or an admin terminal; copy the file instead and expect it to drift.

## What it expects to find

- `~/.agents/rules/rules.md` — your domain rules. The prompt reads it every session.
- Skills named in the text: `unslop`, `brainstorming`, `writing-plans`. Drop the mention
  if you do not have them.
- `CONTEXT.md`, a glossary, or ADRs in the repository, when they exist.

## Where it is mirrored

`cskwork/pi-setup` and `cskwork/pi-setup-public` ship the same file, because the pi
installer links `~/.pi/agent/AGENTS.md` at their copy. This repository is the canonical
one; change it here first.
