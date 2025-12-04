class mobile:
    def __init__(self,company,model,color):
        self.company = company
        self.model = model
        self.color = color
    def purpose(self):
        print("I am your pocket friendly computer")
    def display_info(self):
        print("Company: "+self.company+" ,Model: "+self.model+" ,Color: "+self.color)

mobile1 = mobile("Iphone","14 Pro Max","Deep purple")
mobile1.purpose()
mobile1.display_info()
print(" ")

mobile2 = mobile("Iphone","15 Pro Max","Natural titanium")
mobile2.purpose()
mobile2.display_info()
print(" ")

mobile3 = mobile("Iphone","16 Pro Max","Desert Titanium")
mobile3.purpose()
mobile3.display_info()    