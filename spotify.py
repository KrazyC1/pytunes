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
        music = mp3
        search_result = dict(self.sp.search(music.artist,limit=1,type='artist'))
        artist = search_result['artists']['items'][0]
        artist_id = artist['id']
        list_of_albums = self.sp.artist_albums(artist_id)['items']
        for i in range(len(list_of_albums)):
            if (list_of_albums[i]['name']==music.album):
                list_of_tracks = self.sp.album_tracks(album_id=list_of_albums[i]['id'])
                for j in range(len(list_of_tracks)):
                    if (list_of_tracks['items'][j]['name']==music.title):
                        print(artist['name'])
                        print(artist['genres'][0])
                        print(list_of_tracks['items'][j]['name'])
                        print(list_of_albums[i]['name'])
                        track_id=list_of_tracks['items'][j]['id']
                        break
                break 
                        
                
        
home = '/Users/zaydrianprice/Documents'
spotify_tagger = '/spotify-tagger/music'
test_file = home + spotify_tagger + '/01 Fergalicious (Feat. Will.I.Am).mp3'
test_music = mp3.Mp3(test_file)
test_spotify=Spotify()
test_spotify.search(test_music)