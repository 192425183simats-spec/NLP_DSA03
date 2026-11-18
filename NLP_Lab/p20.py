from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Python is a programming language",
    "Machine learning uses Python",
    "Natural language processing analyzes text"
]

query = ["Python programming"]

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(documents + query)

similarity = cosine_similarity(tfidf[-1], tfidf[:-1])

for i, score in enumerate(similarity[0]):
    print("Document", i + 1, "Score:", round(score, 3))
