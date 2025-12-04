# 📡 News Alert System

A lightweight Forex & Market News Alert System built using Flask, Firebase Firestore, Marketaux API, and Email Alerts.
Users can subscribe with their email, and the system automatically sends curated daily market news based on keywords like USD, EUR, Forex, Trading, Stocks, etc.

# 🚀 Features

-Email subscription system (Flask + Firestore)

-Automated daily news alerts (Scheduler)

-Fetches real-time market news from Marketaux API

-Filters articles by keywords

-Sends beautiful HTML email alerts with:

-Title

-Description

-Source

-Publication date

-Image preview

-Original article link

-Simple UI for subscribing and viewing alerts

# 📦 Technologies Used

- Python 3

- Flask

- Firebase Firestore

- Marketaux API

- SMTP (Gmail App Password recommended)

- HTML templates

- Cron-based automation (schedule library)

# 📁 Folder Structure
- news-alert-system/
│── app.py
│── email_sender.py
│── firebase_db.py
│── news_fetcher.py
│── send_alerts.py
│── daily_alerts_scheduler.py
│── test_news.py
│── test_email.py
│── test_fetch_emails.py
│── requirements.txt
│── .gitignore
│── templates/
│   ├── index.html
│   └── alerts.html
│── serviceAccountKey.json (DO NOT UPLOAD)
│── .env (DO NOT UPLOAD)

# 🛠️ Requirements

- Install these before running the project:

- Python 3.8+

- A Firebase Firestore project

- Marketaux API key → https://www.marketaux.com

- Gmail App Password (if sending emails via Gmail)


📥 Required Files to Add Manually
