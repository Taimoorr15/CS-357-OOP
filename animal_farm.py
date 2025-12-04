class Animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def make_sound(self):
        return "This animal can make a sound"
    def describe(self):
        return "I am "+self.name+" and I am "+str(self.age)+" years old"
    
class Bird(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def fly(self):
        return "I can fly!!"
    
class Mammal(Animal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def walk(self):
        return "I can walkk!!"
    
class Duck(Bird):
    def __init__(self,name,age):
        super().__init__(name,age)
    def make_sound(self):
        return "I can Quackkk"
    
class Parrot(Bird):
    def __init__(self,name,age):
        super().__init__(name,age)
    def make_sound(self):
        return "I can Squeakkkk"
    
class Cow(Mammal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def make_sound(self):
        return "I can mooooooo"
    
class Sheep(Mammal):
    def __init__(self,name,age):
        super().__init__(name,age)
    def make_sound(self):
        return "I can baaaaaaa"
    
d = Duck("Donald", 2)
print(d.describe())
print(d.make_sound())
print(d.fly())