import unittest
import spotify
from spotify import Spotify
from mp3 import Mp3

class TestSpotify(unittest.TestCase):
    def setUp(self):
        self.spotify = Spotify()
        test_music = Mp3('music/01 James Bay - Let It Go.mp3')
        test_music2 = Mp3('music/01 Michael Jackson - Billie Jean.mp3')
        test_spotify=spotify.Spotify()
        self.test_results = test_spotify.sync_spotify(test_music)
        self.test_results2 = test_spotify.sync_spotify(test_music2)
        

    def test_spotify(self):
        test_music = Mp3('music/01 James Bay - Let It Go.mp3')
        expected_output = {
    'title': 'Let It Go',
    'album': 'Chaos And The Calm',
    'artist': 'James Bay',
    'id': '3ZQsCvbpp2HVXt9Mp46f8n',
    'genre': ['neo mellow', 'pop', 'uk pop'],
    'date': '2015-03-25'
}
        actual_output = self.spotify.search(test_music)
        self.assertEqual(actual_output, expected_output)

    def test_spotify2(self):
        test_music2 = Mp3('music/01 Michael Jackson - Billie Jean.mp3')
        expected_output = {
    'title': 'Billie Jean',
    'album': 'Thriller',
    'artist': 'Michael Jackson',
    'id': '7J1uxwnxfQLu4APicE5Rnj',
    'genre': ['pop', 'r&b', 'soul'],
    'date': '1982-11-30'
}
        actual_output = self.spotify.search(test_music2)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()