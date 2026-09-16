# Task 1.1 - Python Fundamentals
# Mini Project: Student Marks Calculator

name = input("Enter student name: ")

mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))

total = mark1 + mark2 + mark3
average = total / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "D"

print("\n----- Student Result -----")
print("Name:", name)
print("Total:", total)
print("Average:", average)
print("Grade:", grade)
