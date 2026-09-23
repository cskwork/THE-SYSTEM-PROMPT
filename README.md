# THE-SYSTEM-PROMPT

한국어 사용자는 [한국어 번역](#한국어-번역-korean-translation)을 참고하세요.

[AGENTS.md](AGENTS.md) is the operating contract I give coding agents. It focuses on understanding the user's intent, agreeing on the outcome and scope, and verifying the result. The agent chooses how much planning, delegation, and investigation the task needs.

The contract keeps explicit boundaries around unrelated work, scope changes, data loss, public APIs, security, and migrations. It supplements each agent's existing instructions. It does not claim to improve performance without testing.

The previous contract is preserved unchanged in [the seven-step archive](archive/AGENTS-2026-09-06-seven-step.md).

## Install

Back up existing files before running these commands, including `~/.agents/AGENTS.md`. The commands overwrite the canonical file and replace the listed links. Keep only the agents you use.

```bash
mkdir -p ~/.agents ~/.claude ~/.codex ~/.gemini ~/.config/opencode ~/.pi/agent
curl -fsSL https://raw.githubusercontent.com/cskwork/THE-SYSTEM-PROMPT/main/AGENTS.md \
  -o ~/.agents/AGENTS.md

ln -sfn ~/.agents/AGENTS.md ~/.claude/CLAUDE.md
ln -sfn ~/.agents/AGENTS.md ~/.codex/AGENTS.md
ln -sfn ~/.agents/AGENTS.md ~/.gemini/GEMINI.md
ln -sfn ~/.agents/AGENTS.md ~/.config/opencode/AGENTS.md
ln -sfn ~/.agents/AGENTS.md ~/.pi/agent/AGENTS.md
```

Gemini CLI reads `GEMINI.md`. On Windows, symlinks require Developer Mode or an administrator terminal. If you copy the file instead, update each copy when the contract changes.

Repository instructions and `~/.agents/rules/rules.md`, when present, provide project and domain guidance.

## Landing page

The [English landing page](https://cskwork.github.io/THE-SYSTEM-PROMPT/) and [Korean landing page](https://cskwork.github.io/THE-SYSTEM-PROMPT/ko.html) live in `docs/`. Rebuild them after changing the contract or page content:

```bash
python3 build.py
```

Commit the generated files with the source changes. GitHub Pages serves the site from `docs/`. The pages link to the current contract and archived version, and their copy buttons copy the current English `AGENTS.md`.

## 한국어 번역 (Korean translation)

아래는 [AGENTS.md](AGENTS.md)를 한국어 사용자가 이해하기 쉽도록 옮긴 **참고용 번역**입니다.

> **설치·교체에는 반드시 영어 원본을 쓰세요.** 위 [Install](#install) 명령은 영어 원본 `AGENTS.md`를 그대로 내려받습니다. 이 번역본을 에이전트 설정 파일(`CLAUDE.md`, `AGENTS.md`, `GEMINI.md` 등)에 넣지 마세요. 원본과 번역의 뜻이 다르면 영어 원본이 우선합니다.

### 운영 지침

먼저 관련 맥락을 살펴봅니다. 새 작업을 구현하기 전에는 의도한 결과, 범위, 성공 판단 기준을 다시 정리해 말하고, 요청이 코드나 데이터와 어긋나는 부분을 짚고, 작업 내용을 바꿀 만한 질문을 함께 담아 사용자의 동의를 기다립니다. 되돌리기 쉽고 의도가 분명한 작은 변경이라면 이해한 내용을 밝히고 바로 진행합니다. 동의를 받은 뒤에는 중간 확인 없이 구현, 검증, 전달까지 마칩니다. 다음 단계를 예고하거나, 계속할지 묻거나, 진행을 막지 않는 결정 사항을 늘어놓으며 턴을 끝내지 않습니다. 현재 상황과 권고는 다음 행동과 같은 메시지에 담습니다. 일찍 멈추는 경우는 사용자 없이는 아무것도 진행할 수 없을 때, 보호된 리소스가 막고 있을 때, 합의한 범위를 크게 바꿔야 할 때, 또는 다음 단계가 데이터 손실, 공개 API 변경, 보안상 영향, 승인되지 않은 마이그레이션을 일으킬 때뿐입니다. 병합(merge)이나 배포·공개는 승인받았을 때만 합니다.

현재 요구를 충족하는 가장 단순한 기존 방법을 씁니다. 복잡성은 실제로 드러난 부족함이 있을 때만 더합니다. 프로젝트의 기존 방식을 따르고, 실패는 숨기지 말고 분명히 드러내며, 호환성과 관련 없는 작업은 그대로 보존합니다. 근본 원인을 고칩니다. 검사(테스트 등)를 통과시키려고 검사를 약하게 만들거나, 건너뛰거나, 지우지 않습니다.

판단의 근거는 코드, 실제 데이터, 권위 있는 자료에 두며, 요청에서 언급하지 않은 관련 자료도 함께 확인합니다. 근거와 어긋나는 주장에는 이의를 제기합니다. 바뀐 동작, 실패 상황, 전달 결과는 먼저 기존 테스트로 검증하고, 실제로 빈틈이 있을 때만 그 부분에 한정된 테스트를 추가합니다. 검사를 통과하고 목표한 결과를 달성하면 멈춥니다. 검사가 실패하거나 막히면 근거와 남은 일을 함께 그대로 알립니다.

작업을 다른 에이전트에게 맡길 때는 품질 기준을 충족하는 가장 저렴한 모델과 추론 수준을 씁니다. `rules.md`에 기본값이 있으면 그것을, 없으면 `claude-opus-5-5`를 medium 추론 수준으로 씁니다. 병렬 실행이 전체 작업량을 줄이는 경우가 아니면 한 번에 하나의 에이전트에게만 맡깁니다. 맡길 때는 목표, 경로, 제약 조건, 완료 기준, 확인된 사실만 담은 깨끗한 맥락을 줍니다. 전체를 조율하는 에이전트는 조율에만 집중합니다. 상태를 반복해서 확인(polling)하거나 할 일 없이 기다리는 작업은 피합니다.

사용자에게 보내는 모든 메시지는 비개발자도 이해할 수 있는 말로 간결하게 씁니다. 결과를 먼저 말하고, 사용자가 행동하는 데 필요한 내용만 담습니다. 코드, 데이터, 기술적 근거는 빼고, 사용자가 결정하는 데 필요한 사실을 쉬운 말로 전하며, 자세한 내용은 원하면 알려 주겠다고 제안하고 요청하면 제공합니다. 범위 밖의 문제는 직접 고치지 말고 권고로 알립니다. 변경 이력이 중요할 때는 누가 언제 무엇을 바꿨는지 환경별로 커밋이나 티켓을 들어 밝히고, 모르면 추측하지 말고 "알 수 없음"이라고 말합니다.

저장소의 지침과 `~/.agents/rules/rules.md`가 있으면 읽습니다.
