class animals:
    def __init__(self,name,location):
        self.name = name
        self.location = location
    def display_info(self):
        print(self.name+" is originally from "+self.location)
    def speak(self):
        print(self.name+" can make a sound")

class cat(animals):
    def sound(self):
        print(self.name+" can meowwww!!")

cat1 = cat("catto","earth")
cat1.display_info()
cat1.speak()
cat1.sound()