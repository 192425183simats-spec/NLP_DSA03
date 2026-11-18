import nltk
from nltk.tag import UnigramTagger
from nltk.corpus import brown

nltk.download('brown')
nltk.download('punkt_tab')

train_data = brown.tagged_sents()[:500]

tagger = UnigramTagger(train_data)

words = ["The", "boy", "plays", "football"]

print("POS Tags:", tagger.tag(words))
