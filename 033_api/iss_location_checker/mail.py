import requests
import datetime
import pytz
import time
import os
import email
import test_emails
import smtplib

# resources:
# https://sunrise-sunset.org/api
# http://open-notify.org/Open-Notify-API/ISS-Location-Now/
# For Test Purposes
iss_response_test = requests.get(url='http://api.open-notify.org/iss-now.json')
iss_latitude_test = int(round(float(iss_response_test.json()['iss_position']['latitude']), 0))
iss_longitude_test = int(round(float(iss_response_test.json()['iss_position']['longitude']), 0))
MY_LATITUDE = iss_latitude_test
MY_LONGITUDE = iss_longitude_test
# MY_LATITUDE = 48.469466
# MY_LONGITUDE = 35.080680
utc_tz = pytz.timezone('UTC')


def verify_if_time_is_correct():
    sunset_params = {'lat': MY_LATITUDE,
                     'lng': MY_LONGITUDE,
                     'formatted': 0}
    sunset_response = requests.get(url='https://api.sunrise-sunset.org/json', params=sunset_params)
    my_sunrise = int(sunset_response.json()['results']['sunrise'].split('T')[1].split(':')[0])
    my_sunset = int(sunset_response.json()['results']['sunset'].split('T')[1].split(':')[0])
    my_current_hour = datetime.datetime.now().astimezone(utc_tz).hour
    print(f"my_sunrise: {my_sunrise}, my_sunset:{my_sunset}")
    print(f'my_current_hour: {my_current_hour}')
    if my_current_hour >= my_sunset or my_current_hour <= my_sunrise:
        return True
    else:
        return False


def verify_if_iss_is_within_5():
    iss_response = requests.get(url='http://api.open-notify.org/iss-now.json')
    iss_latitude = int(round(float(iss_response.json()['iss_position']['latitude']), 0))
    iss_longitude = int(round(float(iss_response.json()['iss_position']['longitude']), 0))
    print(f"iss_latitude: {iss_latitude}, iss_longitude: {iss_longitude}")
    print(f"my_latitude: {MY_LATITUDE}, my_longitude: {MY_LONGITUDE}")
    if MY_LATITUDE in range(iss_latitude - 5, iss_latitude + 5) and MY_LONGITUDE in range(iss_longitude - 5,
                                                                                          iss_longitude + 5):
        return True
    else:
        return False


def create_email():
    message = email.message.Message()
    message['Subject'] = "ISS tracker!"
    message['From'] = test_emails.my_email_02
    message['To'] = test_emails.my_email_01
    message.set_payload('ISS is right upon your location! Look at the sky!')
    return message


def send_email(port=2525):
    with smtplib.SMTP_SSL(test_emails.smtp_urk_net, port) as connection:
        connection.login(test_emails.my_email_02, test_emails.smtp_pass_02)
        connection.send_message(create_email())
        connection.quit()


while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    if not verify_if_time_is_correct():
        print('wait until sunset')
    elif not verify_if_iss_is_within_5():
        print('ISS is too far')
    else:
        print("Look at the sky!!!")
        send_email()
    time.sleep(10)
