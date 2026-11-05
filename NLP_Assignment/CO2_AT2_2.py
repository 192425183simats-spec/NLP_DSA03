words = ["disagree", "agreement", "agreeable"]

data = {
    "disagree": {
        "prefix": "dis-",
        "root": "agree",
        "suffix": "None",
        "type": "Derivational Prefix",
        "meaning": "Opposite of agreeing",
        "normalized": "agree"
    },
    "agreement": {
        "prefix": "None",
        "root": "agree",
        "suffix": "-ment",
        "type": "Derivational Suffix",
        "meaning": "State or result of agreeing",
        "normalized": "agree"
    },
    "agreeable": {
        "prefix": "None",
        "root": "agree",
        "suffix": "-able",
        "type": "Derivational Suffix",
        "meaning": "Capable of being agreed with or pleasant",
        "normalized": "agree"
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
    print("Transformation:", d["type"])
    print("Semantic Meaning:", d["meaning"])
    print("Normalized Form:", d["normalized"])
    print("-" * 75)
