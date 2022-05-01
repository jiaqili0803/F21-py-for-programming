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
    with open(this_file,encoding='iso8859') as f:
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
    min_len = min(len(x),len(y))
    for x in range(min_len):
        if ord(x[i]) > ord(y[i]):
            return ">"
        if ord(x[i]) < ord(y[i]):
            return "<"
    if len(x) < len(y):
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
    
    Returns: music_array
    """
    for x in range(len(music_array)):
        ids = x
        for y in range(x+1, len(music_array)):
            if music_array[ids][1] < music_array[y][1]:
                ids = y
            music_array[x] , music_array[ids] = music_array[ids] , music_array[x]
            
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
       
           
def inSortTracks(music_array):
    for x in range(1,len(music_array)):
        z = music_array[x]
        y = x-1
        while y>=0 and z[2]>music_array[y][2]:
            music_array[y+1] = music_array[y]
            y -= 1
        music_array[y+1] = z 
    return music_array
    
    
    

def altSortTracks():
    
    return music_array

def timeInSortTracks():
    beginTime = timeit.default_timer()
    for x in range(1000):
        inSortTracks(music_array)
    return timeit.default_timer() - beginTime

def timeAltSortTracks():
    beginTime = timeit.default_timer()
    for x in range(1000):
        altSortTracks(music_array)
    return timeit.default_timer() - beginTime


############################# music array

music_array = initialize()
music_array = readFile(music_array, './music.csv')

############################# main

def main():
    time1 = timeBiSearchArtist()
    time2 = timeSeqSearchArtist()
    time3 = timeBubbleSortAlbums()
    time4 = timeAltSortAlbums()
    time5 = timeInSortTracks()
    time6 = timeAltSortTracks()
    
    # print
    print('Time Binary Search: ' + round(time1, 5))
    print('Time Sequential Search: ' + round(time2, 5))
    print('Time bubble Sort: ' + round(time3, 5))
    print('Time Selection Sort: ' + round(time4, 5))
    print('Time In Sort: ' + round(time5, 5))
    print('Time Alt Sort: ' + round(time6, 5))
    
    printData(bubbleSortAlbums(music_array))
if __name__ == '__main__':
    main()
    
########## 
# Q: Based on this project, can you say that a binary search is more efficient than a sequential search? 

# A: We can not say so. We need more data/experiment/comparation.

########## 
# Q: Can you say that one sort is more efficient than another? Why or why not? 

# A: We can not say so. We need more data/experiment/comparation.
