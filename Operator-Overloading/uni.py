class university:
    def __init__(self,name,department):
        self.name = name
        self.department = department
    def __str__(self):
        return "You are enrolled in "+self.name+" and your department is "+self.department
    
uni1 = university("UBIT","BSCS")
print(uni1)