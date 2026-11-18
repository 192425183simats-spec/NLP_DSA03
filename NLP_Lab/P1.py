import re

text = "Python is easy to learn. Python is powerful."

pattern = "Python"

match = re.search(pattern, text)
print("Search Result:", match.group())

matches = re.findall(pattern, text)
print("All Matches:", matches)

result = re.sub("easy", "simple", text)
print("After Replacement:", result)
