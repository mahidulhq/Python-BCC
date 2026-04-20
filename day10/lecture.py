# checkbox/radiobutton
# from tkinter import *
#
# # function
# def selection():
#     selection = "You selected the option " + str(radio.get())
#     label.config(text=selection)
#
# top = Tk()
# top.geometry("300x150")
# radio = IntVar()
# lbl = Label(text="Favourite programming language:")
# lbl.pack()
# R1 = Radiobutton(top, text="C",
#                  variable=radio,
#                  value=1,
#                  command=selection)
# R1.pack(anchor=W)
#
# R2 = Radiobutton(top, text="C++",
#                  variable=radio,
#                  value=2,
#                  command=selection)
# R2.pack(anchor=W)
#
# R3 = Radiobutton(top, text="Java",
#                  variable=radio,
#                  value=3,
#                  command=selection)
# R3.pack(anchor=W)
#
# label = Label(top)
# label.pack()
# top.mainloop()


# current time app
import tkinter as tk
from time import strftime

def show_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, show_time)

root = tk.Tk()
root.title("Current Time App")
root.geometry("300x150")
root.resizable(False, False)

label = tk.Label(root, font=('Century Gothic Bold', 37), fg='red', bg='black')
label.pack(expand=True)

# # adding extra infos
# dev = tk.Label(
#     root,
#     text="Developer: MD. SHOYEB AKHTER",
#     font=('Vivaldi',9),
#     fg='grey'
# )
# dev.pack(side='buttom', pady=10)

show_time()
root.mainloop()

