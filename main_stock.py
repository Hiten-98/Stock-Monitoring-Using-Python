import requests
from twilio.rest import Client


#API KEY of Twilio
account_sid = "ACe1639a65547fb6dbd5508f3b138ca73d"
auth_token = "180fb7946422e5604cc79cfcf045e33e"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


response = requests.get(url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=RELIANCE.BSE&outputsize=full&apikey=5NKRXTPQ5EAWYQQK")
response.raise_for_status()

stocks_data = response.json()["Time Series (Daily)"]
stocks_data_list = [value for (key, value) in stocks_data.items()]

yesterday_stock_data = stocks_data_list[0]
yesterday_closing = yesterday_stock_data["4. close"]
print(yesterday_closing)

day_before_yesterday_stock_data = stocks_data_list[1]
day_before_yesterday_closing = day_before_yesterday_stock_data["4. close"]
print(day_before_yesterday_closing)

difference = float(yesterday_closing) - float(day_before_yesterday_closing)
up_down = None
if difference > 0:
    up_down = "⬆"
else:
    up_down = "⬇"

diff_percentage = round((difference/ float(yesterday_closing)) * 100)
print(diff_percentage)

if abs(diff_percentage) > 0:
    # API Key for news: 4864149089fe4d58a4141049c36e9bdc

    news_response = requests.get(
        url="https://newsapi.org/v2/everything?q=RELIANCE&apiKey=4864149089fe4d58a4141049c36e9bdc")
    news_response.raise_for_status()

    news_data = news_response.json()
    news_data_slice = news_data["articles"][:3]
    #print(news_data_slice)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.

formatted_news = [f"Reliance {up_down}{diff_percentage}%\n\nHeadline {article['title']}. \n\nBrief: {article['description']}" for article in news_data_slice]
print(formatted_news)

client = Client(account_sid, auth_token)
for article in formatted_news:
    message = client.messages \
        .create(
        body=article,
        from_='+18126128368',
        to='+91 84509 04594'
    )


