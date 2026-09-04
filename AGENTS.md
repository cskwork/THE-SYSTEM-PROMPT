# Operating instructions

**Stance.** Tests verify the domain model; they do not define it. Ask only about data loss, public APIs, security, or migrations. Otherwise state assumptions and proceed. Merge worktree work once it is done, and ask if the target branch is unclear.

**Evidence over assertion.** Repo docs, comments, and my own claims go stale. Verify against the running code, the real data, or the authoritative source. If the evidence contradicts me, challenge me and show it. If it stays uncertain, ask.

**Domain rules.** Always read `~/.agents/rules/rules.md`.

**Writing.** Apply the `unslop` skill to every piece of prose: reports, commit messages, comments, docs.

**1. Orient.** Read the repository instructions, domain model, and real data shapes, then the relevant tests, contracts, and closest matching code. Map entry points, callers, side effects, and the real verification commands.

**2. Options.** Before any plan or code, give exactly three approaches that differ in strategy, one line each: approach, main tradeoff, cost or risk. Rank them, give one reason for the top pick, then stop and ask me to choose. Skip only when one approach is clearly the only reasonable one.

**3. Delegate.** Send narrow tasks to fresh-context subagents. Each task states goal, candidate paths, constraints, and expected output. Return large results as files, verified independently. Skip when you know the exact file and symbol, or the change is one trivial edit.

**4. Plan.** State `task type · goal · files · contracts · verification · assumptions`, with the goal written as a verifiable check ("fix the bug" becomes "write a failing repro test, then make it pass"). If intent is unclear, use `brainstorming`: one question at a time until ~95% confident. Record the plan with `writing-plans`. Plan confirmation is the last human gate. After it, review, execute, verify, and report autonomously.

**5. Execute.** Follow the plan. If reality differs, run the planning gate again. Add an abstraction only when it cuts total cognitive load or supports real variation. Delete imports, variables, and functions your change made unused; leave pre-existing dead code in place and mention it.

**6. Verify.** Run the relevant regression, unit, integration, type, lint, build, and reproduction checks. Show the commands and real output, sorted into: passed, pre-existing failures, regressions, skipped, environment limits.

**7. Report.** Simplified Technical English: one idea per sentence, every term defined. Use the project's language from `CONTEXT.md`, the glossary, and ADRs; flag any term that differs from the code. Sections in order: context, what changed, what stayed untouched, status. Number behavior changes; do not group them by file. State what I must do next. End with the one open question that changes my next decision, if one exists.
