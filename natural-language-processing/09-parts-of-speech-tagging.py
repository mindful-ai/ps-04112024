import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Example sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Print the POS tags
print(pos_tags)
