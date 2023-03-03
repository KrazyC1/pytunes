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

    def set_title(self,new_title):
        self.audio['title'] = str(new_title)
        self.audio.save()
    
    def set_artist(self,new_artist):
        self.audio['artist'] = str(new_artist)
        self.audio.save()
    
    def set_album(self,new_album):
        self.audio['album'] = str(new_album)
        self.audio.save()
    
    def set_genre(self,new_genre):
        self.audio['genre'] = str(new_genre)
        self.audio.save()
