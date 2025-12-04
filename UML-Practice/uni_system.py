class Person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def get_role(self):
        return "Your role is a Person"
    def describe(self):
        return "My name is "+self.name+" and my id number is "+str(self.id)
    
class Student(Person):
    def __init__(self,name,id,major,gpa):
        super().__init__(name,id)
        self.major = major
        self.gpa = gpa
    def study(self):
        return "I am currently studying in "+self.major
    def get_role(self):
        return "I am a student !!"

class Professor(Person):
    def __init__(self,name,id,department,title):
        super().__init__(name,id)
        self.department = department
        self.title = title
    def teach(self):
        return "I am teaching in "+self.department+" department"
    def get_role(self):
        return "I am a teacher"
    
class Staff(Person):
    def __init__(self,name,id,job_title,shift):
        super().__init__(name,id)
        self.job_title = job_title
        self.shift = shift
    def work(self):
        return "I work as a "+self.job_title+" during "+self.shift
    def get_role(self):
        return "I am a worker"
    
student1 = Student("Ali", 101, "Computer Science", 3.9)
print(student1.describe())       
print(student1.get_role())       
print(student1.study()) 
print("\n")

prof1 = Professor("Dr. Ahmed", 202, "Physics", "Associate Professor")
print(prof1.describe())          
print(prof1.get_role())          
print(prof1.teach())
print("\n")

staff1 = Staff("Nadeem", 303, "Janitor", "Night")
print(staff1.describe())         
print(staff1.get_role())         
print(staff1.work())


    
