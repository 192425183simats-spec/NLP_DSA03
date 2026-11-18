def dialog_act(sentence):
    sentence = sentence.lower()

    if any(word in sentence for word in ["hello", "hi", "hey"]):
        return "Greeting"

    elif sentence.endswith("?"):
        return "Question"

    elif any(word in sentence for word in ["thanks", "thank you"]):
        return "Thanking"

    elif any(word in sentence for word in ["bye", "goodbye"]):
        return "Farewell"

    else:
        return "Statement"

dialog = [
    "Hello",
    "How are you?",
    "Thank you",
    "Goodbye",
    "I am learning Python"
]

for sentence in dialog:
    print(sentence, "->", dialog_act(sentence))
