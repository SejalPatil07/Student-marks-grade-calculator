from student import get_student_details
from marks import calculate_marks
from grade import calculate_grade
from validation import validate_marks

print("cSTUDENT MARKS & GRADE CALCULATOR")

name = get_student_details()

# Changed float() to int()
maths = int(input("Enter Maths marks: "))
python = int(input("Enter Python marks: "))
english = int(input("Enter English marks: "))

if not validate_marks(maths) or not validate_marks(python) or not validate_marks(english):
    print("Invalid marks! Please enter marks between 0 and 100.")
    exit()

total, percentage = calculate_marks(maths, python, english)
grade = calculate_grade(percentage)

print("\n------- STUDENT RESULT -------")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)