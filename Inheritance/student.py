class student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
    def display_info(self):
        print(self.name+" is a student with the following roll number: "+str(self.roll_number))
class representative(student):
    def __init__(self,name,roll_number,role):
        super().__init__(name,roll_number)
        self.role = role
    def display(self):
        print(self.name+" is a class representative")

std1 = student("Taimoor",6103)
std1.display_info()
print(" ")

std2 = representative("Azfar",6104,"CR")
std2.display_info()
std2.display()