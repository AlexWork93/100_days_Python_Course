import imaplib
import email.message
import time

my_email_01 = 'python100days_test_01@ukr.net'
my_pass_01 = 'ALUeKg3kAm4vcrFb'
my_email_02 = 'pythot100days_test_02@ukr.net'
my_pass_02 = 'wN7RCY01iOFcyPlc'

message_01 = email.message.Message()
message_01['Subject'] = 'My first IMAP email'
message_01['From'] = my_email_01
message_01['To'] = my_email_02
message_01.set_payload('TestEmail')

message_02 = email.message.Message()
message_02['Subject'] = 'My first IMAP email'
message_02['From'] = my_email_02
message_02['To'] = my_email_01
message_02.set_payload('TestEmail')


with imaplib.IMAP4_SSL('imap.ukr.net') as connection:
    connection.login(my_email_01, my_pass_01)
    connection.append('INBOX', '', imaplib.Time2Internaldate(time.time()), str(message_01).encode('utf-8'))
    connection.logout()

with imaplib.IMAP4_SSL('imap.ukr.net') as connection:
    connection.login(my_email_02, my_pass_02)
    connection.append('INBOX', '', imaplib.Time2Internaldate(time.time()), str(message_02).encode('utf-8'))
    connection.logout()
