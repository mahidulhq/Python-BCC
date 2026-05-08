import customtkinter as ctk
import pygame
import os
import sys
import threading
from datetime import datetime
import time

# EXE এর ভেতর থেকে ফাইল খুঁজে বের করার ফাংশন
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class PrayerAlarmApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Prayer Alarm Tool")
        self.geometry("400x300")
        ctk.set_appearance_mode("dark")

        # UI Elements
        self.label = ctk.CTkLabel(self, text="নামাজের সময় সেট করুন (HH:MM)", font=("Arial", 16))
        self.label.pack(pady=20)

        self.time_entry = ctk.CTkEntry(self, placeholder_text="যেমন: 18:30")
        self.time_entry.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="অ্যালার্ম বন্ধ আছে", text_color="yellow")
        self.status_label.pack(pady=10)

        self.start_button = ctk.CTkButton(self, text="অ্যালার্ম সেট করুন", command=self.start_thread)
        self.start_button.pack(pady=20)

        pygame.mixer.init()

    def start_thread(self):
        # ব্যাকগ্রাউন্ডে অ্যালার্ম চেক করার জন্য থ্রেডিং ব্যবহার
        t = threading.Thread(target=self.run_alarm, daemon=True)
        t.start()
        self.status_label.configure(text=f"সেট করা হয়েছে: {self.time_entry.get()}", text_color="green")

    def run_alarm(self):
        target_time = self.time_entry.get()
        audio_file = resource_path("azan.mp3") # আপনার অডিও ফাইলের নাম এখানে দিন

        while True:
            now = datetime.now().strftime("%H:%M")
            if now == target_time:
                pygame.mixer.music.load(audio_file)
                pygame.mixer.music.play()
                self.status_label.configure(text="আজান বাজছে...", text_color="red")
                break
            time.sleep(10)

if __name__ == "__main__":
    app = PrayerAlarmApp()
    app.mainloop()