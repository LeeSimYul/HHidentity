# 미디어 팀 — 드라이브 · 파일명 가이드

**🌐 🇰🇷 한국어 (현재 문서) · [🇺🇸 English Guide](./README.md)**

![Edition](https://img.shields.io/badge/edition-2026-111827?style=flat-square)
![Date](https://img.shields.io/badge/date-YYMMDD-be123c?style=flat-square)
![Versioning](https://img.shields.io/badge/version-v0.x%20%E2%86%92%20v1.0%20%E2%86%92%20v1.x-7c3aed?style=flat-square)
![Team](https://img.shields.io/badge/team-5%EC%9D%B8-b45309?style=flat-square)

> **⚡ 3초 요약** — 이 박스만 복사해도 90% 끝납니다.

```text
폴더      00_Scripts_Board · 01_Raw_Footage · 02_Official_Templates · 03_Graphic_Assets
          04_Audio_Library · 05_Project_Files · 06_Project_Exports · 07_Final_Output
          99_Master_Archive

파일명    [YYMMDD]_[Project]_[Note]_[etc.]_[Version].[ext]
          260922_CommunityDay_RoughCut_1080p_v0.2.mp4

버전      v0.1 → v0.2 …   드래프트      → 06_Project_Exports
          v1.0            승인된 최종   → 07_Final_Output
          v1.1 → v1.2 …   배포 후 수정

3대 원칙  1. 날짜는 YYMMDD. MMDDYY 금지.
          2. 01_Raw_Footage 안의 클립은 절대 리네임 금지.
          3. 프로젝트 파일은 #media-checkin 에 체크아웃하고 열기.
```

| 하고 싶은 것 | 위치 |
| --- | --- |
| 📁 파일을 어디에 둘지 | [§1 폴더](#1-폴더) |
| ✏️ 파일 이름 짓기 | [§2 파일명](#2-파일명) |
| 🔢 버전 번호 매기기 | [§3 버전](#3-버전) |
| 👥 남의 작업 안 깨뜨리기 | [§4 협업](#4-협업) |
| ✅ 출력·종료 전 점검 | [§5 체크리스트](#5-체크리스트) |

> [!NOTE]
> 브랜드 규정은 [`../GUIDELINES.md`](../GUIDELINES.md) 와 [`MEDIA_GUIDELINES.md`](MEDIA_GUIDELINES.md) 에 있습니다.
> 이 문서는 **파일**만 다룹니다 — 어디에 두고, 뭐라고 부르고, 누가 만지는지.
> 영문판과 내용이 다를 경우 [영문판](./README.md)이 기준입니다.

---

## 1. 폴더

드라이브 최상위에 9개. **열 번째를 만들지 마세요.** 숫자 접두사가 다섯 명 화면의 순서를 똑같이 유지합니다.

```text
00_Scripts_Board       대본, 촬영 리스트, 스토리보드, 자막 원문
01_Raw_Footage         카메라 / OBS / VR 원본   ← 파일명 절대 불변
02_Official_Templates  승인된 타이틀 · 로어서드 · 엔드카드 · 썸네일 템플릿
03_Graphic_Assets      로고, 오버레이, 배지, 폰트, 스틸
04_Audio_Library       음악, 효과음, 내레이션 테이크
05_Project_Files       작업 파일 — 프로젝트당 폴더 1개
06_Project_Exports     검토용 출력 — v0.x 전용
07_Final_Output        승인된 마스터 — v1.0 이상
99_Master_Archive      종료 프로젝트: 패키지 + 마스터 + 셀렉트
```

**하위 폴더는 이 두 가지 형태만:**

```text
01_Raw_Footage/260922_CommunityDay_CamA/     [YYMMDD]_[Project]_[Source]
05_Project_Files/260922_CommunityDay/        [YYMMDD]_[Project]
```

`[Source]` = `CamA` · `CamB` · `OBS` · `VR` · `Audio` · `Drone`

> [!CAUTION]
> ⚠️ **`01_Raw_Footage` 안의 클립은 절대 리네임 금지.** `C0042.MP4` 는 카메라가 써준 그대로 둡니다.
>
> - 프로젝트는 **경로**를 저장 → 리네임하면 다섯 명 전부 *"Where is the file…?"*
> - 프록시는 **파일명으로** 원본과 짝지어짐 → 한쪽만 바꾸면 프록시가 조용히 떨어져 나감
> - `.xmp` / `.THM` / `.LRV` 사이드카, 분할 기록 클립도 이름으로 짝지어짐
>
> 잃는 정보는 없습니다. 날짜 · 프로젝트 · 출처는 **폴더명**이 담당하고, 프록시는
> `…_CamA/Proxies/` 에 같은 이름으로 둡니다.

**파일은 다음 단계로 복사. 옆으로 끌어 옮기지 않습니다:**

```text
05_Project_Files → 출력 → 06_Project_Exports → 승인 → 07_Final_Output → 종료 → 99_Master_Archive
```

프로젝트가 링크한 파일을 옮기면 모두의 링크가 깨집니다. 다음 폴더로 출력하는 건 안 깨집니다.

---

## 2. 파일명

```text
260922_CommunityDay_RoughCut_1080p_v0.2.mp4
│      │             │        │     │    └ 확장자, 소문자
│      │             │        │     └───── 버전 (§3)
│      │             │        └─────────── 선택: 해상도, 카메라, 언어, 플랫폼
│      │             └──────────────────── 이 파일이 뭔지
│      └────────────────────────────────── 프로젝트 (끝까지 같은 표기)
└───────────────────────────────────────── 날짜, 연도부터
```

| 필드 | 규칙 | ✅ | ❌ |
| --- | --- | --- | --- |
| `YYMMDD` | 6자리, 연도 먼저, 만든 날 | `260922` | `092226`, `26-09-22` |
| `Project` | 한 덩어리, `PascalCase`, 영문 | `CommunityDay` | `community day`, `커뮤니티데이` |
| `Note` | 이 파일의 정체 | `MainEdit`, `Master` | `edit2`, `final` |
| `etc.` | 선택 수식어 | `1080p`, `CamA`, `KO-sub`, `-14LUFS` | `new`, `fix`, `real` |
| `Version` | `v0.2`, `v1.0` — 항상 두 자리 | `v1.0` | `v2`, `ver1`, `V1.0` |

- **`_` 는 필드 구분, `-` 는 단어 연결.** `KO-sub` 은 한 필드, `KO_sub` 은 두 필드.
- 공백·한글·`( ) [ ] { } # % & / \ * ? : " < > |` 금지 — 드라이브는 되지만 Premiere·ffmpeg 가 깨집니다.
- **프로젝트가 쓰고 있는 파일은 리네임 금지.** 다른 이름 저장이나 출력으로 처리하세요.
- 이 모든 것의 유일한 예외는 `01_Raw_Footage` (§1).

> [!WARNING]
> ⚠️ **`YYMMDD` 만 사용 — `MMDDYY` 금지.** 연도가 앞에 와야 **이름순 정렬 = 날짜순 정렬**이 됩니다.
>
> | | `YYMMDD` ✅ | `MMDDYY` ❌ |
> | --- | --- | --- |
> | 2026-09-22 | `260922` | `092226` |
> | 이름순 = 날짜순 | 예 | 아니오 |
> | 25/12/01 · 26/01/01 · 26/09/22 | `251201` `260101` `260922` | `010126` `092226` `120125` |
>
> **혼용은 둘 중 어느 쪽보다도 나쁩니다.** `090112` 는 2009-01-12 인지 2012-09-01 인지 아무도 모릅니다.
> 예전 `MMDDYY` 이름을 발견하면 손대는 그 자리에서 고치세요 — 프로젝트가 참조 중인 파일만 제외.

<details>
<summary>🔧 예전 <code>MMDDYY</code> 이름 변환 (미리보기)</summary>

`sh` 가 아니라 **`bash`** 로 실행하세요. 출력만 하고 아무것도 바꾸지 않습니다. 이미 `YYMMDD` 인 이름은 건너뜁니다.

```bash
for f in [0-9][0-9][0-9][0-9][0-9][0-9]_*; do
  d=${f%%_*}; rest=${f#*_}; mm=${d:0:2}; dd=${d:2:2}; yy=${d:4:2}
  if (( 10#$yy >= 24 && 10#$yy <= 30 && 10#$mm >= 1 && 10#$mm <= 12 && 10#$dd >= 1 && 10#$dd <= 31 )); then
    echo "mv -- '$f' '$yy$mm${dd}_$rest'"
  else
    echo "# 이미 YYMMDD 이거나 불확실함, 그대로 둠: $f"
  fi
done
```

출력된 줄을 모두 확인하고, 참조 중인 프로젝트가 없는지 본 뒤 `| bash` 를 붙여 다시 실행합니다.

</details>

### 예시

| 어디에 | 파일 |
| --- | --- |
| 🎬 Premiere 편집 | `260922_CommunityDay_MainEdit_v0.3.prproj` |
| ✨ After Effects | `260922_CommunityDay_LowerThird_1440x240_v0.2.aep` |
| 🧊 Blender | `260922_CommunityDay_SignAvatar_CamA_v0.4.blend` |
| 📹 검토용 가편집 | `260922_CommunityDay_RoughCut_1080p_v0.1.mp4` |
| 📹 피드백 반영본 | `260923_CommunityDay_RoughCut_1080p_v0.2.mp4` |
| 🏁 승인된 마스터 | `260925_CommunityDay_Master_YT-2160p_v1.0.mp4` |
| 🏁 세로형 컷다운 | `260925_CommunityDay_Master_Shorts-1080x1920_v1.0.mp4` |
| 🏁 배포 후 오탈자 수정 | `260927_CommunityDay_Master_YT-2160p_v1.1.mp4` |
| 🎨 그래픽 자산 | `260901_Brand_LowerThird_Overlay_1440x240_v1.0.png` |
| 🔊 라이선스 음원 | `260901_Library_BGM_Uplifting-Loop_-14LUFS_v1.0.wav` |
| 🎙️ 내레이션 테이크 | `260922_CommunityDay_VO_Narration-KO_v0.2.wav` |

> [!TIP]
> 💡 외부 자산이면 바로 옆에 `LICENSE.md` — 출처 · 라이선스 · 요구 표기. 라이선스 메모 없으면 배포 불가.

---

## 3. 버전

| 단계 | 번호 | 폴더 |
| --- | --- | --- |
| 🟡 드래프트 / 피드백 | `v0.1`, `v0.2`, `v0.3` … | `06_Project_Exports` |
| 🟢 승인된 배포본 | **`v1.0`** | `07_Final_Output` |
| 🔵 배포 후 수정 | `v1.1`, `v1.2` … | `07_Final_Output` |
| 🟣 같은 제목의 새 편집 | `v2.0` | `07_Final_Output` |

- **덮어쓰지 말고 올리기.** `v0.3` 이 나와도 `v0.2` 는 남깁니다. 피드백 대화가 실재하는 파일을 가리키도록.
- **`07_Final_Output` 에 `v1.0` 미만 없음.** 미승인이면 `v0.x`, 자리는 `06_Project_Exports`.
- **`v1.0` 은 고정.** 배포 후 변경은 한 프레임이라도 `v1.1`.
- **작업 시작 전에 다음 버전으로 다른 이름 저장** — 그래야 `…_v0.3.prproj` 가 `…_v0.3.mp4` 를 만든 편집본으로 계속 열립니다.
- 보관 기준: 모든 `v1.x` + 마지막 `v0.x` 두 개 + 픽처 록본. 나머지는 정리 때 삭제.

> [!CAUTION]
> 🚫 **금지 파일명 — 발견 즉시 반송.** 다시 출력하는 게 다섯 명이 "어느 게 최신이지?" 로 쓰는 시간보다 쌉니다.
>
> | ❌ 금지 | ✅ 대체 |
> | --- | --- |
> | `최종.mp4`, `final.mp4` | `260925_CommunityDay_Master_YT-2160p_v1.0.mp4` |
> | `진짜최종.mp4`, `찐최종.mp4` | `..._v1.1.mp4` |
> | `최종_수정.mp4`, `최종수정2.mp4` | `..._v1.2.mp4` |
> | `video_v2.mp4`, `edit_ver3.prproj` | `..._v0.2.mp4` |
> | `홍길동_수정본.mp4` | `..._v0.3.mp4` |
> | `Untitled.prproj`, `Sequence 01.mp4` | 첫 저장에서 이름 지정 |
> | `Copy of ….mp4`, `..._v0.3 (1).mp4` | 사본 삭제 후 버전 올리기 |
> | `..._v0.3_fixed.prproj` | `..._v0.4.prproj` |
>
> **이름만 보고 최신 파일을 못 고르면, 그 명명은 실패입니다.**

---

## 4. 협업

### 담당

읽기는 전원, 쓰기는 담당자 — 아니면 체크아웃.

| 역할 | 쓰기 |
| --- | --- |
| 🎛️ 리드 엔지니어 | `02_Official_Templates`, `07_Final_Output`, `99_Master_Archive` |
| ✂️ 편집자 A / B | 배정된 `05_Project_Files` 프로젝트, `06_Project_Exports` |
| ✨ 모션 / 그래픽 | `03_Graphic_Assets`, 템플릿 원본 |
| 🔊 오디오 | `04_Audio_Library`, 프로젝트 폴더의 내레이션·믹스 |

`07_Final_Output` 에 쓰는 사람은 리드뿐. 그래야 `v1.0` 이 의미를 유지합니다.

### 넘기기 전에 패키징

프로젝트는 **미디어가 아니라 경로**를 저장합니다. 내 바탕화면 경로는 나머지 네 대에선 빈 껍데기입니다.

> [!IMPORTANT]
> 📦 **임포트는 공용 드라이브에서만** (`01_Raw_Footage`, `03_Graphic_Assets`, `04_Audio_Library`).
> `~/Desktop`(바탕화면), `~/Downloads`(다운로드), 휴대폰 전송 폴더, SD 카드에서 직접 임포트 금지.

| 프로그램 | 이렇게 |
| --- | --- |
| Premiere Pro | `파일 ▸ 프로젝트 관리자 ▸ 파일 수집 후 복사` — *사용하지 않는 클립 제외* 체크 |
| After Effects | `파일 ▸ 종속성 ▸ 파일 수집…` — 생성되는 `.txt` 보고서도 함께 |
| Blender | `외부 데이터 ▸ 상대 경로로 만들기` → 아카이브 전 `리소스 팩` |
| DaVinci Resolve | `파일 ▸ 미디어 관리`(복사) 또는 `.drp` 내보내기 |

- 프로젝트가 링크한 미디어는 이동·리네임 금지 — 복사 후 의도적으로 재연결.
- 프로젝트 폴더마다 `README.txt` 한 줄: 결과물 · 현재 파일 · 미디어 위치.
- **종료 시 패키징은 필수**, 한 번 열어서 재연결되는지 확인까지.
- 공동 작업은 프록시로 — 재연결이 작은 파일만 건드립니다.

### 🔒 Check-in / Check-out — 디스코드 `#media-checkin`

> [!WARNING]
> ⚠️ **드라이브에는 파일 잠금이 없습니다.** 두 명이 같은 `.prproj` 를 저장하면 충돌 사본이 조용히 생기고
> 누군가의 오후가 날아갑니다. 그래서 사회적으로 잠급니다: **열기 전 체크아웃, 닫을 때 체크인.**

```text
🔒 CHECK-OUT  260922_CommunityDay_MainEdit_v0.3.prproj
              @editor-a · 약 2시간 · ETA 18:00 KST

🔓 CHECK-IN   260922_CommunityDay_MainEdit_v0.4.prproj
              @editor-a · 색보정 완료, 다음: 자막
              → 출력: 260923_CommunityDay_RoughCut_1080p_v0.2.mp4
```

| 규칙 | |
| --- | --- |
| 한 파일에 한 명 | 체크아웃 중이면 읽기 전용으로 열거나 대기. "금방 고치기" 예외 없음 |
| ETA 필수 | ETA 없으면 잠금도 없음 — 나머지가 일정을 짜야 합니다 |
| 최대 24시간 | 그 이상이면 체크인하거나 새 ETA로 다시 공지 |
| 24시간 무응답 | 리드가 `⚠️ FORCE-RELEASE` 로 파일과 점유자를 명시해 강제 해제 |
| 출력 중 동기화 일시 중지 | 렌더 → 동기화 재개 → 체크인 |
| 체크인에 새 버전 명시 | 그 번호가 나머지에게는 기준입니다 |
| 공용 자산도 동일 | `02_Official_Templates`, `03_Graphic_Assets` |
| 프로젝트당 스레드 1개 | 이력을 한곳에 |

> [!TIP]
> 💡 대본은 예외 — `00_Scripts_Board` 는 **구글 문서**(진짜 다중 편집)로 두고 `.docx` 사본 대신 링크를 공유하세요.

### 캐시 · 용량

> [!WARNING]
> ⚠️ **미디어 캐시는 공용 드라이브에 두지 않습니다.** 컴퓨터별 일회성 데이터인데 용량이 거대해서,
> 동기화하면 할당량만 태우고 충돌 사본이 쌓입니다.

| 프로그램 | 이 경로로 |
| --- | --- |
| Premiere Pro | 로컬 SSD (`D:\PrCache`, `~/Library/Caches/PrCache`) + **30일** 자동 삭제 |
| After Effects | 로컬 디스크 캐시 20–60 GB, 매월 비우기 |
| Blender | 로컬 임시 경로 |
| Drive for desktop | 드라이브 **스트리밍**, 진행 중인 프로젝트만 *오프라인 사용 가능* |

**매월, 리드 주관:** 30일 넘은 캐시·자동 저장 정리 · `06_Project_Exports` 를 마지막 `v0.x` 두 개 + 픽처 록본만 남기고 정리 · 저장 용량 **80%** 넘으면 아카이브 · 60일 방치 프로젝트 점검.

- 드래프트는 H.264 `.mp4`. ProRes / DNxHR 은 `07_Final_Output` 과 `99_Master_Archive` 에만.
- 카메라 원본은 콜드 스토리지: 드라이브엔 프록시와 셀렉트, 카드 전체는 아카이브 드라이브에 (사본 2개, 1개는 외부).
- 같은 자산 두 벌 금지 — 라이브러리 폴더를 링크하세요.
- 드라이브 충돌 사본(`… (1)`, `Copy of …`)은 생긴 날 삭제.

---

## 5. 체크리스트

**🚀 시작할 때**

- [ ] 프로젝트 토큰 확정 — 끝까지 한 가지 표기
- [ ] 출처별 `01_Raw_Footage/[YYMMDD]_[Project]_[Source]/`, 클립명은 그대로
- [ ] `05_Project_Files/[YYMMDD]_[Project]/` + `README.txt`
- [ ] 임포트 **전에** 미디어를 드라이브로, 프록시 생성
- [ ] 캐시는 로컬 디스크 · 디스코드 스레드 개설

**📤 출력할 때마다**

- [ ] 해당 파일이 나에게 체크아웃되어 있음
- [ ] 출력할 버전으로 프로젝트 저장 완료
- [ ] 이름이 `[YYMMDD]_[Project]_[Note]_[etc.]_[Version].[ext]` 형식
- [ ] `v0.x` → `06_Project_Exports` · `v1.x` → `07_Final_Output`
- [ ] 출처 표기 포함 ([`MEDIA_GUIDELINES.md` §1](MEDIA_GUIDELINES.md#1-license-compliance-and-credit))
- [ ] 금지 파일명 없음, 미디어 유실 경고 없음

**📦 종료할 때**

- [ ] `v1.0`(및 `v1.x`)이 `07_Final_Output` 에
- [ ] 패키징 완료, 한 번 열어 재연결 확인
- [ ] `99_Master_Archive/<연도>/<프로젝트>/` = 패키지 + 마스터 + 셀렉트 + 라이선스 메모
- [ ] 출력물 정리 · 캐시 정리 · 마지막 체크인으로 스레드 종료

---

## 6. 이 폴더의 저장소 자산

이 폴더에는 미디어 팀이 [`../logo`](../logo) 의 벡터 원본에서 파생시킨 브랜드 자산도 함께 있습니다.
원본 폴더는 수정하지 않으며, 그 덕분에 `HelpingHandsVR/identity` 동기화가 충돌 없이 이루어집니다.

| 경로 | 내용 |
| --- | --- |
| [`MEDIA_GUIDELINES.md`](MEDIA_GUIDELINES.md) | 미디어 팀 지침 — 라이선스·출처 표기, 여백, 최소 크기·대비, 역기여 절차 |
| [`README.md`](README.md) | 이 문서의 영문판 (Primary) |
| [`overlays/`](overlays) | OBS / Premiere Pro / After Effects 용 투명 PNG·WebP 로고 오버레이 |
| [`templates/`](templates) | 썸네일 · 포스터 · 카드뉴스 규격과 여백 가이드 |
| [`badges/`](badges) | 방송 로어서드 · 수어 아바타 신원 표시용 미디어 배지 |
| `generate.py` | 위 세 폴더의 모든 파일을 만드는 스크립트 |
| `requirements.txt` | `generate.py` 의 의존성 |

`overlays/`, `badges/`, `templates/guides/` 아래 파일은 **전부 생성물입니다. 직접 수정하지 마세요.**
규격을 바꾸려면 `generate.py` 의 상수를 고치고 다시 실행한 뒤, `MEDIA_GUIDELINES.md` 의 수치도 함께
갱신합니다.

```bash
pip install -r media-team/requirements.txt
python media-team/generate.py
```

마크가 보이는 모든 결과물에는 출처를 표기합니다.

```text
Credit: HelpingHandsVR Identity
```

전체 표기 문구와 규칙은
[`MEDIA_GUIDELINES.md` §1](MEDIA_GUIDELINES.md#1-license-compliance-and-credit) 을 따릅니다.
