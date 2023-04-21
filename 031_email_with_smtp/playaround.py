import smtplib
import email.message
import datetime as dt
import random
import test_emails

message_01 = email.message.Message()
message_01['Subject'] = 'My first IMAP email'
message_01['From'] = test_emails.my_email_01
message_01['To'] = test_emails.my_email_02
message_01.set_payload('TestEmail')


date_to_verify = dt.datetime(day=21, month=4, year=2023)
current_date = dt.datetime.now()

message_02 = email.message.Message()

with open('quotes.txt') as quotes:
    list_of_quotes = quotes.readlines()
    quote_with_author = random.choice(list_of_quotes)
    quote = quote_with_author.split('- ')[0]
    author = quote_with_author.split('- ')[1]
    message_02['Subject'] = f"Quote from {author}"
    message_02['From'] = test_emails.my_email_02
    message_02['To'] = test_emails.my_email_01
    message_02.set_payload(f"{quote}\n{author}")

print(message_02)
print(dt.datetime.now())
print()
print()

with smtplib.SMTP_SSL(test_emails.smtp_urk_net, 2525) as connection:
    connection.login(test_emails.my_email_02, test_emails.smtp_pass_02)
    connection.send_message(message_02)
    connection.quit()
