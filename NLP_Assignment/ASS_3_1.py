
import nltk
import time
import matplotlib.pyplot as plt

from nltk import CFG, PCFG
from nltk.parse import RecursiveDescentParser
from nltk.parse import EarleyChartParser
from nltk.parse import ViterbiParser

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
NP -> Pronoun
VP -> V NP
VP -> V
VP -> VP PP
PP -> P NP
Det -> 'the' | 'a'
N -> 'student' | 'form' | 'room' | 'library'
Pronoun -> 'they'
V -> 'submit' | 'submits' | 'book' | 'crashed'
P -> 'near'
""")

td_grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
NP -> Pronoun
VP -> V NP
VP -> V
VP -> V NP PP
PP -> P NP
Det -> 'the' | 'a'
N -> 'student' | 'form' | 'room' | 'library'
Pronoun -> 'they'
V -> 'submit' | 'submits' | 'book' | 'crashed'
P -> 'near'
""")

pcfg = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.7]
NP -> Pronoun [0.3]
VP -> V NP [0.6]
VP -> V [0.2]
VP -> VP PP [0.2]
PP -> P NP [1.0]
Det -> 'the' [0.7]
Det -> 'a' [0.3]
N -> 'student' [0.4]
N -> 'form' [0.2]
N -> 'room' [0.2]
N -> 'library' [0.2]
Pronoun -> 'they' [1.0]
V -> 'submit' [0.3]
V -> 'submits' [0.2]
V -> 'book' [0.3]
V -> 'crashed' [0.2]
P -> 'near' [1.0]
""")

sentences = [
    "the student submits the form",
    "the student submit the form",
    "they submit the form",
    "the student book the room",
    "the room crashed",
    "the student book the room near the library"
]

td_parser = RecursiveDescentParser(td_grammar)
earley_parser = EarleyChartParser(grammar)
viterbi_parser = ViterbiParser(pcfg)

lengths = []
states = []

for sentence in sentences:
    words = sentence.split()

    print("\nSentence:", sentence)

    start = time.time()
    td = list(td_parser.parse(words))
    td_time = time.time() - start

    start = time.time()
    ep = list(earley_parser.parse(words))
    earley_time = time.time() - start

    start = time.time()
    pp = list(viterbi_parser.parse(words))
    pcfg_time = time.time() - start

    print("Top-down parses:", len(td))
    print("Earley parses:", len(ep))
    print("PCFG parses:", len(pp))

    print("Top-down time:", round(td_time, 6))
    print("Earley time:", round(earley_time, 6))
    print("PCFG time:", round(pcfg_time, 6))

    chart = earley_parser.chart_parse(words)
    chart_states = len(chart.edges())

    print("Earley chart states:", chart_states)

    lengths.append(len(words))
    states.append(chart_states)

plt.plot(lengths, states, marker='o')
plt.xlabel("Sentence Length")
plt.ylabel("Number of Earley States")
plt.title("Sentence Length vs Earley Chart States")
plt.grid()
plt.show()
