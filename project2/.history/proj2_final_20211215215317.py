
#############################

rows = 296
cols = 3


def initialize():
    return [[None]*cols for x in range(rows)]








def readFile(music_array, this_file):
    # open the external file
    with open(this_file) as f:
        for id,line in enumerate(f.readline()):
            artist, album, track = line.strip().split(',')
            album = int(album)
            track = int(track)
            music_array[id][0] = artist
            music_array[id][1] = album
            music_array[id][2] = track
            
    return music_array
    

