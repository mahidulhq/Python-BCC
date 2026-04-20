a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# per variable 4 bite memory used
c = a
a = b
b = c

print("The first number", a)
print("The second number", b)
