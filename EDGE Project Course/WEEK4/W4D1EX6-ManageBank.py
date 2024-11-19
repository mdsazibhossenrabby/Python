

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

class Bank:
    def __init__(self):
        self.accounts=[]

    def AddAccount(self,account):
        self.accounts.append(account)

    def TotalFunds(self):
        return sum(accounti.getBalance() for accounti in self.accounts)

account1=BankAccount(101,10000)
account2=BankAccount(102,15000)
bank=Bank()
bank.AddAccount(account1)
bank.AddAccount(account2)

print(f"Total Funds of both account : {bank.TotalFunds()}")