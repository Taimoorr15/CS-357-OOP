class movie:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre
    def __str__(self):
        return "You are watching "+self.name+" and it belong to the following genre "+self.genre
    
movie1 = movie("Superman","Action and Thriller")
print(movie1)