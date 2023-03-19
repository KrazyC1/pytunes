import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class Spotify:
    """This class is used to allow mp3 objects to interact with
    Spotify's API."""

    def __init__(self):
        """This function is the default constructor of the class that
        sets up the Spotify API's credentials."""
        # Client ID
        self.ci = "cb6906d5bc1c4f80bbeb8006ec63bf42"

        # Client Secret
        self.cs = "42f643e0fb444dc1845f08cddc234908"

        # Client Id and Secret Id have been embedded to the file so that we 
        # can hopelly all work with the API
        client_credentials_manager = SpotifyClientCredentials(
            client_id=self.ci, client_secret=self.cs)  
            # check definition to change API connection
        self.sp = spotipy.Spotify(
            client_credentials_manager=client_credentials_manager)

    def search(self, mp3):
        """
            This fuctions allows you to search for a specific track from
            Spotify's API using the variables in the given mp3 object.
            It will first search for the artist, then the album, and then
            the track name.

        Args:
            mp3 (mp3): The mp3 object used to search Spotifys API.

        Returns:
            results (dict): A dictionary with the results of the search.
        """
        music = mp3
        search_result = dict(self.sp.search(
            music.artist, limit=1, type='artist'))
        artist = search_result['artists']['items'][0]
        artist_id = artist['id']
        list_of_albums = self.sp.artist_albums(artist_id)['items']
        for i in range(len(list_of_albums)):
            if (list_of_albums[i]['name'] == music.album):
                list_of_tracks = self.sp.album_tracks(
                    album_id=list_of_albums[i]['id'])
                for j in range(len(list_of_tracks)):
                    if (list_of_tracks['items'][j]['name'] == music.title):
                        artist_name = artist['name']
                        artist_genres = artist['genres']
                        track_name = list_of_tracks['items'][j]['name']
                        album_name = list_of_albums[i]['name']
                        track_id = list_of_tracks['items'][j]['id']
                        results = {'artist': artist_name, 'genre': artist_genres,
                                   'title': track_name, 'album': album_name,
                                   'track id': track_id}
                        return results
                        break
                break

    def sync_spotify(self, mp3):
        """
            This function uses the search() method to take an mp3, search for
            the track in Spotify's API, and replace the title, artist, album,
            and genre tags on the mp3 to be the same as what is on Spotify.
        Args:
            mp3 (mp3): The mp3 object used to search Spotifys API and sync the
            metadata with.
        """
        search_results = self.search(mp3)
        mp3.set_title(str(search_results['title']))
        mp3.set_artist(str(search_results['artist']))
        mp3.set_album(str(search_results['album']))
        mp3.set_genre(str(search_results['genre']))
