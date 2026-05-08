import tkinter as tk
from time import strftime

running = False  # Tracks whether the clock is running


def show_time():
    if running:  # Update only while the clock is running
        current_time = strftime('%H:%M:%S %p')
        label.config(text=current_time)
        label.after(1000, show_time)


def start_clock():
    global running
    if not running:
        running = True
        show_time()


root = tk.Tk()
root.title("Current Time App")
root.geometry("300x200")
root.resizable(False, False)

label = tk.Label(root, font=('Arial', 30), fg='blue')
label.pack(pady=20)

start_btn = tk.Button(root, text="Show Clock", font=(
    "Arial", 14), command=start_clock)
start_btn.pack()

root.mainloop()
