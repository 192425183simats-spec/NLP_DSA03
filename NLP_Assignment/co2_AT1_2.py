
words = ["unhappy", "happiness", "happily"]

rules = {
    "unhappy": ("un-", "happy", "-", "Derivational"),
    "happiness": ("-", "happy", "-ness", "Derivational"),
    "happily": ("-", "happy", "-ly", "Derivational")
}

print(f"{'Word':<15}{'Prefix':<10}{'Base':<10}{'Suffix':<10}{'Type':<15}{'Root'}")

for word in words:
    prefix, base, suffix, kind = rules[word]
    print(f"{word:<15}{prefix:<10}{base:<10}{suffix:<10}{kind:<15}{base}")
