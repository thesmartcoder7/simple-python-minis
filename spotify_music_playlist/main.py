from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


client_id = "your_client_id"
client_secret = "your_client_secret"

date = input("From which period would you like to listen to? YYY-MM-DD, add the dashes as well: ")

# scraping the Billboard website to get the top 100 songs for a specific year
billboard = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
billboard.raise_for_status()
billboard_site = billboard.text
soup = BeautifulSoup(billboard_site, features="html.parser")

# cleaning data
list_div = soup.select(selector=".chart-results-list")
top_list = list_div[0]
top_100_list = top_list.select(selector="li", class_="o-chart-results-list__item")
title_list = []
artist_list = []
count = 1


# all titles
for item in top_100_list:
    if item.select_one(selector='h3', class_='c-title') is not None:
        title = item.select_one(selector='h3', class_='c-title').text.strip()
        title_list.append(title)
    else:
        pass


# sorting the final artist list
final_title_list = []
index = 0
for _ in range(200):
    if index < len(title_list):
        final_title_list.append(title_list[index].strip())
        index += 2


# all artist names
for item in top_100_list:
    if item.select_one(selector='.a-truncate-ellipsis-2line') is not None:
        artist = item.select_one(selector='.a-truncate-ellipsis-2line').text
        artist_list.append(artist)
    else:
        pass


# sorting the final artist list
# might not use this in this particular code but would be very useful in another application
final_artist_list = []
index = 0
for _ in range(200):
    if index < len(artist_list):
        final_artist_list.append(artist_list[index].strip())
        index += 2


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path=".cache"
    )
)

user_id = sp.current_user()["id"]
song_uris = []

for song in final_title_list:
    result = sp.search(q=f"track:{song}",  type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

new_playlist = sp.user_playlist_create(user=user_id, name=f"Top-100-From-{date}", public=False)
sp.playlist_add_items(playlist_id=new_playlist["id"], items=song_uris)
