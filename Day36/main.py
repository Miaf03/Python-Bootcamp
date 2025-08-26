import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = os.getenv("ALPHAVANTAGE_API_KEY")
news_api_key = os.getenv("NEWS_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE")
my_phone = os.getenv("MY_PHONE")

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
data = stock_response.json()["Time Series (Daily)"]
dates = sorted(data.keys(), reverse=True)
yesterday, day_before = dates[0], dates[1]
price_yesterday = float(data[yesterday]["4. close"])
price_day_before = float(data[day_before]["4. close"])

change = round((price_yesterday - price_day_before) / price_day_before * 100)

if abs(change) >= 5:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "apiKey": news_api_key,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": 3
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    articles = news_response.json()["articles"]

    client = Client(account_sid, auth_token)
    for article in articles:
        title = article["title"]
        description = article["description"] or ""
        message = client.messages.create(
            body=f"{STOCK}: {change}%\nHeadline: {title}\nBrief: {description[:200]}",
            from_=twilio_phone,
            to=my_phone
        )
        print("Sent:", message.status)
else:
    print(f"{STOCK} change {change}% — not significant.")