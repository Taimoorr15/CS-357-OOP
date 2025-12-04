# Create a class Vehicle with method start_engine(). Inherit it in Car and add method play_music()

class vehicle:
    def __init__(self,company,manufacture):
        self.company = company
        self.manufacture = manufacture
    def display_info(self):
        print("This vehicle belongs to "+self.company+" and was manufactured on "+self.manufacture)
    def start_engine(self):
        print("This vehicle is starting")
class car(vehicle):
    def __init__(self,company,manufacture,type,model):
        super().__init__(company,manufacture)
        self.type = type
        self.model = model
    def play_music(self):
        print("Now playing your favourite song!")
    def display_info2(self):
        print("The vahicle is a "+self.model+" which is a "+self.type)

vehicle1 = vehicle("Suzuki","2025")
vehicle1.display_info()
vehicle1.start_engine()
print(" ")

car1 = car("Suzuki","2025","Hatchback","Alto")
car1.display_info()
car1.display_info2()
car1.play_music()
    