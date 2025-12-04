


import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Add subscriber email
def add_email(email):
    doc_ref = db.collection("subscribers").document(email)
    doc_ref.set({"email": email})

# Get all subscriber emails
def get_all_emails():
    subscribers = db.collection("subscribers").stream()
    return [doc.to_dict()['email'] for doc in subscribers]
