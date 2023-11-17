import spacy
nlp = spacy.load('en_core_web_sm')
text = "The capital of France is Paris, and it is known for the Eiffel Tower"
doc = nlp(text)
for ent in doc.ents:
    print(f"Entity : {ent.text}, Type : {ent.label_}")
