class Person:
    def __init__(self,name,age,CNIC):
        self.name = name
        self.age = age
        self.CNIC = CNIC
    def __str__(self):
        return(f"{self.name} is {self.age} years old and his CNIC number is {self.CNIC}")
    