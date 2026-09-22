# Helping Hands Media Team — Drive, Naming & Version Workflow

![Edition](https://img.shields.io/badge/edition-2026-111827?style=flat-square)
![Storage](https://img.shields.io/badge/storage-Google%20Drive-1a73e8?style=flat-square)
![Naming](https://img.shields.io/badge/naming-MMDDYY__Project__Note__Version-0f766e?style=flat-square)
![Versioning](https://img.shields.io/badge/versioning-v0.1%20%E2%86%92%20v1.0%20%E2%86%92%20v1.1-7c3aed?style=flat-square)
![Team](https://img.shields.io/badge/team-5%20members-b45309?style=flat-square)
![Check--in](https://img.shields.io/badge/check--in-Discord-5865F2?style=flat-square)

The operating manual for the **shared Google Drive** of the Helping Hands media team (5 members):
folder structure, file naming, version numbering, and the collaboration rules that keep five people
out of each other's project files.

> **Precedence.** Brand questions are answered by [`../../GUIDELINES.md`](../../GUIDELINES.md) first and
> [`../MEDIA_GUIDELINES.md`](../MEDIA_GUIDELINES.md) second. This document governs **file operations only** —
> where a file lives, what it is called, and who is allowed to touch it right now.

**Contents**

1. [Drive folder structure](#1-drive-folder-structure)
2. [Naming convention](#2-naming-convention)
3. [Version control](#3-version-control)
4. [Collaboration & sync rules for 5 people](#4-collaboration--sync-rules-for-5-people)
5. [Checklists](#5-checklists)

---

## 1. Drive folder structure

The root of the shared drive holds **exactly these nine folders**. Do not add, rename, reorder or
"temporarily" create a tenth folder at the root — the numeric prefixes are what keep the order stable
for everyone.

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

| # | Folder | What belongs here | What must never go here |
| --- | --- | --- | --- |
| 00 | **`00_Scripts_Board`** | Scripts, shot lists, storyboards, captions/subtitle source text, schedules | Media files |
| 01 | **`01_Raw_Footage`** | Camera originals, screen captures, VR session recordings, interview audio — grouped per shoot | Edited or re-encoded clips |
| 02 | **`02_Official_Templates`** | Approved title, lower-third, end-card and thumbnail templates (`.prproj`, `.aep`, `.psd`, `.blend`) | Per-episode working copies |
| 03 | **`03_Graphic_Assets`** | Logos, overlays, badges, icons, fonts, stills — the pieces built from [`../overlays`](../overlays) and [`../badges`](../badges) | Renders of a finished video |
| 04 | **`04_Audio_Library`** | Licensed music, SFX, stingers, voice-over takes | Session/bounce files of a single project |
| 05 | **`05_Project_Files`** | One subfolder per project, holding the editor's working files | Exports |
| 06 | **`06_Project_Exports`** | Review exports — rough cuts, feedback rounds, `v0.x` only | Anything published |
| 07 | **`07_Final_Output`** | The approved master (`v1.0`) and every post-release revision (`v1.1`, `v1.2` …) | Drafts |
| 99 | **`99_Master_Archive`** | Closed projects: packaged project + master + the raw footage worth keeping | Work in progress |

### 1.1 Subfolders

Only levels **below** the root are yours to shape, and only in these two patterns:

```text
01_Raw_Footage/
└── 092226_CommunityDay/          # MMDDYY_Project — one folder per shoot day
    ├── CamA/
    ├── CamB/
    └── Audio/

05_Project_Files/
└── 092226_CommunityDay/          # MMDDYY_Project — one folder per project
    ├── 092226_CommunityDay_MainEdit_v0.3.prproj
    ├── Graphics/                 # project-only art, not library art
    └── Audio/                    # VO takes and the mix session
                                  # no Exports/ here — exports go to 06_Project_Exports
```

**Rule for raw footage:** keep the **camera's original filenames** (`C0042.MP4`, `A001_0912AB.mov`).
The date and project live on the *folder*; renaming clips after import is the single most common cause
of missing-media errors and of broken proxy/metadata pairing.

### 1.2 Where a file moves as it matures

```text
00_Scripts_Board → 01_Raw_Footage → 05_Project_Files → 06_Project_Exports
                                                              ↓ approved
                                                       07_Final_Output
                                                              ↓ project closed
                                                       99_Master_Archive
```

A file is **copied forward, never dragged sideways.** Moving a file that a project references breaks the
link for all five of us; exporting to the next folder does not.

---

## 2. Naming convention

### 2.1 Standard form

```text
[MMDDYY]_[Project]_[Note]_[etc.]_[Version].[ext]
```

Example:

```text
092226_CommunityDay_RoughCut_1080p_v0.2.mp4
│      │             │        │     │    └── extension, always lowercase
│      │             │        │     └─────── version (§3)
│      │             │        └───────────── [etc.] — optional qualifiers
│      │             └────────────────────── note: what this file is
│      └──────────────────────────────────── project name
└─────────────────────────────────────────── date, MMDDYY
```

| Field | Required | Rule | Good | Bad |
| --- | --- | --- | --- | --- |
| `MMDDYY` | ✅ | 6 digits, zero-padded. The date the file was **created**, not exported | `092226` | `9-22-26`, `Sep22` |
| `Project` | ✅ | One token, `PascalCase`, ASCII only. Same spelling for the whole project's life | `CommunityDay` | `community day`, `커뮤니티데이` |
| `Note` | ✅ | What the file *is*: `MainEdit`, `RoughCut`, `Master`, `LowerThird`, `Interview` | `MainEdit` | `edit2`, `final` |
| `etc.` | ⬜ | Zero or more qualifiers: resolution, camera, language, loudness, platform | `1080p`, `CamA`, `KO-sub`, `-14LUFS`, `YT` | `new`, `fix`, `real` |
| `Version` | ✅ | `v<major>.<minor>` (§3) | `v0.2`, `v1.0` | `v2`, `ver1`, `V1.0` |
| `ext` | ✅ | Lowercase, unchanged by hand | `.mp4` | `.MP4` |

Hard rules:

- **`_` separates fields. `-` joins words inside one field.** `KO-sub` is one field; `KO_sub` is two.
- No spaces, no Korean characters, no `()[]{}#%&/\*?:"<>|` — Drive tolerates them, Premiere, ffmpeg and
  shell scripts do not.
- Never rename a file that is **currently referenced** by an open project. Export or save-as instead.

### 2.2 MMDDYY vs. YYMMDD — and how to sort

Our standard is **`MMDDYY`**, because that is how the team reads and says dates out loud. The cost is
that `MMDDYY` **does not sort chronologically**: name-sorting puts January of every year before
February of every year.

| | `MMDDYY` (our standard) | `YYMMDD` | `YYYY-MM-DD` (ISO 8601) |
| --- | --- | --- | --- |
| `2026-09-22` | `092226` | `260922` | `2026-09-22` |
| Sorts by name = sorts by date | ❌ | ✅ | ✅ |
| Reads naturally for this team | ✅ | ❌ | ⬜ |
| Groups a year together | ❌ | ✅ | ✅ |
| Example name-sort result | `010127`, `092226`, `120125` | `251201`, `260101`, `260922` | — |

**Sorting tips that make `MMDDYY` workable in Drive:**

1. **Sort by *Last modified*, not by *Name*** (`수정 날짜` in the Drive list header). This is the default
   view and it is chronologically correct regardless of filename.
2. **Search by prefix instead of scrolling.** Drive matches on name fragments:
   `0922` finds one day, `CommunityDay` finds one project across every folder.
3. **Let folders carry the chronology.** One folder per shoot/project (`092226_CommunityDay`) means you
   almost never need a chronological *file* sort inside it — the version number is the sort key there.
4. **Keep the project token identical all the way through.** `Project` before `Note` is what makes a
   name-sort group a project together, which is the grouping we actually use daily.
5. **Long-term stacks** (`99_Master_Archive`) are organised as `Year/Project/`, so the folder tree
   supplies the chronology that the filename does not.

> **Documented trade-off.** If the team ever votes to switch, `YYMMDD` is the migration target: it is a
> pure digit-order change, so renaming is scriptable. Until that vote, **`MMDDYY` is the only accepted
> form** — mixing the two is worse than either one.

### 2.3 Examples

**Project files — `05_Project_Files/092226_CommunityDay/`**

| Application | Filename |
| --- | --- |
| Premiere Pro edit | `092226_CommunityDay_MainEdit_v0.3.prproj` |
| After Effects lower-third | `092226_CommunityDay_LowerThird_1440x240_v0.2.aep` |
| Blender sign-language avatar scene | `092226_CommunityDay_SignAvatar_CamA_v0.4.blend` |
| Auto-save / crash file | leave Adobe's own name; never promote it to a version |

**Draft & feedback exports — `06_Project_Exports/`** *(`v0.x` only, H.264 `.mp4`)*

| Round | Filename |
| --- | --- |
| First rough cut | `092226_CommunityDay_RoughCut_1080p_v0.1.mp4` |
| After lead's feedback | `092326_CommunityDay_RoughCut_1080p_v0.2.mp4` |
| Picture lock for review | `092426_CommunityDay_PictureLock_1080p_v0.3.mp4` |
| Subtitle check copy | `092426_CommunityDay_PictureLock_KO-sub_1080p_v0.3.mp4` |

**Final masters — `07_Final_Output/`**

| Purpose | Filename |
| --- | --- |
| Approved master | `092526_CommunityDay_Master_YT-2160p_v1.0.mp4` |
| Vertical cutdown | `092526_CommunityDay_Master_Shorts-1080x1920_v1.0.mp4` |
| Post-release typo fix | `092726_CommunityDay_Master_YT-2160p_v1.1.mp4` |

**Assets & audio — `03_Graphic_Assets/`, `04_Audio_Library/`**

| Asset | Filename |
| --- | --- |
| Overlay export | `090126_Brand_LowerThird_Overlay_1440x240_v1.0.png` |
| Thumbnail base | `090126_Brand_Thumbnail_Base_1280x720_v1.2.psd` |
| Licensed BGM | `090126_Library_BGM_Uplifting-Loop_-14LUFS_v1.0.wav` |
| SFX | `090126_Library_SFX_Whoosh-Short_v1.0.wav` |
| Voice-over take | `092226_CommunityDay_VO_Narration-KO_v0.2.wav` |

For every third-party asset, keep a `LICENSE.md` (or `.txt`) **beside the file** naming the source,
licence and attribution string required. An asset without a licence note cannot ship.

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
  round of changes, so `092226_..._v0.3.prproj` still opens the cut that `..._v0.3.mp4` came from.
- Keep, at minimum: **all `v1.x`**, the **last two `v0.x`**, and the `v0.x` that was picture-locked.
  Older drafts can go at project close (§4.4).

### 3.1 Forbidden filenames — zero tolerance

These are **rejected on sight**. A file with one of these names is not a deliverable, and re-exporting
is cheaper than the twenty minutes five people spend guessing which one is current.

| ❌ Never | Why | ✅ Instead |
| --- | --- | --- |
| `final.mp4`, `최종.mp4` | "Final" is a state, not an identifier | `092526_CommunityDay_Master_YT-2160p_v1.0.mp4` |
| `진짜최종.mp4`, `final_final.mp4`, `FINAL_real.mp4` | There is always another one | `..._v1.1.mp4` |
| `최종_수정.mp4`, `final_fix2.mp4` | Unordered — which fix came first? | `..._v1.2.mp4` |
| `video_v2.mp4`, `edit_ver3.prproj` | Single-digit versions collide with `v0.x` / `v1.x` | `..._v0.2.mp4` |
| `홍길동_수정본.mp4` | Owner is in Drive's metadata and in Discord, not in the name | `..._v0.3.mp4` |
| `Untitled.prproj`, `Sequence 01.mp4` | Application defaults | rename on first save |
| `Copy of 092226_...mp4`, `..._v0.3 (1).mp4` | Drive collision artefacts | delete the copy, bump the version |
| `092226_CommunityDay_MainEdit_v0.3_fixed.prproj` | A suffix after the version defeats the version | `..._v0.4.prproj` |

> Rule of thumb: **if the newest file is not obvious from the names alone, the naming failed.**

---

## 4. Collaboration & sync rules for 5 people

### 4.1 Ownership map

Five people, one drive. Every root folder has one accountable owner; everyone else opens files there
read-only unless they have checked them out (§4.3).

| Role | Owns (write) | Reads |
| --- | --- | --- |
| **Lead media engineer / workflow manager** | `02_Official_Templates`, `07_Final_Output`, `99_Master_Archive` | everything |
| **Editor A** | assigned projects in `05_Project_Files`, `06_Project_Exports` | `01`–`04` |
| **Editor B** | assigned projects in `05_Project_Files`, `06_Project_Exports` | `01`–`04` |
| **Motion / graphics** | `03_Graphic_Assets`, template sources in `02_Official_Templates` | `00`, `05` |
| **Audio** | `04_Audio_Library`, VO and mix files in the project folder | `00`, `05`, `06` |

Only the lead writes to `07_Final_Output`. That is how `v1.0` stays meaningful.

### 4.2 Packaging — preventing missing footage

A project file stores **paths**, not media. A path that points at somebody's desktop resolves to
nothing on the other four machines, and Premiere then greets them with *"Where is the file…?"*.

**Before you link anything:** the media must already be in the shared drive, under `01_Raw_Footage`,
`03_Graphic_Assets` or `04_Audio_Library`. Never import from `~/Desktop`, `~/Downloads`, a phone
transfer folder, or an SD card.

Per application, when you hand a project to someone else or archive it:

| Application | Action | Notes |
| --- | --- | --- |
| **Premiere Pro** | `File ▸ Project Manager ▸ Collect Files and Copy to New Location` | Tick *Exclude Unused Clips* and *Include Audio Conform Files*; leave *Convert…* off for masters |
| **After Effects** | `File ▸ Dependencies ▸ Collect Files…` (*Collect Source Files: For All Comps*) | Ship the generated `.txt` report with it |
| **Blender** | `File ▸ External Data ▸ Make Paths Relative`, then `Pack Resources` before archiving | Unpack into the project folder if the `.blend` grows unmanageable |
| **DaVinci Resolve** | `File ▸ Media Management` (copy) or export a `.drp` archive | Relink against the drive path, not a local copy |
| **All** | Relative paths only; identical mount/drive letter per machine where possible | Document the expected root in the project folder |

Rules that follow from this:

- **Never move or rename media that a project links to.** Copy forward (§1.2) and relink deliberately.
- Every project folder gets a one-line `README.txt`: what the deliverable is, which project file is
  current, where its media lives.
- **Package at project close, always** — a `99_Master_Archive` entry that cannot be reopened in a year
  is not an archive.
- Use **proxies** for shared editing (`01_Raw_Footage/<shoot>/Proxies/`), so a relink hits small files.

### 4.3 Discord check-in / check-out

Google Drive has no file locking. Two people saving the same `.prproj` produces a silent conflict copy
and one person's afternoon disappears. So we lock **socially**, in `#media-checkin`.

**Check out before you open. Check in when you save and close.**

```text
🔒 CHECK-OUT  092226_CommunityDay_MainEdit_v0.3.prproj
              @editor-a · ~2h · ETA 18:00 KST

🔓 CHECK-IN   092226_CommunityDay_MainEdit_v0.4.prproj
              @editor-a · colour pass done, next: captions
              → export: 092326_CommunityDay_RoughCut_1080p_v0.2.mp4
```

| Rule | Detail |
| --- | --- |
| **One writer per file** | If it is checked out, you may open it **read-only** or wait. No exceptions for "a quick fix" |
| **One thread per project** | Keep the whole history of a project in a single Discord thread |
| **State the ETA** | No ETA = no lock. Others need to plan around you |
| **Hold limit: 24 h** | Then check in, even mid-edit, or re-post the lock with a new ETA |
| **Stale lock (no reply for 24 h)** | The lead may force-release: post `⚠️ FORCE-RELEASE` naming the file and the holder |
| **Pause sync while exporting** | Let the render finish, then resume, then check in |
| **A check-in names the new version** | The version number in the check-in message is the truth for everyone else |
| **Assets are checked out too** | `02_Official_Templates` and `03_Graphic_Assets` are shared by all five — same protocol |

Scripts in `00_Scripts_Board` are the exception: keep them as **Google Docs**, which are genuinely
multi-user, and link them rather than exporting `.docx` copies.

### 4.4 Media cache & Drive capacity

**Media cache never lives in the shared drive.** Cache is per-machine, disposable and enormous;
syncing it burns quota and produces conflict copies of files nobody reads.

| Application | Setting | Set it to |
| --- | --- | --- |
| Premiere Pro | `Preferences ▸ Media Cache` | A **local SSD** path, e.g. `D:\PrCache` / `~/Library/Caches/PrCache` |
| Premiere Pro | `Media Cache Management` | *Automatically delete cache files older than **30 days***, cap the size |
| After Effects | `Preferences ▸ Media & Disk Cache` | Local disk cache, 20–60 GB, *Empty Disk Cache* monthly |
| Blender | `Preferences ▸ File Paths ▸ Temp` | Local temp path |
| Drive for desktop | Sync mode | **Stream** the drive; mark only your active project *Available offline* |

Housekeeping, monthly (lead runs it, everyone participates):

- Clear caches and Adobe auto-save folders older than 30 days.
- Prune `06_Project_Exports`: keep the last two `v0.x` and the picture-locked one, delete the rest.
- Check the drive's storage page; anything above **80 %** triggers an archive pass.
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

- [ ] Project token agreed and spelled once, for the whole project's life
- [ ] `01_Raw_Footage/MMDDYY_Project/` and `05_Project_Files/MMDDYY_Project/` created
- [ ] All media copied into the drive **before** any import; proxies generated
- [ ] Media cache pointed at a local disk (§4.4)
- [ ] Discord thread opened in `#media-checkin`

**Before every export**

- [ ] File checked out to you, and you are the only writer
- [ ] Project saved as the version you are about to export
- [ ] Name matches `[MMDDYY]_[Project]_[Note]_[etc.]_[Version].[ext]`
- [ ] `v0.x` → `06_Project_Exports` · approved `v1.x` → `07_Final_Output`
- [ ] Credit present per [`../MEDIA_GUIDELINES.md` §1](../MEDIA_GUIDELINES.md#1-license-compliance-and-credit)
- [ ] No forbidden name (§3.1), no missing-media warning on open

**Closing a project**

- [ ] `v1.0` (and any `v1.x`) in `07_Final_Output`
- [ ] Project packaged/collected (§4.2) and reopened once to verify it relinks
- [ ] `99_Master_Archive/<Year>/<Project>/` holds package + masters + selects + licence notes
- [ ] `06_Project_Exports` pruned, caches cleared, Discord thread closed with a final check-in
