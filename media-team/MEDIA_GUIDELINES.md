# Helping Hands Media Team Guidelines (2026 Edition)

These guidelines cover **how the media team produces video, broadcast and social content**.
They supplement — and never replace — [GUIDELINES.md](../GUIDELINES.md), the HelpingHandsVR brand
document. **Where the two disagree, the upstream `GUIDELINES.md` always wins.**

- Scope: every derived asset under `media-team/` (overlays, badges, template guides)
- Base design: 2025 design by Madison (upstream `v2025`)
- Revision: 2026 Edition — adds the specifications for the motion and broadcast pipeline

> 한국어 문서는 이 문서 맨 아래의 접이식 섹션에 있습니다.

---

## 1. License compliance and credit

### 1.1 License status

Neither this repository nor upstream `HelpingHandsVR/identity` ships an explicit `LICENSE` file.
The mark and its derivatives are therefore **not automatically free to use** — they may be used only
within the community rules and the scope of `GUIDELINES.md`.

- Distribution outside the community, commercial use, and merchandise need **prior approval from Helping Hands staff**.
- If you are unsure whether a use is allowed, **ask first and build second**.
- Update this section if upstream adds a `LICENSE`.

### 1.2 Credit

Every piece that shows the mark carries a credit.

| Placement | String |
| --- | --- |
| Video outro / end card | `Credit: HelpingHandsVR Identity` |
| Video description, post body | `Logo & identity: HelpingHandsVR Identity — https://github.com/HelpingHandsVR/identity` |
| Foot of a static image (poster, card news) | `Credit: HelpingHandsVR Identity` |
| Documentation of a derived asset in this repo | the string above, plus a note that it is derived |

Rules:

- Hold an outro credit for **at least 3 seconds**, at **4.5:1 or better** contrast against its background.
- If you modified the mark (recolor, monochrome, replaced background), say so beside the credit.
  For example: `Credit: HelpingHandsVR Identity (modified for broadcast)`
- Never shrink the credit into a watermark until it can no longer be read.

---

## 2. Choosing an asset

| Situation | Asset |
| --- | --- |
| Dark or busy background | `overlays/logo_*` (full color) — the default |
| Anything smaller than 32 px | `overlays/logo_precomposed_*` — no clip mask, so edges stay clean at low resolution |
| White or light background | `overlays/logo_positive_space_*` (single color) |
| The mark has to sit directly on white | `overlays/hands_outlined_*` |
| Corner watermark | `overlays/watermark_logo_*` — **alpha 70% already applied** |
| Identity over live footage | `badges/badge_avatar_*`, `badges/badge_lower_third_*` |
| Sign-language avatar identity chip | `badges/badge_avatar_*_128` or larger |
| Checking layout margins | `templates/guides/*_guide.png` |

Use the `.svg` / `.ai` sources in `logo/` directly whenever you need vectors. The rasters under
`media-team/` are **conveniences**; print and large-format work uses the vectors.

---

## 3. Spacing

### 3.1 Clear space

Writing **D** for the width of the mark's bounding box, keep **at least 0.25 D** clear on every side.

> In the 2025 design the hands break past the edge of the circle, so D is measured on the
> **bounding box of the whole mark, not the diameter of the circle**.

No captions, lower thirds, progress bars, other logos or decorative elements enter that space.

### 3.2 Corner watermark

- Inset **5% of the frame height** from each edge (inside the title-safe area).
- Watermark diameter = **6% of the frame height**, with a **64 px floor**.
- Opacity **60–80%**. The shipped assets are fixed at 70%.
- Keep the corner fixed across a series. The default is the **top right**; use the top left when
  persistent UI (subscriber count, chat overlay) already lives there.

| Resolution | Edge inset | Watermark diameter | Asset |
| --- | --- | --- | --- |
| 1280×720 | 36 px | 64 px (floor applies) | `watermark_logo_256` |
| 1920×1080 | 54 px | 65 px | `watermark_logo_256` |
| 2560×1440 | 72 px | 86 px | `watermark_logo_256` |
| 3840×2160 | 108 px | 130 px | `watermark_logo_512` |

