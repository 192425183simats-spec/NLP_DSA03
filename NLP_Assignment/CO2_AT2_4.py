words = ["activate", "activation", "reactivation"]

data = {
    "activate": {
        "prefix": "None",
        "root": "active",
        "suffix": "-ate",
        "sequence": "Active + ate",
        "meaning": "To make something active",
        "normalized": "activate"
    },
    "activation": {
        "prefix": "None",
        "root": "active",
        "suffix": "-ation",
        "sequence": "Active + ate + ion",
        "meaning": "Process of becoming active",
        "normalized": "activate"
    },
    "reactivation": {
        "prefix": "re-",
        "root": "active",
        "suffix": "-ation",
        "sequence": "Re + Active + ate + ion",
        "meaning": "Process of making active again",
        "normalized": "activate"
    }
}

print("MORPHOLOGICAL PARSING REPORT")
print("-" * 75)

for word in words:
    d = data[word]
    print("Original Word:", word)
    print("Prefix:", d["prefix"])
    print("Root:", d["root"])
    print("Suffix:", d["suffix"])
    print("Derivational Sequence:", d["sequence"])
    print("Semantic Meaning:", d["meaning"])
    print("Normalized Form:", d["normalized"])
    print("-" * 75)
