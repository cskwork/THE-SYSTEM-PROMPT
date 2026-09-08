# Adversarial review by GPT-6 Astra (Codex CLI 0.153.4, low reasoning), 2026-09-09

Reviewer prompt: read CONTRACT.md (= AGENTS.md at v0.6.0) as the model that must obey it; for every sentence check ambiguity, conflict with the Codex base prompt, internal contradiction, enforceability, added pauses, and redundancy; list gaps; answer whether it reports before/after for non-developers unprompted. Raw output follows, unedited.

1. [High] This review establishes how I would obey the contract under the higher-priority instructions present in this Codex session. It does not establish identical behavior in Claude Code, Gemini CLI, opencode, or pi. Their instruction loading, available models, and precedence need separate verification. A shared file cannot itself guarantee shared behavior.

2. [Low] “Explore relevant code, data, and context first.”
   I read “relevant” as permission for targeted investigation, not a requirement to explore everything before responding. Another reading encourages unnecessary reconnaissance for trivial changes. This largely duplicates my defaults, creates no direct conflict, and does not require a pause.
   Proposed rewrite: “Inspect enough relevant context to establish the requested change and its constraints.”

3. [High] “Briefly state the intended outcome, underlying problem, scope, and observable success, then confirm before implementation unless already confirmed.”
   “Already confirmed” could mean an explicit implementation request or approval of my subsequent proposal. I would generally take the first reading because my higher-priority instructions treat actionable requests as authorization and discourage repeated confirmation. The second reading would make me pause after “Fix this typo” or “Implement the attached specification.” Requiring an “underlying problem” also invites invented rationale for straightforward requests. Clarifying intent is already a default; this mandatory presentation and gate are additional behavior.
   Proposed rewrite: “For nontrivial work, briefly state the understood outcome, scope, and success criteria; an explicit implementation request authorizes work within that scope, and clarification is needed only for consequential uncertainty.”

4. [Medium] “Ask focused questions only about points that change the work.”
   I would ask about consequential uncertainty, but almost any preference can technically “change the work.” The sentence does not distinguish a blocking decision from a detail I can reasonably choose. It mostly duplicates my defaults, but could justify unnecessary questions about naming or test organization.
   Proposed rewrite: “Ask only when the answer materially affects scope, correctness, authorization, or an outcome you cannot reasonably infer.”

5. [Medium] “Do not infer extra scope.”
   I would avoid additional features while allowing necessary implementation steps. A literal reading could prohibit adding a regression test or updating a directly affected caller unless named explicitly. That would conflict with completing the agreed outcome and encourage permission requests for routine supporting work. Scope control is already a default.
   Proposed rewrite: “Include supporting work necessary for the agreed outcome; do not add independent improvements.”

6. [Medium] “After agreement, complete implementation, verification, and authorized delivery without further check-ins.”
   I interpret “check-ins” as approval requests, not progress updates. The broader reading would conflict with my higher-priority requirement to communicate during sustained work; that requirement wins. “Agreement” inherits the ambiguity in finding 3. Persistence already matches my defaults, but an absolute reading cannot cover missing credentials or unavailable infrastructure.
   Proposed rewrite: “Once authorized, complete the agreed work and delivery without repeated approval requests, while reporting progress and concrete blockers.”

7. [High] “Ask again only for material changes to the agreement, unapproved data loss, public API changes, security consequences, or migrations.”
   Grammatically, “unapproved” clearly qualifies data loss but not the remaining categories. This can make me ask again during an explicitly requested migration, API change, or security fix. I would preserve earlier authorization, following higher-priority instructions. Conversely, “only” excludes necessary questions about missing access or conflicting requirements. The category list adds pauses beyond my defaults.
   Proposed rewrite: “Ask again only for material departures from the agreed scope or consequences not already authorized; request missing information when it blocks progress.”

8. [Medium] “Merge or publish only when authorized.”
   I would honor authorization already given, but the sentence does not define whether “ship it” includes merge, production deployment, a release, or all three. It also leaves push and external communication unspecified. This mostly duplicates existing authorization boundaries; ambiguous delivery requests could cause a pause.
   Proposed rewrite: “Carry out the delivery actions the user authorized, retaining that authorization across turns; clarify only consequential ambiguity about the destination or action.”

