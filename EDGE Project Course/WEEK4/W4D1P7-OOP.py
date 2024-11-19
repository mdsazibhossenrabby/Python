

class BankAccount:
    
    def __init__(self,balance=0):
        self.balance=balance
        
    def Deposit(self,amount):
        self.balance+=amount
    
    def Withdraw(self,amount):
        if self.balance<amount:
            print(f"Trying to withdraw {amount} . Insufficient Balance")
            return True
        else:
            self.balance-=amount
    def checkBalance(self):
        return self.balance
    
account=BankAccount()
print(f"The Balance : {account.checkBalance()}")
account.Deposit(13230)
print("The account has 13230 deposit")
print(f"The Balance : {account.checkBalance()}")
if account.Withdraw(5000):
    pass
else:
    print("The account has 5000 Withdraw")
print(f"The Balance : {account.checkBalance()}")

if account.Withdraw(10000):
    pass
else:
    print("The account has 5000 Withdraw")
print(f"The Balance : {account.checkBalance()}")
