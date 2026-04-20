#Argument in Function
'''def greet (name):
    print(f"Hello Mr{name}. what about you? Are you interested in our product?")
a=str(input('What is your name?'))
greet(a)'''

'''def a (name,age):
    if age>=18:
        print(f"{name}, you can give a vote")
    elif age<18:
        print(f"{name}, you can not give a vote")
    else:
        print(f"{name}, please give an valid input")
b=str(input("What is your name?"))
c=int(input("enter your age"))

a(b,c)'''

#Arbitary argument
#It may help to manage wp group, like giving a greeting message just insert there name ;)
'''def greet(*name):
    for n in name:
        print(f"Hello{n}. You are most welcome in our group")
a=str(input("Please insert a name"))
a_list= a.split(',')
greet(*a_list)'''

#built in function
a=-10
print(abs(a))
import math
b=64
print(math.sqrt(b))
print(math.pow(20,2))