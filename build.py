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
  "desc": "One file, AGENTS.md: a stance, an evidence rule, and a seven-step loop from orient to report. Symlink it into Claude Code, Codex CLI, Gemini CLI, OpenCode, and pi.",
  "lede": 'The operating contract I hand every coding agent. <b>One file, <code>AGENTS.md</code></b>: a stance, an evidence rule, and a seven-step loop from orient to report.',
  "meta": ["AGENTS.md", "2,861 bytes", "7 steps", "5 agent paths"],
  "copy": "Copy the contract", "repo": "Repository", "raw": "Raw file",
  "s1": "The preamble",
  "s1lead": "Four rules that hold for the whole session, before the loop starts. Every line below is the file itself.",
  "clauses": [
    ("Stance", "Tests verify the domain model; they do not define it. Ask only about data loss, public APIs, security, or migrations. Otherwise state assumptions and proceed. Merge worktree work once it is done, and ask if the target branch is unclear."),
    ("Evidence over assertion", "Repo docs, comments, and my own claims go stale. Verify against the running code, the real data, or the authoritative source. If the evidence contradicts me, challenge me and show it. If it stays uncertain, ask."),
    ("Domain rules", "Always read <code>~/.agents/rules/rules.md</code>."),
    ("Writing", "Apply the <code>unslop</code> skill to every piece of prose: reports, commit messages, comments, docs."),
  ],
  "s2": "The seven-step loop",
  "s2lead": "Orient to report. Step four is the only place the agent stops for a human.",
  "steps": [
    ("Orient", "Read the repository instructions, domain model, and real data shapes, then the relevant tests, contracts, and closest matching code. Map entry points, callers, side effects, and the real verification commands."),
    ("Options", "Before any plan or code, give exactly three approaches that differ in strategy, one line each: approach, main tradeoff, cost or risk. Rank them, give one reason for the top pick, then stop and ask me to choose. Skip only when one approach is clearly the only reasonable one."),
    ("Delegate", "Send narrow tasks to fresh-context subagents. Each task states goal, candidate paths, constraints, and expected output. Return large results as files, verified independently. Skip when you know the exact file and symbol, or the change is one trivial edit."),
    ("Plan", 'State <code>task type · goal · files · contracts · verification · assumptions</code>, with the goal written as a verifiable check ("fix the bug" becomes "write a failing repro test, then make it pass"). If intent is unclear, use <code>brainstorming</code>: one question at a time until ~95% confident. Record the plan with <code>writing-plans</code>. Plan confirmation is the last human gate. After it, review, execute, verify, and report autonomously.'),
    ("Execute", "Follow the plan. If reality differs, run the planning gate again. Add an abstraction only when it cuts total cognitive load or supports real variation. Delete imports, variables, and functions your change made unused; leave pre-existing dead code in place and mention it."),
    ("Verify", "Run the relevant regression, unit, integration, type, lint, build, and reproduction checks. Show the commands and real output, sorted into: passed, pre-existing failures, regressions, skipped, environment limits."),
    ("Report", "Simplified Technical English: one idea per sentence, every term defined. Use the project's language from <code>CONTEXT.md</code>, the glossary, and ADRs; flag any term that differs from the code. Sections in order: context, what changed, what stayed untouched, status. Number behavior changes; do not group them by file. State what I must do next. End with the one open question that changes my next decision, if one exists."),
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
    ("Skills it names", "<b><code>unslop</code>, <code>brainstorming</code>, <code>writing-plans</code></b> — drop the mention if you do not have them."),
    ("Reads when present", "<b><code>CONTEXT.md</code>, a glossary, or ADRs</b> in the repository."),
  ],
  "footer": "cskwork/pi-setup and cskwork/pi-setup-public ship the same file, because the pi installer links ~/.pi/agent/AGENTS.md at their copy. This repository is the canonical one; change it here first.",
  "statusmsg": ("AGENTS.md copied", "Install block copied"),
}

