from bs4 import BeautifulSoup as bs
import requests
import lxml

page_soup = bs(requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/").content, "lxml")
all_movies = [title.text + '\n' for title in page_soup.select(selector="h3.title")]
all_movies.reverse()
with open("movies.txt", mode='w') as movies:
    movies.writelines(all_movies)
    print(all_movies)