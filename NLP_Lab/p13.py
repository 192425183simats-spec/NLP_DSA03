import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'a' | 'the'
N -> 'boy' | 'dog'
V -> 'sees'
""")

parser = nltk.ChartParser(grammar)

sentence = "the boy sees a dog".split()

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
