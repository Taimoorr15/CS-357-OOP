# We use double underscores before a private functions name.

class student:
    def __init__(self,name):
        self.name = name
    def __display(self):
        print("Name: "+self.name)
    def access_private(self):
        self.__display()
s1 = student("Taimoor")
s1.access_private() # THIS WILL PRINT THE PRIVATE FUNCTION AND THIS IS THE CORRECT WAY
# s1.__display() 'student' OBJ HAS NO ATTRIVUTES '.__display()' AND PRIV FUNCTION CAN ONLY BE ACCESSED INSIDE CLASS
# IN SHORT THIS IS NOT THE CORRECT WAY TO PRINT PRIV FUNCTION IN LINE 11