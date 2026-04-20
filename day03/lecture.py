# loop
# usage of continue and break

# without using continue
# for var in range(1,101):
#     if (var % 5 != 0):
#         print(var, end= " ")

# with using continue
# for var in range(1,101):
#     if (var % 5 == 0):
#         continue
#     print(var, end= " ")


# for var in range(1,101):
#     if (var % 5 != 0):
#         print(var, end=" ")
#     else:
#         print(var **2, end=" ")

# fruits = ["apple", "banana", "cherry", "dragon"]
# for x in fruits:
#     if x == "banana":
#         continue # means go back to loop and skip the one mentioned
#     print(x)

# print user inputted using loop
# a = int(input("Enter a number: "))
# for a in range(2,30,3):
#     print(a)


# using rang and take user input for start stop and step
a = int(input("Enter the number start: "))
b = int(input("Enter the number stop: "))
c = int(input("Enter the number step: "))
for i in range(a,b,c):
    # range(start, stop, step)
    # that's how range works
    print(i)