import schedule
import time
from firebase_db import get_all_emails
from news_fetcher import fetch_marketaux_news, filter_news_by_keywords, format_news_payload
from email_sender import send_email

keywords = ["usd","forex","eur","market","jpy","trading","dollar","stocks"]

def send_daily_alerts():
    subscribers = get_all_emails()
    print(f"Found {len(subscribers)} subscribers.")

    if not subscribers:
        print("No subscribers found. Skipping sending emails.")
        return

    # Fetch news
    news = fetch_marketaux_news(limit=20)

    # Filter
    filtered = filter_news_by_keywords(news["data"], keywords)
    # Format
    payload = format_news_payload(filtered)

    # Convert to readable email text (optional, for reference)
    body = """
    <h2 style="color:#2E86C1;">Your Daily Market News Update</h2>
    """
    for article in payload["data"]:
        body += f"""
        <div style="margin-bottom: 25px; border-bottom: 1px solid #ddd; padding-bottom: 15px;">
            <h3 style="margin:0;">{article.get('title')}</h3>
            <p style="color: gray; font-size: 0.9em;">Source: {article.get('source')} | Published: {article.get('published_at')}</p>
            <img src="{article.get('image_url', '')}" alt="" style="max-width: 100%; height: auto; margin: 10px 0;">
            <p>{article.get('description') or article.get('snippet')}</p>
            <a href="{article.get('url')}" target="_blank">Read full article</a>
        </div>
        """

    # Send to all subscribers
    for sub in subscribers:
        send_email(sub, "Your Daily Market News Update", payload["data"])

# Schedule the task to run every day at 08:00 AM
schedule.every().day.at("08:00").do(send_daily_alerts)

if __name__ == "__main__":
    print("Scheduler started. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(60)


# if __name__ == "__main__":
#     send_daily_alerts()