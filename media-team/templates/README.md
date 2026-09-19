
# Templates

영상 썸네일 · 포스터 · 카드뉴스의 **규격과 여백 가이드**입니다.
Size specs and margin guides for video thumbnails, posters and card news.

이 폴더는 편집 도구의 프로젝트 파일(`.psd`, `.aep`, `.prproj`) 대신 **도구에 상관없이 쓸 수 있는
투명 가이드 PNG** 를 제공합니다. 작업 캔버스 맨 위에 가이드를 올려 여백을 맞추고, 내보내기 전에
가이드 레이어를 끄면 됩니다.

Rather than tool-specific project files, this folder ships transparent guide PNGs.
Drop one on the top layer, align to it, and hide the layer before export.

## 규격 / Specifications

| 용도 | 크기 (px) | 비율 | 가이드 |
| --- | --- | --- | --- |
| 영상 썸네일 (표준) | 1280 × 720 | 16:9 | `guides/thumbnail_1280x720_guide.png` |
| 영상 프레임 · 고해상도 썸네일 | 1920 × 1080 | 16:9 | `guides/thumbnail_1920x1080_guide.png` |
| 포스터 A3 세로 (150 dpi) | 1754 × 2480 | 297 × 420 mm | `guides/poster_a3_1754x2480_guide.png` |
| 카드뉴스 정사각 | 1080 × 1080 | 1:1 | `guides/cardnews_1080x1080_guide.png` |
| 카드뉴스 세로 | 1080 × 1350 | 4:5 | `guides/cardnews_1080x1350_guide.png` |
| 스토리 · 쇼츠 | 1080 × 1920 | 9:16 | `guides/story_1080x1920_guide.png` |

## 여백 / Margins

여백은 **짧은 변을 기준**으로 계산합니다. 바깥 여백 6%, 그 안쪽으로 한 번 더 들어간 곳이 본문 안전 영역,
브랜드 블록의 최소 크기는 짧은 변의 8% 입니다.

| 규격 | 바깥 여백 | 본문 안전 영역 | 로고 최소 지름 | 로고 주변 여백 |
| --- | --- | --- | --- | --- |
| 1280 × 720 | 43 px | 86 px | 58 px | 14 px |
| 1920 × 1080 | 65 px | 130 px | 86 px | 22 px |
| 1754 × 2480 | 105 px | 210 px | 140 px | 35 px |
| 1080 × 1080 | 65 px | 130 px | 86 px | 22 px |
| 1080 × 1350 | 65 px | 130 px | 86 px | 22 px |
| 1080 × 1920 | 65 px | 130 px | 86 px | 22 px |

## 가이드 읽는 법 / Reading a guide

| 표시 | 의미 |
| --- | --- |
| 분홍 파선 (바깥) | 트림 여백 — 어떤 요소도 이 밖으로 나가지 않습니다 |
| 파랑 파선 (안쪽) | 본문 안전 영역 — 제목·본문 텍스트는 이 안에 둡니다 |
| 초록 사각형 (우하단) | 브랜드 블록의 **최소** 크기와 그 주변 여백 |
| 좌상단 캡션 | 규격명과 위 수치 |

- 브랜드 블록의 기본 위치는 **우측 하단**입니다. 레이아웃상 필요하면 옮길 수 있지만, 한 시리즈
  안에서는 위치를 고정합니다.
- 초록 사각형은 **최소값**입니다. 더 크게 쓰는 것은 괜찮지만, 그보다 작게는 쓰지 않습니다.
- 포스터를 인쇄 입고할 때는 가이드를 참고용으로만 쓰고, 마크는 `logo/logo.svg` 벡터로 배치합니다.
- 배경이 사진이면 마크를 그대로 올리지 말고 [`../badges`](../badges) 의 스크림 배지를 쓰거나
  `logo_positive_space` 를 사용합니다 ([`../MEDIA_GUIDELINES.md`](../MEDIA_GUIDELINES.md) §4.2 · §4.3).

## 규격 추가 / Adding a format

`generate.py` 의 `TEMPLATE_GUIDES` 에 항목을 추가하고 다시 실행하면 가이드가 생성됩니다.
이 문서의 표도 함께 갱신해 주세요.

> `guides/` 의 파일은 생성물입니다. 직접 수정하지 말고 `python media-team/generate.py` 로 다시 만드세요.
> Generated — do not hand-edit; re-run `python media-team/generate.py`.
