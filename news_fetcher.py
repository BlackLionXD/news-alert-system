import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()
API_TOKEN = os.getenv("MARKETAUX_API_TOKEN")


def fetch_marketaux_news(symbols="EURUSD,USDJPY", limit=10, page=1):
    """
    Fetch news from Marketaux API.
    Returns JSON similar to:
    {
        "meta": {...},
        "data": [...]
    }
    """
    url = "https://api.marketaux.com/v1/news/all"
    params = {
        "api_token": API_TOKEN,
        "symbols": symbols,
        "limit": limit,
        "page": page
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        news_list = response.json().get("data", [])
        
        return {
            "meta": {
                "found": len(news_list),
                "returned": len(news_list),
                "limit": limit,
                "page": page
            },
            "data": news_list
        }

    except Exception as e:
        print("Error fetching Marketaux news:", e)
        return {
            "meta": {
                "found": 0,
                "returned": 0,
                "limit": limit,
                "page": page
            },
            "data": []
        }


# ------------------------------
# REQUIRED BY send_alerts.py
# ------------------------------

def filter_news_by_keywords(news_list, keywords):
    """
    COMPATIBLE with send_alerts.py
    Accepts a list (NOT structured JSON).
    Returns a filtered list.
    """
    filtered = []
    for article in news_list:
        title = article.get("title", "").lower()
        description = article.get("description", "").lower()

        if any(k.lower() in title or k.lower() in description for k in keywords):
            filtered.append(article)

    return filtered


def format_news_payload(filtered_articles):
    """
    COMPATIBLE with send_alerts.py
    Wraps the filtered list into JSON format:
    { "data": [...] }
    """
    return {"data": filtered_articles}


# ------------------------------
# YOUR structured version
# (optional but kept)
# ------------------------------

def filter_news_by_keywords_structured(news_json, keywords):
    """
    Filter the 'data' list in the JSON by keywords.
    Returns JSON in the same structure.
    """
    filtered = []
    for article in news_json.get("data", []):
        title = article.get("title", "").lower()
        description = article.get("description", "").lower()

        if any(k.lower() in title or k.lower() in description for k in keywords):
            filtered.append(article)

    return {
        "meta": {
            "found": len(filtered),
            "returned": len(filtered),
            "limit": news_json.get("meta", {}).get("limit", len(filtered)),
            "page": news_json.get("meta", {}).get("page", 1)
        },
        "data": filtered
    }
