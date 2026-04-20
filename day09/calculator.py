import tkinter as tk

# Initialize main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("360x480")
root.resizable(False, False)
root.iconbitmap("D:\mahidul\pycharm\day08\icon.ico")

# Global expression
expression = ""
equation = tk.StringVar()

# Functions
def press(key):
    global expression
    expression += str(key)
    equation.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

# Entry (display screen)
entry = tk.Entry(root, textvariable=equation, font=("Arial", 20),
                 bd=10, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

# Create number and operator buttons
for i, row in enumerate(buttons):
    for j, btn in enumerate(row):
        if btn == "=":
            action = equalpress
        else:
            action = lambda x=btn: press(x)

        tk.Button(root, text=btn, width=5, height=2, font=("Arial", 14),
                  command=action).grid(row=i+1, column=j, padx=5, pady=5)

# Clear button (spans full width)
tk.Button(root, text="AC", width=22, height=2,fg="Red", font=("Arial", 14),
          command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# Run application
root.mainloop()