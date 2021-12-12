import requests
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API_KEY = "your api key from a news api service"
STOCK_API_KEY = "your api key from a stock api service"
"""
The API endpoints used in this program are:
Stock data = https://www.alphavantage.co/query
News = https://www.newsapi.org/v2/everything
The stock itself is a random one I picked. The program can work for
any stock

Feel free to use this code as it is for educational purposes only!
"""


news_parameters = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "apikey": STOCK_API_KEY,
    "symbol": STOCK,
    "interval": "60min"

}


def send_email(message):
    sender = "sender email"
    password = "sender password"
    receiver = "recepient email"
    message = message
    subject = "Stock Alert!"
    with smtplib.SMTP("your domain name / smpt name") as connection:
        connection.starttls()
        connection.login(user=sender, password=password)
        connection.sendmail(
            from_addr=sender,
            to_addrs=receiver,
            msg=f"Subject:{subject}\n\n{message}"
        )
        print(f"Email to {receiver} has been successfully sent!")


def get_news():
    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news_response_list = news_response.json()["articles"]
    curated_list = news_response_list[:3]
    formatted_email = []
    for article in curated_list:
        formatted_email.append({'title': article['title'], 'headline': article['description'], 'url': article['url']})

    if new_percentage > 100:
        message = f"TESLA 🔼 {difference}% increase!\n"
        for article in formatted_email:
            message += f"Headline: {article['headline']} Read more at {article['url']}\n\n"
        message = message.encode('ascii', 'ignore').decode('ascii')
        send_email(message=message)

    else:
        message = f"TESLA 🔽 {difference}% decrease!\n"
        for article in formatted_email:
            message += f"Headline:{article['headline']} Read more at {article['url']}\n\n"

        message = message.encode('ascii', 'ignore').decode('ascii')
        send_email(message=message)


# stock functionality
stock_response = requests.get(url="https://www.alphavantage.co/query", params=stock_parameters)
stock_response.raise_for_status()
daily_data = stock_response.json()["Time Series (Daily)"]
daily_closes = []

for day in daily_data:
    daily_closes.append(daily_data[day]["4. close"])

two_day_difference = daily_closes[:2]
previous_day = float(two_day_difference[1])
today = float(two_day_difference[0])
new_percentage = round((today / previous_day) * 100)

if new_percentage > 100:
    difference = new_percentage - 100
    if difference >= 5:
        get_news()
else:
    difference = 100 - new_percentage
    if difference >= 5:
        get_news()
