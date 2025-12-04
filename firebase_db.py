


import os
import json
import firebase_admin
from firebase_admin import credentials, firestore

firebase_key = os.getenv("FIREBASE_KEY")
if not firebase_key:
    raise ValueError("FIREBASE_KEY environment variable is not set.")

cred_dict = json.loads(firebase_key)
cred = credentials.Certificate(cred_dict)
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_email(email):
    doc_ref = db.collection("subscribers").document(email)
    doc_ref.set({"email": email})

def get_all_emails():
    docs = db.collection("subscribers").stream()
    return [doc.id for doc in docs]
