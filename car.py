class Car:
    def __init__(self,model,manufacturer,type):
        self.model = model
        self.manufacturer = manufacturer
        self.type = type
    def __str__(self):
        return(f"The car {self.model} by {self.manufacturer} of type {self.type}")
    def is_moving(self):
        return(f"The car with model number {self.model} is moving right now")