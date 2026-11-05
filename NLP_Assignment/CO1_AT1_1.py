
import re

resume = """
Name: Ravi Kumar
Email: ravi.kumar@gmail.com
Mobile: 9876543210
Skills: Python, Java, SQL, Machine Learning, NLP
Experience: 3 years
"""

name = re.search(r"Name:\s*(.+)", resume)
email = re.search(r"[\w.-]+@[\w.-]+\.\w+", resume)
mobile = re.search(r"\b[6-9]\d{9}\b", resume)
experience = re.search(r"Experience:\s*(\d+)\s*years", resume)

skills_list = ["Python", "Java", "SQL",
                "Machine Learning", "NLP"]

skills = []

for skill in skills_list:
    if re.search(r"\b" + re.escape(skill) + r"\b",
                 resume, re.IGNORECASE):
        skills.append(skill)

candidate_name = name.group(1) if name else "Not Found"
candidate_email = email.group() if email else "Not Found"
candidate_mobile = mobile.group() if mobile else "Not Found"
years = int(experience.group(1)) if experience else 0

print("Candidate Profile")
print("Name:", candidate_name)
print("Email:", candidate_email)
print("Mobile:", candidate_mobile)
print("Skills:", skills)
print("Experience:", years, "years")

if years >= 2 and "Python" in skills:
    print("Eligibility: Eligible for Shortlisting")
else:
    print("Eligibility: Not Eligible")
