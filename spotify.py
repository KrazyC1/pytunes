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
        client_credentials_manager = SpotifyClientCredentials(client_id=self.ci, client_secret=self.cs) #check definition to change API connection
        self.sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    
    def search(self,mp3):
        self.music = mp3()
        artist = self.sp.search(self.music['artist'],limit=1,type='artist')
        
    
