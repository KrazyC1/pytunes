from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import mp3
class Spotify:
    def __init__(self):
        #Client ID
        self.ci = "cb6906d5bc1c4f80bbeb8006ec63bf42"

        #Client Secret
        self.cs = "42f643e0fb444dc1845f08cddc234908"

        #Client Id and Secret Id have been embedded to the file so that we can hopelly all work with the API
        client_credentials_manager = SpotifyClientCredentials(client_id=ci, client_secret=cs) #check definition to change API connection
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    def search(self,mp3):
        self.music = mp3()
        artist = self.sp.search(self.music['artist'],limit=1,type='artist')
        
    



#extract playlist
playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

all_tracks = []
for track in sp.playlist_tracks(playlist_URI)["items"]:
    # URI
    track_uri = track["track"]["uri"]

    # Track name
    track_name = track["track"]["name"]

    # Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)

    # Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    artist_genres = artist_info["genres"]

    # Album
    album = track["track"]["album"]["name"]

    # Popularity of the track
    track_pop = track["track"]["popularity"]

    # Append all details to a list
    temp = [track_name, artist_name, artist_pop, artist_genres, album, track_pop]
    all_tracks.append(temp)

for track in all_tracks:
    print(track)
print("Now printing first entry in list")
print(all_tracks[0])
