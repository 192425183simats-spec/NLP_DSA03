import nltk

grammar = nltk.CFG.fromstring("""
S -> Singular | Plural
Singular -> SG_N SG_V
Plural -> PL_N PL_V
SG_N -> 'boy' | 'girl'
PL_N -> 'boys' | 'girls'
SG_V -> 'plays'
PL_V -> 'play'
""")

parser = nltk.ChartParser(grammar)

sentences = [
    "boy plays",
    "boys play",
    "boy play",
    "girls plays"
]

for sentence in sentences:
    words = sentence.split()
    result = list(parser.parse(words))

    if result:
        print(sentence, "-> Correct Agreement")
    else:
        print(sentence, "-> Incorrect Agreement")
