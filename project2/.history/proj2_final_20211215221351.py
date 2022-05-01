
#############################

rows = 296
cols = 3

# innitial empty array
def initialize():
    return [[None]*cols for x in range(rows)]




# read file to array
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
    
# print formatted grid
def printData(music_array):
    print('%-20s\t%-20s\t%-20s' % ('Artist', 'Album', 'Track'))
    for x in music_array:
        print('%-20s\t%-20s\t%-20s' %(x[0], str(x[1]), str(x[2])))
        

#####################

def biSearchArtist():
    
           
