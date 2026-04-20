import tkinter as tk
from time import strftime

def show_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, show_time)

root = tk.Tk()
root.title("Current Time App")
root.geometry("300x200")
root.resizable(False, False)

label = tk.Label(root, font=('Arial', 30), fg='blue')
label.pack(pady=20)

start_btn = tk.Button(root, text="Show Clock", font=("Arial", 14), command=show_time)
start_btn.pack()

root.mainloop()