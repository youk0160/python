class BankAccount:
    allAccts=[]
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance):
        self.int_rate=(int_rate/100)
        self.balance=balance
        # don't worry about user info here; we'll involve the User class soon
    
    def deposit(self, amount):
        self.balance+=amount
        return self
        
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance-=amount
        else:
            print("Not enough balance")
        return self

    def display_account_info(self):
        print(f"Current balance {self.balance} with {self.int_rate} interest rate\n")

    def yield_interest(self):
        self.balance+=self.balance*self.int_rate
        return self

sam = BankAccount(4,87710)
chase = BankAccount(5,303220)

sam.deposit(300).deposit(7300).deposit(100).withdraw(2000).yield_interest().display_account_info()
chase.deposit(600).deposit(900).deposit(100).withdraw(20000000).yield_interest().display_account_info()
