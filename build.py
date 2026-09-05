#!/usr/bin/env python3
"""Generate index.html (EN) and ko.html (KO) from AGENTS.md plus the copy below.

The copy payload each page ships is read from AGENTS.md at build time, so the two
pages can never drift from the contract or from each other. Run after editing
AGENTS.md:  python3 build.py
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).parent
AGENTS = (ROOT / "AGENTS.md").read_text()
BYTES = f"{len(AGENTS.encode()):,} bytes"

GATE = 4  # Plan: the only step that stops for a human
REPO = "https://github.com/cskwork/THE-SYSTEM-PROMPT"
RAW = "https://raw.githubusercontent.com/cskwork/THE-SYSTEM-PROMPT/main/AGENTS.md"

INSTALL = """mkdir -p ~/.agents
curl -fsSL <span class="u">https://raw.githubusercontent.com/cskwork/THE-SYSTEM-PROMPT/main/AGENTS.md</span> \\
  -o ~/.agents/AGENTS.md

ln -sfn ~/.agents/AGENTS.md ~/.claude/CLAUDE.md
ln -sfn ~/.agents/AGENTS.md ~/.codex/AGENTS.md
ln -sfn ~/.agents/AGENTS.md ~/.gemini/GEMINI.md            <span class="c">{gemini}</span>
ln -sfn ~/.agents/AGENTS.md ~/.config/opencode/AGENTS.md
ln -sfn ~/.agents/AGENTS.md ~/.pi/agent/AGENTS.md"""

PATHS = [("Claude Code", "~/.claude/CLAUDE.md"), ("Codex CLI", "~/.codex/AGENTS.md"),
         ("Gemini CLI", "~/.gemini/GEMINI.md"), ("OpenCode", "~/.config/opencode/AGENTS.md"),
         ("pi", "~/.pi/agent/AGENTS.md")]

EN = {
  "lang": "en", "file": "index.html", "other": ("ko.html", "한국어"), "self": "EN",
  "title": "THE-SYSTEM-PROMPT — the operating contract for every coding agent",
  "desc": "One file, AGENTS.md: a stance, an evidence rule, and a seven-step loop from explore to report. Symlink it into Claude Code, Codex CLI, Gemini CLI, OpenCode, and pi.",
  "lede": 'The operating contract I hand every coding agent. <b>One file, <code>AGENTS.md</code></b>: a stance, an evidence rule, and a seven-step loop from explore to report.',
  "meta": ["AGENTS.md", BYTES, "7 steps", "5 agent paths"],
  "copy": "Copy the contract", "repo": "Repository", "raw": "Raw file",
  "s1": "The preamble",
  "s1lead": "Three rules that hold for the whole session, before the loop starts. Every line below is the file itself.",
  "clauses": [
    ("Stance", "After the plan is confirmed, ask only about data loss, public APIs, security, or migrations; otherwise state assumptions and proceed. Delegate narrow tasks to fresh-context subagents: goal, candidate paths, constraints, expected output. Take large results back as files. Skip it when you already know the file and symbol, or the edit is trivial. Worktree work must be merged back into its origin branch once it is done; ask first only if the target branch is unclear."),
    ("Evidence over assertion", "Repo docs, comments, and my own claims go stale. Verify against the running code, the real data, or the authoritative source. If the evidence contradicts me, challenge me and show it. If it stays uncertain, ask."),
    ("Domain rules", "Always read <code>~/.agents/rules/rules.md</code> when it exists."),
  ],
  "s2": "The seven-step loop",
  "s2lead": "Explore to report. Step four is the only place the agent stops for a human.",
  "steps": [
    ("Explore", "Read the repository instructions, domain model, and real data shapes; tests verify that model, they do not define it. Then read the relevant tests, contracts, and closest matching code. Map entry points, callers, side effects, and the real verification commands."),
    ("Intent", "Restate in one sentence what I want, who hits the problem, and what observable check means done. If I led with a solution, ask what problem it solves. Grill me one question at a time, five at most. Label each claim <code>verified: how</code> or <code>assumed: why</code>, mine included. Still fuzzy after five? List what is decided and what is open, then take the top open item instead of guessing."),
    ("Options", "Give exactly three approaches that differ in strategy, one line each: approach, main tradeoff, cost or risk. Rank them, give one reason for the top pick, then stop and ask me to choose. Each option must cite evidence that it can actually work. Skip only when one approach is clearly the only reasonable one."),
    ("Plan", 'State <code>task type · goal · files · contracts · verification · assumptions</code>, with the goal written as a verifiable check ("fix the bug" becomes "write a failing repro test, then make it pass"). Name what must not change. Record the plan. Plan confirmation is the last human gate. After it, review, execute, gather evidence, and report autonomously.'),
    ("Execute", "Follow the plan. If reality differs, run the planning gate again. Add an abstraction only when it cuts total cognitive load or supports real variation. Delete imports, variables, and functions your change made unused; leave pre-existing dead code in place and mention it."),
    ("Evidence", "Run the relevant regression, unit, integration, type, lint, build, and reproduction checks. Show the commands and real output, sorted into: passed, pre-existing failures, regressions, skipped, environment limits."),
    ("Report", "Simplified Plain Language: one idea per sentence, every term defined. State what I must do next. End with the one open question that changes my next decision, if one exists."),
  ],
  "gate": "Last human gate", "unattended": "unattended from here",
  "s3": "Install", "s3lead": "Keep one canonical copy and link it into each agent's config directory.",
  "gemini": "# Gemini CLI reads GEMINI.md",
  "copyinstall": "Copy the install block",
  "caption": "Where each agent reads it", "th": ("Agent", "Path it loads"),
  "caveatlabel": "Before you run it",
  "caveat": "Move any target that is a regular file to a timestamped backup before you replace it. Skip the directories whose agent you have not installed. On Windows, symlinks need Developer Mode or an admin terminal; copy the file instead and expect it to drift.",
  "s4": "What it leaves out",
  "s4lead": "It is written to sit on top of a harness prompt, not replace it, so it carries only the rules that change default behaviour: give three ranked options before coding, verify claims against running code rather than docs, sort verification output into passed / pre-existing / regression / skipped, and report in a fixed section order.",
  "expects": [
    ("Reads every session", "<b><code>~/.agents/rules/rules.md</code></b> — your domain rules."),
    ("Skills it names", "<b>None.</b> It runs as written on any harness, with or without a skill library."),
    ("Asks for nothing else", "No <b><code>CONTEXT.md</code></b>, glossary, or ADR is required — step one reads whatever repository instructions already exist."),
  ],
  "footer": "cskwork/pi-setup and cskwork/pi-setup-public ship the same file, because the pi installer links ~/.pi/agent/AGENTS.md at their copy. This repository is the canonical one; change it here first.",
  "statusmsg": ("AGENTS.md copied", "Install block copied"),
}

KO = dict(EN, **{
  "lang": "ko", "file": "ko.html", "other": ("index.html", "EN"), "self": "한국어",
  "title": "THE-SYSTEM-PROMPT — 모든 코딩 에이전트가 읽는 운영 계약",
  "desc": "파일 하나, AGENTS.md. 태도와 증거 규칙, 그리고 explore에서 report까지 이어지는 7단계 루프가 들어 있다. Claude Code·Codex CLI·Gemini CLI·OpenCode·pi에 심링크로 걸어 쓴다.",
  "lede": '내가 쓰는 모든 코딩 에이전트에 똑같이 걸어 두는 운영 계약. <b>파일 하나, <code>AGENTS.md</code></b>에 태도와 증거 규칙, explore에서 report까지의 7단계 루프가 들어 있다.',
  "meta": ["AGENTS.md", BYTES, "7단계", "에이전트 경로 5개"],
  "copy": "계약 전문 복사", "repo": "저장소", "raw": "원문 파일",
  "s1": "서두",
  "s1lead": "루프가 시작되기 전, 세션 내내 걸려 있는 세 가지 규칙이다. 아래는 한국어 설명이고, 복사 버튼으로 받는 원문은 영어 파일 그대로다.",
  "clauses": [
    ("태도", "계획이 승인된 뒤에는 데이터 손실과 공개 API, 보안, 마이그레이션에 관한 것만 묻는다. 나머지는 가정을 밝히고 그대로 진행한다. 작업은 좁게 잘라 새 컨텍스트의 서브에이전트에 넘긴다. 목표와 후보 경로, 제약, 기대 산출물을 적어 주고, 결과가 크면 파일로 받는다. 고칠 파일과 심볼을 이미 알거나 사소한 수정이면 직접 한다. worktree에서 한 작업은 끝나는 대로 원래 브랜치에 반드시 병합한다. 대상 브랜치가 분명하지 않을 때만 먼저 물어본다."),
    ("주장보다 증거", "저장소 문서도, 주석도, 내가 하는 말도 낡는다. 돌아가는 코드나 실제 데이터, 아니면 정본에 대고 확인한다. 증거가 내 말과 어긋나면 그 증거를 들어 반박한다. 그래도 불확실하면 묻는다."),
    ("도메인 규칙", "<code>~/.agents/rules/rules.md</code>가 있으면 언제나 읽는다."),
  ],
  "s2": "7단계 루프",
  "s2lead": "explore에서 report까지 이어진다. 에이전트가 사람을 기다리는 곳은 4단계 하나뿐이다.",
  "steps": [
    ("Explore <span class=\"gl\">탐색</span>", "저장소 지침과 도메인 모델, 실제 데이터 형태를 먼저 읽는다. 테스트는 그 모델을 검증할 뿐, 정의하지는 않는다. 그다음 관련 테스트와 계약, 가장 비슷한 코드를 읽는다. 진입점과 호출자, 부수 효과, 그리고 실제로 돌아가는 검증 명령까지 짚어 둔다."),
    ("Intent <span class=\"gl\">의도</span>", "내가 원하는 것을 한 문장으로 다시 말한다. 누가 그 문제를 겪는지, 무엇이 관찰 가능한 완료 조건인지까지 담는다. 내가 해결책부터 꺼냈다면 그 해결책이 푸는 문제가 무엇인지 되묻는다. 한 번에 하나씩, 다섯 개를 넘기지 않고 끝까지 캐묻는다. 주장마다 <code>verified: 방법</code> 또는 <code>assumed: 이유</code>를 붙인다. 내가 한 말도 예외가 아니다. 다섯 번을 물어도 흐릿하면 결정된 것과 열린 것을 나눠 적고, 짐작하는 대신 맨 위 열린 항목부터 푼다."),
    ("Options <span class=\"gl\">선택지</span>", "전략이 서로 다른 세 가지 접근을 한 줄씩 제시한다. 한 줄에 접근과 핵심 트레이드오프, 비용이나 위험을 담는다. 순위를 매기고 1순위를 고른 이유를 하나만 붙인 다음, 거기서 멈춰 선택을 기다린다. 선택지마다 실제로 될 수 있다는 증거를 댄다. 합리적인 접근이 하나뿐일 때만 건너뛴다."),
    ("Plan <span class=\"gl\">계획</span>", '<code>task type · goal · files · contracts · verification · assumptions</code>를 적는다. 목표는 검증할 수 있는 형태로 쓴다. "버그를 고친다"가 아니라 "실패하는 재현 테스트를 먼저 쓰고, 그 테스트를 통과시킨다"처럼. 무엇이 바뀌면 안 되는지 적는다. 계획은 기록으로 남긴다. 계획 승인이 사람이 개입하는 마지막 지점이다. 그 뒤로는 검토와 실행, 증거 수집, 보고를 알아서 끝낸다.'),
    ("Execute <span class=\"gl\">실행</span>", "계획대로 간다. 현실이 계획과 다르면 계획 게이트를 다시 거친다. 추상화는 전체 인지 부하를 줄이거나 실제로 존재하는 변형을 감당할 때만 넣는다. 내 변경 때문에 쓰이지 않게 된 import와 변수, 함수는 지운다. 원래부터 죽어 있던 코드는 그대로 두고 언급만 한다."),
    ("Evidence <span class=\"gl\">증거</span>", "회귀와 단위, 통합, 타입, 린트, 빌드, 재현 검사 가운데 해당하는 것을 돌린다. 명령과 실제 출력을 그대로 보여주고, 통과 / 기존 실패 / 회귀 / 건너뜀 / 환경 제약으로 나눠 정리한다."),
    ("Report <span class=\"gl\">보고</span>", "쉬운 표준 문장(Simplified Plain Language)으로 쓴다. 한 문장에 한 가지 생각만 담고, 쓰는 용어는 모두 정의한다. 내가 다음에 해야 할 일을 밝힌다. 내 다음 결정을 바꿀 열린 질문이 하나 있다면 그것으로 끝낸다."),
  ],
  "gate": "사람이 보는 마지막 지점", "unattended": "여기서부터 사람 없이 진행",
  "s3": "설치", "s3lead": "정본 한 벌만 두고, 그 파일을 에이전트마다 설정 디렉터리에 링크한다.",
  "gemini": "# Gemini CLI는 GEMINI.md를 읽는다",
  "copyinstall": "설치 블록 복사",
  "caption": "에이전트별 로드 경로", "th": ("에이전트", "읽는 경로"),
  "caveatlabel": "실행하기 전에",
  "caveat": "대상이 심링크가 아니라 일반 파일이면 먼저 타임스탬프 백업으로 옮긴다. 설치하지 않은 에이전트의 디렉터리는 건너뛴다. Windows에서 심링크를 만들려면 개발자 모드나 관리자 터미널이 필요하다. 여의치 않으면 복사해서 쓰되, 사본은 시간이 지나면 원본과 어긋난다는 점을 감안한다.",
  "s4": "무엇을 뺐는가",
  "s4lead": "이 파일은 하네스(에이전트를 실행하는 틀) 프롬프트를 대체하지 않고 그 위에 얹힌다. 그래서 기본 동작을 실제로 바꾸는 규칙만 담았다. 코드보다 먼저 순위 매긴 세 가지 안 내놓기, 문서가 아니라 돌아가는 코드로 주장 검증하기, 검증 출력을 통과·기존 실패·회귀·건너뜀으로 나누기, 정해진 순서로 보고하기.",
  "expects": [
    ("매 세션 읽는다", "<b><code>~/.agents/rules/rules.md</code></b> — 당신의 도메인 규칙."),
    ("본문이 부르는 스킬", "<b>없다.</b> 스킬 라이브러리가 있든 없든, 쓰인 그대로 어느 하네스에서나 돌아간다."),
    ("그 밖에 요구하는 것", "<b><code>CONTEXT.md</code></b>도 용어집도 ADR도 필요 없다 — 1단계가 저장소에 이미 있는 지침을 읽을 뿐이다."),
  ],
  "footer": "cskwork/pi-setup과 cskwork/pi-setup-public도 같은 파일을 싣는다. pi 설치기가 ~/.pi/agent/AGENTS.md를 그쪽 사본에 링크하기 때문이다. 정본은 이 저장소이니, 고칠 일이 있으면 여기서 먼저 고친다.",
  "statusmsg": ("AGENTS.md를 복사했습니다", "설치 블록을 복사했습니다"),
})


# ---- walkthrough: one made-up bug, followed through all seven steps ----
UI = {
  "en": {"illus": "Open a step to watch it on a made-up bug: password-reset links that come back as “Invalid token”. The exchanges are illustrative, not transcripts.",
         "see": "Watch this step", "locked": "Waits for approval", "approve": "Approve the plan",
         "approved": "Plan approved. Steps 5 to 7 run unattended.", "reset": "Start over",
         "you": "you", "agent": "agent", "prog": "Step {n} of 7 · {name}", "waiting": "waiting for your approval",
         "hint": "Approve the plan first.",
         "theme": ["Dark", "Light"], "agents": "Agents you use", "shell": "Shell",
         "unix": "macOS / Linux", "win": "Windows PowerShell", "perrepo": "Per-repo (Cursor, Windsurf, Antigravity)",
         "verify": "Then confirm every link resolves", "copyverify": "Copy the check", "wincopy": "# Windows: copy instead of link; rerun after each update", "level": "Walk the level"},
  "ko": {"illus": "단계를 열면 가상의 버그 하나를 끝까지 따라갑니다. 비밀번호 재설정 링크가 “Invalid token”으로 튕기는 문제입니다. 대화는 예시이지 실제 기록이 아닙니다.",
         "see": "이 단계 보기", "locked": "승인을 기다린다", "approve": "계획 승인",
         "approved": "계획이 승인됐다. 5~7단계는 사람 없이 진행된다.", "reset": "처음부터",
         "you": "나", "agent": "에이전트", "prog": "7단계 중 {n} · {name}", "waiting": "승인 대기 중",
         "hint": "먼저 계획을 승인해야 한다.",
         "theme": ["다크", "라이트"], "agents": "쓰는 에이전트", "shell": "셸",
         "unix": "macOS / Linux", "win": "Windows PowerShell", "perrepo": "레포별 (Cursor, Windsurf, Antigravity)",
         "verify": "그다음 링크가 전부 풀리는지 확인", "copyverify": "확인 명령 복사", "wincopy": "# Windows: 링크 대신 복사. 업데이트 때마다 다시 실행", "level": "레벨로 걷기"},
}

XC = {
  "en": [
    [("agent", "Read <code>CONTRIBUTING.md</code>, the <code>auth/</code> module, and the reset-token table. Real rows: <code>expires_at</code> is stored in UTC; <code>TokenService#verify</code> compares it against local time. Callers: <code>ResetController#confirm</code> only. The real check is <code>npm test -- auth</code>.")],
    [("agent", "Restating: after a password reset, the fresh link is rejected as “Invalid token”. One customer hit it 14 times this week [verified: support log #4821]. Done means a fresh link logs the user in, and a test proves it. You opened with “extend the token TTL”. Which problem does that solve, the expiry maths or the copy?"),
     ("you", "The expiry maths. TTL is fine.")],
    [("agent", "1. Compare in UTC inside <code>verify()</code>. One line; risk: another caller assumes local time [verified: one caller]. 2. Store <code>expires_at</code> as an epoch integer. Fixes it for good; needs a migration. 3. Normalise the clock at the API edge. Hides the bug, does not remove it. Recommend 1: the smallest change at the real cause."),
     ("you", "1.")],
    [("agent", "bugfix · fresh reset links log the user in · <code>auth/token_service.ts</code>, <code>auth/token_service.test.ts</code> · contract: <code>verify()</code> keeps its signature and its behaviour for valid tokens · verification: a failing repro test, then <code>npm test -- auth</code> · assumes: the server clock is UTC. Must not change: the token format.")],
    [("agent", "Wrote <em>rejects a fresh token when the server clock is ahead</em>. It fails. Switched the comparison to <code>Date.now()</code> against <code>expires_at.getTime()</code>. It passes. Deleted the <code>localOffset</code> helper the fix made unused; left <code>legacyVerify</code> in place and noted it.")],
    [("agent", "<code>npm test -- auth</code>: 41 passed. Regressions: none. Pre-existing: <code>session.test.ts</code> is skipped, and was before. Environment limit: no staging box with a skewed clock, so the repro test simulates the skew.")],
    [("agent", "Context: reset links were rejected as expired. Changed: (1) <code>verify()</code> compares in UTC. Untouched: token format, TTL, <code>legacyVerify</code>. Status: fixed, tests green. Next for you: deploy and watch the reset-failure metric for a day. Open question: keep <code>legacyVerify</code>, or remove it in a follow-up?")],
  ],
  "ko": [
    [("agent", "<code>CONTRIBUTING.md</code>, <code>auth/</code> 모듈, 재설정 토큰 테이블을 읽었다. 실제 행을 보니 <code>expires_at</code>은 UTC로 저장되는데 <code>TokenService#verify</code>는 로컬 시간과 비교한다. 호출자는 <code>ResetController#confirm</code> 하나. 실제 검증 명령은 <code>npm test -- auth</code>.")],
    [("agent", "다시 말하면: 비밀번호를 재설정한 뒤 새 링크가 “Invalid token”으로 거부된다. 한 고객이 이번 주에만 14번 겪었다 [verified: 지원 로그 #4821]. 완료란 새 링크로 로그인이 되고, 그것을 테스트가 증명하는 상태다. “토큰 TTL을 늘리자”로 시작하셨는데, 그건 만료 계산 문제를 푸는 건가요, 문구 문제를 푸는 건가요?"),
     ("you", "만료 계산. TTL은 그대로.")],
    [("agent", "1. <code>verify()</code> 안에서 UTC로 비교. 한 줄. 위험: 다른 호출자가 로컬 시간을 가정할 수 있다 [verified: 호출자 1곳]. 2. <code>expires_at</code>을 epoch 정수로 저장. 근본 해결이지만 마이그레이션 필요. 3. API 경계에서 시계를 맞춤. 버그를 가릴 뿐 없애지 않는다. 1을 추천: 원인 자리에서 가장 작은 변경."),
     ("you", "1.")],
    [("agent", "bugfix · 새 재설정 링크로 로그인된다 · <code>auth/token_service.ts</code>, <code>auth/token_service.test.ts</code> · 계약: <code>verify()</code>의 시그니처와 유효 토큰에 대한 동작은 그대로 · 검증: 실패하는 재현 테스트, 그다음 <code>npm test -- auth</code> · 가정: 서버 시계는 UTC. 바뀌면 안 되는 것: 토큰 형식.")],
    [("agent", "<em>서버 시계가 앞서 있으면 새 토큰을 거부한다</em> 테스트를 썼다. 실패한다. 비교를 <code>Date.now()</code> 대 <code>expires_at.getTime()</code>으로 바꿨다. 통과한다. 이 수정으로 쓰이지 않게 된 <code>localOffset</code> 헬퍼는 지웠고, <code>legacyVerify</code>는 그대로 두고 언급했다.")],
    [("agent", "<code>npm test -- auth</code>: 41개 통과. 회귀: 없음. 기존 실패: <code>session.test.ts</code>가 건너뛰기 상태인데 원래부터 그랬다. 환경 제약: 시계가 어긋난 스테이징이 없어서 재현 테스트가 어긋남을 흉내 낸다.")],
    [("agent", "맥락: 재설정 링크가 만료된 것으로 거부됐다. 바뀐 것: (1) <code>verify()</code>가 UTC로 비교한다. 손대지 않은 것: 토큰 형식, TTL, <code>legacyVerify</code>. 상태: 수정 완료, 테스트 통과. 다음에 하실 일: 배포 후 하루 동안 재설정 실패 지표를 지켜본다. 열린 질문: <code>legacyVerify</code>를 둘까요, 후속 작업에서 지울까요?")],
  ],
}


def loop_markup(t):
    ui, xc = UI[t["lang"]], XC[t["lang"]]
    out = []
    for i, (name, body) in enumerate(t["steps"], 1):
        cls = "step gate" if i == GATE else ("step after" if i > GATE else "step")
        plain = name.split("<")[0].strip()
        lines = "\n".join(
            '          <li class="%s"><span class="who">%s</span><p>%s</p></li>' % (who, ui[who], text)
            for who, text in xc[i - 1])
        locked = i > GATE
        dcls = "xd locked" if locked else "xd"
        dis = ' aria-disabled="true"' if locked else ""
        summary = ui["locked"] if locked else ui["see"]
        approve = '\n        <button type="button" class="btn approve">%s</button>' % ui["approve"] if i == GATE else ""
        mark = '\n      <p class="mark">%s</p>' % t["gate"] if i == GATE else ""
        out.append('''    <li class="%s" id="step-%d" data-step="%d" data-name="%s"><span class="n">%d</span>
      <h3>%s</h3>
      <p>%s</p>
      <details class="%s" name="loop"%s>
        <summary><svg class="ic chev" aria-hidden="true"><use href="#chev"/></svg>%s</summary>
        <ol class="xc">
%s
        </ol>%s
      </details>%s
    </li>''' % (cls, i, i, plain, i, name, body, dcls, dis, summary, lines, approve, mark))
        if i == GATE:
            out.append('    <li class="after divider" aria-hidden="true"><p class="unattended">%s</p></li>' % t["unattended"])
    return "\n".join(out)


# ---- the level: the contract itself, parsed from AGENTS.md, laid along a corridor ----
def parse_contract():
    import re
    paras = [p.strip() for p in AGENTS.strip().split("\n\n") if p.strip() and not p.startswith("# ")]
    out = []
    for p in paras:
        m = re.match(r"\*\*(?:(\d+)\. )?([^*]+?)\.\*\*\s+(.*)", p, re.S)
        n, label, text = m.group(1), m.group(2), m.group(3)
        text = html.escape(text, quote=False)
        text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
        out.append((int(n) if n else None, label, text))
    return out


def level_page():
    blocks = parse_contract()
    pre = [b for b in blocks if b[0] is None]
    steps = [b for b in blocks if b[0] is not None]
    stations = []
    pre_html = "\n".join(f'      <div class="clause"><h3>{l}</h3><p>{t}</p></div>' for _, l, t in pre)
    stations.append(f'''    <section class="station" data-i="0" style="--i:0" aria-labelledby="st0">
      <p class="tag">Before the loop</p>
      <h2 id="st0">Three rules that hold for the whole session</h2>
{pre_html}
    </section>''')
    for n, l, t in steps:
        gate = n == GATE
        extra = ""
        if gate:
            extra = '''
      <div class="door" aria-hidden="true"><div class="leaf l"></div><div class="leaf r"></div></div>
      <p class="mark">Last human gate</p>
      <button type="button" class="btn approve">Approve the plan</button>'''
        stations.append(f'''    <section class="station{" gate" if gate else ""}{" after" if n > GATE else ""}" data-i="{n}" style="--i:{n}" aria-labelledby="st{n}">
      <p class="tag">Step {n} of 7</p>
      <h2 id="st{n}">{l}</h2>
      <p class="body">{t}</p>{extra}
    </section>''')
    stations.append(f'''    <section class="station outro" data-i="8" style="--i:8" aria-labelledby="st8">
      <p class="tag">End of the loop</p>
      <h2 id="st8">Take the file with you</h2>
      <p class="body">{BYTES}. Copy it, put it at <code>~/.agents/AGENTS.md</code>, and link it into every agent you run.</p>
      <div class="acts">
        <button type="button" class="btn" data-copy="agents-md">Copy the contract</button>
        <a class="btn ghost" href="index.html#install">Install it</a>
      </div>
      <span class="status" role="status" aria-live="polite"></span>
    </section>''')
    dots = "\n".join(f'      <li><button type="button" data-go="{i}" aria-label="Station {i}"></button></li>' for i in range(9))
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>THE-SYSTEM-PROMPT — the level</title>
<meta name="description" content="The operating contract laid out as a corridor: three standing rules, seven stations, one gate you have to open yourself. Every word is the file.">
<meta name="color-scheme" content="light dark">
<meta property="og:type" content="website">
<meta property="og:title" content="THE-SYSTEM-PROMPT — the level">
<meta property="og:description" content="Walk the contract: three rules, seven stations, one gate. Every word is the file.">
<meta property="og:url" content="https://cskwork.github.io/THE-SYSTEM-PROMPT/level.html">
<meta property="og:image" content="https://cskwork.github.io/THE-SYSTEM-PROMPT/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%2315171c'/><path d='M10 7v18M16 7v18' stroke='%23fbfaf7' stroke-width='2'/><path d='M7 16h18' stroke='%23c0392b' stroke-width='2'/></svg>">
<link rel="stylesheet" href="style.css">
<link rel="stylesheet" href="level.css">
</head>
<body class="level">
<a class="skip" href="#flat">Skip the corridor, read it flat</a>
<header class="hud">
  <a class="home" href="index.html">THE-<span>SYSTEM</span>-PROMPT</a>
  <p class="where" role="status" aria-live="polite"></p>
  <div class="hud-acts">
    <button type="button" class="flat-toggle" aria-pressed="false">Flat view</button>
    <button type="button" class="theme" hidden data-labels="Dark|Light">Dark</button>
  </div>
</header>

<div class="stage" id="stage">
  <div class="floor" aria-hidden="true"></div>
  <div class="world" id="world">
{chr(10).join(stations)}
  </div>
</div>

<nav class="rail" aria-label="Stations">
  <ol>
{dots}
  </ol>
</nav>

<footer class="pad">
  <button type="button" class="nav prev" aria-label="Previous station">↑</button>
  <p class="hint">Scroll, arrow keys, or swipe. The gate opens only when you approve the plan.</p>
  <button type="button" class="nav next" aria-label="Next station">↓</button>
</footer>

<script id="agents-md" type="text/plain">{AGENTS}</script>
<script>window.COPY_MSG={{"agents-md":"AGENTS.md copied"}};</script>
<script src="app.js"></script>
<script src="level.js"></script>
</body>
</html>
'''


def page(t):
    other_href, other_label = t["other"]
    clauses = "\n".join(
        f'    <div><p class="k">{k}</p><p class="v">{v}</p></div>' for k, v in t["clauses"])
    expects = "\n".join(
        f'    <div><p class="k">{k}</p><p class="v">{v}</p></div>' for k, v in t["expects"])
    steps = loop_markup(t)
    ui = UI[t["lang"]]
    rows = "\n".join(f'        <tr><td>{a}</td><td><code>{b}</code></td></tr>' for a, b in PATHS)
    meta = "\n".join(f'      <span>{m}</span>' for m in t["meta"])
    return f'''<!DOCTYPE html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<meta name="color-scheme" content="light dark">
<meta property="og:type" content="website">
<meta property="og:title" content="{t["title"]}">
<meta property="og:description" content="{t["desc"]}">
<meta property="og:url" content="https://cskwork.github.io/THE-SYSTEM-PROMPT/{"" if t["lang"] == "en" else t["file"]}">
<meta property="og:image" content="https://cskwork.github.io/THE-SYSTEM-PROMPT/og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" hreflang="en" href="{REPO.replace("https://github.com/cskwork", "https://cskwork.github.io")}/">
<link rel="alternate" hreflang="ko" href="https://cskwork.github.io/THE-SYSTEM-PROMPT/ko.html">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%2315171c'/><path d='M10 7v18M16 7v18' stroke='%23fbfaf7' stroke-width='2'/><path d='M7 16h18' stroke='%23c0392b' stroke-width='2'/></svg>">
<link rel="stylesheet" href="style.css">
</head>
<body>
<svg width="0" height="0" aria-hidden="true" style="position:absolute"><symbol id="ext" viewBox="0 0 12 12"><path d="M4 2h6v8"/><path d="M10 2 2.5 9.5"/></symbol><symbol id="chev" viewBox="0 0 12 12"><path d="M3 4.5 6 7.5l3-3"/></symbol></svg>

<header class="sheet">
  <nav class="lang"><a href="{t["file"]}" aria-current="page">{t["self"]}</a><a href="{other_href}">{other_label}</a><button type="button" class="theme" hidden data-labels="{ui["theme"][0]}|{ui["theme"][1]}">{ui["theme"][0]}</button></nav>
  <h1>THE-<span>SYSTEM</span>-PROMPT</h1>
  <div class="grid masthead">
    <p class="meta">
{meta}
    </p>
    <p class="lede">{t["lede"]}</p>
  </div>
  <div class="acts">
    <button type="button" class="btn" data-copy="agents-md">{t["copy"]}</button>
    <a class="link" href="{REPO}">{t["repo"]} <svg class="ic"><use href="#ext"/></svg></a>
    <a class="link" href="{RAW}">{t["raw"]} <svg class="ic"><use href="#ext"/></svg></a>
    <a class="link level-link" href="level.html">{ui["level"]} <svg class="ic"><use href="#ext"/></svg></a>
  </div>
  <span class="status" role="status" aria-live="polite"></span>
</header>

<main>
<section id="preamble" class="sheet"><div class="grid">
  <h2>{t["s1"]}</h2>
  <div>
  <p class="lead">{t["s1lead"]}</p>
  <div class="rows">
{clauses}
  </div>
  </div>
</div></section>

<section id="loop" class="sheet"><div class="grid">
  <div class="head"><h2>{t["s2"]}</h2><p class="prog" role="status" aria-live="polite"></p><button type="button" class="reset" hidden>{ui["reset"]}</button></div>
  <div>
  <p class="lead">{t["s2lead"]}</p>
  <p class="illus">{ui["illus"]}</p>
  <ol class="loop anim">
{steps}
  </ol>
  </div>
</div></section>

<section id="install" class="sheet"><div class="grid">
  <h2>{t["s3"]}</h2>
  <div>
  <p class="lead">{t["s3lead"]}</p>
  <form class="cfg" hidden>
    <fieldset><legend>{ui["agents"]}</legend>
      <label><input type="checkbox" name="agent" value="claude" checked> Claude Code</label>
      <label><input type="checkbox" name="agent" value="codex" checked> Codex CLI</label>
      <label><input type="checkbox" name="agent" value="gemini" checked> Gemini CLI</label>
      <label><input type="checkbox" name="agent" value="opencode" checked> OpenCode</label>
      <label><input type="checkbox" name="agent" value="pi" checked> pi</label>
      <label><input type="checkbox" name="agent" value="repo"> {ui["perrepo"]}</label>
    </fieldset>
    <fieldset><legend>{ui["shell"]}</legend>
      <label><input type="radio" name="shell" value="unix" checked> {ui["unix"]}</label>
      <label><input type="radio" name="shell" value="win"> {ui["win"]}</label>
    </fieldset>
  </form>
  <pre id="install-block"><code>{INSTALL.format(gemini=t["gemini"])}</code></pre>
  <div class="acts">
    <button type="button" class="btn" data-copy="install-block">{t["copyinstall"]}</button>
  </div>
  <span class="status" role="status" aria-live="polite"></span>
  <div class="verify" hidden>
    <p class="k">{ui["verify"]}</p>
    <pre id="verify-block"><code></code></pre>
    <div class="acts"><button type="button" class="btn" data-copy="verify-block">{ui["copyverify"]}</button></div>
    <span class="status" role="status" aria-live="polite"></span>
  </div>
  <table>
    <caption>{t["caption"]}</caption>
    <thead><tr><th scope="col">{t["th"][0]}</th><th scope="col">{t["th"][1]}</th></tr></thead>
    <tbody>
{rows}
    </tbody>
  </table>
  <p class="caveat"><b>{t["caveatlabel"]}</b>{t["caveat"]}</p>
  </div>
</div></section>

<section id="scope" class="sheet"><div class="grid">
  <h2>{t["s4"]}</h2>
  <div>
  <p class="lead">{t["s4lead"]}</p>
  <div class="rows">
{expects}
  </div>
  </div>
</div></section>
</main>

<footer class="sheet"><div class="grid">
  <p><a href="{REPO}">cskwork/THE-SYSTEM-PROMPT</a> · <a href="{RAW}">raw AGENTS.md</a></p>
  <p>{t["footer"]}</p>
</div></footer>

<script id="agents-md" type="text/plain">{AGENTS}</script>
<script>window.COPY_MSG={{"agents-md":"{t["statusmsg"][0]}","install-block":"{t["statusmsg"][1]}"}};window.WALK={{"prog":"{ui["prog"]}","waiting":"{ui["waiting"]}","approved":"{ui["approved"]}","hint":"{ui["hint"]}","see":"{ui["see"]}","locked":"{ui["locked"]}"}};window.CFG={{"gemini":"{t["gemini"]}","wincopy":"{ui["wincopy"]}"}};</script>
<script src="app.js"></script>
</body>
</html>
'''


for t in (EN, KO):
    (ROOT / t["file"]).write_text(page(t))
    print(t["file"], len((ROOT / t["file"]).read_text()), "bytes")
(ROOT / "level.html").write_text(level_page())
print("level.html", len((ROOT / "level.html").read_text()), "bytes")
