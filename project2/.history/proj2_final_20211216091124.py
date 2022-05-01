############################# import line
import timeit

############################# initial
rows = 296
cols = 3

# innitial empty array
def initialize():
    return [[None]*cols for x in range(rows)]


############################# read and structured file data

# read file to array
def readFile(music_array, this_file):
    # open the external file
    with open(this_file) as f:
        for ids,line in enumerate(f.readline()):
            artist, album, track = line.strip().split(',')
            album = int(album)
            track = int(track)
            music_array[ids][0] = artist
            music_array[ids][1] = album
            music_array[ids][2] = track
            
    return music_array
    
# print formatted grid
def printData(music_array):
    print('%-20s\t%-20s\t%-20s' % ('Artist', 'Album', 'Track'))
    for x in music_array:
        print('%-20s\t%-20s\t%-20s' %(x[0], str(x[1]), str(x[2])))
        

############################# 4 biSearchArtist + seqSearchArtist
def campare_str(x,y):
    x = x.lower().replace('-','')
    y = y.lower().replace('-','')
    if x == y:
        return '='
    elif len(x) < len(y):
        return '<'
    else:
        return '>'

def biSearchArtist(music_array, artist, start, end):
    if music_array[start][0] != artist and start == end:
        print('NOT FOUND')
        return -1
    if music_array[start][0] == artist and start == end:
        return start+1
    
    compare= campare_str(artist, music_array[(start+end)//2][0])
    if compare ==">":
        return biSearchArtist(music_array, artist, ((start+end)//2)+1, end)
    elif compare =="<":
        return biSearchArtist(music_array, artist, start, ((start+end)//2)-1)
    else:
        return ((start+end)//2)+1
    
def seqSearchArtist(music_array, artist):
    for x in range(len(music_array)):
        if music_array[x][0] == artist:
            return x+1
    return -1

def timeBiSearchArtist():
    beginTime = timeit.default_timer()
    for x in range(100000):
        biSearchArtist(music_array, 'Usher', 0, len(music_array)-1)
    return timeit.default_timer - beginTime

def timeSeqSearchArtist():
    beginTime = timeit.default_timer()
    for x in range(100000):
        seqSearchArtist(music_array, 'Usher')
    return timeit.default_timer - beginTime


############################# 5 bubble sort algorithm + alt
    
def bubbleSortAlbums(music_array):
    for x in range(1, len(music_array)):
        for y in range(0, len(music_array)-x):
            if music_array[y][1] < music_array[y+1][1]:
                music_array[y], music_array[y+1] = music_array[y+1], music_array[y]
    return music_array


def altSortAlbums(music_array):
    """
    This is a selection sort
    """
    for x in range(len(music_array)):
        ids = x
        for y in range(x+1, len(music_array)):
            if music_array[ids][1] < music_array[y][1]:
                ids = y
            music_array[x] = music_array[ids]
            music_array[ids] = music_array[x]
    return music_array


def timeBubbleSortAlbums():
    beginTime = timeit.default_timer()
    for x in range(1000):
        bubbleSortAlbums(music_array)
    return timeit.default_timer() - beginTime

    
def timeAltSortAlbums():
    beginTime = timeit.default_timer()
    for x in range(1000):
        altSortAlbums(music_array)
    return timeit.default_timer() - beginTime


############################# 6 inSortTracks altSortTracks
       
           


timeInSortTracks