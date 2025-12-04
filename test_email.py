
from email_sender import send_email

# Fake single article for testing
test_articles = [
    {
        "title": "Test News Title",
        "description": "This is a test description for your Forex Alert System.",
        "snippet": "This is a test snippet.",
        "url": "https://example.com",
        "image_url": "https://via.placeholder.com/600x300",
        "source": "Test Source",
        "published_at": "2025-01-01"
    }
]

send_email(
    "ibrahimgidi2019@gmail.com",
    "Test Alert - Forex System",
    test_articles
)
