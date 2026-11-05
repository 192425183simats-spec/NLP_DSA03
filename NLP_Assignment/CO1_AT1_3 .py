
import re

student = {
    "Register Number": "22CS101",
    "Email": "22cs101@university.edu",
    "Course Code": "CS101",
    "Semester": "5",
    "Mobile": "9876543210"
}

patterns = {
    "Register Number": r"^\d{2}[A-Z]{2}\d{3}$",
    "Email": r"^[\w.-]+@university\.edu$",
    "Course Code": r"^[A-Z]{2,4}\d{3}$",
    "Semester": r"^[1-8]$",
    "Mobile": r"^[6-9]\d{9}$"
}

valid = True

print("University Registration Validation")

for field, pattern in patterns.items():
    value = student[field]

    if re.fullmatch(pattern, value):
        print(field, ":", value, "- Valid")
    else:
        print(field, ":", value, "- Invalid")
        valid = False

print("\nFinal Registration Status")

if valid:
    print("Registration Successful")
else:
    print("Registration Failed")
