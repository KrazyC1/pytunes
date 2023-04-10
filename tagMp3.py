from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

#Client ID
ci = "cb6906d5bc1c4f80bbeb8006ec63bf42"

#Client Secret
cs = "42f643e0fb444dc1845f08cddc234908"

#Client Id and Secret Id have been embedded to the file so that we can hopelly all work with the API
client_credentials_manager = SpotifyClientCredentials(client_id=ci, client_secret=cs) #check definition to change API connection
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#extract playlist
playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

all_tracks = []
#all_date_tracks = []

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
    album_id = track["track"]["album"]["uri"]
    album_info = sp.album(album_id)
    album_date = album_info["release_date"]
    
    album = track["track"]["album"]["name"]
    #album_date = track["release_date"]
    
    # Popularity of the track
    track_pop = track["track"]["popularity"]
    
    #release date 
    #album_Date = album_date["release_date"]

    # Append all details to a list
    temp = [track_name, artist_name, artist_pop, artist_genres, album, album_date, track_pop]
    all_tracks.append(temp)
    

for track in all_tracks:
    print(track)
    
print("\n")
print("Now printing first entry in list")
print(all_tracks[0])

print("\n")
print("Sorted by date published:")

# Sort by date string in each sub-array
all_tracks.sort(key=lambda x: x[5])

# Print sorted ArrayList
for all_tracks_date_sorted in all_tracks:
    print(all_tracks_date_sorted)
    


    