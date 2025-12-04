# Create a class Account with a private method __check_pin() and a public method withdraw(). 
# The withdraw method should call the private method to check PIN before proceeding

class Account():
    def __init__(self,pin,withdrawl):
        self.pin = pin
        self.withdrawl = withdrawl
    def __checkpin(self):
        print("Your pin is correct!")
    def withdraw(self):
        self.__checkpin()
        print("Processing...\nWithdrawing your payment\nThank you for choosing us :)")
        


account1 = Account("1234","1200")
account1.withdraw()