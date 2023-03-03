import os
# Type 'python3 -m pip install mutagen' to install
from mutagen.easyid3 import EasyID3

class Mp3:
    
    def __init__(self, file_path):
        self.audio = EasyID3(file_path)
        
        self.file_path = file_path
        self.title = str(self.audio.get('title', [''])[0])
        self.artist = str(self.audio.get('artist', [''])[0])
        self.album = str(self.audio.get('album', [''])[0])
        self.genre = str(self.audio.get('genre', [''])[0])

    def __str__(self):
        return f"Title: {self.title}\nArtist: {self.artist}\nAlbum: {self.album}\nGenre: {self.genre}"

