class bank:
    def __init__(self,name,account_number,balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
    def greet(self):
        print("Hello "+self.name+" you have logged into your account")
    def __balance(self):
        print("Your account balance is: "+self.balance)
    def access_private(self):
        self.__balance()
    
acc1 = bank("Taimoor","122","1")
acc1.greet()
acc1.access_private()
