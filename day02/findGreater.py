a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# on python "else" is "elif"
# after loop condition we have to use :

if (a > b and a > c):
    print("The number", a, " is greater than others")
elif (b > a and b > c):
    print("The number", b, " is greater than others")
elif (c > a and c > b):
    print("The number", c, " is greater than others")

