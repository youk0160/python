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
        print(f"current balance is {self.balance} with {self.int_rate} interest rate\n")

    def yield_interest(self):
        self.balance+=self.balance*self.int_rate
        return self

class User:
    def __init__(self, name, email, acct):
        self.name=name
        self.email=email
        self.acct=acct

    def make_deposit(self, amount):
        self.acct.deposit(amount)
        return self

    def withdrawal(self, amount):
        self.acct.withdraw(amount)
        return self

    def display_user_balance(self):
        print(f"{self.name} ", end="")
        self.acct.display_account_info()

    def transfer_money(self,other_user,amount):
        if self.is_enough_bal(amount):
            self.withdrawal(amount)
            other_user.make_deposit(amount)
    
    def is_enough_bal(self, amount):
        if self.acct_bal > amount:
            return True
        else:
            return False


chaseB = BankAccount(4,8000)

summer = User('Summer Lee', 's@l', chaseB)

summer.make_deposit(20000).withdrawal(21000).display_user_balance()
