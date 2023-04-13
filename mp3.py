"""This is a module that creates an mp3 object."""
# pylint: disable=too-many-instance-attributes

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3


class Mp3:
    """
        This is a class that creates an mp3 object from an .mp3 file so that
        Pytunes can manipulate the mp3 files ID3 tags.
    """

    def __init__(self, file_path):
        """
            This fuction is the default contructor of Mp3 class. It will
            take in a file path and extract the song title, artist, album,
            and genre from the .mp3 file it is given.
            Args:
                file_path (string): The file path of the mp3 to be
                manipulated.
        """
        self.audio = EasyID3(file_path)
        """The .mp3 file that is pulled from the file path."""
        self.mp3_info = MP3(file_path)
        """The .mp3 file that is pulled from the file path."""
        self.file_path = str(file_path)
        """A string that holds the mp3's file path."""
        self.title = str(self.audio.get('title', [''])[0])
        """A string that holds the mp3's song title."""
        self.artist = str(self.audio.get('artist', [''])[0])
        """A string that holds the mp3's artist name."""
        self.album = str(self.audio.get('album', [''])[0])
        """A string that holds the mp3's album title."""
        self.genre = str(self.audio.get('genre', [''])[0])
        """A string that holds the mp3's genre(s)."""
        self.length = int(self.mp3_info.info.length)
        """A integer that holds the mp3's song length."""
        self.date = str(self.audio.get('date', [''])[0])
        """A string that holds the mp3's release date."""

    def __str__(self):
        """Returns a string of title, artist, album, and genre"""
        return f"Title: {self.title}\nArtist: {self.artist}\
            \nAlbum: {self.album}\nGenre: {self.genre}\nLength: \
                {self.length}\nDate: {self.date}"

    def set_title(self, new_title):
        """
            This fuction is a setter for the .mp3's title tag.
        Args:
            new_title (string): This is the new title to give the .mp3 file.
        """
        self.audio['title'] = str(new_title)
        self.audio.save()

    def set_artist(self, new_artist):
        """
            This function is a setter for the .mp3's artist tag.
        Args:
            new_artist (string): This is the name of the new artist to
            give to the .mp3 file.
        """
        self.audio['artist'] = str(new_artist)
        self.audio.save()

    def set_album(self, new_album):
        """
            This function is a setter for the .mp3's album tag.
        Args:
            new_album (string): This is the name of the new album to
            give to the .mp3 file.
        """
        self.audio['album'] = str(new_album)
        self.audio.save()

    def set_genre(self, new_genre):
        """
            This function is the setter for the the .mp3's genre tag.
        Args:
            new_genre (string): This is the new name(s) of the
            genre(s) to give to the .mp3 file.
        """
        self.audio['genre'] = str(new_genre)
        self.audio.save()

    def set_date(self, new_date):
        """
            This function is the setter for the the .mp3's date tag.
        Args:
            new_date (str): This is the new release to
            give to the .mp3 file.
        """
        self.audio['date'] = str(new_date)
        self.audio.save()

    def get_title(self):
        """A function that returns the mp3's title."""
        return self.title

    def get_artist(self):
        """A function that returns the mp3's artist."""
        return self.artist

    def get_album(self):
        """A function that returns the mp3's album."""
        return self.album

    def get_genre(self):
        """A function that returns the mp3's genre."""
        return self.genre

    def get_date(self):
        """A function that returns the mp3's release date."""
        return self.date
