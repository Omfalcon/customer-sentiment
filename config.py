import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Flask Settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    DEBUG = os.getenv('FLASK_DEBUG', 'True').lower() == 'true'

    # MongoDB Settings
    MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
    DATABASE_NAME = os.getenv('DATABASE_NAME', 'sentiment_watchdog')

    # Clerk Authentication
    CLERK_SECRET_KEY = os.getenv('CLERK_SECRET_KEY')
    CLERK_PUBLISHABLE_KEY = os.getenv('CLERK_PUBLISHABLE_KEY')

    # Google/Gmail API
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET')
    GOOGLE_REDIRECT_URI = os.getenv('GOOGLE_REDIRECT_URI', 'http://localhost:5000/auth/callback')

    # Gemini AI
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    # Alert Settings
    NEGATIVE_SENTIMENT_THRESHOLD = float(os.getenv('NEGATIVE_SENTIMENT_THRESHOLD', '0.3'))
    ALERT_CHECK_INTERVAL = int(os.getenv('ALERT_CHECK_INTERVAL', '300'))  # 5 minutes