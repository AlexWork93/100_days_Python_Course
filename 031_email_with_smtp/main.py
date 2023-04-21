##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas
import smtplib
import random
import email
import os
import test_emails
import datetime as dt


def get_text_from_file(file):
    with open(file) as f:
        result = ''.join(f.read())
    return result


def construct_email(birthday_data, from_address=test_emails.my_email_02):
    folder_name = 'letter_templates'
    list_of_letter_names = [f'{folder_name}/{n}' for n in os.listdir(folder_name)]
    list_of_emails = [get_text_from_file(n) for n in list_of_letter_names]
    message = email.message.Message()
    message['Subject'] = "Happy Birthday!"
    message['From'] = from_address
    message['To'] = birthday_data['email']
    message.set_payload(random.choice(list_of_emails).replace("[NAME]", birthday_data['name']))
    return message


def update_birthdays_csv_with_test_data():
    try:
        birthdays_dataframe = pandas.read_csv('birthdays_new.csv')
    except FileNotFoundError:
        birthdays_dataframe = pandas.read_csv('birthdays.csv')

    new_row = {'name': ['Name1'],
               'email': [test_emails.my_email_01],
               'year': [1993],
               'month': [dt.datetime.now().month],
               'day': [dt.datetime.now().day]
               }
    birthdays_dataframe = pandas.concat([birthdays_dataframe, pandas.DataFrame(new_row)], ignore_index=True)
    pandas.DataFrame(birthdays_dataframe).to_csv('birthdays_new.csv', index=False)


def get_birthdays_data_for_today():
    current_date = dt.datetime.now()
    current_day = current_date.day
    current_month = current_date.month
    birthdays_dataframe = pandas.read_csv('birthdays_new.csv')
    list_of_birthdays_today = birthdays_dataframe[birthdays_dataframe['month'] == current_month]
    list_of_birthdays_today = list_of_birthdays_today[list_of_birthdays_today['day'] == current_day]
    dict_of_birthdays_today = pandas.DataFrame(list_of_birthdays_today).to_dict(orient='records')
    print(dict_of_birthdays_today)
    return [{'name': n['name'], 'email': n['email']} for n in dict_of_birthdays_today if 'name' in n or "email" in n]


def send_email(bd_message, port=2525):
    print(bd_message)
    with smtplib.SMTP_SSL(test_emails.smtp_urk_net, port) as connection:
        connection.login(test_emails.my_email_02, test_emails.smtp_pass_02)
        connection.send_message(bd_message)
        connection.quit()


update_birthdays_csv_with_test_data()
update_birthdays_csv_with_test_data()
birthday_data_for_today = get_birthdays_data_for_today()
print(birthday_data_for_today)
list_of_emails_for_today = [construct_email(birthday_data) for birthday_data in birthday_data_for_today]

for message in list_of_emails_for_today:
    send_email(message)