9. [Medium] “Choose the simplest approach that fixes the root cause without weakening checks.”
   I read “simplest” as the smallest maintainable correction, not the fewest changed lines. “Root cause” can expand a bounded fix into architectural work, conflicting with scope control. “Without weakening checks” can also preserve an incorrect assertion or obsolete validation rule. I would correct demonstrably wrong checks, but this wording could trigger a permission request. Most of the intent already matches my defaults.
   Proposed rewrite: “Choose the simplest maintainable fix within scope, preserving valid safeguards and correcting checks shown to encode wrong behavior.”

10. [Medium] “Preserve unrelated work and compatibility unless changes are agreed.”
    I would preserve unrelated user work regardless of authorization to change compatibility. The trailing exception could instead be read as permission to overwrite unrelated work after a general agreement. Compatibility also needs an identifiable baseline. Preservation is already a default; an unexpected breaking change appropriately causes a pause.
    Proposed rewrite: “Preserve unrelated user work, and maintain compatibility except for explicitly agreed breaking changes.”

11. [Medium] “Minimise total consumption without compromising correctness or verification, accepting slower completion when useful.”
    I would reduce unnecessary tool calls, context, and repeated work. “Total consumption” could instead mean money, tokens, compute, or elapsed human attention, which can favor different choices. Absolute non-compromise is not measurable, and slower completion does not necessarily cost less. Cost awareness is partly default; this preference strengthens it without providing a decision rule.
    Proposed rewrite: “Reduce unnecessary tokens, tool calls, and repeated work while preserving evidence appropriate to the task’s risk.”

12. [Medium] “Run one delegate at a time; add parallel delegates only when it reduces total work or rework or meets an explicit deadline.”
    I read this as conditional guidance when delegation is useful, not a mandate to delegate every task. Another reading establishes a default delegate even for tiny edits. Predicted savings cannot be guaranteed, and deadline-driven parallelism can conflict with minimizing consumption. My higher-priority delegation restrictions still win. This changes scheduling preferences but should not cause a user pause.
    Proposed rewrite: “Delegate only when the expected benefit exceeds coordination cost; use concurrent delegates only for independent work that reduces expected total effort or meets an explicit deadline.”

13. [High] “Use GPT-6 Astra (`gpt-6-astra`) at low reasoning for all agents.”
    I read this as a requested runtime configuration wherever I can actually select one. Text cannot switch the already-running coordinator’s model or reasoning setting. Availability under the other CLIs is unverified. A literal reading could halt useful work or demand configuration changes when the named model is unavailable. This is additional behavior, not a default, and cannot override host capabilities.
    Proposed rewrite: “Configure supported runtimes to use `gpt-6-astra` at low reasoning; report any mismatch and do not claim this file changed the active configuration.”

14. [High] “When delegating, keep the coordinator on orchestration.”
    I would reserve execution for delegates while assigning, reviewing, and integrating their work. “Orchestration” does not clarify whether I may inspect code, reproduce a failure, or run verification myself. Strict interpretation creates idle time and extra handoffs. In this session, higher-priority instructions permit spawning only alongside useful local work, so this cannot require a passive coordinator. It adds behavior that can conflict with the cost goal.
    Proposed rewrite: “When delegating, avoid duplicating the delegate’s work; the coordinator may inspect, integrate, and verify as needed.”

15. [High] “Start each delegate from a clean context, without the conversation history, with only the objective, paths, constraints, and acceptance criteria.”
    I would start without inherited conversation history, but “only” excludes relevant findings, failed attempts, approved decisions, and evidence. That invites repeated investigation and inconsistent authorization, contradicting evidence reuse and low cost. Host instructions and tools may still be inherited, so fully clean context is not enforceable through this sentence. This materially changes my normal delegation behavior.
    Proposed rewrite: “Start delegates without conversation history and provide a compact brief containing the objective, paths, constraints, authorization boundaries, acceptance criteria, and relevant verified findings.”

16. [Medium] “Reuse an agent for related work; start fresh for unrelated work.”
    I would reuse a delegate within the same task. “Related” could instead mean the same repository, even after its assumptions become stale. It also appears to conflict with “Start each delegate from a clean context” unless that means initial creation only. This affects context management without normally requiring a user pause.
    Proposed rewrite: “Reuse a delegate while its context remains relevant and current; start a new delegate when the objective or assumptions materially change.”

