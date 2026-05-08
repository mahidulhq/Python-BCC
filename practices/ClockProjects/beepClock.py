import tkinter as tk
from time import strftime
import winsound


def show_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)

    # Play a beep at the start of every minute.
    if strftime('%S') == "00":
        winsound.Beep(1000, 300)

    label.after(1000, show_time)


root = tk.Tk()
root.title("Current Time App")
root.geometry("300x200")
root.resizable(False, False)

label = tk.Label(root, font=('Arial', 30), fg='blue')
label.pack(expand=True)

b1 = tk.Button(root, text="Show Clock", command=show_time)
b1.pack()

root.mainloop()
