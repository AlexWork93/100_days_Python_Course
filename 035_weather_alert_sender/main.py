import requests
import test_emails
from twilio.rest import Client


print(f'{test_emails.open_weather_endpoint}')

response = requests.get(url=f'{test_emails.open_weather_endpoint}', params=test_emails.params)

print(response.json()['main']['temp'])



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
account_sid = test_emails.twilio_account_sid
auth_token = test_emails.twilio_auth_token
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
    body=f"current temp is {response.json()['main']['temp']}",
    from_='+16317720159',
    to='+16317720159'
)

print(message.sid)
