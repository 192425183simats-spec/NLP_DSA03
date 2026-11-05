words = ["govern", "government", "governance"]

data = {
    "govern": {
        "root": "govern",
        "affix": "None",
        "level": "Base Form",
        "normalized": "govern"
    },
    "government": {
        "root": "govern",
        "affix": "-ment",
        "level": "First Derivational Level",
        "normalized": "govern"
    },
    "governance": {
        "root": "govern",
        "affix": "-ance",
        "level": "First Derivational Level",
        "normalized": "govern"
    }
}

print("MORPHOLOGICAL NORMALIZATION REPORT")
print("-" * 75)

for word in words:
    d = data[word]
    print("Original Word:", word)
    print("Root Word:", d["root"])
    print("Affix:", d["affix"])
    print("Derivational Level:", d["level"])
    print("Normalized Form:", d["normalized"])
    print("-" * 75)
