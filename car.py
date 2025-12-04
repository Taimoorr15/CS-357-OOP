class car:
    def __init__(self,model,company):
        self.model = model
        self.company = company
    def __str__(self):
        return "The car is "+self.model+" from the company "+self.company
    
car1 = car("Alto","Suzuki")
print(car1)