17. [Medium] “Ground decisions in code, real data, and authoritative sources; challenge claims contradicted by evidence, including documentation, tests, and user assumptions.”
    I would treat documentation, tests, and user assumptions as claims that evidence can overturn. The grammar also permits reading documentation and tests as the authoritative evidence doing the overturning. No source automatically wins: observed behavior may itself be the bug, and tests may encode outdated requirements. “Real data” should not rule out synthetic fixtures. Evidence-based reasoning largely duplicates my defaults.
    Proposed rewrite: “Use relevant implementation, observed behavior, requirements, and authoritative sources; investigate disagreements rather than assuming code, tests, documentation, or user claims are correct.”

18. [High] “Reuse verified evidence and refresh it only when state changes.”
    I would reuse evidence only while its assumptions remain valid. Literal compliance requires knowing whether state changed before checking it. External deployments, dependencies, permissions, and data can change unnoticed. My higher-priority freshness and verification requirements win when another check is needed. This is a useful cost preference expressed as an unsafe absolute.
    Proposed rewrite: “Reuse verified evidence while its inputs and assumptions remain current; refresh it when relevant state changes or freshness is uncertain.”

19. [Medium] “Verify intended behavior before claiming completion.”
    I would choose checks that exercise the requested outcome. Another reading accepts whatever tests happen to pass. It does not specify what to say when verification is blocked, or distinguish local correctness from successful delivery. It mostly duplicates my defaults and should not require approval for ordinary checks.
    Proposed rewrite: “Verify the agreed outcome with relevant evidence, and distinguish verified results, untested behavior, and blocked checks before claiming completion.”

20. [Medium] “Use independent review when risk justifies it.”
    I would seek a separate reviewer for consequential changes, but “risk” has no threshold and “independent” could mean another agent, another context, or a human. This can introduce an unplanned human approval gate or unnecessary delegation. It partly overlaps my defaults but remains discretionary.
    Proposed rewrite: “For changes with substantial security, data-loss, compatibility, or correctness risk, obtain a separate review when available and disclose any review limitation.”

21. [Medium] “When history matters, say who changed what, when, where, why, and how: give dates with commits or tickets, separate change, merge, deployment, and symptom dates by environment, and say "unknown" rather than infer.”
    I would apply this to attribution and incident timelines. A broader reading turns every bug fix into a historical investigation. Commit authorship does not prove decision ownership, and commit time does not establish deployment or symptom time. “Unknown rather than infer” can also suppress useful, clearly labeled hypotheses. This adds valuable reporting discipline but can increase work substantially.
    Proposed rewrite: “When historical attribution affects the answer, report supported actors, changes, reasons, and dates, distinguish change, merge, deployment, and symptom timing by environment, and label unknowns and hypotheses.”

22. [Low] “Never describe timing only as "old", "existing", or "recent".”
    I would avoid these words as substitutes for dates in historical claims. A literal reading treats “existing validation” as a timing claim and demands irrelevant archaeology. This partly repeats the preceding sentence and should not cause a pause.
    Proposed rewrite: “For historical timing claims, use supported dates or say the date is unknown.”

23. [Medium] “Keep it readable by non-developers, with technical evidence below.”
    I read “it” primarily as the historical explanation in the same paragraph, though it could apply to every response. “Below” imposes an ordering but does not require a before-and-after explanation. Plain language already matches my defaults; universally separating technical evidence is additional formatting and may be awkward for code-focused requests.
    Proposed rewrite: “In completion reports, explain the user-visible change in plain language first, followed by the technical evidence needed to assess it.”

24. [Low] “Explain concepts, decisions, and tradeoffs when they help; go deeper when asked.”
    I would explain what helps the user assess the result. “When they help” could justify almost any digression, but the next sentence limits that reading. It duplicates my defaults, has no direct conflict, and creates no approval gate.
    Proposed rewrite: “Explain decisions and tradeoffs needed to assess the result; add depth when requested.”

25. [Low] “Avoid unsolicited tutorials and reteaching; questions do not prove knowledge gaps, and receiving explanations does not prove mastery.”
    I read this as avoiding assumptions about the user’s competence, not as forbidding an answer to an explanatory question. A stricter reading could make me omit necessary context because it resembles teaching. The first clause largely matches my defaults; the remaining clauses usefully constrain personalization but offer no concrete reporting rule.
    Proposed rewrite: “Answer at the requested depth without inferring the user’s competence from a question or a previous explanation.”

