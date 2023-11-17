from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

nltk.download('wordnet')
nltk.download('words')
nltk.download('stopwords')
#nltk.download('maxent_ne_chunker')

text = "you must be take care while crossing road and also look up the magic"

port = PorterStemmer()
words = word_tokenize(text)
print("Original words:", words)

stem1 = [port.stem(word) for word in words]
print("Stemmed words:", stem1)
 
