import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')

text = "The boys are playing football"

words = word_tokenize(text)
lemmatizer = WordNetLemmatizer()

for word in words:
    print(word, ":", lemmatizer.lemmatize(word))
