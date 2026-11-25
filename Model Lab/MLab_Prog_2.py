
from collections import Counter

reviews = [
    "The product is very good",
    "The product is very useful",
    "Very good product and good quality"
]

words = " ".join(reviews).lower().split()

def generate_ngrams(words, n):
    return [" ".join(words[i:i+n])
            for i in range(len(words)-n+1)]

for n in range(1, 4):
    ngrams = generate_ngrams(words, n)
    print("\n", n, "- Grams:")
    print(Counter(ngrams).most_common(5))
