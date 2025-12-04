class Person:
    def __init__(self, name: str, age: int, email: str):
        self._name = name
        self._age = age
        self._email = email

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, other: str):
        self._name = other

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, other: int):
        self._age = other

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, other: str):
        self._email = other

    def __str__(self):
        return f"{self._name} is {self._age} years old and has the email: {self._email}"

    