# Domain rules

Workflow: `~/.agents/AGENTS.md`. Routing overrides generic delegate and wrapper defaults.

## Models
- Default, backend logic, simple work, browser automation and QA/E2E: `gpt-6.1-sol`, high reasoning, Fast (priority service tier).
- UI/UX, visual design, frontend, document writing, difficult implementation/debugging and architecture: `claude-opus-5-5`, medium reasoning. Includes small frontend/document tasks.
- Opus: use `call-agent` with `--model claude-opus-5-5 --effort medium`; preserve preflights and permissions. Replace high-only wrappers with equivalent medium calls.
- Host coordinates; execute natively when its model, reasoning and speed match. QA of Opus-built interfaces uses Sol.
- Unavailable model: report the blocker; obtain owner approval before substitution.

## Safety
- `rm -rf` is limited to the current run's scratch space.
