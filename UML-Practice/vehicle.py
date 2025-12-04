class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def start(self):
        return "I am startingg"
    def describe(self):
        return "Company: "+self.make+", Model: "+self.model+", Year: "+str(self.year)
    
class Car(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
    def open_trunk(self):
        return "Opening Trunkkk"
    def start(self):
        return "Car engine starting"
    
class Bike(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
    def pop_wheelie(self):
        return "I can pop a wheeliee vroomm"
    def start(self):
        return "kick-starting the bike"
    
class Truck(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
    def load_cargo(self):
        return "I can load alot of cargoo ahahaha(evil laugh)"
    def start(self):
        return "Truck is roaring back to life"
    
car1 = Car("Suzuki","Alto",2025)
print(car1.describe())
print(car1.start())
print(car1.open_trunk())
print(" ")

bike1 = Bike("Yamaha","R1",2025)
print(bike1.describe())
print(bike1.start())
print(bike1.pop_wheelie())
print(" ")

truck1 = Truck("Mercedes","Big Truck",2024)
print(truck1.describe())
print(truck1.start())
print(truck1.load_cargo())
