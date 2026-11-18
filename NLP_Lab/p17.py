from nltk.corpus import wordnet
import nltk

nltk.download('wordnet')

word = "computer"

synsets = wordnet.synsets(word)

for syn in synsets:
    print("Synset:", syn.name())
    print("Meaning:", syn.definition())
    print("Examples:", syn.examples())
    print()
