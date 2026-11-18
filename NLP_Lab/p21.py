import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'student' | 'book' | 'teacher'
V -> 'reads' | 'teaches'
""")

parser = nltk.ChartParser(grammar)

sentence = "the student reads a book".split()

for tree in parser.parse(sentence):
    print("Parse Tree:")
    print(tree)

    print("Noun Phrases:")
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            print(" ".join(subtree.leaves()))
