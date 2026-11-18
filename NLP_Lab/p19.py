import nltk
from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

nltk.download('wordnet')
nltk.download('punkt_tab')

sentence = "I went to the bank to deposit money"

words = word_tokenize(sentence)

sense = lesk(words, 'bank')

print("Word: bank")

if sense:
    print("Meaning:", sense.definition())
else:
    print("No meaning found")