KO = dict(EN, **{
  "lang": "ko", "file": "ko.html", "other": ("index.html", "EN"), "self": "한국어",
  "title": "THE-SYSTEM-PROMPT — 모든 코딩 에이전트가 읽는 운영 계약",
  "desc": "파일 하나, AGENTS.md. 태도와 증거 규칙, 그리고 orient에서 report까지 이어지는 7단계 루프가 들어 있다. Claude Code·Codex CLI·Gemini CLI·OpenCode·pi에 심링크로 걸어 쓴다.",
  "lede": '내가 쓰는 모든 코딩 에이전트에 똑같이 걸어 두는 운영 계약. <b>파일 하나, <code>AGENTS.md</code></b>에 태도와 증거 규칙, orient에서 report까지의 7단계 루프가 들어 있다.',
  "meta": ["AGENTS.md", "2,861 bytes", "7단계", "에이전트 경로 5개"],
  "copy": "계약 전문 복사", "repo": "저장소", "raw": "원문 파일",
  "s1": "서두",
  "s1lead": "루프가 시작되기 전, 세션 내내 걸려 있는 네 가지 규칙이다. 아래는 한국어 설명이고, 복사 버튼으로 받는 원문은 영어 파일 그대로다.",
  "clauses": [
    ("태도", "테스트는 도메인 모델을 검증할 뿐, 정의하지는 않는다. 데이터 손실과 공개 API, 보안, 마이그레이션에 관한 것만 묻는다. 나머지는 가정을 밝히고 그대로 진행한다. worktree에서 한 작업은 끝나는 대로 병합하되, 대상 브랜치가 분명하지 않으면 물어본다."),
    ("주장보다 증거", "저장소 문서도, 주석도, 내가 하는 말도 낡는다. 돌아가는 코드나 실제 데이터, 아니면 정본에 대고 확인한다. 증거가 내 말과 어긋나면 그 증거를 들어 반박한다. 그래도 불확실하면 묻는다."),
    ("도메인 규칙", "언제나 <code>~/.agents/rules/rules.md</code>를 읽는다."),
    ("글쓰기", "보고서와 커밋 메시지, 주석, 문서까지 모든 글에 <code>unslop</code> 스킬을 적용한다."),
  ],
  "s2": "7단계 루프",
  "s2lead": "orient에서 report까지 이어진다. 에이전트가 사람을 기다리는 곳은 4단계 하나뿐이다.",
  "steps": [
    ("Orient <span class=\"gl\">파악</span>", "저장소 지침과 도메인 모델, 실제 데이터 형태를 먼저 읽는다. 그다음 관련 테스트와 계약, 가장 비슷한 코드를 읽는다. 진입점과 호출자, 부수 효과, 그리고 실제로 돌아가는 검증 명령까지 짚어 둔다."),
    ("Options <span class=\"gl\">선택지</span>", "계획이나 코드를 내놓기 전에, 전략이 서로 다른 세 가지 접근을 한 줄씩 제시한다. 한 줄에 접근과 핵심 트레이드오프, 비용이나 위험을 담는다. 순위를 매기고 1순위를 고른 이유를 하나만 붙인 다음, 거기서 멈춰 선택을 기다린다. 합리적인 접근이 하나뿐일 때만 건너뛴다."),
    ("Delegate <span class=\"gl\">위임</span>", "작업을 좁게 잘라 새 컨텍스트의 서브에이전트에 넘긴다. 작업마다 목표와 후보 경로, 제약, 기대하는 산출물을 적어 준다. 결과가 크면 파일로 받아 따로 검증한다. 고칠 파일과 심볼을 이미 알거나 한 번에 끝나는 사소한 수정이면 위임하지 않는다."),
    ("Plan <span class=\"gl\">계획</span>", '<code>task type · goal · files · contracts · verification · assumptions</code>를 적는다. 목표는 검증할 수 있는 형태로 쓴다. "버그를 고친다"가 아니라 "실패하는 재현 테스트를 먼저 쓰고, 그 테스트를 통과시킨다"처럼. 의도가 분명하지 않으면 <code>brainstorming</code>으로 한 번에 하나씩, 확신이 95%에 이를 때까지 묻는다. 계획은 <code>writing-plans</code>로 남긴다. 계획 승인이 사람이 개입하는 마지막 지점이다. 그 뒤로는 검토와 실행, 검증, 보고를 알아서 끝낸다.'),
    ("Execute <span class=\"gl\">실행</span>", "계획대로 간다. 현실이 계획과 다르면 계획 게이트를 다시 거친다. 추상화는 전체 인지 부하를 줄이거나 실제로 존재하는 변형을 감당할 때만 넣는다. 내 변경 때문에 쓰이지 않게 된 import와 변수, 함수는 지운다. 원래부터 죽어 있던 코드는 그대로 두고 언급만 한다."),
    ("Verify <span class=\"gl\">검증</span>", "회귀와 단위, 통합, 타입, 린트, 빌드, 재현 검사 가운데 해당하는 것을 돌린다. 명령과 실제 출력을 그대로 보여주고, 통과 / 기존 실패 / 회귀 / 건너뜀 / 환경 제약으로 나눠 정리한다."),
    ("Report <span class=\"gl\">보고</span>", "Simplified Technical English로 쓴다. 한 문장에 한 가지 생각만 담고, 쓰는 용어는 모두 정의한다. <code>CONTEXT.md</code>와 용어집, ADR에 있는 프로젝트 언어를 쓰고, 코드와 어긋나는 용어는 짚어 준다. 순서는 맥락, 바뀐 것, 손대지 않은 것, 상태. 동작 변화에는 번호를 붙이고 파일별로 묶지 않는다. 내가 다음에 해야 할 일을 밝힌다. 내 다음 결정을 바꿀 열린 질문이 하나 있다면 그것으로 끝낸다."),
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
    ("본문이 부르는 스킬", "<b><code>unslop</code>, <code>brainstorming</code>, <code>writing-plans</code></b> — 없다면 해당 문장을 지우면 된다."),
    ("있으면 읽는다", "저장소의 <b><code>CONTEXT.md</code></b>와 용어집, ADR."),
  ],
  "footer": "cskwork/pi-setup과 cskwork/pi-setup-public도 같은 파일을 싣는다. pi 설치기가 ~/.pi/agent/AGENTS.md를 그쪽 사본에 링크하기 때문이다. 정본은 이 저장소이니, 고칠 일이 있으면 여기서 먼저 고친다.",
  "statusmsg": ("AGENTS.md를 복사했습니다", "설치 블록을 복사했습니다"),
})


