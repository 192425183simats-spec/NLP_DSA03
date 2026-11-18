import nltk

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*s$', 'NNS'),
    (r'.*', 'NN')
]

tagger = nltk.RegexpTagger(patterns)

words = ["playing", "walked", "quickly", "books", "student"]

print("POS Tags:", tagger.tag(words))
