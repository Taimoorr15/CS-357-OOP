class car:
    def __init__(self,model,company):
        self.model = model
        self.company = company
    def copy(self,other):
        self.model = other.model
        self.company = other.company
car1 = car("Alto","Suzuki")
car2 = car(" "," ")
car2.copy(car1)
print(car2.model,car2.company)