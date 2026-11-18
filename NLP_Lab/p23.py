from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

text = [
    "Python is a programming language",
    "Python is used for software development",
    "Software development involves writing code"
]

vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(text)

scores = []

for i in range(len(text) - 1):
    score = cosine_similarity(
        vectors[i], vectors[i + 1]
    )[0][0]

    scores.append(score)

    print("Sentence Similarity:", round(score, 3))

print("Coherence Score:", round(sum(scores) / len(scores), 3))
