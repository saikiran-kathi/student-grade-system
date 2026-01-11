# Student Grade System

print("Student Grade System")

name = input("Enter student name: ")
marks = float(input("Enter marks (0 - 100): "))

if marks >= 75:
    grade = "Distinction"
    result = "Pass"
elif marks >= 60:
    grade = "First Class"
    result = "Pass"
elif marks >= 50:
    grade = "Second Class"
    result = "Pass"
elif marks >= 35:
    grade = "Pass Class"
    result = "Pass"
else:
    grade = "Fail"
    result = "Fail"

print("\n--- Result ---")
print("Student Name :", name)
print("Marks        :", marks)
print("Grade        :", grade)
print("Result       :", result)
