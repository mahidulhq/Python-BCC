# loop
# write --> user input n then loop then result the full summation
from email.contentmanager import raw_data_manager
from tkinter.constants import BROWSE

# usr input --> sum all --> print
# n = int(input("Enter a number: ")) # taking user input
# sum = 0
# for i in range(1,n+1): # range works as range(start, stop); on i the value set to 1;
#     # the sum set to 0 before, so now sum = 0 + 1;
#     sum += i
#     # after first action the loop continues
# print(sum)

# with proper formating
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
#
#     if i < n:
#         print(i, end=" + ")
#     else:
#         print(i, end=" ")
# print("=", sum)

# witout using ">"
# n = int(input("Enter a number: "))
# sum = 0
# for i in range(1,n+1):
#     sum += i
#     print(i, end=" ")
#     if i != n:
#         print("+", end=" ")
# print("=", sum)


# now, 1....n porjonto all odd number summation
# n = int(input("Enter a number: "))
# sum = 0
#
# for i in range(1, n+1,2):
#     print(i, end=" ")
#     if i < n:
#         print("+", end=" ")
#     sum += i
# print("=", sum)


# # 1---n result shows multiplication
# n = int(input("Enter a number: "))
# multi = 1
# for i in range(1,n+1):
#     multi = multi * i
#
#     if i < n:
#         print(i, end=" * ")
#     else:
#         print(i, end=" ")
# print("=", multi)




#2D
# 1 loop  mane raw(->) --> outer loop
# 2 loop coloum(^) --> inner loop
# for i in range(5)
#     for i in range(5)

# for i in range(4):
#     print("")
#     for i in range(3):
#         print("*", end=" ")

# or
for i in range(4):
    for i in range(3):
        print("*", end=" ")
    print("")