### 3.3 Intro and outro

| | Intro | Outro |
| --- | --- | --- |
| Mark diameter | **28%** of frame height | **20%** of frame height |
| Position | Frame center (up to ~2% optical lift allowed) | Top center |
| Minimum hold | **1.5 s** | **3 s**, credit included |
| Fade | 0.3–0.5 s | 0.5 s |
| Surrounding space | nothing within **0.5 D** of the mark | credit text sits **0.5 D** below the mark |

- Keep intro and outro backgrounds **flat or low-saturation**. If the mark has to sit over a clip, put a scrim under it (§4.3).
- Only **fades, uniform scaling and position moves** are allowed. No squash and stretch, rotation, skew, or animating the parts separately (§5).

### 3.4 Lower thirds and identity display

- The `badges/badge_lower_third_*` plates carry the mark in the left cap; the rest is the **text area**.
- Writing H for the plate height, the mark is fixed at diameter `0.72 H`, inset `0.14 H` from the left.
  Adding the clear space from §3.1 (`0.25 D`), text starts **`1.04 H` from the left**. Right padding is `0.28 H`.

| Plate | Mark | Text area (x) | Text width |
| --- | --- | --- | --- |
| `960×160` (1080p) | ⌀115 px at x=22 | 166 – 915 px | 749 px |
| `1440×240` (4K) | ⌀173 px at x=34 | 250 – 1373 px | 1123 px |

- Place the plate **inside the action-safe area (93% of the frame)**, lifted **8% of the frame height** off the bottom edge.
- On an interpreted stream the **interpreter's signing space comes first**. If the lower third collides
  with it, move it to the opposite side; if it still collides, use `badge_avatar_*` instead.

---

## 4. Minimum size and background contrast

### 4.1 Minimum size

| Use | Minimum diameter | Asset |
| --- | --- | --- |
| 1080p broadcast watermark | 64 px | `watermark_logo_256` |
| 4K broadcast watermark | 128 px | `watermark_logo_512` |
| Thumbnail / card news brand block | 8% of the short edge (86 px at 1080) | `logo_256` |
| Sign-language avatar identity chip | 128 px | `badge_avatar_*_128` |
| Screen / UI | 24 px | `logo_precomposed_256` |
| Print | 10 mm | `logo/logo.svg` |

- **Below 32 px** the clip-mask edge breaks up, so always use `logo_precomposed_*`.
- **Below 24 px** drop the mark and use a text credit instead.
- Never upscale. Come down from a **larger** source, and re-render with `generate.py` if none is large enough.

### 4.2 Background contrast

Measured with WCAG 2.1 relative luminance:

| Brand color | On white | On black | On scrim `#0B1218` |
| --- | --- | --- | --- |
| Helping Hands Blue `#3291D3` | **3.43:1** | 6.13:1 | 5.50:1 |
| Helping Hands Green `#4DCE7D` | **2.01:1** | 10.44:1 | 9.37:1 |
| White hands `#FFFFFF` | 1.00:1 | 21.00:1 | 18.85:1 |

Rules:

- The mark's edge needs **3:1 or better** against its backdrop.
- **Helping Hands Green measures 2.01:1 on white, below that bar.** On light backgrounds do not place
  the full-color mark directly — use `logo_positive_space_*` or `hands_outlined_*`.
- The white hands measure 2.01:1 against the green section. That is internal to the mark and is not
  ours to change, but it is why the minimum sizes in §4.1 exist: **never shrink the mark to the point
  where the hands mush together**.

### 4.3 Over live footage

Footage brightness changes frame to frame, so a static contrast calculation does not hold.
**Always put the mark on a scrim plate when it sits over footage.**

| Scrim | Value | Use |
| --- | --- | --- |
| Dark | `#0B1218` @ 72% | Bright or high-contrast footage |
| Light | `#FFFFFF` @ 86% | Dark, even footage |

