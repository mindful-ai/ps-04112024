from sklearn.feature_extraction.text import TfidfVectorizer

# Define the same example documents
documents = ["I love programming in Python.", "Python programming is fun.", "I love coding in Python."]

# Create a TfidfVectorizer object
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the documents to get the TF-IDF matrix
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# Get the vocabulary (unique words)
tfidf_vocabulary = tfidf_vectorizer.get_feature_names_out()

# Convert the TF-IDF matrix to an array to view the word scores
tfidf_array = tfidf_matrix.toarray()

print("TF-IDF Vocabulary:", tfidf_vocabulary)
print("TF-IDF Matrix:\n", tfidf_array)
