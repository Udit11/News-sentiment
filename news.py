import requests

def fetch_news(query: str, api_key: str, max_articles=5):
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&pageSize={max_articles}&sortBy=publishedAt&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])
    return [
        {
            "title": article["title"],
            "description": article.get("description", ""),
            "url": article.get("url")
        } for article in articles
    ]
