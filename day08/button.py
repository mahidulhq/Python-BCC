from tkinter import *

parent = Tk()
parent.title("Amar Application")
parent.geometry("300x300")
parent.resizable(False, False)

redbutton = Button(parent, text="Red", fg="red")
redbutton.pack(side=LEFT)

blackbutton = Button(parent, text="Black", fg="black")
blackbutton.pack(side=RIGHT)

bluebutton = Button(parent, text="Blue", fg="blue")
bluebutton.pack(side=TOP)

greenbutton = Button(parent, text="Green", fg="green")
greenbutton.pack(side=BOTTOM)

parent.mainloop()