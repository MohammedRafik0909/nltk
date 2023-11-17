import spacy
import nltk
nltk.download('punkt')
import re
def pos_tagging(text):
    patterns = [
        (r'\b(?:The|the)\b','DET'),
        (r'\b(?:Cat|Dog)\b','NOUN'),
        (r'\b(?:is|am|are)\b','VERB'),
        (r'\b(?:quickly|brightly)\b','ADV'),
        #(r'\b(?:[A-Za-z]+)\b','NOUN')
    ]
    for pattern ,pos_tag in patterns:
        text = re.sub(pattern,pos_tag,text)
    return text

input_text = "The Cat is running quickly and the Dog is brightly chasing it"

tagged_text = pos_tagging(input_text)
print(tagged_text)

