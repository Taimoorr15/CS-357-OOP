# Create a class Book with title, author, and price, and overload the print using __str__()

class book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def __str__(self):
        return "Book: "+self.title+"\nAuthor: "+self.author+"\nPrice: "+str(self.price)

book1 = book("Maths","Taimoor",1200)
print(book1)