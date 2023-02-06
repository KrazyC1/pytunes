from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
#import testgui

client_credentials_manager = SpotifyClientCredentials() #check definition to change API connection
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print("What would you like to search?")
search = str(input())
print("Searching for: " + search )
results = sp.search(q=search, limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i+1, t['name'])
