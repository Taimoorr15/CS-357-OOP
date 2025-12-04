class Student:
    def __init__(self,name,roll_number,section):
        self.name = name
        self.roll_number = roll_number
        self.section = section
    def study(self):
        print("Hey, I am " + self.name + " and I am here to study")
    def play(self):
        print("Hey, I am " + self.name + " and I like to play football")
    def display_info(self):
        print("Name: " +self.name+ ",Roll-Number: " +self.roll_number+ ", Section: " +self.section )

student1 = Student("Taimoor","B24110006103","BSCS-B")
student1.display_info()
student1.study()
student1.play()

student2 = Student("Babar","B24110006104","BSAI-A")
student2.display_info()
student2.study()
student2.play()

student3 = Student("Aleeza","B2411006105","BSCS-C")
student3.display_info()
student3.study()
student3.play()