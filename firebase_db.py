import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Load Firebase credentials from environment variable
firebase_key_json = os.environ.get("FIREBASE_KEY")
if not firebase_key_json:
    raise ValueError("FIREBASE_KEY environment variable is not set.")

cred_dict = json.loads(firebase_key_json)
cred = credentials.Certificate(cred_dict)

# Initialize Firebase app
firebase_admin.initialize_app(cred)

# Firestore client
db = firestore.client()

# Example functions
def add_email(email):
    doc_ref = db.collection("subscribers").document(email)
    doc_ref.set({"email": email})

def get_all_emails():
    subscribers = db.collection("subscribers").stream()
    return [doc.to_dict()["email"] for doc in subscribers]
