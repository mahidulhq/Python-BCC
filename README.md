# Python-BCC — 14-day Python Training Projects

Completed as part of a 14-day government-funded Python training program, this repository contains daily exercises, practice projects, and small apps that demonstrate fundamental Python concepts, simple GUIs, and packaging to Windows executables.

## What this is
A collection of learning materials and small projects used during a 14-day Python course. It includes day-by-day exercises (beginner friendly), small GUI utilities (Tkinter / customtkinter), example scripts (email sender, alarms), and notes on packaging apps into Windows .exe files.

### Stack
- Language(s): Python (primary), HTML, PHP, CSS (small amounts for web-like practice pages)
- Runtime: Python 3.8+ (recommend 3.10+ for some projects)
- Notable libraries: customtkinter, pygame, PyInstaller (for packaging)

## Repository layout
```
.day files and config
.vscode/                         IDE settings
day01/ - day14/                  Daily exercises and small scripts (beginner examples)
practices/                       Practice projects and guides
  ClockProjects/                 clock-related examples
  EXE/                           packaged exe examples (dist files may be here)
  EXE File Creation.md           guide: how to build a Windows .exe with PyInstaller
  normalAlarm.py                 simple alarm example
  homeworkSystem.py              example CLI/GUI homework management script
  s_projects/                    small projects
    AlarmClock/                  prayer/alarm desktop app (customtkinter + pygame)
      README.md
      alarmClock.py
      azan.mp3 (audio asset)
    EmailSender/                  simple Tkinter Gmail SMTP sender
      README.md
      emailSender.py
```

## Notable projects and files
- day01–day14: Incremental exercises; example names include `numberExcercise.py`, `main.py`, `evenOdd.py`, etc. Good for following the course progression.
- practices/s_projects/AlarmClock: Desktop alarm app using `customtkinter` and `pygame`. Plays `azan.mp3` when the set time is reached.
- practices/s_projects/EmailSender: Tkinter app demonstrating sending plain-text email using Gmail SMTP and an app password.
- practices/EXE File Creation.md: Step-by-step PyInstaller guide for creating single-file Windows executables; includes notes about including data files like audio.

## How to run (quick start)
1. Clone this repo:
```bash
git clone https://github.com/mahidulhq/Python-BCC.git
cd Python-BCC
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install common dependencies used by GUI examples:
```bash
pip install customtkinter pygame pyinstaller
```
Note: Some sample scripts (like `emailSender.py`) use only the standard library and do not require extra packages.

4. Run example projects:

- Alarm Clock (source)
```bash
cd practices/s_projects/AlarmClock
python alarmClock.py
```
Make sure `azan.mp3` is in the same folder as `alarmClock.py`. The UI expects a time in `HH:MM` (24-hour) format and checks the clock every ~10 seconds.

- Email Sender
```bash
cd practices/s_projects/EmailSender
python emailSender.py
```
This sends plain-text email via Gmail SMTP you must use a Gmail account with 2-Step Verification and an App Password (do not use your normal Gmail password).

## Packaging to Windows .exe (summary)
The repository includes an EXE packaging guide in `practices/EXE File Creation.md`. The basic PyInstaller command shown there:

```bash
pyinstaller --noconsole --onefile --add-data "azan.mp3;." Azan.py
```

- `--onefile` produces a single executable.
- `--noconsole` / `--windowed` hides the console for GUI apps.
- For Windows, `--add-data "source;dest"` uses a semicolon to separate source and destination.
- If your project loads external assets, include them with `--add-data` and use a `resource_path()` helper at runtime to locate assets inside the bundled exe.

## Tips & caveats
- Alarm matching is exact to `HH:MM` and the background check runs every ~10s, so it may trigger shortly after the minute flips.
- Do not hardcode real credentials in `emailSender.py`. Use environment variables or a secrets manager for real use.
- Some GUI examples update the UI from background threads — this is acceptable for small demos but avoid for production-level apps.

## Contact / Credits
Author: mahidulhq  
Description: Completed a 14-day government-funded Python training program.