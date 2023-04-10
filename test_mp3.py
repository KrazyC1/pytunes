import unittest
import mp3

class TestMp3(unittest.TestCase):
    
    SAMPLE_FOLDER = '/Users/zaydrianprice/Documents/GitHub'
    SPOTIFY_TAGGER = '/spotify-tagger/music/'
    FILE_PATH_1 = str(SAMPLE_FOLDER + SPOTIFY_TAGGER + '01 Fergalicious (Feat. Will.I.Am).mp3')
    FILE_PATH_2 = str(SAMPLE_FOLDER + SPOTIFY_TAGGER + '01 Forever (Main Version) 1.mp3')
    
    test_music_1 = mp3.Mp3(FILE_PATH_1)
    test_music_2 = mp3.Mp3(FILE_PATH_2)
    
    def test_title(self):
        self.assertEqual(TestMp3.test_music_1.get_title(), 'Fergalicious')
        self.assertEqual(TestMp3.test_music_2.get_title(), 'Forever')
        
    def test_artist(self):
        self.assertEqual(TestMp3.test_music_1.get_artist(), 'Fergie')
        self.assertEqual(TestMp3.test_music_2.get_artist(), 'Chris Brown')
        
    def test_album(self):
        self.assertEqual(TestMp3.test_music_1.get_album(), 'The Dutchess')
        self.assertEqual(TestMp3.test_music_2.get_album(), 'Forever')
        
if __name__ == '__main__':
    unittest.main()



