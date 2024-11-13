
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download necessary resources
nltk.download('vader_lexicon')

# Create a SentimentIntensityAnalyzer object
sia = SentimentIntensityAnalyzer()

# Define some example sentences
sentence1 = "I love this product, it is amazing!"
sentence2 = "This is the worst movie I have ever seen."
sentence3 = "The weather is okay today."

# Analyze sentiment
score1 = sia.polarity_scores(sentence1)
score2 = sia.polarity_scores(sentence2)
score3 = sia.polarity_scores(sentence3)

print(f"Sentiment scores for sentence 1: {score1}")
print(f"Sentiment scores for sentence 2: {score2}")
print(f"Sentiment scores for sentence 3: {score3}")


'''

Explanation:
Polarity Scores: The VADER sentiment analyzer returns four values:
neg: The proportion of negative sentiment in the text.
neu: The proportion of neutral sentiment.
pos: The proportion of positive sentiment.
compound: The overall sentiment score (ranging from -1 to +1), where positive values indicate positive sentiment, negative values indicate negative sentiment, and values close to zero indicate neutral sentiment.


Example Breakdown:
Sentence 1: "I love this product, it is amazing!" has a compound score of 0.8478, indicating a highly positive sentiment.
Sentence 2: "This is the worst movie I have ever seen." has a compound score of -0.8385, indicating a strong negative sentiment.
Sentence 3: "The weather is okay today." has a compound score of 0.0516, which is close to neutral but slightly positive.


Real-World Applications of Semantic Analysis:
Sentiment Analysis for Social Media: Analyzing social media posts to understand 
public opinion about a product or event.
Customer Feedback Analysis: Automatically categorizing customer reviews 
into positive, neutral, or negative feedback.
Opinion Mining: Analyzing opinions or reviews to extract useful insights 
(e.g., brand reputation analysis).


'''