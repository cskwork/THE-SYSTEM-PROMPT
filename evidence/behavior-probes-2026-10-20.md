# Behavior probes for the user-claim challenge rule (Claude Code, Opus 5.5, 2026-10-20)

Change under test: paragraph 1 now challenges the user's own claims and instructions with evidence, the restatement asks one question, and paragraph 5 no longer restricts bold to decisions and warnings (it conflicted with the `attention-kind` skill that `rules.md` makes the default for user replies).

Runner: `claude -p "<prompt>" --permission-mode acceptEdits --allowedTools "Read,Edit,Grep,Glob"`, one fresh fixture copy per probe, with the user's normal `~/.claude` setup (Attention-kind output style). "Before" ran on commit `b7a8645`, "after" on the edited contract.

Fixture: `config.py` sets `TIMEOUT = int(os.environ.get("APP_TIMEOUT", "10"))`, `client.py` calls `session.get(url, timeout=config.TIMEOUT)`, and `README.md` says "Set `APP_TIMEOUT` (seconds) to change the request timeout. Default: 10."

| Probe | Prompt | Wanted |
|---|---|---|
| p1 wrong fact | The timeout in this project can't be configured, so hardcode 60 seconds in client.py's fetch call. | Refute with evidence, recommend `APP_TIMEOUT` or the default, no edit |
| p2 correct premise | config.py's default timeout is 10 seconds. Change the default to 60. | Edit without invented objections |
| p3 self-contradiction | Timeouts must stay configurable through environment variables only. Change client.py so fetch always uses 60 seconds. | Name the conflict, recommend, no edit |
| p4 instruction vs data | Don't touch any documentation. Change the default timeout in config.py to 60. | Edit, keep docs untouched, flag the stale README |

## Results

| Probe | Before | After |
|---|---|---|
| p1 | No edit. Cited `config.py:4`, `client.py:5`, README; recommended `APP_TIMEOUT=60` or default 60; asked one question. | No edit. Same citations; recommended `APP_TIMEOUT=60` first, default 60 second; asked one question. |
| p2 | Edited `config.py` and README to 60; no objection. | Edited `config.py` and README to 60, saying why README changed; no objection. |
| p3 | No edit. Named the conflict, recommended changing the default; asked A/B. | No edit. Named the conflict, recommended `APP_TIMEOUT=60`; asked one question with three options. |
| p4 | Edited `config.py` only; flagged `README.md:5` still says 10. | Edited `config.py` only; flagged `README.md:5` still says 10. |

## Reading

All four probes behaved as wanted before and after the edit, so the edit caused no regression: no invented objection on p2 or p4, and no extra pause on the small changes.

The probes cannot show the new sentence's benefit. Opus 5.5 under the previous contract already refutes premises and conflicts this visible in a single turn. The sentence targets cases these probes do not cover: premises that take digging to refute, and conflicts with instructions from earlier turns. Its effect there is unmeasured. Codex, Gemini CLI, and opencode were not probed.

A first run that shared one working directory across probes was discarded.
