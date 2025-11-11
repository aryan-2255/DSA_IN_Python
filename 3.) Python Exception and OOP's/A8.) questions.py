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


# question 

class BankAccount:
     

     def __init__(self, a_n, ba):
          self.account_number = a_n
          self.balance = ba
    
     def withraw(self,amt):
        if(amt > self.balance):
             raise RuntimeError("insufficent balance")
        if(amt < 0):
             raise ValueError("invalid input")
     

p1 = BankAccount(1234,1000.0)
try:
     try:
        try:
            p1.withraw(1500)
        except RuntimeError as msg:
          print(msg)
     except ValueError as msg:
        print(msg)
except Exception:
     print("unknown error")
    

