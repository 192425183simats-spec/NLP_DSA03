words = ["create", "creates", "creating"]

data = {
    "create": {
        "suffix": "None",
        "root": "create",
        "category": "Base Form",
        "normalized": "create"
    },
    "creates": {
        "suffix": "-s",
        "root": "create",
        "category": "Third Person Singular Present",
        "normalized": "create"
    },
    "creating": {
        "suffix": "-ing",
        "root": "create",
        "category": "Present Participle",
        "normalized": "create"
    }
}

print("INFLECTIONAL NORMALIZATION REPORT")
print("-" * 75)

for word in words:
    d = data[word]
    print("Original Word:", word)
    print("Identified Suffix:", d["suffix"])
    print("Grammatical Category:", d["category"])
    print("Extracted Root:", d["root"])
    print("Normalized Form:", d["normalized"])
    print("-" * 75)
