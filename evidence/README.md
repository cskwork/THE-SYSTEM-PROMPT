# Why the contract says what it says

This folder records the reasoning behind the current `AGENTS.md`, so that future edits
do not re-add rules the agent harness already enforces, and so that anyone reading the
contract can see why it is short.

## Design rule

`AGENTS.md` supplements each agent's built-in system prompt. It should contain only
instructions that the harness does **not** already give, or that deliberately override
a harness default. Anything the harness already says is duplicated context: it costs
input tokens on every turn and, for a model that follows context files closely, it can
cause unintended pauses when two copies of a rule are read as two separate demands.

## Primary harness: Codex CLI with GPT-6 Astra

The contract targets GPT-6 Astra (`gpt-6-astra`) at low reasoning. Codex CLI ships a
model-specific base prompt for that slug. It was extracted from the Codex CLI 0.153.4
binary (`instructions_template` for slug `gpt-6-astra`, 3,282 words) on 2026-09-09.
The extraction method is at the end of this file.

OpenAI's [GPT-6 Astra guide](https://developers.openai.com/api/docs/guides/latest-model)
publishes prompt snippets for autonomy, instruction precedence, writing style, delegation,
and test calibration. Those snippets are written for developers who build their own
system prompt over the API. Codex CLI already embeds them in its base prompt, so copying
them into `AGENTS.md` adds nothing for Codex users.

## Rules removed in v0.6.0 because the Codex base prompt already states them

| Removed from `AGENTS.md` | Codex base prompt (gpt-6-astra, 0.153.4) |
|---|---|
| Finish authorized preparation first so approval is the last step. | "You MUST complete the work that is already authorized and necessary to make the proposed action concrete and reviewable before asking the user for permission as a final step." |
| Treat "can you…" and "help me…" as requests to do the work. | "When the user's prompt indicates a request for action, such as 'can you...', 'I want to...', 'help me...' and similar expressions, treat these as instructions to do the work and take action. Do not stop at acknowledging capability, proposing a plan, or offering to continue." |
| Skip tests that only mirror a reversible, low-impact change. | "Do not write tests for reversible, low-impact changes or that mirror the implementation." |
| Repeat investigation, tests, or reviews only for changed state, failures, or unresolved concerns. | "Once those pass, broaden or repeat testing only when new changes, failures, or unresolved concerns justify it." |
| User instructions outrank repository, rule, and skill guidance; if any makes you pause, name the file and quote the line. | "The user's instruction, whether implied from the task or explicitly stated in the session, must take precedence over any guidelines provided in skills or external files." and "If a skill causes you to ask for permission or confirmation, pause, or leave requested work unfinished, name and link to the exact SKILL.md you read, quote the relevant instruction." |
| Communicate in plain language. Lead with the outcome and separate evidence from uncertainty. Write short paragraphs; use lists only for genuinely parallel items, never nested. | "Use plain, simple language", "Lead with the outcome and then develop your reasoning", "Include the evidence needed to understand the conclusion and its practical limits", "Default to using clear, concise paragraphs... Use lists only when the information is genuinely parallel, sequential, or easier to compare, and avoid nested lists". |
| Keep progress updates brief; name the next useful action. | "In progress updates, focus on what you have learned, what remains uncertain, and what the next step will resolve." |
| Adapt to demonstrated understanding, context, and memory. | "Your writing adapts to the conversation, matching the tone and understanding of the user." |

Claude Code's built-in prompt covers the same ground for autonomy on reversible actions,
finishing the task instead of stopping at a plan, leading with the answer, and using lists
only for parallel items. Gemini CLI and opencode base prompts were not checked.

## Rules removed for other reasons

- **`fork_turns="none"`.** A Codex-only parameter name in a file that five agents load.
  The intent is kept in tool-neutral words: each delegate starts from a clean context with
  only the brief. In Codex the `spawn_agent` tool documents `fork_turns` as defaulting to
  `all`, which forks the whole parent conversation into every child; the plain-English rule
  maps to `none` without naming it.
- **"Delegates must not spawn agents."** Codex's multi-agent prompt says the opposite
  ("Child agents can also spawn their own sub-agents"). The owner chose to allow nesting,
  so the line was dropped rather than moved to configuration.
- **Token accounting sentence.** It only applied when the agent discussed cost, and the
  general rule to challenge claims that evidence contradicts already forbids unmeasured
  savings claims.
- **Memory scope ("learning preferences or demonstrated understanding").** The owner's
  actual memory store holds project and reference notes, not learning preferences, so the
  scope did not describe practice. The two load-bearing clauses stay: memory is revisable,
  and nothing is saved without approved text.

## One wording conflict fixed

v0.5.0 said "Prefer sequential work" and the first v0.6.0 draft said "Work sequentially".
The Codex base prompt instructs the model to batch independent searches and reads in a
single call and to parallelize independent tool calls. Read literally, the contract line
would make Astra serialize tool calls, which costs time and saves no tokens. The rule now
reads "Run one delegate at a time", which limits only agent fan-out.

## What remains, and why each line is not in the harness

- **Confirm before implementation.** Codex says the opposite: "You don't need user
  permission for reversible tasks". This is a deliberate override. Expect Astra to state
  that `AGENTS.md` is the source of the pause; that is the harness working as designed.
- **The four re-confirmation boundaries** (data loss, public API, security, migrations)
  and "do not infer extra scope". Not in the harness.
- **Simplest root-cause fix; preserve unrelated work.** Not in the harness.
- **Cost first; one delegate at a time; no polling or idle work.** Codex prefers
  parallel delegation when it saves time. This is an explicit cost-over-speed choice.
- **Astra low for all agents; clean-context delegation; reuse an agent for related
  work.** Codex defaults to full-history forks and inherits the parent model. Overrides.
- **Before-and-after reports for non-developers, and change history in who, what, when,
  where, why, how with dates and commits.** Codex says to report what changed, why, and
  how it was tested, but not the before/after framing or the non-developer audience.
- **No unsolicited tutorials; questions do not prove gaps.** Not in the harness.
- **Memory: revisable, approved text only.** Overrides harness defaults that write memory
  autonomously.
- **Read `~/.agents/rules/rules.md`.** A local path the harness does not know.

## Reproducing the extraction

```bash
BIN=$(dirname "$(readlink -f "$(which codex)")")/../node_modules/@openai/codex-darwin-arm64/vendor/aarch64-apple-darwin/bin/codex
python3 - "$BIN" <<'PY'
import json, sys
b = open(sys.argv[1], 'rb').read()
key = b'"instructions_template": "You are Codex, an agent based on GPT-6'
i = b.index(key); j = b.index(b'"', i + len(b'"instructions_template": ')) + 1
k = j
while True:
    k = b.index(b'"', k); n = 0; t = k - 1
    while b[t] == 0x5c: n += 1; t -= 1
    if n % 2 == 0: break
    k += 1
print(json.loads(b[j-1:k+1].decode()))
PY
```

Codex CLI is open source, so the same text can be read in the `openai/codex` repository
for the matching release. Versions after 0.153.4 may change the base prompt; re-check the
overlap table before re-adding any rule.
