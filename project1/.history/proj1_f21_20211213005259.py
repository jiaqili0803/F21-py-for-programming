#########################################
##### Name:  Jiaqi Li                       #####
##### Uniqname:   ellali                  #####
#########################################

####################
###### Part 1 ######
####################
'''class Media:

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
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url='No URL', album="No Album", genre="No Genre", track_length= 0):
        
        super().__init__(title="No Title", author="No Author", release_year="No Release Year", url='No URL')
        self.title = title
        self.author = author
        self.release_year = release_year
        self.url = url
        self.album = album
        self.genre = genre
        self.track_length = track_length
        
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.genre}]"      
    
    def length(self):
        return self.track_length/1000
    
    

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url='No URL', rating="No Rating", movie_length=0):
        
        super().__init__(title="No Title", author="No Author", release_year="No Release Year", url='No URL')
        self.title = title
        self.author = author
        self.release_year = release_year
        self.url = url
        self.rating = rating
        self.movie_length = movie_length
     
        
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.rating}]"      
    
    def length(self):
        return self.movie_length/60000
        '''

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
    def __init__(self, album="No Album", genre="No Genre", track_length= 0):
        
        super().__init__(title="No Title", author="No Author", release_year="No Release Year", url='No URL', json=None)
        
        if self.json is not None:
            '''self.title = self.json['trackName']
            self.author = self.json['artistName']
            self.release_year = self.json['releaseDate'][0:4]
            self.url = self.json['collectionViewUrl']'''
            self.album = self.json['collectionName']
            self.genre = self.json['primaryGenreName']
            self.track_length = self.json['trackTimeMillis']
        else:
            '''self.title = title
            self.author = author
            self.release_year = release_year
            self.url = url'''
            self.album = album
            self.genre = genre
            self.track_length = track_length
            
        
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.genre}]"      
    
    def length(self):
        return int(self.track_length/1000)
    
    

class Movie(Media):
    def __init__(self, rating="No Rating", movie_length=0):
        
        super().__init__(title="No Title", author="No Author", release_year="No Release Year", url='No URL', json=None)
        
        if self.json is not None:
            '''self.title = self.json['trackName']
            self.author = self.json['artistName']
            self.release_year = self.json['releaseDate'][0:4]
            self.url = self.json['collectionViewUrl']'''
            self.rating = self.json['contentAdvisoryRating']
            self.movie_length = self.json['trackTimeMillis']
           
        else:
            #self.title = title
            #self.author = author
            #self.release_year = release_year
            #self.url = url
            self.rating = rating
            self.movie_length = movie_length
            
     
        
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.rating}]"      
    
    def length(self):
        return int(self.movie_length/60000)

 
 

if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    pass

####################
###### Part 3 ######
####################
