class Student:
    count = 0
    total_gpa = 0

    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # INSTANCE METHOd
    def get_info(self):
        return f"{self.name} has a gpa of {self.gpa}"
    
    @classmethod
    def get_count(cls):
        return f"Total number of students are {cls.count}"
    
    @classmethod
    def average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa is {cls.total_gpa/cls.count}"
        
student1 = Student("Taimoor",3.8)
student2 = Student("Shaham",3.7)
student3 = Student("Owais",3.6)

print(Student.get_count())
print(Student.average_gpa())