Every asset in `badges/` already carries one of these. Use the same values if you build your own.

---

## 5. Prohibited

In addition to the rules in `GUIDELINES.md`, media work never does the following.

- **Rotate, skew, mirror or non-uniformly scale** the mark
- Move the hands and the circle **independently**, animate parts separately, or squash and stretch
- Add **drop shadows, glows, bevels or outlines** to the mark (except the white-background outline `GUIDELINES.md` permits)
- Lay **captions, stickers or emoji over the mark**, or use the mark as a caption backing plate
- Drop watermark opacity **below 60%**, to the point the mark is unidentifiable
- **Replace the gradient colors** without approval (follow §6). Monochrome substitutes such as
  `watermark_mono_light_*` are for **technical constraints only** and need staff sign-off before routine use.
- Any use **outside a PG-13 standard**, or in a context that defames or harasses a person or group

---

## 6. Contributing back upstream

Assets the media team builds that are **generally useful to the whole community** go back to
upstream `HelpingHandsVR/identity`.

### 6.1 What goes up, what stays

| PR to upstream | Stays in this fork (`media-team/`) |
| --- | --- |
| New vector sources, general-purpose logo variants | Campaign- or episode-specific comps |
| Reproducible generator scripts | One-off assets cut to a particular broadcast layout |
| Documentation fixes — typos, wrong figures | Internal team workflow notes |
| General specifications (e.g. watermark spacing) | Team schedules and owner information |

> The `media-team/` path itself never goes upstream. That separation is what keeps upstream merges conflict-free.

### 6.2 Procedure

```bash
# 1. Register the upstream original (once)
git remote add upstream https://github.com/HelpingHandsVR/identity.git

# 2. Confirm the base branch (v2025 as of 2026-09)
git remote show upstream | sed -n '/HEAD branch/p'

# 3. Fetch the latest original and branch from it
git fetch upstream
git switch -c feat/<topic> upstream/v2025

# 4. Push to this fork
git push -u origin feat/<topic>
```

Then open a pull request on GitHub from `LeeSimYul/HHidentity:feat/<topic>` to `HelpingHandsVR/identity:v2025`.

### 6.3 Pre-PR checklist

- [ ] Does the change respect the color, orientation and composition rules in `GUIDELINES.md`?
- [ ] Did you include the **vector source or the generator**, not only rasters?
- [ ] For generated assets, is the **reproduction command** (e.g. `python media-team/generate.py`) in the PR body?
- [ ] If it introduces a new color, typeface or variant of the mark, is the **staff approval** attached?
- [ ] Does it pull in outside assets (fonts, photos, icons)? If so, is their license stated?
- [ ] Are the commits scoped to a single topic?
- [ ] Did any team-only file from `media-team/` slip in?

### 6.4 Syncing with upstream

When the original is updated, bring the fork along. Merge into `v2026`, this fork's default branch —
`--ff-only` no longer applies, because the fork carries its own commits under `media-team/`.

```bash
git fetch upstream
git switch v2026
git merge upstream/v2025
git push origin v2026
```

After any sync that touches the logo sources (`logo/`), **regenerate the derived assets**.

```bash
pip install -r media-team/requirements.txt
python media-team/generate.py
git add media-team
git commit -m "chore: regenerate media-team assets for upstream logo update"
```

---

## 7. Regenerating assets

Everything under `media-team/overlays`, `media-team/badges` and `media-team/templates/guides` is
**output from `media-team/generate.py`**. Do not hand-edit it — change the constants and re-run.

```bash
pip install -r media-team/requirements.txt
python media-team/generate.py
```

To change a specification, edit the constants at the top of `generate.py` (`WATERMARK_ALPHA`,
`DARK_PLATE`, `MARGIN_RATIO`, `LOGO_MIN_RATIO`, …) **and update the matching figures in this document**.

---

<details>
<summary><strong>한국어 (Korean)</strong></summary>

> 위 영문 문서의 국문판입니다. 두 판본이 어긋날 경우 **영문판을 기준**으로 삼고, 어긋난 부분은 이슈로 알려 주세요.

