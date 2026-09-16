# Task 1.1 - Python Fundamentals
# Topic: File Handling

# Write data to a file
with open("student_data.txt", "w") as file:
    file.write("Name: Adhithi\n")
    file.write("Course: AI & Data Science\n")
    file.write("Year: 3\n")

print("Data written successfully.")

# Read data from the file
with open("student_data.txt", "r") as file:
    data = file.read()

print("\nFile contents:")
print(data)