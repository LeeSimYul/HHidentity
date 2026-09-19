
# Overlays

Transparent logo overlays for OBS Studio, Premiere Pro and After Effects.

Every asset ships twice: `.png` for editor compatibility, and lossless `.webp` for size.

## Files

| File | Shape | Use |
| --- | --- | --- |
| `logo_{256,512,1024}` | square | Full-color mark. The default for dark or busy backgrounds |
| `logo_precomposed_{256,512,1024}` | square | The same mark without the clip mask. Use **below 32 px** |
| `logo_positive_space_{256,512,1024}` | square | Single-color (positive space) mark, for white and light backgrounds |
| `hands_outlined_{256,512,1024}` | square | Outlined hands, for when the mark must sit directly on white |
| `watermark_logo_{256,512}` | square | Corner watermark, **alpha 70% already applied** |
| `watermark_mono_light_{256,512}` | square | White single-color watermark. A **technical substitute only**, when contrast cannot be met otherwise |

## Placement

Summarised from [`../MEDIA_GUIDELINES.md` §3.2](../MEDIA_GUIDELINES.md#32-corner-watermark):

| Resolution | Edge inset | Watermark diameter | Asset |
| --- | --- | --- | --- |
| 1280×720 | 36 px | 64 px | `watermark_logo_256` |
| 1920×1080 | 54 px | 65 px | `watermark_logo_256` |
| 2560×1440 | 72 px | 86 px | `watermark_logo_256` |
| 3840×2160 | 108 px | 130 px | `watermark_logo_512` |

- Keep **0.25× the mark's bounding box width** clear on all sides.
- Keep the watermark corner **fixed** across a series (default: top right).
- Scale **down** from a larger source; never upscale.
- No rotation, mirroring, non-uniform scaling or added shadows.

## Over live footage

A bare transparent overlay loses contrast as the footage changes. For identity over footage, use the
scrim-backed plates in [`../badges`](../badges).

> Generated — do not hand-edit; re-run `python media-team/generate.py`.

---

<details>
<summary><strong>한국어 (Korean)</strong></summary>

OBS Studio · Premiere Pro · After Effects 에 바로 올릴 수 있는 **투명 배경 로고 오버레이**입니다.
모든 파일은 `PNG`(편집 도구 호환성)와 `WebP`(무손실, 파일 크기 절감) 두 가지로 제공됩니다.

## 파일

| 파일 | 크기 | 용도 |
| --- | --- | --- |
| `logo_{256,512,1024}` | 정사각 | 풀컬러 마크. 어둡거나 복잡한 배경용 기본값 |
| `logo_precomposed_{256,512,1024}` | 정사각 | 클립 마스크가 없는 동일 마크. **32 px 미만**의 작은 표시에 사용 |
| `logo_positive_space_{256,512,1024}` | 정사각 | 단색(포지티브 스페이스) 마크. 흰색·밝은 배경용 |
| `hands_outlined_{256,512,1024}` | 정사각 | 아웃라인이 있는 손 모양. 흰 배경에 마크를 직접 올려야 할 때 |
| `watermark_logo_{256,512}` | 정사각 | 화면 모서리 워터마크. **알파 70% 사전 적용** |
| `watermark_mono_light_{256,512}` | 정사각 | 흰색 단색 워터마크. 대비 확보가 불가능한 푸티지에서 **기술적 대체본으로만** 사용 |

## 배치 규칙

[`../MEDIA_GUIDELINES.md` §3.2](../MEDIA_GUIDELINES.md#32-corner-watermark) 요약:

| 해상도 | 가장자리 여백 | 워터마크 지름 | 권장 파일 |
| --- | --- | --- | --- |
| 1280×720 | 36 px | 64 px | `watermark_logo_256` |
| 1920×1080 | 54 px | 65 px | `watermark_logo_256` |
| 2560×1440 | 72 px | 86 px | `watermark_logo_256` |
| 3840×2160 | 108 px | 130 px | `watermark_logo_512` |

- 마크 사방으로 **바운딩 박스 너비의 0.25배** 여백을 비웁니다.
- 워터마크 위치는 한 시리즈 안에서 **고정**합니다(기본: 우측 상단).
- 목표 크기보다 **큰** 소스를 줄여 쓰고, 절대 확대하지 않습니다.
- 회전·반전·비균일 스케일·그림자 추가는 금지입니다.

## 실사 푸티지 위

투명 오버레이를 그대로 올리면 프레임에 따라 대비가 무너집니다.
푸티지 위 신원 표시는 스크림이 적용된 [`../badges`](../badges) 를 사용하세요.

> 생성물입니다. 직접 수정하지 말고 `python media-team/generate.py` 로 다시 만드세요.

</details>
