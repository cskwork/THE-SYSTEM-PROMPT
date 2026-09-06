# THE-SYSTEM-PROMPT

[AGENTS.md](AGENTS.md) is the operating contract I give coding agents. It focuses on understanding the user's intent, agreeing on the outcome and scope, and verifying the result. The agent chooses how much planning, delegation, and investigation the task needs.

The contract keeps explicit boundaries around unrelated work, scope changes, data loss, public APIs, security, and migrations. It supplements each agent's existing instructions. It does not claim to improve performance without testing.

The previous contract is preserved unchanged in [the seven-step archive](archive/AGENTS-2026-09-06-seven-step.md).

## Install

Back up existing files before running these commands, including `~/.agents/AGENTS.md`. The commands overwrite the canonical file and replace the listed links. Keep only the agents you use.

```bash
mkdir -p ~/.agents ~/.claude ~/.codex ~/.gemini ~/.config/opencode ~/.pi/agent
curl -fsSL https://raw.githubusercontent.com/cskwork/THE-SYSTEM-PROMPT/main/AGENTS.md \
  -o ~/.agents/AGENTS.md

ln -sfn ~/.agents/AGENTS.md ~/.claude/CLAUDE.md
ln -sfn ~/.agents/AGENTS.md ~/.codex/AGENTS.md
ln -sfn ~/.agents/AGENTS.md ~/.gemini/GEMINI.md
ln -sfn ~/.agents/AGENTS.md ~/.config/opencode/AGENTS.md
ln -sfn ~/.agents/AGENTS.md ~/.pi/agent/AGENTS.md
```

Gemini CLI reads `GEMINI.md`. On Windows, symlinks require Developer Mode or an administrator terminal. If you copy the file instead, update each copy when the contract changes.

Repository instructions and `~/.agents/rules/rules.md`, when present, provide project and domain guidance.

## Landing page

The [English landing page](https://cskwork.github.io/THE-SYSTEM-PROMPT/) and [Korean landing page](https://cskwork.github.io/THE-SYSTEM-PROMPT/ko.html) live in `docs/`. Rebuild them after changing the contract or page content:

```bash
python3 build.py
```

Commit the generated files with the source changes. GitHub Pages serves the site from `docs/`. The pages link to the current contract and archived version, and their copy buttons copy the current English `AGENTS.md`.
