
import re

grammar = {
    "S": [["show", "product"]],
    "product": [["me", "item"], ["item"]],
    "item": [["mobile"], ["laptop"], ["shoes"], ["watch"]]
}

def parse(query):
    words = query.lower().split()

    def match(symbol, index):
        if symbol not in grammar:
            if index < len(words) and words[index] == symbol:
                return index + 1
            return None

        for rule in grammar[symbol]:
            pos = index
            for part in rule:
                result = match(part, pos)
                if result is None:
                    break
                pos = result
            else:
                return pos
        return None

    result = match("S", 0)
    return result == len(words)

queries = [
    "show mobile",
    "show me laptop",
    "show shoes",
    "buy mobile"
]

for query in queries:
    if parse(query):
        print(query, ": Valid Query")
    else:
        print(query, ": Invalid Query")
