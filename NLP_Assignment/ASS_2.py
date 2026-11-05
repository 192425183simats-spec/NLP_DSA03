from collections import Counter

sentences = [
    "i want bus timing",
    "when is the next bus",
    "where is the bus stop",
    "i need ticket information",
    "tell me the bus fare"
]

unigram = Counter()
bigram = Counter()
trigram = Counter()
bigram_context = Counter()
trigram_context = Counter()

for sentence in sentences:
    words = ["<s>"] + sentence.split() + ["</s>"]

    unigram.update(words)

    for i in range(len(words)-1):
        bigram[(words[i], words[i+1])] += 1
        bigram_context[words[i]] += 1

    for i in range(len(words)-2):
        trigram[(words[i], words[i+1], words[i+2])] += 1
        trigram_context[(words[i], words[i+1])] += 1

V = len(unigram)

print("UNIGRAM PROBABILITIES")
for word, count in unigram.items():
    print(word, round(count / sum(unigram.values()), 3))

print("\nBIGRAM PROBABILITIES")
for pair, count in bigram.items():
    p = count / bigram_context[pair[0]]
    print(pair, round(p, 3))

print("\nTRIGRAM PROBABILITIES")
for tri, count in trigram.items():
    p = count / trigram_context[tri[:2]]
    print(tri, round(p, 3))

print("\nLAPLACE SMOOTHING")
for pair, count in bigram.items():
    p = (count + 1) / (bigram_context[pair[0]] + V)
    print(pair, round(p, 3))