이 문서는 **미디어 팀이 영상·방송·소셜 콘텐츠를 제작할 때** 지켜야 할 지침입니다.
상위 문서인 [GUIDELINES.md](../GUIDELINES.md)(HelpingHandsVR 브랜드 원칙)를 대체하지 않으며, 이를 **보완**합니다.
두 문서가 충돌할 경우 **언제나 원본 `GUIDELINES.md`가 우선**합니다.

- 적용 범위: `media-team/` 아래의 모든 파생 자산 (오버레이 · 배지 · 템플릿 가이드)
- 기준 디자인: 2025 design by Madison (upstream `v2025`)
- 개정: 2026 Edition — 모션/방송 파이프라인용 규격 추가

---

## 1. 라이선스 준수 및 출처 표기

### 1.1 라이선스 상태

이 저장소(및 upstream `HelpingHandsVR/identity`)에는 **명시적인 `LICENSE` 파일이 없습니다.**
따라서 로고와 파생 자산은 자동으로 자유 이용이 허용되지 않으며, **커뮤니티 규칙과 `GUIDELINES.md`의 범위 안에서만** 사용합니다.

- 커뮤니티 외부 배포, 상업적 이용, 굿즈·상품화는 **사전에 Helping Hands 스태프의 승인**을 받습니다.
- 사용 가능 여부가 불확실하면 **먼저 묻고, 그 다음 만듭니다.**
- upstream에 `LICENSE`가 추가되면 이 절을 갱신합니다.

### 1.2 크레딧 표기

로고가 등장하는 모든 결과물에는 출처를 표기합니다.

| 위치 | 표기 문자열 |
| --- | --- |
| 영상 아웃트로 / 엔드카드 | `Credit: HelpingHandsVR Identity` |
| 영상 설명란 · 게시물 본문 | `Logo & identity: HelpingHandsVR Identity — https://github.com/HelpingHandsVR/identity` |
| 정적 이미지(포스터·카드뉴스) 하단 | `Credit: HelpingHandsVR Identity` |
| 저장소 내 파생 자산 문서 | 위 문자열 + 파생 사실 명시 |

표기 규칙:

- 아웃트로 크레딧은 **최소 3초** 노출하고, 본문 대비 **4.5:1 이상**의 명도 대비를 확보합니다.
- 로고를 변형(색상 교체, 단색화, 배경 치환)했다면 크레딧 옆에 파생 사실을 명시합니다.
  예: `Credit: HelpingHandsVR Identity (modified for broadcast)`
- 크레딧을 워터마크 안에 넣어 읽을 수 없게 축소하지 않습니다.

---

## 2. 자산 선택

| 상황 | 사용할 자산 |
| --- | --- |
| 어둡거나 복잡한 배경 | `overlays/logo_*` (풀컬러) |
| 32 px 미만의 작은 표시 | `overlays/logo_precomposed_*` (클립 마스크 없음, 저해상도에서 에지가 깨끗함) |
| 흰색·밝은 배경 | `overlays/logo_positive_space_*` |
| 흰 배경에 마크를 직접 올려야 할 때 | `overlays/hands_outlined_*` |
| 화면 모서리 워터마크 | `overlays/watermark_logo_*` (알파 70% 사전 적용) |
| 실사 푸티지 위 신원 표시 | `badges/badge_avatar_*`, `badges/badge_lower_third_*` |
| 수어 아바타 신원 칩 | `badges/badge_avatar_*_128` 이상 |
| 레이아웃 여백 확인 | `templates/guides/*_guide.png` |

원본 벡터가 필요하면 `logo/` 의 `.svg` / `.ai` 를 그대로 사용합니다. `media-team/` 의 래스터 자산은 **편의를 위한 파생본**이며, 인쇄·대형 출력에는 벡터를 씁니다.

---

## 3. 여백 규정

### 3.1 기본 여백 (clear space)

