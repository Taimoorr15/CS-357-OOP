class car:
    def __init__(self,company,model,colour):
        self.company = company
        self.model = model
        self.colour = colour
    def drive(self):
        print("I can take you to your destination!")
    def display_info(self):
        print("Company: "+self.company+"- Model: "+self.model+"- Colour: "+self.colour)

car1 = car("Suzuki","Alto","White")
car1.drive()
car1.display_info()
print(" ")

car2 = car("Honda","Civic","Black")
car2.drive()
car2.display_info()
print(" ")

car3 = car("BMW","M5CS","White")
car3.drive()
car3.display_info()
print(" ")

car4 = car("Mercedes","AMG-E63","White")
car4.drive()
car4.display_info()