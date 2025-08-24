from flask import Flask, render_template, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

# MongoDB Setup
client = MongoClient(os.getenv('MONGODB_URI'))
db = client.sentiment_watchdog
messages_collection = db.messages

# Gemini AI Setup
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-pro')

def analyze_sentiment_gemini(text):
    try:
        prompt = f"Analyze this customer message sentiment. Return ONLY a JSON format: {{sentiment: 'positive/negative/neutral', score: 0.0-1.0, emotion: 'angry/happy/frustrated/etc'}}\n\nMessage: {text}"
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return {'sentiment': 'neutral', 'score': 0.0, 'emotion': 'unknown'}

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/api/messages')
def get_messages():
    messages = list(messages_collection.find({}).sort('timestamp', -1).limit(50))
    # Convert ObjectId to string for JSON serialization
    for msg in messages:
        msg['_id'] = str(msg['_id'])
    return jsonify(messages)

@app.route('/api/analytics')
def get_analytics():
    # Mock analytics data - we'll implement real aggregation later
    analytics = {
        'gmail': {'positive': 90, 'negative': 20, 'neutral': 20},
        'chat': {'positive': 10, 'negative': 20, 'neutral': 20}
    }
    return jsonify(analytics)

if __name__ == '__main__':
    app.run(debug=True)