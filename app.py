from flask import Flask, render_template, request
from firebase_db import add_email, get_all_emails
from news_fetcher import fetch_marketaux_news, filter_news_by_keywords, format_news_payload

app = Flask(__name__)

keywords = ["usd","forex","eur","market","jpy","trading","dollar","stocks"]

@app.route("/", methods=["GET", "POST"])
def home():
    message = None
    try:
        if request.method == "POST":
            email = request.form.get("email")
            if email:
                add_email(email)
                message = "You have successfully subscribed!"
    except Exception as e:
        print(f"Error subscribing email: {e}")
        message = "Something went wrong. Please try again."

    return render_template("index.html", message=message)

@app.route("/subscribers")
def subscribers():
    try:
        emails = get_all_emails()
        return {"subscribers": emails}
    except Exception as e:
        print(f"Error fetching subscribers: {e}")
        return {"subscribers": [], "error": "Unable to fetch subscribers"}

@app.route("/alerts")
def alerts():
    articles = []
    error_message = None
    try:
        # Fetch and filter news
        news = fetch_marketaux_news(limit=20)
        filtered = filter_news_by_keywords(news.get("data", []), keywords)
        payload = format_news_payload(filtered)
        articles = payload.get("data", [])
        if not articles:
            error_message = "No news available at the moment."
    except Exception as e:
        print(f"Error fetching news: {e}")
        error_message = "Unable to fetch news. Please check your internet connection or try again later."

    # Pass articles and error message to template
    return render_template("alerts.html", articles=articles, error_message=error_message)

# Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0')
