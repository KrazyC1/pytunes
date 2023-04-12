import unittest
import mp3

class TestMp3(unittest.TestCase):
    
    SAMPLE_FOLDER = 'C:./Users/matte/OneDrive/Documents/IntroToSoftwareEgineering'
    SPOTIFY_TAGGER = '/spotify-tagger/music/'
    #FILE_PATH_1 = str(SAMPLE_FOLDER + SPOTIFY_TAGGER + '01 Fergalicious (Feat. Will.I.Am).mp3')
    #FILE_PATH_2 = str(SAMPLE_FOLDER + SPOTIFY_TAGGER + '01 Forever (Main Version) 1.mp3')
    FILE_PATH_1 = 'C:/Users/matte/OneDrive/Documents/IntroToSoftwareEgineering/spotify-tagger/music/01 Fergalicious (Feat. Will.I.Am).mp3'
    FILE_PATH_2 = 'C:/Users/matte/OneDrive/Documents/IntroToSoftwareEgineering/spotify-tagger/music/01 Forever (Main Version) 1.mp3'
    
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
        
    def test_genre(self):
        TestMp3.test_music_1.set_genre("['dance pop', 'pop', 'post-teen pop', 'rap']")
        TestMp3.test_music_2.set_genre("['dance pop', 'r&b']")
        self.assertEqual(TestMp3.test_music_1.get_genre(), "['dance pop', 'pop', 'post-teen pop', 'rap']")
        self.assertEqual(TestMp3.test_music_2.get_genre(), "['dance pop', 'r&b']")
if __name__ == '__main__':
    unittest.main()