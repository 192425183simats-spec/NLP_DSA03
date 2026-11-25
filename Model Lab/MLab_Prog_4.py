
import spacy

nlp = spacy.load("en_core_web_sm")

text = """
Apple announced a new investment in India on
25 November 2026. CEO Tim Cook met financial
experts in New York. Goldman Sachs supported
the investment.
"""

doc = nlp(text)

entities = {}

for ent in doc.ents:
    entity_type = ent.label_

    entities.setdefault(entity_type, []).append({
        "Entity": ent.text,
        "Start": ent.start_char,
        "End": ent.end_char
    })

for category, values in entities.items():
    print("\nCategory:", category)
    for item in values:
        print(item)
