import tkinter as tk
from time import strftime


def show_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, show_time)


root = tk.Tk()
root.title("Current Time App")
root.geometry("300x170")
root.resizable(False, False)

label = tk.Label(root, font=('Arial', 30), fg='blue')
label.pack(expand=True)

# Developer name footer
dev_label = tk.Label(
    root,
    text="Developer: @mahidulhq",
    font=('Arial', 9),
    fg='gray'
)
dev_label.pack(side='bottom', pady=5)

show_time()
root.mainloop()
