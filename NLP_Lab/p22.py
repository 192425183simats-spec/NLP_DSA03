import nltk

text = "Ravi is a student. He studies Python. He likes programming."

sentences = nltk.sent_tokenize(text)

previous_name = None

for sentence in sentences:
    words = nltk.word_tokenize(sentence)

    for word in words:
        if word == "Ravi":
            previous_name = word
        elif word in ["He", "he"]:
            print(word, "refers to", previous_name)
