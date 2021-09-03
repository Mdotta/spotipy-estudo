import spotipy
from spotipy.oauth2 import SpotifyOAuth
import secret

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=secret.CLIENT_ID,
                                               client_secret=secret.CLIENT_SECRET,
                                               redirect_uri="http://localhost/",
                                               scope="playlist-modify-public"))

current_user = sp.current_user()

playlists_to_clone = [
    '36TRM1AwOi9d4iwKhoZUYt?si=iHTYDDltQBWh_5UkfYDKRg'
    ]


def copy_playlist(playlist_id):
    print("Retrieving playlist...")
    ##playlist anime
    # playlist_to_clone = sp.playlist_items('1vqJoGlZHR3JdZ9bp2l3Ru?si=FxKgnQQvQvGXEXPmn0wsGA')
    ##playlist pest
    playlist_to_clone = sp.playlist_items(playlist_id)
    ##random
    # playlist_to_clone = sp.playlist_items('1HvmDfhGmyEbJKSntaOYg1?si=nt6cQ10CS8aubHOffmOGOw')
    print("Playlist ",playlist_to_clone['name']," found")

    print("Creating cloned playlist....")
    user_id = current_user['id']
    playlist_name = playlist_to_clone['name']
    cloned_playlist = sp.user_playlist_create(user_id,
                            playlist_name)
    print("Playlist ",playlist_name," created")

    ##TODO - lidar com playlists com mais de 100 musicas

    print("Populating playlist...")
    tracks_to_add = []
    c = 0
    stepper = 0
    playlist_counter = enumerate(playlist_to_clone['tracks']['items'])
    while c < playlist_counter:
        loopMax = stepper+49
        if playlist_counter-stepper < 50:
            loopMax = playlist_counter-stepper

        for index in range(stepper,loopMax):
            item = playlist_to_clone['tracks']['items'][index]
            track_id = item['track']['id']
            track_name = item['track']['name']
            print("track ",track_name, " added")
            tracks_to_add.append(track_id)
            c+=1
        stepper = c

    sp.playlist_add_items(cloned_playlist['id'], tracks_to_add)

current_user = sp.current_user()

playlists_to_clone = [
    '36TRM1AwOi9d4iwKhoZUYt?si=iHTYDDltQBWh_5UkfYDKRg'
    ]
