# printing row
# outer loop --> row
# inner loop --> column
# for i in range(4):
#     for i in range(3):
#         print(i, end=" ")
#     print()

# printing specific output:
# *
# * *
# * * *
# * * * *
# for i in range(4):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# same statemnet but with user inout
# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# printing on this format:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# for i in range(4):
#     for j in range(i+1):
#         print(j+1, end=" ")
#     print()
#
# or
# for i in range(4):
#     for j in range(1,i+2):
#         print(j, end=" ")
#     print()

# printing user input number reverse way like 10 9 8 7 6 5 4 3 2 1
# n = int(input("Enter a number: "))
# for i in range(n, 0,-1): # decrement --> -1 and increment --> 1
#     print(i)

# printing even number in reverse
# n = int(input("Enter a number: "))
# for i in range(n, 0, -2): # decrement --> -1 and increment --> 1
#     print(i)


# printing this:
# * * * *
# * * *
# * *
# *
# n = int(input("Enter a number: "))
# for i in range(n,0,-1):
#     for j in range(i): # this works too --> range(i,0,-1)
#         print("*", end=" ")
#     print()
#

# printing this:
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# n = int(input("Enter a number: "))
# for i in range(n,0,-1):
#     for j in range(i): # this works too --> range(i,0,-1)
#         print(i, end=" ")
#     print()


# printing this:
# 1 2 3 4
# 1 2 3
# 1 2
# 1
# n = int(input("Enter a number: "))
# for i in range(n,0,-1):
#     for j in range(i): # this works too --> range(i,0,-1)
#         print(j+1, end=" ")
#     print()

# printing this:
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# n = int(input("Enter a number: "))
# for i in range(n, 0, -1):
#     for j in range(i, 0, -1):
#         print(j, end=" ")
#     print()

# printing this:
# * * * *
#   * * *
#     * *
#       *
# for i in range(3 ,0,-1):
#     for k in range(3-i):
#         print(" ", end=" ")
#
#     for j in range(i,0,-1):
#         print("*", end=" ")
#     print()

# printing :
# 3 3 3
#   2 2
#     1
# for i in range(3 ,0,-1):
#     for k in range(3-i):
#         print(" ", end=" ")
#
#     for j in range(i,0,-1):
#         print(i, end=" ")
#     print()

# printing this:
# 4
# 4 3
# 4 3 2
# 4 3 2 1

for i in range(4, 0, -1):
    for j in range(4, i-1, -1): # range(4, 4-i, -1) works too
        print(j, end=" ")
    print()