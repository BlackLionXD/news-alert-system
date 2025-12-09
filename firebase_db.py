


import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Add subscriber email
# Add subscriber email + keywords
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