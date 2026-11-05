def search_documents(query, documents):

    query_words = set(normalize_text(query))

    results = []

    for document in documents:

        document_words = set(
            normalize_text(document)
        )

        if query_words.issubset(document_words):
            results.append(document)

    return results


query = "treated"

search_results = search_documents(
    query, clinical_text
)

print("Search Results:")

for result in search_results:
    print(result)
