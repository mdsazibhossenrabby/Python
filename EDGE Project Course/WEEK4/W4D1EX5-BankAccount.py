



class BankAccount:
    def __init__(self,accountNumber,balance=0):
        self.accountNumber=accountNumber
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        self.balance-=amount

    def getBalance(self):
        return  self.balance

account=BankAccount(1231,50000)
account.deposit(10000)
print(f"The Balance : {account.getBalance()}")
account.withdraw(5000)
print(f"The Balance : {account.getBalance()}")
