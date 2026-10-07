# Domain rules

Workflow: `~/.agents/AGENTS.md`. Routing overrides delegate/wrapper defaults.

## Models
- Default/backend/simple work/browser/QA: `gpt-6.1-sol`, high, Fast (priority).
- UI/UX/visual design/frontend/documents/hard implementation/debugging/architecture: `claude-opus-5-5`, medium, even for small tasks.
- Opus: `call-agent --model claude-opus-5-5 --effort medium`; override high-only wrappers, preserve preflights/permissions.
- Coordinate; execute natively when model/effort/speed match. Sol verifies Opus interfaces.
- Opus unavailable: report and use the default automatically. Ask before other substitutions.

## Safety
- `rm -rf` is limited to the current run's scratch space.
