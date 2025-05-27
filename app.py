from fastapi import FastAPI
from pydantic import BaseModel
from sentiment import get_sentiment
from news import fetch_news

API_KEY = "548ae23fbf734c3d87f0213e91fef25e"  # Replace with your actual key

app = FastAPI(title="AI News Sentiment Analyzer")

class Query(BaseModel):
    symbol: str

@app.post("/sentiment")
def analyze_sentiment(query: Query):
    articles = fetch_news(query.symbol, API_KEY)
    results = []
    for article in articles:
        combined_text = article["title"] + " " + article["description"]
        sentiment = get_sentiment(combined_text)
        results.append({
            "title": article["title"],
            "url": article["url"],
            **sentiment
        })
    return {"symbol": query.symbol.upper(), "results": results}
