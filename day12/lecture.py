# OOP using pyton

# # create a class-->
# class myClass:
#     x = 5
#
# # creating a object to access items from the class-->
# obj = myClass()
#
# # printing from the class
# print(obj.x)


# # makeing two classes and printing values
# # create a class-->
# class firstClass:
#     x = 5
# class secondClass:
#     y = 10
#
# # creating a object to access items from the class-->
# obj = firstClass()
# sobj = secondClass()
#
# # printing from the class
# print(obj.x)
# print(sobj.y)


# class one:
#     pass # skips error on empty class
# print()


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)
