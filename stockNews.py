import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "YNMCVTU0SWP57QJF"
NEWS_API_KEY = "525d6eb665fc43b6b6032778f2226668"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_SID = "AC9c4383af7ccb119e6ce500c4e59b5e6e"
TWILIO_AUTH_TOKEN = "2166cd45e9d5310cacf88b7a6d185ec2"

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
    "outputsize": "compact",
}
response = requests.get("https://www.alphavantage.co/query", params=parameters)

response.raise_for_status()
print(response.status_code)
data = response.json()['Time Series (Daily)']
# print(data)
# data_slice = data['2020-12-29']["1. open"]
# print(data_slice)

# data_list = [new_item for item in list]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
print(yesterday_data)
yesterday_closing_price = yesterday_data["4. close"]
print(f"yesterday_closing_price: {yesterday_closing_price}")
# new_data_slice = [data for (key, value) in data_slice.items()]
# print(new_data_slice)

# print(data)
# for x, y in data.items():
#   print(x, y)
# new_data = [data for (key, value) in data.items()]
# print(new_data)
# print(new_data[0])
# print(new_data[1])

#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"day_before_yesterday_closing_price: {day_before_yesterday_closing_price}")

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference_in_price = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
difference_in_price = round(difference_in_price, 4)
up_down = None
if difference_in_price > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

print(f"difference_in_price: {difference_in_price}")

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = round((100*difference_in_price)/float(yesterday_closing_price), 2)
print(f"percentage_difference: {percentage_difference}%")
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_response = requests.get("https://newsapi.org/")
news_response.raise_for_status()
# print(news_response.content)
#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}
news_response_n = requests.get(NEWS_ENDPOINT, params=news_params)
news_response_n.raise_for_status()
print(news_response_n.status_code)
articles = news_response_n.json()['articles']
print(f"news_data: {articles}")
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
# print(news_response_n.json())
top_three_articles = articles[:3]
print(top_three_articles)

## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
# new_list = [new_item for item in list if test]
#[new_item for item in list]
formatted_articles_list = [f"{STOCK_NAME}: {up_down}{percentage_difference}% \n Headline: {article['title']}. \n Brief: {article['description']}" for article in top_three_articles]
print(f"news_message_list_title: {formatted_articles_list}")
#TODO 9. - Send each article as a separate message via Twilio.
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for article in formatted_articles_list:
    message = client.messages \
            .create(
            body=article,
            from_='+14242197880',
            to='+19096313719'
        )
    print(message.status)
    print(message.sid)

#Optional TODO: Format the message like this:

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

