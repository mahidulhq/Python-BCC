# EXE File Creation Guide

This document explains how to package a Python project into a Windows `.exe` file using PyInstaller.

## Prerequisites

- Python installed on your system
- Your project files ready
- `pyinstaller` installed

## Step 1: Open Command Prompt and go to the project folder

In Command Prompt, move to the folder where your Python project is located.

```bat
F:
cd path\to\your\project
```

## Step 2: Install PyInstaller

Install PyInstaller using pip:

```bash
python -m pip install pyinstaller
```

If your project uses extra packages, install them too:

```bash
pip install customtkinter pygame pyinstaller
```

## Step 3: Build the EXE

For a normal Python script:

```bash
python -m PyInstaller --onefile --windowed main.py
```

### What the options mean

- `--onefile` creates a single executable file
- `--windowed` hides the console window for GUI apps
- `main.py` is the entry script you want to package

## Example for the Alarm App

If your project uses an audio file such as `azan.mp3`, use this command:

```bash
pyinstaller --noconsole --onefile --add-data "azan.mp3;." Azan.py
```

### What this command does

- `--noconsole` hides the terminal window
- `--onefile` builds a single `.exe`
- `--add-data "azan.mp3;."` includes the MP3 file inside the build
- `Azan.py` is the main script

## Important Notes

- Keep the audio file in the same folder as the Python script while testing.
- On Windows, `--add-data` uses a semicolon (`;`) between source and destination.
- If your script loads external files, you may need a helper like `resource_path()` to find them inside the EXE.
- Make sure the main script name in the command matches your real file name.

## Output Files

PyInstaller usually creates:

- `build/` folder
- `dist/` folder
- `.spec` file

The final executable will be inside the `dist/` folder.

## Troubleshooting

- If the EXE does not open, check whether all required dependencies are installed.
- If an asset file is missing, confirm it was added with `--add-data`.
- If you see path errors after packaging, use a resource helper function to load files correctly.

## Summary

To package a Python GUI app into an EXE:

1. Install PyInstaller
2. Run the build command
3. Include any extra files your app needs
4. Use the `.exe` file from the `dist/` folder
