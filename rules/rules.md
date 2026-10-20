# Domain rules

Routing overrides generic delegate/wrapper defaults.

## Models
- Default, backend logic, simple work, browser automation, QA/E2E: `gpt-6.1-sol`, high reasoning, Fast (priority).
- UI/UX, visual design, frontend, document writing, difficult implementation/debugging, architecture: `claude-opus-5-5`, medium reasoning. Includes small frontend/document tasks.
- Opus: use the `call-agent` skill with `--model claude-opus-5-5 --effort medium`; preserve preflights/permissions. Replace high-only wrappers with equivalent medium calls.
- Sol from Claude Code: the Agent tool runs only Claude models, so send Sol slices through the `call-agent` skill (Codex route), never an Opus subagent.
- Execute natively when model/reasoning/speed match. Sol handles QA of Opus-built interfaces.
- Opus unavailable: report and automatically use the default without additional approval. Ask before other substitutions.

## Safety
- `rm -rf` is limited to the current run's scratch space.

## Skills
- Default skills: `attention-kind` for user replies, `grill-with-docs` (`grilling` + `domain-modeling`) when sharpening a plan or design, `domain-modeling` when defining or updating domain terms (`GLOSSARY.md`) and ADRs (`docs/adr/`), and `research` when investigating questions against primary sources in a background agent.
