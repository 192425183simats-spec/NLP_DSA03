
words = ["played", "player", "playing"]

rules = {
    "played": ("-ed", "Inflectional", "play"),
    "player": ("-er", "Derivational", "play"),
    "playing": ("-ing", "Inflectional", "play")
}

print(f"{'Word':<12}{'Stem':<10}{'Affix':<10}{'Type':<15}{'Normalized'}")

for word in words:
    affix, kind, stem = rules[word]
    print(f"{word:<12}{stem:<10}{affix:<10}{kind:<15}{stem}")
