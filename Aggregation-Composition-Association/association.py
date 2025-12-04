class Teacher:
    def __init__(self,name):
        self.name = name

class Student:
    def __init__(self,name):
        self.name = name

teacher = Teacher("Miss Humera")
student = Student("M.Taimoor")
print(f"{student.name} is taught by {teacher.name}")

# This is an Association example as the student and teacher just know each other and exist independently.