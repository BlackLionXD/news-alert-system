


from news_fetcher import fetch_marketaux_news, filter_news_by_keywords, format_news_payload



from flask import Flask, render_template, request
from firebase_db import add_email, get_all_emails

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = None

    if request.method == "POST":
        email = request.form.get("email")
        if email:
            add_email(email)
            message = "You have successfully subscribed!"

    return render_template("index.html", message=message)


@app.route("/subscribers")
def subscribers():
    emails = get_all_emails()
    return {"subscribers": emails}
keywords = ["usd","forex","eur","market","jpy","trading","dollar","stocks"]

@app.route("/alerts")
def alerts():
    # Fetch and filter news
    news = fetch_marketaux_news(limit=20)
    filtered = filter_news_by_keywords(news["data"], keywords)
    payload = format_news_payload(filtered)
    
    # Pass to template
    return render_template("alerts.html", articles=payload["data"])


if __name__ == "__main__":
    app.run(debug=True)
