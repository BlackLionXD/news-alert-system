



from firebase_db import add_email, get_all_emails

# Add a test email
add_email("test@example.com")

# Fetch and print all emails
emails = get_all_emails()
print(emails)
