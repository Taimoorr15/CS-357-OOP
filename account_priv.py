class account:
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def __password(self):
        print("Your password is: "+self.password)
    def access_private(self):
        self.__password()

acc1 = account("Taimoor","15")
print(acc1.username)
acc1.access_private()
        