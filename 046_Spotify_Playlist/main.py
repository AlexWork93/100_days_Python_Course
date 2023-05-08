import re
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import bs4
import lxml

import test_emails

# Ask user for desired date and check input. Keep asking until the valid input

keep_asking = True
input_mess = '2000-08-12'
# while keep_asking:
#     input_mess = input("enter please a date in format YYYY-MM-DD\n")
#     pattern = re.compile('^\\d{4}-\\d{2}-\\d{2}$')
#     if re.match(pattern=pattern, string=input_mess):
#         keep_asking = False
#     else:
#         print('invalid input')
print(input_mess)

# Authentication in spotify

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=test_emails.spotify_data['Client ID'],
                                               client_secret=test_emails.spotify_data['Client secret'],
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-public"))
user_id = sp.current_user()['id']
print(user_id)

# scrap the page with 100 popular songs for particular date

response = requests.get(url=f'https://www.billboard.com/charts/hot-100/{input_mess}/')
billboard_soup = bs4.BeautifulSoup(response.content, 'lxml')
chart_result_rows = billboard_soup.select(selector='ul.o-chart-results-list-row h3#title-of-a-story')

# create a list of songs spotify uris based on the list of popular songs from previous step

# list_of_uris = []
# for row in chart_result_rows:
#     print(row.parent()[1].text.strip() + " - " + row.parent()[0].text.strip())
#     result = sp.search(q=f'{row.parent()[1].text.strip() + " - " + row.parent()[0].text.strip()}', type='track')
#     list_of_uris.append(result['tracks']['items'][0]['uri'])
#     print(result['tracks']['items'][0]['uri'])

# Create a playlist using the list uf uris

# playlist = sp.user_playlist_create(user=user_id, name=f'{input_mess} Billboard 100')
# print(playlist['id'])
#
# sp.playlist_add_items(playlist_id=playlist['id'], items=list_of_uris)

# When all previous steps are done, get list of playlists and print list of tracks from it

list_of_playlists = sp.user_playlists(user=user_id)
list_of_tracks_in_response = sp.playlist_items(playlist_id=list_of_playlists['items'][0]['id'])['items']
for track in list_of_tracks_in_response:
    print(track['track']['album']['artists'][0]['name'])
    print(track['track']['name'])
    print('======================================================================')