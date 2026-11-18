import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the'
N -> 'boy' | 'girl'
V -> 'sees'
""")

parser = nltk.EarleyChartParser(grammar)

sentence = "the boy sees the girl".split()

for tree in parser.parse(sentence):
    print(tree)
