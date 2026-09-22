# Media Team — Drive & Naming Guide

**🌐 [🇰🇷 한국어 안내서](./README.ko.md) · 🇺🇸 English (this document)**

![Edition](https://img.shields.io/badge/edition-2026-111827?style=flat-square)
![Date](https://img.shields.io/badge/date-YYMMDD-be123c?style=flat-square)
![Versioning](https://img.shields.io/badge/version-v0.x%20%E2%86%92%20v1.0%20%E2%86%92%20v1.x-7c3aed?style=flat-square)
![Team](https://img.shields.io/badge/team-5%20members-b45309?style=flat-square)

> **⚡ TL;DR** — copy this box, you're 90 % done.

```text
FOLDERS   00_Scripts_Board · 01_Raw_Footage · 02_Official_Templates · 03_Graphic_Assets
          04_Audio_Library · 05_Project_Files · 06_Project_Exports · 07_Final_Output
          99_Master_Archive

NAME      [YYMMDD]_[Project]_[Note]_[etc.]_[Version].[ext]
          260922_CommunityDay_RoughCut_1080p_v0.2.mp4

VERSION   v0.1 → v0.2 …   drafts        → 06_Project_Exports
          v1.0            approved      → 07_Final_Output
          v1.1 → v1.2 …   fixes after release

3 RULES   1. Dates are YYMMDD. Never MMDDYY.
          2. Never rename a clip inside 01_Raw_Footage.
          3. Check out in #media-checkin before you open a project file.
```

| I need to… | Go to |
| --- | --- |
| 📁 put a file in the right place | [§1 Folders](#1-folders) |
| ✏️ name a file | [§2 File names](#2-file-names) |
| 🔢 number a version | [§3 Versions](#3-versions) |
| 👥 not break someone else's edit | [§4 Teamwork](#4-teamwork) |
| ✅ ship or close a project | [§5 Checklists](#5-checklists) |

> [!NOTE]
> Brand rules live in [`../GUIDELINES.md`](../GUIDELINES.md) and [`MEDIA_GUIDELINES.md`](MEDIA_GUIDELINES.md).
> This guide is about **files** — where they go, what they're called, who may touch them.

---

## 1. Folders

Nine folders at the drive root. **Don't add a tenth.** The numbers keep the order identical on all five machines.

```text
00_Scripts_Board       scripts, shot lists, storyboards, subtitle text
01_Raw_Footage         camera / OBS / VR originals   ← filenames never change
02_Official_Templates  approved title, lower-third, end-card, thumbnail templates
03_Graphic_Assets      logos, overlays, badges, fonts, stills
04_Audio_Library       music, SFX, VO takes
05_Project_Files       working files — one folder per project
06_Project_Exports     review exports — v0.x only
07_Final_Output        approved masters — v1.0 and up
99_Master_Archive      closed projects: package + master + selects
```

**Two subfolder shapes, nothing else:**

```text
01_Raw_Footage/260922_CommunityDay_CamA/     [YYMMDD]_[Project]_[Source]
05_Project_Files/260922_CommunityDay/        [YYMMDD]_[Project]
```

`[Source]` = `CamA` · `CamB` · `OBS` · `VR` · `Audio` · `Drone`

> [!CAUTION]
> ⚠️ **Never rename a clip in `01_Raw_Footage`.** Leave `C0042.MP4` exactly as the camera wrote it.
>
> - The project stores the **path** → rename = *"Where is the file…?"* for all five of us
> - Proxies pair to originals **by filename** → rename one side and the proxy silently detaches
> - `.xmp` / `.THM` / `.LRV` sidecars and spanned clips match by basename too
>
> Nothing is lost: the date, project and source live on the **folder**. Proxies go in
> `…_CamA/Proxies/` with the same basename.

**Files move forward by copying — never by dragging sideways:**

```text
05_Project_Files → export → 06_Project_Exports → approved → 07_Final_Output → closed → 99_Master_Archive
```

Moving a file a project links to breaks it for everyone. Exporting to the next folder doesn't.

---

## 2. File names

```text
260922_CommunityDay_RoughCut_1080p_v0.2.mp4
│      │             │        │     │    └ lowercase extension
│      │             │        │     └───── version (§3)
│      │             │        └─────────── optional: resolution, camera, language, platform
│      │             └──────────────────── what it is
│      └────────────────────────────────── project (same spelling all project long)
└───────────────────────────────────────── date, year first
```

| Field | Rule | ✅ | ❌ |
| --- | --- | --- | --- |
| `YYMMDD` | 6 digits, year first, the day you made it | `260922` | `092226`, `26-09-22` |
| `Project` | one token, `PascalCase`, ASCII | `CommunityDay` | `community day`, `커뮤니티데이` |
| `Note` | what the file is | `MainEdit`, `Master` | `edit2`, `final` |
| `etc.` | optional qualifiers | `1080p`, `CamA`, `KO-sub`, `-14LUFS` | `new`, `fix`, `real` |
| `Version` | `v0.2`, `v1.0` — always two digits | `v1.0` | `v2`, `ver1`, `V1.0` |

- **`_` splits fields, `-` joins words inside one.** `KO-sub` is one field, `KO_sub` is two.
- No spaces, no Korean, none of `( ) [ ] { } # % & / \ * ? : " < > |` — Drive allows them, Premiere and ffmpeg don't.
- **Never rename a file a project is using.** Save-as or export instead.
- Only exception to all of this: `01_Raw_Footage` (§1).

> [!WARNING]
> ⚠️ **`YYMMDD` only — never `MMDDYY`.** Year first is the one order where **sorting by name = sorting by date**.
>
> | | `YYMMDD` ✅ | `MMDDYY` ❌ |
> | --- | --- | --- |
> | 2026-09-22 | `260922` | `092226` |
> | Name-sort = date-sort | yes | no |
> | Dec 1 '25 · Jan 1 '26 · Sep 22 '26 | `251201` `260101` `260922` | `010126` `092226` `120125` |
>
> **Mixing is worse than either one.** `090112` could be 2009-01-12 or 2012-09-01 — nobody can tell.
> Found a legacy `MMDDYY` name? Fix it the moment you touch it, unless a project links to it.

<details>
<summary>🔧 Converting legacy <code>MMDDYY</code> names (dry run)</summary>

Run with **bash, not sh**. It only prints; nothing changes. Prefixes that already read as `YYMMDD` are left alone.

```bash
for f in [0-9][0-9][0-9][0-9][0-9][0-9]_*; do
  d=${f%%_*}; rest=${f#*_}; mm=${d:0:2}; dd=${d:2:2}; yy=${d:4:2}
  if (( 10#$yy >= 24 && 10#$yy <= 30 && 10#$mm >= 1 && 10#$mm <= 12 && 10#$dd >= 1 && 10#$dd <= 31 )); then
    echo "mv -- '$f' '$yy$mm${dd}_$rest'"
  else
    echo "# already YYMMDD or unclear, left alone: $f"
  fi
done
```

Read every line, check no project links to those files, then re-run piped to `bash`.

</details>

### Examples

| Where | File |
| --- | --- |
| 🎬 Premiere edit | `260922_CommunityDay_MainEdit_v0.3.prproj` |
| ✨ After Effects | `260922_CommunityDay_LowerThird_1440x240_v0.2.aep` |
| 🧊 Blender | `260922_CommunityDay_SignAvatar_CamA_v0.4.blend` |
| 📹 Rough cut for review | `260922_CommunityDay_RoughCut_1080p_v0.1.mp4` |
| 📹 After feedback | `260923_CommunityDay_RoughCut_1080p_v0.2.mp4` |
| 🏁 Approved master | `260925_CommunityDay_Master_YT-2160p_v1.0.mp4` |
| 🏁 Vertical cutdown | `260925_CommunityDay_Master_Shorts-1080x1920_v1.0.mp4` |
| 🏁 Typo fix after release | `260927_CommunityDay_Master_YT-2160p_v1.1.mp4` |
| 🎨 Graphic asset | `260901_Brand_LowerThird_Overlay_1440x240_v1.0.png` |
| 🔊 Licensed music | `260901_Library_BGM_Uplifting-Loop_-14LUFS_v1.0.wav` |
| 🎙️ VO take | `260922_CommunityDay_VO_Narration-KO_v0.2.wav` |

> [!TIP]
> 💡 Third-party asset? Put a `LICENSE.md` right next to it — source, licence, required credit.
> No licence note, no shipping.

---

## 3. Versions

| Stage | Numbers | Folder |
| --- | --- | --- |
| 🟡 Draft / feedback | `v0.1`, `v0.2`, `v0.3` … | `06_Project_Exports` |
| 🟢 Approved release | **`v1.0`** | `07_Final_Output` |
| 🔵 Fix after release | `v1.1`, `v1.2` … | `07_Final_Output` |
| 🟣 New edit of the same title | `v2.0` | `07_Final_Output` |

- **Bump, never overwrite.** `v0.2` stays after `v0.3` exists, so feedback still points at something real.
- **Nothing below `v1.0` in `07_Final_Output`.** Not approved = `v0.x` = `06_Project_Exports`.
- **`v1.0` is frozen.** Any change after publishing is `v1.1`, even one frame.
- **Save-as to the next version _before_ you start changing things** — so `…_v0.3.prproj` still opens the cut that made `…_v0.3.mp4`.
- Keep all `v1.x`, the last two `v0.x`, and the picture-locked `v0.x`. Delete the rest at cleanup.

> [!CAUTION]
> 🚫 **Banned filenames — rejected on sight.** Re-exporting is cheaper than five people guessing which file is current.
>
> | ❌ Never | ✅ Instead |
> | --- | --- |
> | `final.mp4`, `최종.mp4` ("final") | `260925_CommunityDay_Master_YT-2160p_v1.0.mp4` |
> | `진짜최종.mp4` ("really final"), `final_final.mp4` | `..._v1.1.mp4` |
> | `최종_수정.mp4` ("final, revised"), `final_fix2.mp4` | `..._v1.2.mp4` |
> | `video_v2.mp4`, `edit_ver3.prproj` | `..._v0.2.mp4` |
> | `홍길동_수정본.mp4` ("&lt;person&gt;_revision") | `..._v0.3.mp4` |
> | `Untitled.prproj`, `Sequence 01.mp4` | rename on first save |
> | `Copy of ….mp4`, `..._v0.3 (1).mp4` | delete the copy, bump the version |
> | `..._v0.3_fixed.prproj` | `..._v0.4.prproj` |
>
> **If you can't tell which file is newest from the names alone, the naming failed.**

---

## 4. Teamwork

### Who owns what

Everyone reads everything. Writing is by owner — or by check-out.

| Role | Writes |
| --- | --- |
| 🎛️ Lead engineer | `02_Official_Templates`, `07_Final_Output`, `99_Master_Archive` |
| ✂️ Editor A / B | their projects in `05_Project_Files`, `06_Project_Exports` |
| ✨ Motion / graphics | `03_Graphic_Assets`, template sources |
| 🔊 Audio | `04_Audio_Library`, VO and mix files in the project folder |

Only the lead writes `07_Final_Output`. That's what keeps `v1.0` meaningful.

### Package before you hand off

A project stores **paths, not media**. A path on your desktop is nothing on the other four machines.

> [!IMPORTANT]
> 📦 **Import only from the shared drive** (`01_Raw_Footage`, `03_Graphic_Assets`, `04_Audio_Library`).
> Never from `~/Desktop`, `~/Downloads`, a phone transfer folder or an SD card.

| App | Do this |
| --- | --- |
| Premiere Pro | `File ▸ Project Manager ▸ Collect Files and Copy` — tick *Exclude Unused Clips* |
| After Effects | `File ▸ Dependencies ▸ Collect Files…` — ship the `.txt` report too |
| Blender | `External Data ▸ Make Paths Relative`, then `Pack Resources` before archiving |
| DaVinci Resolve | `File ▸ Media Management` (copy) or export a `.drp` |

- Never move or rename media a project links to — copy forward and relink on purpose.
- One `README.txt` per project folder: deliverable, current file, where the media lives.
- **Always package at project close**, then reopen it once to prove it relinks.
- Edit from proxies so a relink touches small files.

### 🔒 Check-in / check-out — Discord `#media-checkin`

> [!WARNING]
> ⚠️ **Drive has no file locking.** Two people saving the same `.prproj` = a silent conflict copy and
> somebody's afternoon gone. So we lock socially: **check out before you open, check in when you close.**

```text
🔒 CHECK-OUT  260922_CommunityDay_MainEdit_v0.3.prproj
              @editor-a · ~2h · ETA 18:00 KST

🔓 CHECK-IN   260922_CommunityDay_MainEdit_v0.4.prproj
              @editor-a · colour pass done, next: captions
              → export: 260923_CommunityDay_RoughCut_1080p_v0.2.mp4
```

| Rule | |
| --- | --- |
| One writer per file | Checked out? Open read-only or wait. No "quick fix" exceptions |
| Always give an ETA | No ETA, no lock — the others plan around you |
| Max hold 24 h | Then check in, or re-post the lock with a new ETA |
| Stale 24 h+ | Lead posts `⚠️ FORCE-RELEASE` with the file and the holder |
| Pause sync while exporting | Render → resume sync → check in |
| Name the new version in the check-in | That number is the truth for everyone else |
| Shared assets count too | `02_Official_Templates`, `03_Graphic_Assets` — same protocol |
| One thread per project | Whole history in one place |

> [!TIP]
> 💡 Scripts are the exception — keep `00_Scripts_Board` in **Google Docs** (really multi-user) and share links, not `.docx` copies.

### Cache & capacity

> [!WARNING]
> ⚠️ **Media cache never goes on the shared drive.** It's per-machine, disposable and huge — syncing it burns quota and spawns conflict copies.

| App | Point it at |
| --- | --- |
| Premiere Pro | local SSD (`D:\PrCache`, `~/Library/Caches/PrCache`) + auto-delete after **30 days** |
| After Effects | local disk cache, 20–60 GB, empty it monthly |
| Blender | local temp path |
| Drive for desktop | **stream** the drive; only your active project *Available offline* |

**Monthly, led by the lead:** clear caches and auto-saves over 30 days · prune `06_Project_Exports` to the last two `v0.x` + the picture lock · archive pass if storage is over **80 %** · flag projects idle 60 days.

- Drafts are H.264 `.mp4`. ProRes / DNxHR only in `07_Final_Output` and `99_Master_Archive`.
- Camera originals are cold storage: proxies + selects on the drive, full cards on the archive drive (2 copies, 1 off-site).
- Never keep two copies of an asset — link to the library folder instead.
- Delete Drive conflict copies (`… (1)`, `Copy of …`) the day they appear.

---

## 5. Checklists

**🚀 Starting**

- [ ] Project token agreed — one spelling, whole project
- [ ] `01_Raw_Footage/[YYMMDD]_[Project]_[Source]/` per source, clip names untouched
- [ ] `05_Project_Files/[YYMMDD]_[Project]/` + `README.txt`
- [ ] Media on the drive **before** importing; proxies made
- [ ] Cache on a local disk · Discord thread open

**📤 Before every export**

- [ ] File checked out to you
- [ ] Project saved as the version you're exporting
- [ ] Name matches `[YYMMDD]_[Project]_[Note]_[etc.]_[Version].[ext]`
- [ ] `v0.x` → `06_Project_Exports` · `v1.x` → `07_Final_Output`
- [ ] Credit included ([`MEDIA_GUIDELINES.md` §1](MEDIA_GUIDELINES.md#1-license-compliance-and-credit))
- [ ] No banned name, no missing-media warning

**📦 Closing**

- [ ] `v1.0` (and any `v1.x`) in `07_Final_Output`
- [ ] Packaged, reopened once, relinks cleanly
- [ ] `99_Master_Archive/<Year>/<Project>/` = package + masters + selects + licence notes
- [ ] Exports pruned · caches cleared · thread closed with a final check-in

---

## 6. Repository assets in this folder

This folder also holds the brand assets the media team derives from the vector sources in
[`../logo`](../logo). The upstream folders are never modified, which keeps merges from
`HelpingHandsVR/identity` conflict-free.

| Path | Contents |
| --- | --- |
| [`MEDIA_GUIDELINES.md`](MEDIA_GUIDELINES.md) | Media team guidelines — licensing and credit, spacing, minimum sizes, contrast, contributing back upstream |
| [`README.ko.md`](README.ko.md) | The Korean edition of this document |
| [`overlays/`](overlays) | Transparent PNG/WebP logo overlays for OBS, Premiere Pro and After Effects |
| [`templates/`](templates) | Thumbnail, poster and card news specifications with margin guides |
| [`badges/`](badges) | Lower-third and sign-language avatar identity badges |
| `generate.py` | Builds every file in the three folders above |
| `requirements.txt` | Dependencies for `generate.py` |

Everything under `overlays/`, `badges/` and `templates/guides/` is **generated — do not hand-edit it.**
To change a specification, edit the constants in `generate.py`, re-run it, and update the matching
figures in `MEDIA_GUIDELINES.md`.

```bash
pip install -r media-team/requirements.txt
python media-team/generate.py
```

Credit every piece that shows the mark:

```text
Credit: HelpingHandsVR Identity
```

The full strings and rules are in
[`MEDIA_GUIDELINES.md` §1](MEDIA_GUIDELINES.md#1-license-compliance-and-credit).
