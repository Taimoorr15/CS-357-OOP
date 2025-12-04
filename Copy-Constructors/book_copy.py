class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def copy(self,other):
        self.title = other.title
        self.author = other.author
b1 = book("Maths","Taimoor")
b2 = book(" "," ")
b2.copy(b1)
print(b2.title,b2.author)