마크의 **바운딩 박스 너비를 D** 라 할 때, 사방으로 **최소 0.25 D** 의 여백을 확보합니다.

> 2025 디자인에서 손 모양은 원의 경계를 벗어납니다. 따라서 D는 **원의 지름이 아니라 마크 전체의 바운딩 박스**를 기준으로 측정합니다.

여백 안에는 자막, 로어서드, 진행바, 다른 로고, 장식 요소를 배치하지 않습니다.

### 3.2 화면 모서리 워터마크

- 프레임 가장자리로부터 **프레임 높이의 5%** 를 띄웁니다 (타이틀 세이프 영역 준수).
- 워터마크 지름 = **프레임 높이의 6%**, 단 **최소 64 px**.
- 불투명도 **60–80%**. 배포 자산은 70%로 고정되어 있습니다.
- 위치는 하나의 시리즈 안에서 고정합니다. 기본값은 **우측 상단**이며, 우측 상단에 상시 UI(구독자 수, 채팅 오버레이 등)가 있으면 좌측 상단을 씁니다.

| 해상도 | 가장자리 여백 | 워터마크 지름 | 권장 파일 |
| --- | --- | --- | --- |
| 1280×720 | 36 px | 64 px (최소값 적용) | `watermark_logo_256` |
| 1920×1080 | 54 px | 65 px | `watermark_logo_256` |
| 2560×1440 | 72 px | 86 px | `watermark_logo_256` |
| 3840×2160 | 108 px | 130 px | `watermark_logo_512` |

### 3.3 인트로 / 아웃트로

| 항목 | 인트로 | 아웃트로 |
| --- | --- | --- |
| 마크 지름 | 프레임 높이의 **28%** | 프레임 높이의 **20%** |
| 위치 | 화면 중앙 (광학 중심 기준, 상단으로 약 2% 보정 허용) | 중앙 상단 |
| 최소 유지 시간 | **1.5초** | **3초** (크레딧 포함) |
| 페이드 | 0.3–0.5초 | 0.5초 |
| 주변 여백 | 마크 사방 **0.5 D** 내에 다른 요소 없음 | 크레딧 텍스트는 마크 하단에서 **0.5 D** 아래 |

- 인트로/아웃트로 배경은 **단색 또는 저채도**로 유지합니다. 영상 클립 위에 마크를 띄워야 한다면 스크림(§4.3)을 깝니다.
- 애니메이션은 **페이드 · 균일 스케일 · 위치 이동**만 허용합니다. 스쿼시/스트레치, 회전, 스큐, 파츠 분해는 금지입니다(§5).

### 3.4 로어서드 / 신원 표시

- `badges/badge_lower_third_*` 플레이트는 좌측 캡에 마크가, 나머지 영역이 **텍스트 영역**입니다.
- 플레이트 높이를 H라 할 때 마크는 지름 `0.72 H`, 좌측 여백 `0.14 H` 로 고정되어 있습니다. 여기에 §3.1의 여백(`0.25 D`)을 더하면 텍스트는 **좌측 `1.04 H` 지점부터** 시작합니다. 우측 여백은 `0.28 H` 입니다.

| 플레이트 | 마크 | 텍스트 영역 (x 범위) | 텍스트 폭 |
| --- | --- | --- | --- |
| `960×160` (1080p) | 지름 115 px, x=22 | 166 – 915 px | 749 px |
| `1440×240` (4K) | 지름 173 px, x=34 | 250 – 1373 px | 1123 px |

- 플레이트는 **액션 세이프 영역(프레임의 93%) 안**, 하단 가장자리로부터 프레임 높이의 **8%** 위에 배치합니다.
- 수어 통역 화면에서는 **통역자의 손 동작 영역을 가리지 않는 위치**를 우선합니다. 충돌 시 로어서드를 반대쪽으로 옮기고, 그래도 겹치면 배지를 `badge_avatar_*` 로 대체합니다.

---

## 4. 최소 크기 및 배경 대비

### 4.1 최소 크기

