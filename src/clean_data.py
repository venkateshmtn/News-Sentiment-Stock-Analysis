import pandas as pd

# Load data
df = pd.read_csv("data/news.csv")

print("Before cleaning:", df.shape)

# Remove null values
df = df.dropna(subset=['title', 'description'])

# Combine title + description
df['content'] = df['title'] + " " + df['description']

# Convert to lowercase
df['content'] = df['content'].str.lower()

# Remove duplicates
df = df.drop_duplicates(subset=['content'])

print("After cleaning:", df.shape)

# Save cleaned data
df.to_csv("data/cleaned_news.csv", index=False)

print("✅ Data cleaned and saved!")