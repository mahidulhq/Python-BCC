def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if b == 0:
        return "cannot divide by zero"
    return a/b

print("###############################")
print("####  A SIMPLE CALCULATOR  ####")
print("###############################")
print()
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit  Calculator")
print()
while(1):
    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exitiing Calculator")
        break
    if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5:
        a = int(input("Enter 1st number: "))
        b = int(input("Enter 2nd number: "))
        if choice == 1:
            print("ADDITION: ", add(a,b))
        if choice == 2:
            print("SUBTRACTION: ", sub(a,b))
        if choice == 3:
            print("MULTIPLICATION: ", mul(a,b))
        if choice == 4:
            print("DIVISION: ", div(a,b))
    else:
        print("WRONG CHOICE")