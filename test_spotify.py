import spotify
import mp3

home = '/Users/zaydrianprice/Documents'
spotify_tagger = '/spotify-tagger/music'
test_file = home + spotify_tagger + '/01 Fergalicious (Feat. Will.I.Am).mp3'
test_music = mp3.Mp3(test_file)
test_spotify=spotify.Spotify()
test_spotify.sync_spotify(test_music)
print(test_music)