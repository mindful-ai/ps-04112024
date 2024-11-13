from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')

# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Sample text for pragmatic analysis (sentiment analysis)
text = "I just love getting stuck in traffic on my way to work. It's the best part of my day!"

# Analyze sentiment
sentiment = sid.polarity_scores(text)

print("Pragmatic Analysis - Sentiment Analysis (Understanding Context):")
print(sentiment)
