from bs4 import BeautifulSoup as BS
import lxml
import requests
import re

# with open(file='index.html', mode='r') as html_file:
#     soup = BS(html_file.read(), 'lxml')
#     print(soup.prettify())
#     # print(soup.findAll(name='a'))
#     print(soup.select(selector='a')[0].get('class'))


response = requests.get(url='https://news.ycombinator.com/')
soup = BS(response.content, 'lxml')

print(soup.prettify())

print(soup.select_one(selector='.title span a').text)
print(soup.select_one(selector='.title span a').get('href'))
print(soup.select_one(selector='span .score').text.split(' ')[0])
print(re.search('\\d+', soup.select_one(selector='span .score').text).group())

# Get list of articles and list of upvotes and print a title of the article with the highest upvotes

article_titles = [article.text for article in soup.select(selector='.title span a')]
article_upvotes = [int(re.search('\\d+', upvote.text).group()) for upvote in soup.select(selector='span .score')]

print(article_titles[article_upvotes.index(max(article_upvotes))])



