# oop practice: Homework System

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_basic_info(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def is_adult(self):
        if self.age >= 18:
            return "Adult"
        return "Not Adult"


class Student(Person):
    def __init__(self, name, age, student_id, class_name):
        super().__init__(name, age)  # Call parent constructor
        self.student_id = student_id
        self.class_name = class_name

    def show_student_info(self):
        self.show_basic_info()  # Call parent method
        print("Student ID:", self.student_id)
        print("Class:", self.class_name)
        print("Status:", self.is_adult())
        print("------------------------")


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)  # Call parent constructor
        self.subject = subject
        self.salary = salary

    def show_teacher_info(self):
        self.show_basic_info()  # Call parent method
        print("Subject:", self.subject)
        print("Salary:", self.salary)
        print("Status:", self.is_adult())
        print("------------------------")


if __name__ == "__main__":
    student1 = Student("Rahim", 16, "S101", "Class 9")
    student2 = Student("Karim", 19, "S102", "Class 11")
    teacher1 = Teacher("Mr. Hasan", 35, "Mathematics", 45000)

    student1.show_student_info()
    student2.show_student_info()
    teacher1.show_teacher_info()
