# Both __str__ and __repr__ are dunder (double underscore)
# methods used to control how your object looks when printed, but they serve different audiences:
# str is for For readability – end user / casual viewer
# repr is for For debugging / developers

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"  # For users

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"  # For devs

b = Book("1984", "George Orwell")

print(str(b))   # 1984 by George Orwell
print(repr(b))  # Book('1984', 'George Orwell')

print(b)        # Uses __str__ if available
