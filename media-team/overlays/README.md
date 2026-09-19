
# Overlays

OBS Studio · Premiere Pro · After Effects 에 바로 올릴 수 있는 **투명 배경 로고 오버레이**입니다.
Transparent logo overlays for OBS Studio, Premiere Pro and After Effects.

모든 파일은 `PNG`(편집 도구 호환성)와 `WebP`(무손실, 파일 크기 절감) 두 가지로 제공됩니다.
Every asset ships as `.png` for editor compatibility and lossless `.webp` for size.

## 파일 / Files

| 파일 | 크기 | 용도 |
| --- | --- | --- |
| `logo_{256,512,1024}` | 정사각 | 풀컬러 마크. 어둡거나 복잡한 배경용 기본값 |
| `logo_precomposed_{256,512,1024}` | 정사각 | 클립 마스크가 없는 동일 마크. **32 px 미만**의 작은 표시에 사용 |
| `logo_positive_space_{256,512,1024}` | 정사각 | 단색(포지티브 스페이스) 마크. 흰색·밝은 배경용 |
| `hands_outlined_{256,512,1024}` | 정사각 | 아웃라인이 있는 손 모양. 흰 배경에 마크를 직접 올려야 할 때 |
| `watermark_logo_{256,512}` | 정사각 | 화면 모서리 워터마크. **알파 70% 사전 적용** |
| `watermark_mono_light_{256,512}` | 정사각 | 흰색 단색 워터마크. 대비 확보가 불가능한 푸티지에서 **기술적 대체본으로만** 사용 |

## 배치 규칙 / Placement

`MEDIA_GUIDELINES.md` [§3.2](../MEDIA_GUIDELINES.md#32-화면-모서리-워터마크) 요약:

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

## 실사 푸티지 위 / Over live footage

투명 오버레이를 그대로 올리면 프레임에 따라 대비가 무너집니다.
푸티지 위 신원 표시는 스크림이 적용된 [`../badges`](../badges) 를 사용하세요.

> 생성물입니다. 직접 수정하지 말고 `python media-team/generate.py` 로 다시 만드세요.
> Generated — do not hand-edit; re-run `python media-team/generate.py`.
