from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
#import testgui

#Client ID
ci = "cb6906d5bc1c4f80bbeb8006ec63bf42"

#Client Secret
cs = "42f643e0fb444dc1845f08cddc234908"

#Client Id and Secret Id have been embedded to the file so that we can hopelly all work with the API
client_credentials_manager = SpotifyClientCredentials(client_id=ci, client_secret=cs) #check definition to change API connection
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

print("What would you like to search?")
search = str(input())
print("Searching for: " + search )
results = sp.search(q=search, limit=20)
for i, t in enumerate(results['tracks']['items']):
    print(' ', i+1, t['name'])
