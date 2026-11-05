
words = ["connected", "connecting", "connection"]

rules = {
    "connected": ("connect", "-ed", "Inflectional"),
    "connecting": ("connect", "-ing", "Inflectional"),
    "connection": ("connect", "-ion", "Derivational")
}

print(f"{'Word':<15}{'Root':<12}{'Suffix':<10}{'Type':<15}{'Normalized'}")

for word in words:
    root, suffix, kind = rules[word]
    print(f"{word:<15}{root:<12}{suffix:<10}{kind:<15}{root}")
