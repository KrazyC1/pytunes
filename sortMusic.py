def sortMusic(music, sortBy):
    if sortBy ==  "artistName":
        sorted_music = sorted(music, key = lambda x: x[0])
        return sorted_music
    elif sortBy == "songName":
        sorted_music = sorted(music, key = lambda x: x[1])
        return sorted_music

#test
music = [("Drake","God's plan","2018", 3.19),("ArtistB","SongB","2018", 3.19),("ArtistA","SongA","2015",2.54),("ArtistC","SongC","2017",3.24),("Future","Mask Off","2014",3.45)]
sorted_music = sortMusic(music, "songName")
print(sorted_music)