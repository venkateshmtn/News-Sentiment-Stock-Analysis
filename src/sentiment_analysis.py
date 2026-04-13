import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

# Load data
df = pd.read_csv("data/cleaned_news.csv")

# Initialize analyzer
sia = SentimentIntensityAnalyzer()

# Function to get sentiment
def get_sentiment(text):
    score = sia.polarity_scores(str(text))['compound']
    
    if score > 0.05:
        return "Positive"
    elif score < -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment
df['sentiment'] = df['content'].apply(get_sentiment)

print(df[['content', 'sentiment']].head())

# Save result
df.to_csv("data/final_news.csv", index=False)

print("✅ Sentiment analysis completed!")