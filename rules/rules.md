# Domain rules

Shared domain rules. The workflow lives in `~/.agents/AGENTS.md`.
Task-specific model routing below takes precedence over general delegation defaults.

## Environment
- macOS arm64; interpreters: node via nvm (v22.22.3), python3 via /opt/homebrew/bin/python3.12, git /usr/bin/git.

## Safety
- Never run rm -rf on paths outside the current run's own scratch space.

## Networking

## Agents
- Default model: `gpt-6.1-sol` at medium reasoning with Fast mode (priority service tier), except the Opus categories below.
- Routine backend and application logic, and very simple tasks outside UI/UX/frontend: use `gpt-6.1-sol` at medium reasoning with Fast mode (priority service tier).
- Browser automation, browser QA, and end-to-end browser verification: use `gpt-6.1-sol` at medium reasoning with Fast mode (priority service tier), including verification of Opus-built interfaces.
- UI, UX, visual design, frontend implementation, and document writing: use `claude-opus-5-5` at medium reasoning via the `call-agent` skill, including small frontend and document-writing tasks.
- Difficult implementation, complex debugging, architecture, or tasks that exceed the routine Sol path: use `claude-opus-5-5` at medium reasoning via `call-agent`.
- For Claude calls, pass `--model claude-opus-5-5 --effort medium` explicitly. Do not use a wrapper that hardcodes `--effort high` for a medium-reasoning task; preserve the call-agent preflights and permission boundaries when making the equivalent direct call.
- These task-specific choices override generic delegate defaults and wrapper defaults. Keep coordination with the host; use its native execution when it already matches the requested model, reasoning, and speed. If the selected model is unavailable, report the blocker and get the owner's approval before substituting another model.

## Writing
- Use the `humanizer` skill by default when writing or editing prose; preserve facts, technical identifiers, and the requested language and tone.

## Skills
- OfficeCLI skills, including `morph-ppt` and `morph-ppt-3d`, are excluded from global skill installation and updates.
