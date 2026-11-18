import nltk
from nltk.tokenize import word_tokenize

nltk.download('averaged_perceptron_tagger_eng')
nltk.download('punkt_tab')

text = "The student reads a book"

words = word_tokenize(text)

tags = nltk.pos_tag(words)

print("POS Tags:")
print(tags)
