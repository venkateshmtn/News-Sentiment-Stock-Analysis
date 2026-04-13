import pandas as pd

# Load data
df = pd.read_csv("data/final_news.csv")

# Convert date column
df['publishedAt'] = pd.to_datetime(df['publishedAt'])

# Extract date only
df['date'] = df['publishedAt'].dt.date

# Convert sentiment to score
def sentiment_to_score(label):
    if label == "Positive":
        return 1
    elif label == "Negative":
        return -1
    else:
        return 0

df['sentiment_score'] = df['sentiment'].apply(sentiment_to_score)

# Group by date
daily_sentiment = df.groupby('date')['sentiment_score'].mean().reset_index()

print(daily_sentiment.head())

# Save
daily_sentiment.to_csv("data/daily_sentiment.csv", index=False)

print("✅ Aggregation completed!")