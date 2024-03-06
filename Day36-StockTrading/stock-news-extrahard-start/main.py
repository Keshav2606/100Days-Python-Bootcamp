import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = "ACf37f08a539c79e7e968db1983fb4ae02"
auth_token = ""

stock_api_key = ""
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": stock_api_key,
}
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]

yesterday_data = data_list[0]
yesterday_close_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_close_price = float(day_before_yesterday_data["4. close"])

price_difference = yesterday_close_price - day_before_yesterday_close_price

percentage_change = (price_difference/day_before_yesterday_close_price)*100

if percentage_change < 0:
    percentage_change *= -1
    stock_msg = f"TSLA: 🔻{percentage_change}%"
else:
    stock_msg = f"TSLA: 🔺{percentage_change}%"

news_api_key = ""
news_parameters = {
    "q": "tesla",
    "from": "2024-02-05",
    "sortBy": "publishedAt",
    "language": "en",
    "apiKey": news_api_key,

}
news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
news_response.raise_for_status()
news_data = news_response.json()
latest_news = news_data["articles"][0]
news_title = latest_news["title"]
news_description = latest_news["description"]

if -5 >= percentage_change >= 5:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="+14067408619",
        body=f"\n{stock_msg}\nHeadline: {news_title}\nBrief: {news_description}",
        to="+918178753778"
    )

    print(message.status)


# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?.
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
