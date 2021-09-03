import spotipy
from spotipy.oauth2 import SpotifyOAuth
import secret

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secret.CLIENT_ID,
                                               client_secret=secret.CLIENT_SECRET,
                                               redirect_uri="localhost:8888/callback",
                                               scope="playlist-modify-public"))


current_user = sp.current_user()

print("Retrieving playlist...")
##playlist anime
# playlist_to_clone = sp.playlist_items('1vqJoGlZHR3JdZ9bp2l3Ru?si=FxKgnQQvQvGXEXPmn0wsGA')
##playlist pest
playlist_to_clone = sp.playlist_items('6cuRDsO4IQo7a5h4qUMD3n?si=gCJs2iM9TsCyd0DmcJo7vg')
##random
# playlist_to_clone = sp.playlist_items('1HvmDfhGmyEbJKSntaOYg1?si=nt6cQ10CS8aubHOffmOGOw')
print("Playlist ",playlist_to_clone['name']," found")

print("Creating cloned playlist....")
user_id = current_user['id']
playlist_name = playlist_to_clone['name'] + " clone"
cloned_playlist = sp.user_playlist_create(user_id,
                        playlist_name)
print("Playlist ",playlist_name," created")

##TODO - lidar com playlists com mais de 100 musicas

print("Populating playlist...")
tracks_to_add = []
c = 0
for idx, item in enumerate(playlist_to_clone['tracks']['items']):
    track_id = item['track']['id']
    track_name = item['track']['name']
    print("track ",track_name, " added")
    tracks_to_add.append(track_id)
    c+=1

sp.playlist_add_items(cloned_playlist['id'], tracks_to_add)