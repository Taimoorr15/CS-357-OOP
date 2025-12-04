# We will create a copy constructor for student in python

class student:
    def __init__(self,name,roll_number):
        self.name = name
        self.roll_number = roll_number
    def progress(self):
        print("I have been improving recently!")
    def copy(self,other):
        self.name = other.name
        self.roll_number = other.roll_number

s1 = student("Taimoor","B2411000")
s2 = student(" "," ")
s2.copy(s1)
print(s2.name,s2.roll_number)