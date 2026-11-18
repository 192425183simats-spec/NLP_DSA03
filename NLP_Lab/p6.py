import random

text = "I love natural language processing and I love Python"

words = text.split()

bigrams = {}

for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]
    bigrams.setdefault(word, []).append(next_word)

word = "I"
result = [word]

for i in range(8):
    if word not in bigrams:
        break
    word = random.choice(bigrams[word])
    result.append(word)

print("Generated Text:", " ".join(result))
