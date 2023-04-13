"""This is a module to creates an object for the Spotify API to interact \
    with."""
# pylint: disable=too-many-locals
# pylint: disable=unused-variable
# pylint: disable=invalid-name

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
            mp3 (Mp3): The Mp3 object used to search Spotifys API.
        Returns:
            results (dict): A dictionary with the results of the search.
        """
        search_title = str(mp3.get_title())
        print("Title to be searched is: " + search_title)
        search_artist = str(mp3.get_artist())
        print("Artist to be searched is: " + search_artist)
        search_album = str(mp3.get_album())
        print("Album to be searched is: " + search_album + "\n")

        search_result = self.sp.search(q=search_artist, type='artist', limit=1)
        print(search_result)
        artist_name = search_result['artists']['items'][0]['name']
        artist_id = search_result['artists']['items'][0]['id']
        artist_genre = search_result['artists']['items'][0]['genres']
        song_album = None
        song_album_id = None
        song_album_date = None

        artist_albums = self.sp.artist_albums(artist_id=artist_id)['items']
        for i, album in enumerate(artist_albums):
            if album['name'] == search_album:
                song_album = album['name']
                song_album_id = album['id']
                song_album_date = album['release_date']
                break

        if song_album is None or song_album_id is None:
            print(f"Album '{search_album}' not found for artist '\
                {search_artist}'. Searching for song without album...")
            fallback_search = self.sp.search(q=f'artist:{search_artist}\
                track:{search_title}', type='track', limit=1)
            if not fallback_search['tracks']['items']:
                raise ValueError(f"Song '{search_title}' not found for \
                    artist '{search_artist}'")
            track = fallback_search['tracks']['items'][0]
            song_title = track['name']
            song_id = track['id']
            song_album = track['album']['name']
            song_album_id = track['album']['id']
            song_album_date = track['album']['release_date']
        else:
            album_songs = self.sp.album_tracks(album_id=song_album_id)['items\
                ']
            for j, song in enumerate(album_songs):
                if song['name'] == search_title:
                    song_title = song['name']
                    song_id = song['id']
                    break

        album_songs = self.sp.album_tracks(album_id=song_album_id)['items']
        for j, song in enumerate(album_songs):
            if song['name'] == search_title:
                song_title = song['name']
                song_id = song['id']
                break

        results = {'title': song_title, 'album': song_album,
                   'artist': artist_name, 'id': song_id,
                   'genre': artist_genre, 'date': song_album_date}
        print(results)
        return results

    def sync_spotify(self, mp3):
        """
            This function uses the search() method to take an mp3, search for
            the track in Spotify's API, and replace the title, artist, album,
            and genre tags on the mp3 to be the same as what is on Spotify.
        Args:
            mp3 (mp3): The mp3 object used to search Spotifys API and sync the
            metadata with.
        """
        music = mp3
        search_results = self.search(music)
        music.set_title(str(search_results['title']))
        music.set_artist(str(search_results['artist']))
        music.set_album(str(search_results['album']))
        music.set_genre(str(search_results['genre']))
        music.set_date(str(search_results['date']))
