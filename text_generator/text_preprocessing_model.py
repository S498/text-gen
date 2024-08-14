import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def preprocess_text(text):
    tokens = word_tokenize(text)
    cleaned_text = " ".join(tokens)
    return cleaned_text
