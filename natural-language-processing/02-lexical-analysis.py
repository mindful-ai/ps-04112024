import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download necessary NLTK data
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Sample text for lexical analysis
text = "Apple is looking at buying U.K. startup for $1 billion"

# Tokenize the text
tokens = word_tokenize(text)

# Perform POS tagging
tagged_tokens = pos_tag(tokens)

# Display tokens and their POS tags
print("Lexical Analysis - Tokenization and POS Tagging:")
for token, tag in tagged_tokens:
    print(f"{token}: {tag}")
