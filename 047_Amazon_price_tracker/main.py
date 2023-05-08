import requests
import bs4
import lxml
import smtplib
import email

import test_emails

cello_url = 'https://www.amazon.com/strad-Cello-Handmade-winning-luthier/dp/B0BBDMNGFX/ref=sr_1_1?crid=8G3OBL2ACUBT&keywords=cello&qid=1683443481&sprefix=cello%2Caps%2C175&sr=8-1&th=1'

my_headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
}

response = requests.get(url=cello_url, headers=my_headers)

cello_soup = bs4.BeautifulSoup(response.content, 'lxml')
whole_price_part = cello_soup.select_one(selector='#centerCol .a-price-whole').text\
    .replace(',', '', -1)\
    .replace('.', '', -1)
fraction_price_part = cello_soup.select_one(selector='#centerCol .a-price-fraction').text
cello_full_price_float = float(f'{whole_price_part}.{fraction_price_part}')
print(cello_full_price_float)

# Here could be some price validation, but not this time xD

email_payload = f'Price for product you were interested in is lower now\n' \
                f'Current price is ${cello_full_price_float}\n' \
                f'{cello_url}'

message = email.message.Message()
message['Subject'] = "Amazon price tracker"
message['From'] = test_emails.my_email_02
message['To'] = test_emails.my_email_01
message.set_payload(email_payload)

with smtplib.SMTP_SSL(test_emails.smtp_urk_net, port=2525) as connection:
    connection.login(test_emails.my_email_02, test_emails.smtp_pass_02)
    connection.send_message(message)
    connection.quit()
