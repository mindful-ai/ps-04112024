


import nltk
from nltk import word_tokenize, pos_tag, ne_chunk

# Download necessary NLTK datasets
nltk.download('punkt')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')

# Example sentence
sentence = "Apple Inc. is planning to open a new store in Berlin on 15th January 2025. Tim Cook, the CEO of Apple, announced it in a press conference."

# Tokenize the sentence and perform POS tagging
tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)

# Perform NER using NLTK's named entity chunker
tree = ne_chunk(tagged)

# Print the named entities
print(tree)



'''

Common NLTK POS Tags:
NN: Noun, singular or mass

Example: "dog", "computer", "idea"
NNS: Noun, plural

Example: "dogs", "computers", "ideas"
NNP: Proper noun, singular

Example: "John", "Apple", "New York"
NNPS: Proper noun, plural

Example: "Johns", "Apples", "New Yorks"
VB: Verb, base form

Example: "run", "eat", "play"
VBD: Verb, past tense

Example: "ran", "ate", "played"
VBG: Verb, gerund or present participle

Example: "running", "eating", "playing"
VBN: Verb, past participle

Example: "run", "eaten", "played"
VBP: Verb, non-3rd person singular present

Example: "run", "eat", "play"
VBZ: Verb, 3rd person singular present

Example: "runs", "eats", "plays"
JJ: Adjective

Example: "beautiful", "big", "fast"
JJR: Adjective, comparative

Example: "bigger", "faster", "more beautiful"
JJS: Adjective, superlative

Example: "biggest", "fastest", "most beautiful"
RB: Adverb

Example: "quickly", "happily", "often"
RBR: Adverb, comparative

Example: "more quickly", "better"
RBS: Adverb, superlative

Example: "most quickly", "best"
PRP: Personal pronoun

Example: "I", "you", "he"
PRP$: Possessive pronoun

Example: "my", "your", "his"
DT: Determiner

Example: "the", "a", "some"
IN: Preposition or subordinating conjunction

Example: "in", "on", "at", "with", "because"
TO: Infinitive marker

Example: "to" run, "to" eat
CC: Coordinating conjunction

Example: "and", "but", "or"
UH: Interjection

Example: "wow", "ouch", "hey"

'''