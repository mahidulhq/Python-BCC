# Prayer Alarm Tool

A simple desktop alarm app built with Python using `customtkinter` and `pygame`. It lets you set a time in `HH:MM` format and plays an audio file when the current time matches the target time.

## How It Works

1. The app opens a dark-themed Tkinter-based window.
2. You enter a prayer/alarm time in 24-hour format, such as `18:30`.
3. When you click **Set Alarm**, the app starts a background thread.
4. That thread checks the current time every 10 seconds.
5. When the current time matches the selected time, the app loads and plays `azan.mp3`.

## Features

- Clean desktop GUI using `customtkinter`
- Background time checking with threading
- Audio playback using `pygame`
- Works both from source and from a bundled EXE

## Requirements

- Python 3.10+ recommended
- `customtkinter`
- `pygame`

## Install Dependencies

```bash
pip install customtkinter pygame
```

## Project Files

- `alarmClock.py`: Main application file
- `azan.mp3`: Alarm sound file required by the app

## Run the App

```bash
python alarmClock.py
```

## Usage

1. Open the app.
2. Enter the target time in `HH:MM` format.
3. Click **অ্যালার্ম সেট করুন** / **Set Alarm**.
4. Keep the app open until the selected time is reached.
5. When the time matches, the audio file starts playing.

## Audio File Setup

The app looks for an audio file named `azan.mp3`.

- When running from source, place `azan.mp3` in the same folder as `alarmClock.py`.
- When running as a bundled EXE, the `resource_path()` helper locates the file inside the packaged app.

## Important Notes

- Time must match exactly in `HH:MM` format.
- The app checks every 10 seconds, so the alarm may trigger slightly after the exact minute changes.
- If `azan.mp3` is missing, playback will fail.
- The GUI updates from a background thread, which is fine for this small project but not ideal for larger apps.

## Troubleshooting

- If the alarm does not play, confirm that `azan.mp3` exists and is named correctly.
- Make sure the entered time uses 24-hour format.
- If `pygame` fails to initialize audio, check your system sound settings.
