# Task 1.1 - Python Fundamentals
# Topic: Conditional Statements

marks = 75

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print("Marks:", marks)
print("Grade:", grade)