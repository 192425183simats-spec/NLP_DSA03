import nltk

grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'the' 'boy' [0.6] | 'the' 'girl' [0.4]
VP -> 'runs' [0.7] | 'walks' [0.3]
""")

parser = nltk.ViterbiParser(grammar)

sentence = "the boy runs".split()

for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())
