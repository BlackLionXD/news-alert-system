


from news_fetcher import fetch_marketaux_news, filter_news_by_keywords_structured

# Fetch 10 articles
news_json = fetch_marketaux_news(symbols="EURUSD,USDJPY,GBPUSD", limit=10, page=1)

# Filter by Forex keywords
keywords = ["forex", "USD", "EUR", "trading", "market"]
filtered_json = filter_news_by_keywords_structured(news_json, keywords)

import json
print(json.dumps(filtered_json, indent=4))
