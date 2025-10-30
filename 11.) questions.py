#Q:- BankAccount
class InsucificentFunds(Exception):
         pass
class BankAccount:
    def __init__(self):
        self.AccountNumber=int(input("Enter the number"))
        self.Account_holder_name=input("Enter the name")
        self.balance=float(input("Enter the balance"))
    def withdraw(self):
        self.withdra = float(input("Enter the withdraw amount"))
        try:
            if(self.withdra > self.balance):
                raise InsucificentFunds("It has insucificent funds")
        except InsucificentFunds as msg:
            print(msg)
        else:
            print("fund is withdraw")
        
b1 = BankAccount()
b1.withdraw()