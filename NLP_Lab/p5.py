from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "plays", "running", "happily"]

for word in words:
    print(word, "->", stemmer.stem(word))
