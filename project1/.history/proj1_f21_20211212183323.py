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





if __name__ == "__main__":
    # your control code for Part 4 (interactive search) should go here
    pass
