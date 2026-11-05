
import re

products = [
    "Python Programming Book",
    "Java Programming Book",
    "Python Laptop",
    "Wireless Mouse",
    "Laptop Bag",
    "Python Course",
    "SQL Database Book"
]

def search_products(keyword, search_type):
    if search_type == "exact":
        pattern = r"\b" + re.escape(keyword) + r"\b"

    elif search_type == "prefix":
        pattern = r"^" + re.escape(keyword)

    elif search_type == "suffix":
        pattern = re.escape(keyword) + r"$"

    elif search_type == "partial":
        pattern = re.escape(keyword)

    else:
        print("Invalid search type")
        return

    matches = []

    for product in products:
        if re.search(pattern, product, re.IGNORECASE):
            matches.append(product)

    print("\nSearch Type:", search_type)
    print("Keyword:", keyword)

    if matches:
        print("Matching Products:")
        for product in matches:
            print(product)
    else:
        print("No matching products found")

    print("Total Matching Products:", len(matches))


search_products("Python", "exact")
search_products("Python", "prefix")
search_products("Book", "suffix")
search_products("Laptop", "partial")
search_products("python", "partial")
