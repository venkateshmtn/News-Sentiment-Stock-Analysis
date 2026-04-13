import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 News Sentiment vs Stock Analysis")

# Load data
df = pd.read_csv("data/final_news.csv")

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df.head())

# Sentiment count
st.subheader("Sentiment Distribution")
sentiment_counts = df['sentiment'].value_counts()
st.bar_chart(sentiment_counts)

# Load aggregated data
daily = pd.read_csv("data/daily_sentiment.csv")

# Load stock data (merged already logic reused)
import yfinance as yf

daily['date'] = pd.to_datetime(daily['date'])
start = daily['date'].min()
end = daily['date'].max()

stock = yf.download("TSLA", start=start, end=end)
stock.columns = stock.columns.get_level_values(0)
stock.reset_index(inplace=True)

merged = pd.merge(daily, stock, left_on='date', right_on='Date', how='inner')

# Plot
st.subheader("Sentiment vs Stock Price")

fig, ax = plt.subplots()
sns.regplot(x='sentiment_score', y='Close', data=merged, ax=ax)

st.pyplot(fig)