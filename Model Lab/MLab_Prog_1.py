
import re

text = """
Job ID: JOB123
Salary: 5 LPA - 8 LPA
Experience: 2 years
Email: hr@gmail.com
Deadline: 30-12-2026
"""

patterns = {
    "Job ID": r'JOB\d+',
    "Salary": r'\d+\s*LPA\s*-\s*\d+\s*LPA',
    "Experience": r'\d+\s*years?',
    "Email": r'[\w.-]+@[\w.-]+\.\w+',
    "Deadline": r'\d{2}-\d{2}-\d{4}'
}

for category, pattern in patterns.items():
    result = re.findall(pattern, text)
    print(category, ":", result if result else "Not Available")
