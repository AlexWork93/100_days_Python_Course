import requests
import email
import smtplib
import test_emails
from datetime import datetime, timedelta

yesterday_str = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
before_yesterday_str = (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d')

print(yesterday_str)

ibm_params = {'function': 'TIME_SERIES_DAILY_ADJUSTED',
              'symbol': 'IBM',
              'apikey': 'demo'
              }

ibm_stack_rate = 'https://www.alphavantage.co/query'

news_params = {'q': 'tesla',
               'from': yesterday_str,
               'sortBy': 'publishedAt',
               'apiKey': test_emails.news_api_uth_token
               }
news_endpoint = 'https://newsapi.org/v2/everything'

ibm_response = requests.get(url=ibm_stack_rate, params=ibm_params)

news_response = requests.get(url=news_endpoint, params=news_params)

rate_yesterday = round(float(ibm_response.json()['Time Series (Daily)'][yesterday_str]['4. close']), 4)
rate_before_yesterday = round(float(ibm_response.json()['Time Series (Daily)'][before_yesterday_str]['4. close']), 4)
print(rate_yesterday)
print(rate_before_yesterday)
print(news_response.json()['articles'][0])

if rate_yesterday > rate_before_yesterday:
    difference = round((((rate_yesterday - rate_before_yesterday) / rate_before_yesterday) * 100), 4)
    print("yesterday is", difference, "% bigger than num2")
else:
    difference = round((((rate_before_yesterday - rate_yesterday) / rate_yesterday) * 100), 4) * -1
    print("yesterday is", difference, "% bigger than num1")

payload = f"Testa stack rate is {difference}\npossible reason for this is:\n{news_response.json()['articles'][0]['title']}\n{news_response.json()['articles'][0]['description']}\nRead full: {news_response.json()['articles'][0]['url']}"
payload = payload.encode('utf-8')

message = email.message.Message()
message['Subject'] = "Tesla stack rate"
message['From'] = test_emails.my_email_02
message['To'] = test_emails.my_email_01
message.set_payload(payload)

with smtplib.SMTP_SSL(test_emails.smtp_urk_net, 2525) as connection:
    connection.login(test_emails.my_email_02, test_emails.smtp_pass_02)
    connection.send_message(message)
    connection.quit()
