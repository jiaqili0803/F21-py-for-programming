#########################################
##### Name:  Jiaqi Li                       #####
##### Uniqname:   ellali                  #####
#########################################

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

class Song(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url='No URL', album="No Album", genre="No Genre", track_length= 0):
        
        super().__init__(title="No Title", author="No Author", release_year="No Release Year", url='No URL')
        # self.title = title
        # self.author = author
        # self.release_year = release_year
        # self.url = url
        self.album = album
        self.genre = genre
        self.track_length = track_length
        
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.genre}]"      
    
    def length(self):
        return self.track_length  
    
    

class Movie(Media):
    def __init__(self, title="No Title", author="No Author", release_year="No Release Year", url='No URL', rating=""):
        
        super().__init__()
        # self.title = title
        # self.author = author
        # self.release_year = release_year
        # self.url = url
        self.album = album
        self.genre = genre
        self.track_length = track_length
        
    def info(self):
        return f"{self.title} by {self.author} ({self.release_year}) [{self.genre}]"      
    
    def length(self):
        return self.track_length  
        



if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    pass
