from nltk.tag import DefaultTagger, RegexpTagger, SequentialBackoffTagger

default_tagger = DefaultTagger('NN')

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD')
]

rule_tagger = RegexpTagger(patterns, backoff=default_tagger)

words = ["playing", "walked", "student", "running"]

print("Tagged Words:", rule_tagger.tag(words))
