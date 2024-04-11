import requests
from datetime import datetime, timedelta
from twilio.rest import Client


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# twilio.com msg
account_sid = "ACC_ID"
auth_token = "AUTH_TOKEN"
client = Client(account_sid, auth_token)
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
api_key_stock = "API_KEY_STOCK"
api_key_news = "API_KEY_NEWS"
up_down = None

param_stock = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": api_key_stock
}
presentday = datetime.now()  # or presentday = datetime.today()
yesterday = presentday - timedelta(1)
day_before_yesterday = yesterday - timedelta(1)


stock_res = requests.get(url=STOCK_ENDPOINT, params=param_stock)
stock_res.raise_for_status()
print(stock_res.json())
yday_closing_stock = (float(stock_res.json()['Time Series (Daily)'][str(yesterday.date())]['2. high']))
day_before_yday_closing_stock = (float(stock_res.json()['Time Series (Daily)'][str(day_before_yesterday.date())]
                                       ['2. high']))
difference = yday_closing_stock - day_before_yday_closing_stock
percentage = round((difference / yday_closing_stock)*100)

print("Yday_closing_stock", yday_closing_stock)
print("Day_before_yday_closing_stock :", day_before_yday_closing_stock)
print("Difference : ", difference)
print("Percentage : ", percentage)

if difference < 5:
    up_down = "🔻"
else:
    up_down = "🔺"


def get_news():
    param_news = {
        "q": COMPANY_NAME,
        "from": str(day_before_yesterday.date()),
        "sortBy": "publishedAt",
        "apiKey": api_key_news
    }
    news_res = requests.get(url=NEWS_ENDPOINT, params=param_news)
    three_articles = news_res.json()["articles"][:3]
    formatted_articles = [(f"{STOCK}: {up_down} {percentage}% \n\n Headline: {article['title']}, \n\n "
                          f"Brief: {article['description']}") for article in three_articles]
    for article in formatted_articles:
        message = client.messages \
            .create(body=article, from_='+12513201209', to='+353892030026')


if percentage > 5:  # check if stock got down or up by 5 %
    get_news()
