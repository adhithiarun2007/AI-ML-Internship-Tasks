# Task 1.1 - Python Fundamentals
# Topic: Object-Oriented Programming

class Student:

    def __init__(self, name, course, year):
        self.name = name
        self.course = course
        self.year = year

    def display_details(self):
        print("Name:", self.name)
        print("Course:", self.course)
        print("Year:", self.year)


student1 = Student(
    "Adhithi",
    "AI & Data Science",
    3
)

student1.display_details()