| 용도 | 최소 지름 | 권장 파일 |
| --- | --- | --- |
| 1080p 방송 워터마크 | 64 px | `watermark_logo_256` |
| 4K 방송 워터마크 | 128 px | `watermark_logo_512` |
| 썸네일 · 카드뉴스 브랜드 블록 | 짧은 변의 8% (1080 기준 86 px) | `logo_256` |
| 수어 아바타 신원 칩 | 128 px | `badge_avatar_*_128` |
| 화면 / UI | 24 px | `logo_precomposed_256` |
| 인쇄 | 10 mm | `logo/logo.svg` |

- **32 px 미만**에서는 클립 마스크 경계가 깨지므로 반드시 `logo_precomposed_*` 를 사용합니다.
- **24 px 미만**에서는 마크를 쓰지 않고 텍스트 표기로 대체합니다.
- 업스케일 금지: 필요한 크기보다 **큰** 소스에서 줄여 씁니다. 부족하면 `generate.py` 로 다시 렌더링합니다.

### 4.2 배경 대비

측정값(WCAG 2.1 상대 명도 기준):

| 브랜드 색 | 흰색 배경 | 검정 배경 | 스크림 `#0B1218` |
| --- | --- | --- | --- |
| Helping Hands Blue `#3291D3` | **3.43:1** | 6.13:1 | 5.50:1 |
| Helping Hands Green `#4DCE7D` | **2.01:1** | 10.44:1 | 9.37:1 |
| 흰색 손 `#FFFFFF` | 1.00:1 | 21.00:1 | 18.85:1 |

규칙:

- 마크의 가장자리와 배경 사이 대비는 **3:1 이상**이어야 합니다.
- **Helping Hands Green은 흰색 배경에서 2.01:1 로 기준에 미달합니다.** 밝은 배경에서는 풀컬러 마크를 직접 올리지 말고 `logo_positive_space_*` 또는 `hands_outlined_*` 를 사용합니다.
- 흰색 손은 그린 구간 위에서 2.01:1 입니다. 이는 마크 내부 구조이므로 수정하지 않되, **마크를 더 줄여서 손 모양이 뭉개지는 상황을 만들지 않습니다**(§4.1의 최소 크기가 이 이유로 존재합니다).

### 4.3 실사 푸티지 위

푸티지의 밝기는 프레임마다 바뀌므로 정적인 대비 계산이 성립하지 않습니다. 따라서 **푸티지 위에 마크를 올릴 때는 반드시 스크림 플레이트를 사용합니다.**

| 스크림 | 값 | 사용 |
| --- | --- | --- |
| Dark | `#0B1218` @ 72% | 밝거나 대비가 심한 푸티지 |
| Light | `#FFFFFF` @ 86% | 어둡고 균일한 푸티지 |

`badges/` 의 모든 자산에는 이 스크림이 이미 적용되어 있습니다. 직접 만들 경우 위 값을 그대로 사용합니다.

---

## 5. 금지 사항

`GUIDELINES.md` 의 원칙에 더해, 미디어 제작에서 다음을 금지합니다.

- 마크의 **회전 · 기울이기 · 좌우 반전 · 비균일 스케일**
- 손 모양과 배경 원의 **분리 이동**, 파츠 단위 애니메이션, 스쿼시/스트레치
- 마크에 **드롭섀도 · 글로우 · 베벨 · 아웃라인 추가**(단, `GUIDELINES.md` 가 허용한 흰 배경용 아웃라인 제외)
- 마크 위에 **자막 · 스티커 · 이모지 겹치기**, 또는 마크를 자막 배경판으로 사용
- 워터마크 불투명도를 **60% 미만**으로 낮춰 식별 불가능하게 만드는 것
- 승인 없이 **그라디언트 색상 교체**(§6의 절차를 따르세요). `watermark_mono_light_*` 같은 단색 대체본은 **기술적 제약이 있을 때만** 사용하며, 정기 사용 전 스태프 확인을 받습니다.
- **PG-13 기준을 벗어나는 콘텐츠**, 특정 개인·집단을 비방하는 맥락에서의 사용

