
# Media Team Extensions (2026 Edition)

Derived assets for the Helping Hands media team — video, broadcast and social work.

Everything here is generated from the vector sources in [`../logo`](../logo). The upstream folders are
never modified, which keeps merges from `HelpingHandsVR/identity` conflict-free.

> Read [MEDIA_GUIDELINES.md](MEDIA_GUIDELINES.md) before using any of this.

## Layout

| Path | Contents |
| --- | --- |
| [`MEDIA_GUIDELINES.md`](MEDIA_GUIDELINES.md) | Media team guidelines — licensing and credit, spacing, minimum sizes, contrast, contributing back upstream |
| [`overlays/`](overlays) | Transparent PNG/WebP logo overlays for OBS, Premiere Pro and After Effects |
| [`templates/`](templates) | Thumbnail, poster and card news specifications with margin guides |
| [`badges/`](badges) | Lower-third and sign-language avatar identity badges |
| `generate.py` | Builds every file in the three folders above |
| `requirements.txt` | Dependencies for `generate.py` |

## Regenerating

Everything under `overlays/`, `badges/` and `templates/guides/` is **generated — do not hand-edit it.**
To change a specification, edit the constants in `generate.py`, re-run it, and update the matching
figures in `MEDIA_GUIDELINES.md`.

```bash
pip install -r media-team/requirements.txt
python media-team/generate.py
```

## Credit

```
Credit: HelpingHandsVR Identity
```

The full strings and rules are in
[MEDIA_GUIDELINES.md §1](MEDIA_GUIDELINES.md#1-license-compliance-and-credit).

---

<details>
<summary><strong>한국어 (Korean)</strong></summary>

미디어 팀이 영상·방송·소셜 콘텐츠를 만들 때 쓰는 파생 자산 모음입니다.
원본 자산(`logo/`, `logo_variants/`)과의 충돌을 피하기 위해 **모든 파생물은 이 폴더 안에만** 둡니다.

> 사용 전 반드시 [MEDIA_GUIDELINES.md](MEDIA_GUIDELINES.md) 를 읽어 주세요.

## 구성

| 경로 | 내용 |
| --- | --- |
| [`MEDIA_GUIDELINES.md`](MEDIA_GUIDELINES.md) | 미디어 팀 지침 (라이선스·여백·최소 크기·대비·역기여 절차) |
| [`overlays/`](overlays) | OBS / Premiere Pro / After Effects 용 투명 PNG·WebP 로고 오버레이 |
| [`templates/`](templates) | 썸네일 · 포스터 · 카드뉴스 규격과 여백 가이드 |
| [`badges/`](badges) | 방송 로어서드 · 수어 아바타 신원 표시용 미디어 배지 |
| `generate.py` | 위 세 폴더의 모든 파일을 만드는 스크립트 |
| `requirements.txt` | `generate.py` 의 의존성 |

## 재생성

`overlays/`, `badges/`, `templates/guides/` 아래 파일은 **전부 생성물입니다. 직접 수정하지 마세요.**
규격을 바꾸려면 `generate.py` 의 상수를 고치고 다시 실행한 뒤, `MEDIA_GUIDELINES.md` 의 수치도 함께 갱신합니다.

```bash
pip install -r media-team/requirements.txt
python media-team/generate.py
```

## 출처 표기

```
Credit: HelpingHandsVR Identity
```

전체 표기와 규칙은 [MEDIA_GUIDELINES.md §1](MEDIA_GUIDELINES.md#1-license-compliance-and-credit) 을 따릅니다.

</details>
