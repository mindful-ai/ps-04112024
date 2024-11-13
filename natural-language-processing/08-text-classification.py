import nltk
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# Download NLTK data
nltk.download('movie_reviews')
nltk.download('stopwords')

# Load the movie review data (positive and negative reviews)
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

# Shuffle the dataset for randomness
import random
random.shuffle(documents)

# Preprocessing function: joins words into a string for text classification
def preprocess_data(documents):
    return [" ".join(doc) for doc, _ in documents], [category for _, category in documents]

# Prepare the data
text_data, labels = preprocess_data(documents)

# Convert text to features using Bag of Words model (CountVectorizer)
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(text_data)
y = labels

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a classifier (Naive Bayes classifier)
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Classification Report:\n", classification_report(y_test, y_pred))
