# pip install gensim

import gensim
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK data for tokenization
nltk.download('punkt')

# Example corpus of sentences
corpus = [
    "I love programming in Python.",
    "Python programming is fun.",
    "I love coding in Python.",
    "I enjoy learning new programming languages.",
    "Natural language processing is fun."
]

# Tokenize the sentences into words
tokenized_corpus = [word_tokenize(sentence.lower()) for sentence in corpus]

# Create a Word2Vec model using the skip-gram approach
model = Word2Vec(tokenized_corpus, vector_size=50, window=5, min_count=1, sg=1)

# Train the model (this happens automatically when you initialize it with data)
model.train(tokenized_corpus, total_examples=len(tokenized_corpus), epochs=10)

# Save the model (optional)
model.save("word2vec.model")

# Find the vector for the word 'python'
vector = model.wv['python']
print("Vector for 'python':")
print(vector)

# Find words similar to 'python'
similar_words = model.wv.most_similar('python', topn=3)
print("\nWords similar to 'python':")
print(similar_words)


'''
vector_size: The number of dimensions for the word vectors (embedding size). In this case, it's set to 50.
window: The maximum distance between the current and predicted word within a sentence.
min_count: Ignores all words with total frequency lower than this.

sg: If set to 1, it uses the Skip-gram model. If set to 0, it uses CBOW.



Vector for 'python': This is the dense vector representation of the word 'python'. 
It’s a high-dimensional vector that captures semantic meaning. 
In this example, it's a 50-dimensional vector.

Similar Words: The words 'programming', 'coding', and 'fun' are most similar to 
'python' in the vector space, meaning they have similar contexts or meanings in the 
training corpus.


'''