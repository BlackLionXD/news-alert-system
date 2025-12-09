import os
import json
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Parse Firebase service account from .env
firebase_key_json = os.getenv("FIREBASE_KEY")
if not firebase_key_json:
    raise ValueError("FIREBASE_KEY is not set in the environment variables.")

cred_dict = json.loads(firebase_key_json)
cred = credentials.Certificate(cred_dict)

# Initialize Firebase app (only if not already initialized)
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Add subscriber email + optional keywords
def add_email(email, keywords=[]):
    doc_ref = db.collection("subscribers").document(email)
    doc_ref.set({
        "email": email,
        "keywords": keywords
    })

# Get all subscriber emails
def get_all_emails():
    subscribers = db.collection("subscribers").stream()
    return [doc.to_dict()['email'] for doc in subscribers]

# Get all subscribers with keywords
def get_all_subscribers():
    """
    Returns list of subscribers as dicts:
    [{'email': 'a@gmail.com', 'keywords': ['usd', 'forex']}, ...]
    """
    subscribers = []
    docs = db.collection("subscribers").stream()
    for doc in docs:
        data = doc.to_dict()
        subscribers.append({
            "email": data.get("email"),
            "keywords": data.get("keywords", [])
        })
    return subscribers
