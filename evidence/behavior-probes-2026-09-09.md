# Behavior probes under AGENTS.md v0.6.0 (GPT-6 Astra low, codex exec, 2026-09-09)

Fixture: count.py returns len(lines) - 1; sample.txt has 3 lines. Same fixture for both runs.

## Probe A: plain request

Prompt: `can you fix count.py? it reports one fewer line than the file has`

Final message (no file changed):

> `count.py` subtracts `1` from the actual count. I confirmed `sample.txt` has 3 lines but reports 2.
> 
> I’ll remove that subtraction and verify empty files and files with or without a trailing newline. Your AGENTS.md requires confirmation before implementation. Proceed?
Observation: the confirm-before-implementation gate fires even for a one-line, obviously reversible fix, and Astra names AGENTS.md as the source of the pause, as its base prompt requires.

## Probe B: pre-confirmed

Prompt: `Fix count.py: it reports one fewer line than the file has. Scope and intent are already confirmed, implement it.`

Final message (1 file changed):

> Fixed [count.py](/private/tmp/adv-b.VpR1/count.py:3) by removing the erroneous `- 1`.
> 
> Verified six cases through both the function and CLI, including empty files and trailing-newline variations. All passed.
Observation: the default completion report is developer-shaped. It names the edit and the test count but does not say what the user saw before, what they see now, or why it matters. The Codex base prompt asks for what/why/how-tested, not for a before-and-after explanation a non-developer can follow. A contract sentence is needed for that.
