import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define a simple CFG for syntactic parsing
grammar = CFG.fromstring("""
  S -> NP VP
  VP -> V NP
  NP -> Det N
  V -> "saw" | "ate"
  Det -> "a" | "an"
  N -> "dog" | "cat"
""")

# Initialize a parser
parser = ChartParser(grammar)

# Sample sentence for syntactic analysis
sentence = "a dog saw a cat".split()

# Parse the sentence
print("Syntactic Analysis - Parse Tree:")
for tree in parser.parse(sentence):
    tree.pretty_print()
