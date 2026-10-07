# Domain rules

Workflow: `~/.agents/AGENTS.md`. Routing overrides generic delegate/wrapper defaults.

## Models
- Default, backend logic, simple work, browser automation, QA/E2E: `gpt-6.1-sol`, high reasoning, Fast (priority).
- UI/UX, visual design, frontend, document writing, difficult implementation/debugging, architecture: `claude-opus-5-5`, medium reasoning. Includes small frontend/document tasks.
- Opus: use the `call-agent` skill with `--model claude-opus-5-5 --effort medium`; preserve preflights/permissions. Replace high-only wrappers with equivalent medium calls.
- Host coordinates; execute natively when model/reasoning/speed match. Sol handles QA of Opus-built interfaces.
- Opus unavailable: report and automatically use the default without additional approval. Ask before other substitutions.

## Safety
- `rm -rf` is limited to the current run's scratch space.
