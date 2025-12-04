# Make a class Employee with name and salary. Inherit it into Manager and add department

class employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print("The employees name is "+self.name+" and their salary is "+str(self.salary))
class manager(employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
    def display_info2(self):
        print(self.name+" is the manager of "+self.department+" department")

employee1 = employee("John",1200)
employee1.display_info()
print(" ")

manager1 = manager("Taimoor",1200000000,"Developer")
manager1.display_info()
manager1.display_info2()