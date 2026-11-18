def plural(noun):
    if noun.endswith(('s', 'x', 'ch', 'sh')):
        return noun + "es"
    elif noun.endswith('y'):
        return noun[:-1] + "ies"
    else:
        return noun + "s"

words = ["cat", "box", "baby", "bus", "watch"]

for word in words:
    print(word, "->", plural(word))
