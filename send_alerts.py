import schedule
import time
from firebase_db import get_all_subscribers
from news_fetcher import fetch_marketaux_news, filter_news_by_keywords, format_news_payload
from email_sender import send_email

def send_daily_alerts():
    subscribers = get_all_subscribers()
    print(f"Found {len(subscribers)} subscribers.")

    if not subscribers:
        print("No subscribers found. Skipping sending emails.")
        return

    # Fetch news once
    news = fetch_marketaux_news(limit=20)

    # Send personalized email to each subscriber
    for sub in subscribers:
        user_keywords = sub.get("keywords", [])
        if not user_keywords:
            continue  # skip if no keywords selected

        filtered = filter_news_by_keywords(news.get("data", []), user_keywords)
        payload = format_news_payload(filtered)

        if payload.get("data"):
            send_email(sub["email"], "Your Daily Market News Update", payload["data"])
            print(f"Sent email to {sub['email']}")
        else:
            print(f"No news for {sub['email']}")

# Schedule the task to run every day at 08:00 AM
# schedule.every().day.at("08:00").do(send_daily_alerts)

# if __name__ == "__main__":
#     print("Scheduler started. Press Ctrl+C to stop.")
#     while True:
#         schedule.run_pending()
#         time.sleep(60)


if __name__ == "__main__":
    send_daily_alerts()