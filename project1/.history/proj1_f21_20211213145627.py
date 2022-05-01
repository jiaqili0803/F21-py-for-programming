#########################################
##### Name:  Jiaqi Li                       #####
##### Uniqname:   ellali                  #####
#########################################

import requests
import json

####################
###### Part 1 ######
####################
class Media:

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url='No URL'):
        self.title = title
        self.author = author
        self.release_year = release_year
        self.url = url
    
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year})"

    def length(self):
        return 0


# Other classes, functions, etc. should go here
# part1

class Song(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url='No URL', album="No Album", genre="No Genre", track_length= 0):  #consruct all attributes
        
        #inherente super's attributes
        super().__init__(title, author, release_year, url) 
        
        #self.title = title
        #self.author = author
        #self.release_year = release_year
        #self.url = url
        
        #only need new or override
        self.album = album
        self.genre = genre
        self.track_length = track_length
        
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.genre}]"      
    
    def length(self):
        return self.track_length/1000
    
    

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url='No URL', rating="No Rating", movie_length=0):
        
        super().__init__(title, author, release_year, url)
        #self.title = title
        #self.author = author
        #self.release_year = release_year
        #self.url = url
        self.rating = rating
        self.movie_length = movie_length
     
        
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.rating}]"      
    
    def length(self):
        return self.movie_length/60000
        

####################
###### Part 2 ######
####################

class Media:

    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url='No URL', json=None):
        self.json = json
        if self.json is not None:
            self.title = self.json['collectionName']
            self.author = self.json['artistName']
            self.release_year = self.json['releaseDate'][0:4]
            self.url = self.json['collectionViewUrl']
        else:
            self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url
           
    
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year})"

    def length(self):
        return 0

class Song(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url='No URL', json=None, album="No Album", genre="No Genre", track_length= 0):
        
        super().__init__(title, author, release_year, url, json)
        
        if self.json is not None:
            self.title = self.json['trackName'] #changed
            self.album = self.json['collectionName']
            self.genre = self.json['primaryGenreName']
            self.track_length = self.json['trackTimeMillis']
        else:
            self.album = album
            self.genre = genre
            self.track_length = track_length
            
        
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.genre}]"      
    
    def length(self):
        return int(self.track_length/1000)
    
    

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url='No URL', json=None, rating="No Rating", movie_length=0):
        
        super().__init__(title, author, release_year, url, json)
        
        if self.json is not None:
            self.title = self.json['trackName'] #changed
            self.rating = self.json['contentAdvisoryRating']
            self.movie_length = self.json['trackTimeMillis']
           
        else:
            self.rating = rating
            self.movie_length = movie_length
            
     
        
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.rating}]"      
    
    def length(self):
        return int(self.movie_length/60000)


####################
###### Part 3 ######
####################
#baseurl = "https://itunes.apple.com/search?"
#parameter_dictionary = {'rel_rhy':'blue'}
#response = requests.get(baseurl, parameter_dictionary)

response = requests.get('https://itunes.apple.com/search?term=jack+johnson&limit=25')   #json str
results_object = response.json()  # json str to dict


jack_johnson_list = results_object["results"]  #list with 25 dict
#print(type(jack_johnson_list))
print(len(jack_johnson_list))  #range = 25
for x in jack_johnson_list:
    print(x["trackName"])
    
    
    

if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    
    ####################
    ###### Part 4 ######
    ####################
    def itune_interface(input):
        if input = 'exit':
            exit()
        else:
            # get data
            itune_url = f"https://itunes.apple.com/search?term={input}"
            response = requests.get(itune_url)
            results_object = response.json()  # dict
            result = results_object["results"] # result_list
    
            #grouping
            songs = []
            movies = []
            other_media = []
            url = {}
            
            for item in result:
                #validation Keyerror
                try: 
                    if item['kind'] == 'song':
                        songs.append(Song(item))
                        
                    elif 'movie' in item['kind']:
                        movies.append(Movie(item))
                        
                    else:
                        other_media.append(Media(item))
                except KeyError:
                    pass # continue for loop
                
            
            # printing
            number = 1
            print('SONGS')
            for song in songs:
                print(f'{number}{Song.info()}')
                number = number+1
                
            print('MOVIES')
            print('OTHER MEDIA')
