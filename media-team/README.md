# Helping Hands Media Team — Drive, Naming & Version Guide

**🌐 Language · [🇰🇷 한국어 안내서](./README.ko.md) · 🇺🇸 English (this document)**

![Edition](https://img.shields.io/badge/edition-2026-111827?style=flat-square)
![Storage](https://img.shields.io/badge/storage-Google%20Drive-1a73e8?style=flat-square)
![Date format](https://img.shields.io/badge/date-YYMMDD-be123c?style=flat-square)
![Naming](https://img.shields.io/badge/naming-YYMMDD__Project__Note__Version-0f766e?style=flat-square)
![Versioning](https://img.shields.io/badge/versioning-v0.1%20%E2%86%92%20v1.0%20%E2%86%92%20v1.1-7c3aed?style=flat-square)
![Team](https://img.shields.io/badge/team-5%20members-b45309?style=flat-square)
![Check--in](https://img.shields.io/badge/check--in-Discord-5865F2?style=flat-square)

The operating manual for the Helping Hands media team (5 members): the shared **Google Drive** folder
structure, the **file naming convention**, **version numbering**, and the collaboration rules that keep
five people out of each other's project files.

> [!IMPORTANT]
> **Precedence.** Brand questions are answered by [`../GUIDELINES.md`](../GUIDELINES.md) first and
> [`MEDIA_GUIDELINES.md`](MEDIA_GUIDELINES.md) second. This document governs **file operations only** —
> where a file lives, what it is called, and who is allowed to touch it right now.

**Contents**

1. [Drive folder structure](#1-drive-folder-structure)
2. [Naming convention](#2-naming-convention)
3. [Version control](#3-version-control)
4. [Collaboration & sync rules for 5 people](#4-collaboration--sync-rules-for-5-people)
5. [Checklists](#5-checklists)
6. [Repository assets in this folder](#6-repository-assets-in-this-folder)

---

## 1. Drive folder structure

The root of the shared drive holds **exactly these nine folders**.

```text
Helping Hands Media Team/
├── 00_Scripts_Board/
├── 01_Raw_Footage/
├── 02_Official_Templates/
├── 03_Graphic_Assets/
├── 04_Audio_Library/
├── 05_Project_Files/
├── 06_Project_Exports/
├── 07_Final_Output/
└── 99_Master_Archive/
```

> [!WARNING]
> Do not add, rename, reorder or "temporarily" create a tenth folder at the root. The numeric prefixes
> are what keep the order identical on all five machines.

| # | Folder | What belongs here | What must never go here |
| --- | --- | --- | --- |
| 00 | **`00_Scripts_Board`** | Scripts, shot lists, storyboards, subtitle source text, schedules | Media files |
| 01 | **`01_Raw_Footage`** | Camera originals, OBS screen captures, VR session recordings, interview audio — grouped per shoot | Edited or re-encoded clips |
| 02 | **`02_Official_Templates`** | Approved title, lower-third, end-card and thumbnail templates (`.prproj`, `.aep`, `.psd`, `.blend`) | Per-episode working copies |
| 03 | **`03_Graphic_Assets`** | Logos, overlays, badges, icons, fonts, stills — including the files built from [`overlays/`](overlays) and [`badges/`](badges) | Renders of a finished video |
| 04 | **`04_Audio_Library`** | Licensed music, SFX, stingers, voice-over takes | Session/bounce files of a single project |
| 05 | **`05_Project_Files`** | One subfolder per project, holding the editor's working files | Exports |
| 06 | **`06_Project_Exports`** | Review exports — rough cuts, feedback rounds, **`v0.x` only** | Anything published |
| 07 | **`07_Final_Output`** | The approved master (`v1.0`) and every post-release revision (`v1.1`, `v1.2` …) | Drafts |
| 99 | **`99_Master_Archive`** | Closed projects: packaged project + master + the raw footage worth keeping | Work in progress |

### 1.1 Subfolder patterns

Only levels **below** the root are yours to shape, and only in these two patterns.

```text
01_Raw_Footage/
├── 260922_CommunityDay_CamA/     # [YYMMDD]_[Project]_[Source]
├── 260922_CommunityDay_CamB/
├── 260922_CommunityDay_OBS/
├── 260922_CommunityDay_VR/
└── 260922_CommunityDay_Audio/

05_Project_Files/
└── 260922_CommunityDay/          # [YYMMDD]_[Project]
    ├── 260922_CommunityDay_MainEdit_v0.3.prproj
    ├── Graphics/                 # project-only art, not library art
    ├── Audio/                    # VO takes and the mix session
    └── README.txt                # deliverable, current file, where its media lives
                                  # no Exports/ here — exports go to 06_Project_Exports
```

`[Source]` is the origin of the clips: `CamA`, `CamB`, `OBS`, `VR`, `Audio`, `Screen`, `Drone`.

### 1.2 `01_Raw_Footage` — original filenames are preserved

> [!CAUTION]
> **Never rename a clip inside `01_Raw_Footage`.** Camera, OBS and VR originals keep the filename their
> device gave them — `C0042.MP4`, `A001_0922AB.mov`, `2026-09-22_19-04-31.mkv`.

Renaming after import is the single most common cause of two failures:

| Failure | How renaming causes it |
| --- | --- |
| **Missing footage / "Where is the file…?"** | A project file stores the *path*, including the filename. Renaming the clip breaks the link for all five of us, and a manual relink of 200 clips is an afternoon |
| **Broken proxy pairing** | Premiere and Resolve pair a proxy to its original **by filename**. Rename one side and the proxy silently detaches, so the edit falls back to full-resolution media — or fails to attach at all |
| **Lost sidecar & metadata pairing** | `.xmp`, `.THM`, `.LRV` sidecars and multi-file spanned clips are matched by basename too |

The date, project and source therefore live on the **folder**, named
`[YYMMDD]_[Project]_[Source]` — which gives us the same sortable, searchable information without
touching a single link.

```text
✅ 01_Raw_Footage/260922_CommunityDay_CamA/C0042.MP4
❌ 01_Raw_Footage/260922_CommunityDay_Interview_CamA_v0.1.MP4
```

Proxies go beside them, in `01_Raw_Footage/260922_CommunityDay_CamA/Proxies/`, **also with the original
basename**.

### 1.3 How a file moves as it matures

```text
00_Scripts_Board → 01_Raw_Footage → 05_Project_Files → 06_Project_Exports
                                                              │ approved
                                                              ▼
                                                       07_Final_Output
                                                              │ project closed
                                                              ▼
                                                       99_Master_Archive
```

> [!TIP]
> A file is **copied forward, never dragged sideways.** Moving a file that a project references breaks
> the link for everyone; exporting into the next folder does not.

---

## 2. Naming convention

### 2.1 Standard form

```text
[YYMMDD]_[Project]_[Note]_[etc.]_[Version].[ext]
```

```text
260922_CommunityDay_RoughCut_1080p_v0.2.mp4
│      │             │        │     │    └── extension, always lowercase
│      │             │        │     └─────── version (§3)
│      │             │        └───────────── [etc.] — optional qualifiers
│      │             └────────────────────── note: what this file is
│      └──────────────────────────────────── project name
└─────────────────────────────────────────── date, YYMMDD (2026-09-22)
```

| Field | Required | Rule | Good | Bad |
| --- | --- | --- | --- | --- |
| `YYMMDD` | ✅ | 6 digits, zero-padded, **year first**. The date the file was **created** | `260922` | `092226`, `26-09-22`, `Sep22` |
| `Project` | ✅ | One token, `PascalCase`, ASCII only. Same spelling for the whole project's life | `CommunityDay` | `community day`, `커뮤니티데이` |
| `Note` | ✅ | What the file *is*: `MainEdit`, `RoughCut`, `Master`, `LowerThird`, `Interview` | `MainEdit` | `edit2`, `final` |
| `etc.` | ⬜ | Zero or more qualifiers: resolution, camera, language, loudness, platform | `1080p`, `CamA`, `KO-sub`, `-14LUFS`, `YT` | `new`, `fix`, `real` |
| `Version` | ✅ | `v<major>.<minor>`, lowercase `v` (§3) | `v0.2`, `v1.0` | `v2`, `ver1`, `V1.0` |
| `ext` | ✅ | Lowercase, never changed by hand | `.mp4` | `.MP4` |

Hard rules:

- **`_` separates fields. `-` joins words inside one field.** `KO-sub` is one field; `KO_sub` is two.
- No spaces, no Korean characters, none of `( ) [ ] { } # % & / \ * ? : " < > |` — Drive tolerates them,
  Premiere, ffmpeg and shell scripts do not.
- **Never rename a file that a project currently references.** Export, or save-as, instead.
- The only exception to this whole section is `01_Raw_Footage` (§1.2).

### 2.2 Why `YYMMDD` — and why never mix

`YYMMDD` is the **single team-wide date standard**. It is the only 6-digit form where sorting by name
is the same as sorting by date, because the digits run from the slowest-changing unit to the fastest.

| | `YYMMDD` ✅ **our standard** | `MMDDYY` ❌ |
| --- | --- | --- |
| `2026-09-22` | `260922` | `092226` |
| Name-sort equals date-sort | ✅ | ❌ |
| Groups a year together | ✅ | ❌ |
| Groups a month together | ✅ | ❌ |
| Name-sort of Dec 1 '25 / Jan 1 '26 / Sep 22 '26 | `251201`, `260101`, `260922` — correct | `010126`, `092226`, `120125` — scrambled |

> [!WARNING]
> **Mixing the two formats is worse than either one alone.** `092226` and `260922` are both valid-looking
> 6-digit strings, so a mixed folder can no longer be read, sorted or scripted — and a name like
> `090112` is genuinely ambiguous: 2009-01-12 under one rule, 2012-09-01 under the other.
> If you find a legacy `MMDDYY` name, **rename it to `YYMMDD` the moment you touch it** — as long as
> no project file links to it (§2.1).

Everything downstream depends on this one rule:

- Sorting a folder by **Name** in Drive gives chronological order — no need to switch to *Last modified*.
- Searching `2609` in Drive finds one month; `26` finds one year.
- Scripts and `ls | sort` agree with what people see on screen.

<details>
<summary>Converting legacy <code>MMDDYY</code> names (dry-run first)</summary>

Run it with **bash, not sh** (the substring expansions are bash-only). It prints the renames it would
perform and changes nothing. A prefix is only offered when it reads as `MMDDYY` — month `01`–`12`, day
`01`–`31`, year `24`–`30` — so names already in `YYMMDD` are left alone.

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

Read every line, confirm that no project links to those files, then re-run piped to `bash`.

</details>

### 2.3 Examples

**Project files** — `05_Project_Files/260922_CommunityDay/`

| Application | Filename |
| --- | --- |
| Premiere Pro edit | `260922_CommunityDay_MainEdit_v0.3.prproj` |
| After Effects lower-third | `260922_CommunityDay_LowerThird_1440x240_v0.2.aep` |
| Blender sign-language avatar scene | `260922_CommunityDay_SignAvatar_CamA_v0.4.blend` |
| Auto-save / crash file | leave the application's own name; never promote it to a version |

**Draft & feedback exports** — `06_Project_Exports/` · `v0.x` only, H.264 `.mp4`

| Round | Filename |
| --- | --- |
| First rough cut | `260922_CommunityDay_RoughCut_1080p_v0.1.mp4` |
| After the lead's feedback | `260923_CommunityDay_RoughCut_1080p_v0.2.mp4` |
| Picture lock for review | `260924_CommunityDay_PictureLock_1080p_v0.3.mp4` |
| Subtitle check copy | `260924_CommunityDay_PictureLock_KO-sub_1080p_v0.3.mp4` |

**Final masters** — `07_Final_Output/`

| Purpose | Filename |
| --- | --- |
| Approved master | `260925_CommunityDay_Master_YT-2160p_v1.0.mp4` |
| Vertical cutdown | `260925_CommunityDay_Master_Shorts-1080x1920_v1.0.mp4` |
| Post-release typo fix | `260927_CommunityDay_Master_YT-2160p_v1.1.mp4` |

**Assets & audio** — `03_Graphic_Assets/`, `04_Audio_Library/`

| Asset | Filename |
| --- | --- |
| Overlay export | `260901_Brand_LowerThird_Overlay_1440x240_v1.0.png` |
| Thumbnail base | `260901_Brand_Thumbnail_Base_1280x720_v1.2.psd` |
| Licensed BGM | `260901_Library_BGM_Uplifting-Loop_-14LUFS_v1.0.wav` |
| SFX | `260901_Library_SFX_Whoosh-Short_v1.0.wav` |
| Voice-over take | `260922_CommunityDay_VO_Narration-KO_v0.2.wav` |

> [!NOTE]
> For every third-party asset, keep a `LICENSE.md` (or `.txt`) **beside the file**, naming the source,
> the licence and the attribution string it requires. An asset without a licence note cannot ship.

---

## 3. Version control

Semantic versioning, media-team flavour. Two digits, always.

| Stage | Numbers | Lives in | Meaning |
| --- | --- | --- | --- |
| **Draft / feedback** | `v0.1`, `v0.2`, `v0.3` … | `06_Project_Exports` | Not approved. Every feedback round is a new minor number |
| **Official release** | **`v1.0`** | `07_Final_Output` | Approved by the lead and published. Exactly one `v1.0` per deliverable |
| **Post-release revision** | `v1.1`, `v1.2` … | `07_Final_Output` | Published, then corrected — typo, audio fix, re-cut |
| **Re-version / re-brand** | `v2.0` | `07_Final_Output` | A new edit of the same title, not a fix |

Rules:

- **Bump, never overwrite.** A new export is a new number. `v0.2` stays on the drive after `v0.3` exists,
  so feedback threads keep pointing at something real.
- **Nothing in `07_Final_Output` is below `v1.0`.** If it is not approved, it is a `v0.x` and it belongs
  in `06_Project_Exports`.
- **`v1.0` is immutable.** A change after publication is `v1.1`, even a one-frame fix.
- **The project file carries the version it produced.** Save-as to `v0.4` *before* you start the next
  round of changes, so `260922_..._v0.3.prproj` still opens the cut that `..._v0.3.mp4` came from.
- Keep, at minimum: **all `v1.x`**, the **last two `v0.x`**, and the `v0.x` that was picture-locked.

### 3.1 Forbidden filenames — zero tolerance

> [!CAUTION]
> These are **rejected on sight**. A file with one of these names is not a deliverable. Re-exporting is
> cheaper than the twenty minutes five people spend guessing which file is current.

| ❌ Never | Why | ✅ Instead |
| --- | --- | --- |
| `final.mp4`, `최종.mp4` ("final") | "Final" is a state, not an identifier | `260925_CommunityDay_Master_YT-2160p_v1.0.mp4` |
| `진짜최종.mp4` ("really final"), `final_final.mp4`, `FINAL_real.mp4` | There is always another one | `..._v1.1.mp4` |
| `최종_수정.mp4` ("final, revised"), `final_fix2.mp4` | Unordered — which fix came first? | `..._v1.2.mp4` |
| `video_v2.mp4`, `edit_ver3.prproj` | Single-digit versions collide with `v0.x` / `v1.x` | `..._v0.2.mp4` |
| `홍길동_수정본.mp4` ("<person>_revision") | The owner is in Drive's metadata and in Discord, not in the name | `..._v0.3.mp4` |
| `Untitled.prproj`, `Sequence 01.mp4` | Application defaults | rename on first save |
| `Copy of 260922_….mp4`, `..._v0.3 (1).mp4` | Drive collision artefacts | delete the copy, bump the version |
| `260922_CommunityDay_MainEdit_v0.3_fixed.prproj` | A suffix after the version defeats the version | `..._v0.4.prproj` |

> [!TIP]
> Rule of thumb: **if the newest file is not obvious from the names alone, the naming failed.**

---

## 4. Collaboration & sync rules for 5 people

### 4.1 Ownership map

Five people, one drive. Every root folder has one accountable owner; everyone else opens files there
read-only unless they have checked them out (§4.3).

| Role | Owns (write) | Reads |
| --- | --- | --- |
| **Lead media engineer / workflow manager** | `02_Official_Templates`, `07_Final_Output`, `99_Master_Archive` | everything |
| **Editor A** | assigned projects in `05_Project_Files`, `06_Project_Exports` | `00`–`04` |
| **Editor B** | assigned projects in `05_Project_Files`, `06_Project_Exports` | `00`–`04` |
| **Motion / graphics** | `03_Graphic_Assets`, template sources in `02_Official_Templates` | `00`, `05` |
| **Audio** | `04_Audio_Library`, VO and mix files in the project folder | `00`, `05`, `06` |

Only the lead writes to `07_Final_Output`. That is how `v1.0` stays meaningful.

### 4.2 Packaging — preventing missing footage

A project file stores **paths**, not media. A path that points at somebody's desktop resolves to nothing
on the other four machines.

> [!IMPORTANT]
> **Before you link anything:** the media must already be in the shared drive, under `01_Raw_Footage`,
> `03_Graphic_Assets` or `04_Audio_Library`. Never import from `~/Desktop`, `~/Downloads`, a phone
> transfer folder, or an SD card.

When you hand a project to someone else, or archive it:

| Application | Action | Notes |
| --- | --- | --- |
| **Premiere Pro** | `File ▸ Project Manager ▸ Collect Files and Copy to New Location` | Tick *Exclude Unused Clips* and *Include Audio Conform Files*; leave *Convert…* off for masters |
| **After Effects** | `File ▸ Dependencies ▸ Collect Files…` (*Collect Source Files: For All Comps*) | Ship the generated `.txt` report with it |
| **Blender** | `File ▸ External Data ▸ Make Paths Relative`, then `Pack Resources` before archiving | Unpack into the project folder if the `.blend` grows unmanageable |
| **DaVinci Resolve** | `File ▸ Media Management` (copy), or export a `.drp` archive | Relink against the drive path, not a local copy |
| **All** | Relative paths only; the same mount point / drive letter on every machine where possible | Record the expected root in the project `README.txt` |

Rules that follow:

- **Never move or rename media that a project links to.** Copy forward (§1.3) and relink deliberately.
- Every project folder gets a one-line `README.txt`: the deliverable, which project file is current,
  where its media lives.
- **Package at project close, always** — a `99_Master_Archive` entry that cannot be reopened in a year is
  not an archive. Reopen the packaged copy once to prove it relinks.
- Edit from **proxies** (§1.2) so a relink touches small files.

### 4.3 Discord check-in / check-out

Google Drive has **no file locking**. Two people saving the same `.prproj` produces a silent conflict
copy, and one person's afternoon disappears. So we lock **socially**, in `#media-checkin`.

> [!IMPORTANT]
> **Check out before you open. Check in when you save and close.**

```text
🔒 CHECK-OUT  260922_CommunityDay_MainEdit_v0.3.prproj
              @editor-a · ~2h · ETA 18:00 KST

🔓 CHECK-IN   260922_CommunityDay_MainEdit_v0.4.prproj
              @editor-a · colour pass done, next: captions
              → export: 260923_CommunityDay_RoughCut_1080p_v0.2.mp4
```

| Rule | Detail |
| --- | --- |
| **One writer per file** | If it is checked out, open it **read-only** or wait. No exceptions for "a quick fix" |
| **One thread per project** | The whole history of a project stays in a single Discord thread |
| **State the ETA** | No ETA = no lock. The others need to plan around you |
| **Hold limit: 24 h** | Then check in, even mid-edit, or re-post the lock with a new ETA |
| **Stale lock (no reply for 24 h)** | The lead may force-release: post `⚠️ FORCE-RELEASE` naming the file and the holder |
| **Pause sync while exporting** | Let the render finish, resume sync, then check in |
| **A check-in names the new version** | The version number in the check-in message is the truth for everyone else |
| **Assets are checked out too** | `02_Official_Templates` and `03_Graphic_Assets` are shared by all five — same protocol |

> [!TIP]
> Scripts in `00_Scripts_Board` are the exception: keep them as **Google Docs**, which are genuinely
> multi-user, and link them instead of exporting `.docx` copies.

### 4.4 Media cache & Drive capacity

> [!WARNING]
> **Media cache never lives in the shared drive.** Cache is per-machine, disposable and enormous;
> syncing it burns quota and produces conflict copies of files nobody reads.

| Application | Setting | Set it to |
| --- | --- | --- |
| Premiere Pro | `Preferences ▸ Media Cache` | A **local SSD** path, e.g. `D:\PrCache` or `~/Library/Caches/PrCache` |
| Premiere Pro | `Media Cache Management` | *Automatically delete cache files older than* **30 days**, and cap the size |
| After Effects | `Preferences ▸ Media & Disk Cache` | Local disk cache, 20–60 GB; *Empty Disk Cache* monthly |
| Blender | `Preferences ▸ File Paths ▸ Temp` | A local temp path |
| Drive for desktop | Sync mode | **Stream** the drive; mark only your active project *Available offline* |

Monthly housekeeping — the lead runs it, everyone participates:

- Clear caches and application auto-save folders older than 30 days.
- Prune `06_Project_Exports`: keep the last two `v0.x` and the picture-locked one; delete the rest.
- Check the drive's storage page. Above **80 %** triggers an archive pass.
- Confirm nothing in `05_Project_Files` has been idle for over 60 days without an archive plan.

Capacity rules:

- **Drafts are H.264 `.mp4`.** ProRes / DNxHR belong in `07_Final_Output` and `99_Master_Archive` only.
- **Camera originals are cold storage.** Keep proxies plus the selects on the drive; the full card image
  goes to the archive drive (2 copies, one off-site) and is referenced from the project `README.txt`.
- **Never store two copies of the same asset.** Link into `03_Graphic_Assets` / `04_Audio_Library`
  instead of copying into a project folder.
- Delete Drive conflict artefacts (`… (1)`, `Copy of …`) the day they appear — after checking which one
  is real.

---

## 5. Checklists

**Starting a project**

- [ ] Project token agreed, and spelled the same way for the project's whole life
- [ ] `01_Raw_Footage/[YYMMDD]_[Project]_[Source]/` created per source; clip names left untouched
- [ ] `05_Project_Files/[YYMMDD]_[Project]/` created with a `README.txt`
- [ ] All media copied into the drive **before** any import; proxies generated
- [ ] Media cache pointed at a local disk (§4.4)
- [ ] Discord thread opened in `#media-checkin`

**Before every export**

- [ ] The file is checked out to you, and you are the only writer
- [ ] Project saved as the version you are about to export
- [ ] Name matches `[YYMMDD]_[Project]_[Note]_[etc.]_[Version].[ext]`
- [ ] `v0.x` → `06_Project_Exports` · approved `v1.x` → `07_Final_Output`
- [ ] Credit present per [`MEDIA_GUIDELINES.md` §1](MEDIA_GUIDELINES.md#1-license-compliance-and-credit)
- [ ] No forbidden name (§3.1), and no missing-media warning when the project opens

**Closing a project**

- [ ] `v1.0` (and any `v1.x`) in `07_Final_Output`
- [ ] Project packaged/collected (§4.2) and reopened once to verify it relinks
- [ ] `99_Master_Archive/<Year>/<Project>/` holds package + masters + selects + licence notes
- [ ] `06_Project_Exports` pruned, caches cleared, Discord thread closed with a final check-in

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
