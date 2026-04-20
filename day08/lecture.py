# # learing how to make gui --> tkinter
# import tkinter as tk # header
#
# root = tk.Tk() # makes the window
# root.title("Amar Application") # title of the window
# root.geometry("300x300") # window size
# root.resizable(False, False)
#
# root.mainloop() # runs the whole tkinter gui code/ runs the loop to keep the window open



from tkinter import *
import tkinter as tk
parent = tk.Tk()
parent.title("Current Time App")
parent.geometry("300x150")
parent.resizable(False, False)

name = Label(parent,text = "Name").grid(row = 0, column = 0)
e1 = Entry(parent).grid(row = 0, column = 1)
password = Label(parent,text = "Password").grid(row = 1, column = 0)
e2 = Entry(parent).grid(row = 1, column = 1)
submit = Button(parent,
                text = "Submit",
                fg="white",
                bg="black"
                ).grid(row = 4, column = 0)
parent.mainloop()