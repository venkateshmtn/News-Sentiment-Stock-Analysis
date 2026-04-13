
import requests
import pandas as pd

API_KEY = "d66ea308e7534aae823bcf2cf384dca0"

url = f"https://newsapi.org/v2/everything?q=tesla&language=en&pageSize=100&apiKey={API_KEY}"

response = requests.get(url)

print("Status Code:", response.status_code)

data = response.json()
print("Response keys:", data.keys())

if 'articles' not in data:
    print("❌ No articles found. Check API key or limit.")
else:
    articles = data['articles']
    print("Total articles:", len(articles))

    news_data = []

    for article in articles:
        news_data.append({
            "title": article.get('title'),
            "description": article.get('description'),
            "publishedAt": article.get('publishedAt'),
            "source": article.get('source', {}).get('name')
        })

    df = pd.DataFrame(news_data)

    print("DataFrame shape:", df.shape)

    df.to_csv("data/news.csv", index=False)

    print("✅ News data saved!")