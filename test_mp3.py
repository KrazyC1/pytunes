import unittest
import mp3

class TestSpotifyTagger(unittest.TestCase):
    
    FILE_PATH_1 = 'music/01 Fergalicious (Feat. Will.I.Am).mp3'
    FILE_PATH_2 = 'music/01 Forever (Main Version) 1.mp3'
    
    test_music_1 = mp3.Mp3(FILE_PATH_1)
    test_music_2 = mp3.Mp3(FILE_PATH_2)

    def test_file_path(self):
        self.assertEqual(self.test_music_1.file_path, self.FILE_PATH_1)
        self.assertEqual(self.test_music_2.file_path, self.FILE_PATH_2)

    def test_length(self):
        self.assertIsInstance(self.test_music_1.length, int)
        self.assertIsInstance(self.test_music_2.length, int)

    def test_date(self):
        self.test_music_1.set_date("2006-09-13")
        self.test_music_2.set_date("2008-06-09")
        self.assertEqual(self.test_music_1.get_date()[:4], "2006")
        self.assertEqual(self.test_music_2.get_date()[:4], "2008")

    def test_modify_metadata(self):
        self.test_music_1.set_title("New Title")
        self.test_music_1.set_artist("New Artist")
        self.test_music_1.set_album("New Album")
        self.test_music_1.set_genre("New Genre")
        self.assertEqual(self.test_music_1.get_title(), "New Title")
        self.assertEqual(self.test_music_1.get_artist(), "New Artist")
        self.assertEqual(self.test_music_1.get_album(), "New Album")
        self.assertEqual(self.test_music_1.get_genre(), "New Genre")

    def test_import_multiple_mp3_files(self):
        folder_path = 'music/'
        mp3_files = ['01 Fergalicious (Feat. Will.I.Am).mp3', '01 Forever (Main Version) 1.mp3']
        mp3_list = []
        for mp3_file in mp3_files:
            file_path = folder_path + mp3_file
            mp3_list.append(mp3.Mp3(file_path))
        self.assertEqual(len(mp3_list), 2)

if __name__ == '__main__':
    unittest.main()
