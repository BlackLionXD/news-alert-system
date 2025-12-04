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



# 🛠️ Requirements

- Install these before running the project:

- Python 3.8+

- A Firebase Firestore project

- Marketaux API key → https://www.marketaux.com

- Gmail App Password (if sending emails via Gmail)


# 📥 Required Files to Add Manually

These MUST exist in project root:

- ✅ 1. .env

Create a file named .env:

EMAIL_ADDRESS=your@gmail.com
EMAIL_PASSWORD=your_app_password
MARKETAUX_API_TOKEN=your_marketaux_token

- ✅ 2. serviceAccountKey.json

Download from Firebase Console → Project Settings → Service Accounts.

Never commit .env or serviceAccountKey.json to GitHub.

# ▶️ How to Run the Project (Step-by-Step)
- 1️⃣ Clone the project
git clone https://github.com/BlackLionXD/news-alert-system.git
cd news-alert-system

- 2️⃣ Create and activate virtual environment
python -m venv venv
venv\Scripts\activate     # Windows
# or
# source venv/bin/activate   # macOS/Linux

- 3️⃣ Install dependencies
pip install -r requirements.txt

- 4️⃣ Add your .env and serviceAccountKey.json files

(See required files above)

# 🧪 Optional: Test everything first
Test News API
python test_news.py

Test Sending Email
python test_email.py

Test Firestore subscribers
python test_fetch_emails.py

# 🌐 Run the Flask Web App

This runs the subscription page and alerts viewer.

python app.py
# Demonstration
![Screenshot_5-12-2025_25333_127 0 0 1](https://github.com/user-attachments/assets/c6c1fe5d-fab3-4817-8ab7-62965e0b52a1)
![Screenshot_5-12-2025_25225_127 0 0 1](https://github.com/user-attachments/assets/05a56325-e0da-4999-83c0-96b0e95b5a26)