def page(t):
    other_href, other_label = t["other"]
    clauses = "\n".join(
        f'    <div><p class="k">{k}</p><p class="v">{v}</p></div>' for k, v in t["clauses"])
    expects = "\n".join(
        f'    <div><p class="k">{k}</p><p class="v">{v}</p></div>' for k, v in t["expects"])
    steps = []
    for i, (name, body) in enumerate(t["steps"], 1):
        cls = ' class="gate"' if i == 4 else (' class="after"' if i > 4 else "")
        mark = f'<p class="mark">{t["gate"]}</p>' if i == 4 else ""
        steps.append(f'    <li{cls}><span class="n">{i}</span><h3>{name}</h3><p>{body}</p>{mark}</li>')
        if i == 4:
            steps.append(f'    <li class="after divider" aria-hidden="true"><p class="unattended">{t["unattended"]}</p></li>')
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
<link rel="alternate" hreflang="en" href="{REPO.replace("https://github.com/cskwork", "https://cskwork.github.io")}/">
<link rel="alternate" hreflang="ko" href="https://cskwork.github.io/THE-SYSTEM-PROMPT/ko.html">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' rx='6' fill='%2315171c'/><path d='M10 7v18M16 7v18' stroke='%23fbfaf7' stroke-width='2'/><path d='M7 16h18' stroke='%23c0392b' stroke-width='2'/></svg>">
<link rel="stylesheet" href="style.css">
</head>
<body>
<svg width="0" height="0" aria-hidden="true" style="position:absolute"><symbol id="ext" viewBox="0 0 12 12"><path d="M4 2h6v8"/><path d="M10 2 2.5 9.5"/></symbol></svg>

<header class="sheet">
  <nav class="lang"><a href="{t["file"]}" aria-current="page">{t["self"]}</a><a href="{other_href}">{other_label}</a></nav>
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
  <h2>{t["s2"]}</h2>
  <div>
  <p class="lead">{t["s2lead"]}</p>
  <ol class="loop anim">
{chr(10).join(steps)}
  </ol>
  </div>
</div></section>

<section id="install" class="sheet"><div class="grid">
  <h2>{t["s3"]}</h2>
  <div>
  <p class="lead">{t["s3lead"]}</p>
  <pre id="install-block"><code>{INSTALL.format(gemini=t["gemini"])}</code></pre>
  <div class="acts">
    <button type="button" class="btn" data-copy="install-block">{t["copyinstall"]}</button>
  </div>
  <span class="status" role="status" aria-live="polite"></span>
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
<script>window.COPY_MSG={{"agents-md":"{t["statusmsg"][0]}","install-block":"{t["statusmsg"][1]}"}};</script>
<script src="app.js"></script>
</body>
</html>
'''


for t in (EN, KO):
    (ROOT / t["file"]).write_text(page(t))
    print(t["file"], len((ROOT / t["file"]).read_text()), "bytes")
