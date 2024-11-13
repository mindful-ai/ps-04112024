import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# Example sentence
sentence = "I love programming with Python"

# Tokenize the sentence
tokens = word_tokenize(sentence)

# Create Unigrams (1-Grams)
unigrams = list(ngrams(tokens, 1))
print("Unigrams:", unigrams)

# Create Bigrams (2-Grams)
bigrams = list(ngrams(tokens, 2))
print("Bigrams:", bigrams)

# Create Trigrams (3-Grams)
trigrams = list(ngrams(tokens, 3))
print("Trigrams:", trigrams)
