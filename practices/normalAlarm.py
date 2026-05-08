import pygame
import time
from datetime import datetime


def play_audio(file_path):
    """Play the alarm audio file."""
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Keep the program running until playback finishes.
    while pygame.mixer.music.get_busy():
        time.sleep(1)


def start_alarm(alarm_time, audio_file):
    """
    alarm_time: Time in "HH:MM" format, for example "17:30".
    audio_file: Audio file name or path, for example "azan.mp3".
    """
    print(f"Alarm set for: {alarm_time}")
    print("Waiting...")

    while True:
        # Get the current time in hour:minute format.
        now = datetime.now().strftime("%H:%M")

        if now == alarm_time:
            print(f"Time reached! Playing audio: {audio_file}")
            play_audio(audio_file)
            break  # Stop after the alarm plays once.

        time.sleep(10)  # Check every 10 seconds to reduce CPU usage.


# Usage:
# 1. Place the audio file in the same folder as this script.
# 2. Update the time and file name below.
target_time = "15:56"  # Set your target time in 24-hour format.
audio_path = "azan.mp3"  # Set your audio file name.

start_alarm(target_time, audio_path)