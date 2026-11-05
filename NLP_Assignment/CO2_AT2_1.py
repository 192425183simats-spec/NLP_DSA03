words = ["analyzing", "analysis", "analytical"]

data = {
    "analyzing": {
        "root": "analyze",
        "affix": "-ing",
        "type": "Inflectional",
        "normalized": "analyze"
    },
    "analysis": {
        "root": "analy",
        "affix": "-sis",
        "type": "Derivational",
        "normalized": "analyze"
    },
    "analytical": {
        "root": "analysis",
        "affix": "-ical",
        "type": "Derivational",
        "normalized": "analyze"
    }
}

print("MORPHOLOGICAL ANALYSIS REPORT")
print("-" * 85)

for word in words:
    d = data[word]
    print("Original Word:", word)
    print("Root Word:", d["root"])
    print("Affix:", d["affix"])
    print("Transformation:", d["type"])
    print("Normalized Form:", d["normalized"])
    print("-" * 85)
