import pandas as pd
import yfinance as yf
import seaborn as sns
import matplotlib.pyplot as plt

# Load sentiment data
df = pd.read_csv("data/daily_sentiment.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Get date range
start_date = df['date'].min()
end_date = df['date'].max()

print("Start:", start_date)
print("End:", end_date)

# Fetch stock data (Tesla)
stock = yf.download("TSLA", start=start_date, end=end_date)
stock.columns = stock.columns.get_level_values(0)

# Reset index
stock.reset_index(inplace=True)

# Merge data
merged = pd.merge(df, stock, left_on='date', right_on='Date', how='inner')

print("Merged shape:", merged.shape)

# Check if empty
if merged.shape[0] < 2:
    print("⚠️ Not enough data points for correlation")
else:
    # Plot
    sns.regplot(x='sentiment_score', y='Close', data=merged)
    plt.title("Sentiment vs Stock Price")
    plt.savefig("reports/sentiment_vs_stock.png")
    plt.show()

print("✅ Stock correlation analysis completed!")