26. [Low] “Treat memory as continuity that can be revised.”
    I would treat memory as fallible context, not authority. “Can be revised” could also sound like permission to edit it, but the next sentence and my higher-priority memory rules restrict that. This mostly duplicates my defaults and adds little observable behavior alone.
    Proposed rewrite: “Treat memory as fallible context and resolve conflicts using current evidence and instructions.”

27. [Medium] “Propose memories at natural stopping points and save only text the user has approved, through the supported memory mechanism.”
    I would propose a memory only when it appears durable and useful, but the wording can encourage a proposal after every task. “Natural stopping points” is vague, and approval of wording is not necessarily an explicit request to save it. My higher-priority instructions require an explicit memory-update request, which wins. This can add recurring user interruptions beyond my defaults.
    Proposed rewrite: “Propose memory updates only for useful durable information, and save the agreed text only when the user explicitly requests it through the supported mechanism.”

28. [Medium] “Read repository instructions and `~/.agents/rules/rules.md` when present.”
    I would read applicable instructions before acting, including instructions scoped to files I touch. The sentence does not establish timing, scope, precedence, or treatment of instructions discovered in untrusted task content. It largely duplicates repository-reading defaults, while the specific global path is additional behavior. Reading a file does not make it outrank higher-priority instructions.
    Proposed rewrite: “Before acting, read applicable repository instructions and `~/.agents/rules/rules.md` when present, following the host’s instruction precedence.”

29. [High] Missing from “confirm before implementation unless already confirmed” and “After agreement”: a durable definition of authorization. There is no explicit rule for preserving agreement across follow-up messages, summaries, or delegate handoffs. “Looks good” could approve a plan without authorizing publication. Conversely, a status question could mistakenly interrupt an authorized implementation.
    Proposed addition: “Carry the agreed outcome, boundaries, and authorized delivery actions across turns and handoffs; treat follow-ups as amendments unless the user clearly replaces or cancels the task.”

30. [High] Missing from “authorized delivery” and “Verify intended behavior”: delivery-specific proof. Passing local tests does not establish a successful push, merge, release, deployment, or live interaction.
    Proposed addition: “Verify each authorized delivery action at its destination, and report local validation separately from remote or live results.”

31. [Medium] Missing from “complete implementation, verification, and authorized delivery”: a useful incomplete-work outcome. The contract does not say how to stop honestly when access, infrastructure, or required information is unavailable. Persistence can become repeated retries or a premature completion claim.
    Proposed addition: “When blocked, finish independent work, state the exact blocker and remaining work, and request only what is needed to proceed.”

32. [Medium] Missing from “Minimise total consumption”: a stopping rule for investigation, testing, and review. None of those activities has a natural ceiling, particularly under adversarial review.
    Proposed addition: “After the agreed checks pass, expand investigation or repeat verification only when new evidence, changes, or unresolved risk justifies it.”

33. [Medium] Missing from the shared-file design: separation between portable behavioral rules and runtime configuration. “Use GPT-6 Astra” and “Start each delegate from a clean context” depend on host capabilities, while intent and evidence rules are broadly portable. The contract provides no way to report partial compliance.
    Proposed addition: “Report unavailable runtime capabilities when they affect the task; do not claim compliance with settings or mechanisms the host cannot enforce.”

34. [Medium] Missing from “Keep it readable by non-developers”: a general completion-report contract. To answer your specific question, no, I would not reliably produce a before-and-after explanation without being told. In this session I naturally lead with the outcome, explain the change, and summarize verification because higher-priority instructions require that. I might still say “Added a null guard; tests pass,” which does not explain the previous problem or resulting behavior to a non-developer. The quoted sentence neither clearly governs every completion report nor explicitly requests before-and-after language.
    Proposed addition: “When finishing a code change, briefly explain what happened before, what happens now, and how you verified it, in language a non-developer can follow; include any remaining limitations.”

35. [Low] No files were modified. The findings above use the contract read in this directory and the instructions active in this session. Prior memory informed the preference for concise, behavior-changing rewrites; it was not treated as proof of current behavior in other CLIs.

