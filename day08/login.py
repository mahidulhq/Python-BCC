from tkinter import *

parent = Tk()

parent.title("oi kiree >_<")
parent.geometry("300x300")
parent.resizable(False, False)

frame = Frame(parent)
frame.place(relx=0.5, rely=0.5, anchor='center')

Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
Entry(frame).grid(row=0, column=1, padx=5, pady=5)

Label(frame, text="Password").grid(row=1, column=0, padx=5, pady=5)
Entry(frame).grid(row=1, column=1, padx=5, pady=5)

Button(frame, text="Submit", fg="white", bg="black").grid(row=2, column=0, columnspan=2, pady=10)

parent.mainloop()