---

## 6. 원본 저장소로의 역기여 (PR) 절차

미디어 팀이 만든 자산 중 **커뮤니티 전체에 일반적으로 유용한 것**은 upstream `HelpingHandsVR/identity` 에 역기여합니다.

### 6.1 무엇을 올리고, 무엇을 남기는가

| upstream에 PR | 이 포크에 유지 (`media-team/`) |
| --- | --- |
| 새로운 벡터 소스, 범용 로고 변형 | 캠페인·에피소드 전용 컴프 |
| 재현 가능한 생성 스크립트 | 특정 방송 레이아웃에 맞춘 일회성 자산 |
| 오탈자·수치 오류 등 문서 수정 | 팀 내부 워크플로 메모 |
| 범용 규격(예: 워터마크 여백 규정) | 팀 일정·담당자 정보 |

> `media-team/` 경로 자체는 upstream에 올리지 않습니다. 이 분리가 upstream 병합을 충돌 없이 유지하는 핵심입니다.

### 6.2 절차

```bash
# 1. upstream 원본을 등록 (최초 1회)
git remote add upstream https://github.com/HelpingHandsVR/identity.git

# 2. 기준 브랜치 확인 (2026-09 기준 v2025)
git remote show upstream | sed -n '/HEAD branch/p'

# 3. 최신 원본을 가져와 그 위에서 작업 브랜치를 만든다
git fetch upstream
git switch -c feat/<주제> upstream/v2025

# 4. 변경 후 이 포크로 푸시
git push -u origin feat/<주제>
```

푸시한 뒤 GitHub에서 `LeeSimYul/HHidentity:feat/<주제>` → `HelpingHandsVR/identity:v2025` 로 PR을 엽니다.

### 6.3 PR 전 체크리스트

- [ ] 변경이 `GUIDELINES.md` 의 색상·방향·구성 원칙을 지키는가
- [ ] 래스터만이 아니라 **벡터 소스 또는 생성 스크립트**를 함께 포함했는가
- [ ] 생성 자산이라면 `python media-team/generate.py` 처럼 **재현 명령**을 PR 본문에 적었는가
- [ ] 새 색상·서체·마크 변형을 도입한다면 **스태프 승인 근거**를 PR에 첨부했는가
- [ ] 저장소에 없던 외부 자산(폰트, 사진, 아이콘)을 포함하지 않았는가 — 포함한다면 라이선스를 명시했는가
- [ ] 커밋이 한 가지 주제로 정리되어 있는가
- [ ] `media-team/` 경로의 팀 전용 파일이 섞여 들어가지 않았는가

### 6.4 upstream 동기화

원본이 갱신되면 포크를 따라 올립니다. 이 포크의 기본 브랜치인 `v2026` 으로 병합하며, 포크에 `media-team/`
자체 커밋이 있으므로 `--ff-only` 는 더 이상 사용할 수 없습니다.

```bash
git fetch upstream
git switch v2026
git merge upstream/v2025
git push origin v2026
```

로고 소스(`logo/`)가 바뀐 동기화 이후에는 **파생 자산을 반드시 다시 생성**합니다.

```bash
pip install -r media-team/requirements.txt
python media-team/generate.py
git add media-team
git commit -m "chore: regenerate media-team assets for upstream logo update"
```

---

## 7. 자산 재생성

`media-team/overlays`, `media-team/badges`, `media-team/templates/guides` 아래의 파일은 **전부 `media-team/generate.py` 의 출력물**입니다. 손으로 고치지 말고 스크립트의 상수를 바꾼 뒤 다시 실행하세요.

```bash
pip install -r media-team/requirements.txt
python media-team/generate.py
```

규격을 바꾸려면 `generate.py` 상단의 상수(`WATERMARK_ALPHA`, `DARK_PLATE`, `MARGIN_RATIO`, `LOGO_MIN_RATIO` 등)를 수정하고, **이 문서의 해당 수치도 함께 갱신**합니다.

</details>
