# email_sender.py
import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email(to_email, subject, articles):
    """
    Send an HTML email with full news content.
    articles: list of dictionaries with keys: title, description, snippet, url, image_url, source, published_at
    """
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject

    # Build HTML content
    html_body = """
    <h2 style="color:#2E86C1;">Your Daily Market News Update</h2>
    """
    for article in articles:
        html_body += f"""
        <div style="margin-bottom:25px; border-bottom:1px solid #ddd; padding-bottom:15px;">
            <h3>{article.get('title')}</h3>
            <p style="color:gray; font-size:0.9em;">Source: {article.get('source')} | Published: {article.get('published_at')}</p>
            {f'<img src="{article.get("image_url")}" style="max-width:100%; height:auto; margin:10px 0;">' if article.get("image_url") else ""}
            <p>{article.get('description') or article.get('snippet')}</p>
            <a href="{article.get('url')}" target="_blank">Read full article</a>
        </div>
        """

    msg.set_content("Your email client does not support HTML.")
    msg.add_alternative(html_body, subtype='html')

    # Send email via Gmail SMTP
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print(f"Email sent to {to_email}")
