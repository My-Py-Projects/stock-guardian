import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables.
load_dotenv()

# Init Variables.
STOCK_NAME = "AMZN"
COMPANY_NAME = "Amazon.com Inc."
API_KEY_STOCK = os.getenv("API_KEY_STOCK")
API_KEY_NEWS = os.getenv("API_KEY_NEWS")
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
USER_PHONE = os.getenv("USER_PHONE")

# API requests.
response = requests.get(f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={API_KEY_STOCK}")
data = response.json().get("Time Series (Daily)", {})

# Days variables.
yesterday = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")
day_before_yesterday = (datetime.today() - timedelta(days=2)).strftime("%Y-%m-%d")

# Try to access the latest stock prices. If the market was closed, use the last two available records.
try:

    yesterday_closing_price = float(data[yesterday]["4. close"])
    day_before_closing_price = float(data[day_before_yesterday]["4. close"])

except KeyError:

    available_dates = sorted(data.keys(), reverse=True)

    yesterday = available_dates[0]
    day_before_yesterday = available_dates[1]

    yesterday_closing_price = float(data[yesterday]["4. close"])
    day_before_closing_price = float(data[day_before_yesterday]["4. close"])

# Calculate the percentage change.
difference = (yesterday_closing_price - day_before_closing_price)
diff_percentage = (difference / day_before_closing_price) * 100

# Fetch news articles.
news_response = requests.get(
    f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={API_KEY_NEWS}"
)
news_data = news_response.json()

# Get top 3 news articles.
articles = news_data["articles"][:3]

# Create message body.
message_body = (
    f"📢 The stock of {COMPANY_NAME} ({STOCK_NAME}) varied by {diff_percentage:.2f}% in the last cycle!\n\n"
)

for article in articles:
    message_body += f"📰 {article['title']}\n{article['description']}\n🔗 {article['url']}\n\n"

# Send message via WhatsApp (Twilio).
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
message = client.messages.create(
    from_=TWILIO_PHONE,
    body=message_body,
    to=USER_PHONE
)

print(message.status)
