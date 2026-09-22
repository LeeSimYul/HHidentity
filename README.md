
# Helping Hands Identity Toolkit

This repository contains 'press kit', 'branding artifacts', or other such assets relevant to the community's identity.

Please see the [GUIDELINES](GUIDELINES.md).

---

## About this repository (fork)

This is a fork of **[HelpingHandsVR/identity](https://github.com/HelpingHandsVR/identity)**.

| | |
| --- | --- |
| Upstream | `HelpingHandsVR/identity` (default branch `v2025`) |
| This fork's default branch | **`v2026`** — the current reference point, where work lands |
| Role of this fork | The upstream brand assets, plus a **media team motion and broadcast pipeline** |
| Extension assets | [`media-team/`](media-team) |
| Extension revision | 2026 Edition, built on the 2025 design by Madison |

The upstream assets (`logo/`, `logo_variants/`, `GUIDELINES.md`) are **never modified**. Everything the
media team derives lives under `media-team/`, and that separation is what keeps merges from upstream
conflict-free.

### Media team extensions

| Path | Contents |
| --- | --- |
| [`media-team/README.md`](media-team/README.md) | **Media team operating guide** — Drive folder structure, `YYMMDD` naming convention, version control, 5-person collaboration rules (Korean edition: [`README.ko.md`](media-team/README.ko.md)) |
| [`media-team/MEDIA_GUIDELINES.md`](media-team/MEDIA_GUIDELINES.md) | Media team guidelines — licensing and credit, clear space, minimum sizes and contrast, contributing back upstream |
| [`media-team/overlays/`](media-team/overlays) | Transparent PNG/WebP logo overlays for OBS, Premiere Pro and After Effects |
| [`media-team/templates/`](media-team/templates) | Thumbnail, poster and card news specifications with margin guides |
| [`media-team/badges/`](media-team/badges) | Lower-third and sign-language avatar identity badges |

Every image under `media-team/` is **generated** from the vectors in `logo/`. Edit the generator, not the output:

```bash
pip install -r media-team/requirements.txt
python media-team/generate.py
```

### Where to start

1. [`GUIDELINES.md`](GUIDELINES.md) — the brand rules, which always take precedence
2. [`media-team/MEDIA_GUIDELINES.md`](media-team/MEDIA_GUIDELINES.md) — the media production rules
3. The `README.md` in each folder — file lists and placement figures
4. Credit every piece: `Credit: HelpingHandsVR Identity`

### Branches

| Branch | Role |
| --- | --- |
| **`v2026`** | This fork's default branch. Upstream assets + the media team extensions; every change lands here |
| `v2025` | The 2025 edition snapshot, kept for reference. Not updated day to day |
| `upstream/v2025` | The original repository's default branch — what we merge *from* |

### Staying in sync with upstream

Register the `upstream` remote to keep following the original repository.

```bash
# once
git remote add upstream https://github.com/HelpingHandsVR/identity.git

# confirm the original default branch (v2025 as of 2026-09)
git remote show upstream | sed -n '/HEAD branch/p'

# sync upstream into this fork's default branch
git fetch upstream
git switch v2026
git merge upstream/v2025
git push origin v2026
```

> [!NOTE]
> This fork carries its own commits under `media-team/`, so `v2026` is **not** a fast-forward of
> `upstream/v2025`. Earlier editions of this README used `git merge --ff-only`, which now fails by
> design — use the plain merge above. It stays conflict-free as long as the upstream assets
> (`logo/`, `logo_variants/`, `GUIDELINES.md`) are never edited here.

Re-run `python media-team/generate.py` after any sync that touches `logo/`.
The procedure for contributing assets back upstream is in
[`media-team/MEDIA_GUIDELINES.md` §6](media-team/MEDIA_GUIDELINES.md#6-contributing-back-upstream).

---

<details>
<summary><strong>한국어 (Korean)</strong></summary>

> 위 영문 문서의 국문판입니다. 두 판본이 어긋날 경우 **영문판을 기준**으로 삼아 주세요.

## 이 저장소에 대하여 (포크)

이 저장소는 **[HelpingHandsVR/identity](https://github.com/HelpingHandsVR/identity) 의 포크**입니다.

| 항목 | 값 |
| --- | --- |
| Upstream | `HelpingHandsVR/identity` (기본 브랜치 `v2025`) |
| 이 포크의 기본 브랜치 | **`v2026`** — 현재 기준점이며 모든 작업이 반영되는 브랜치 |
| 이 포크의 역할 | 원본 브랜드 자산 + **미디어 팀 모션/방송 파이프라인 확장** |
| 확장 자산 위치 | [`media-team/`](media-team) |
| 확장 버전 | 2026 Edition (2025 design by Madison 기반) |

원본 자산(`logo/`, `logo_variants/`, `GUIDELINES.md`)은 **수정하지 않습니다.**
미디어 팀이 만든 파생물은 전부 `media-team/` 안에만 두며, 이 분리 덕분에 upstream 동기화가 충돌 없이 이루어집니다.

### 미디어 팀 확장 자산

| 경로 | 내용 |
| --- | --- |
| [`media-team/README.md`](media-team/README.md) | **미디어 팀 운영 안내서** — 드라이브 폴더 구조, `YYMMDD` 파일 명명 규칙, 버전 관리, 5인 협업 규칙 (국문판: [`README.ko.md`](media-team/README.ko.md)) |
| [`media-team/MEDIA_GUIDELINES.md`](media-team/MEDIA_GUIDELINES.md) | 미디어 팀 지침 — 라이선스·출처 표기, 여백, 최소 크기·대비, 역기여 절차 |
| [`media-team/overlays/`](media-team/overlays) | OBS / Premiere Pro / After Effects 용 투명 PNG·WebP 로고 오버레이 |
| [`media-team/templates/`](media-team/templates) | 썸네일 · 포스터 · 카드뉴스 규격과 여백 가이드 |
| [`media-team/badges/`](media-team/badges) | 방송 로어서드 · 수어 아바타 신원 표시용 미디어 배지 |

`media-team/` 아래의 이미지는 전부 `logo/` 의 벡터에서 **자동 생성**됩니다. 직접 수정하지 말고 다시 생성하세요.

```bash
pip install -r media-team/requirements.txt
python media-team/generate.py
```

### 활용 순서

1. [`GUIDELINES.md`](GUIDELINES.md) — 브랜드 원칙 (항상 우선)
2. [`media-team/MEDIA_GUIDELINES.md`](media-team/MEDIA_GUIDELINES.md) — 미디어 제작 규정
3. 각 폴더의 `README.md` — 파일 목록과 배치 수치
4. 결과물에 출처 표기: `Credit: HelpingHandsVR Identity`

### 브랜치 구성

| 브랜치 | 역할 |
| --- | --- |
| **`v2026`** | 이 포크의 기본 브랜치. 원본 자산 + 미디어 팀 확장이 모두 모이는 곳이며, 모든 변경은 여기로 반영됩니다 |
| `v2025` | 2025 에디션 스냅샷. 참고용으로 보존하며 상시 갱신하지 않습니다 |
| `upstream/v2025` | 원본 저장소의 기본 브랜치 — 우리가 **가져오는** 쪽 |

### Upstream 동기화

원본 저장소의 변경사항을 계속 따라가려면 `upstream` 리모트를 등록합니다.

```bash
# 최초 1회
git remote add upstream https://github.com/HelpingHandsVR/identity.git

# 원본 기본 브랜치 확인 (2026-09 기준 v2025)
git remote show upstream | sed -n '/HEAD branch/p'

# 이 포크의 기본 브랜치로 동기화
git fetch upstream
git switch v2026
git merge upstream/v2025
git push origin v2026
```

> [!NOTE]
> 이 포크에는 `media-team/` 아래의 자체 커밋이 있으므로 `v2026` 은 `upstream/v2025` 의 fast-forward 가
> **아닙니다.** 이전 판의 README 가 쓰던 `git merge --ff-only` 는 이제 구조상 실패하므로 위의 일반 병합을
> 사용합니다. 원본 자산(`logo/`, `logo_variants/`, `GUIDELINES.md`)을 수정하지 않는 한 이 병합은 충돌 없이
> 끝납니다.

`logo/` 가 변경된 동기화 이후에는 `python media-team/generate.py` 로 파생 자산을 다시 만듭니다.
원본에 역기여(PR)하는 절차는
[`media-team/MEDIA_GUIDELINES.md` §6](media-team/MEDIA_GUIDELINES.md#6-contributing-back-upstream) 을 따릅니다.

</details>
