class User:
    def __init__(self, name, email, acct_bal):
        self.name=name
        self.email=email
        self.acct_bal=acct_bal

    def make_deposit(self, amount):
        self.acct_bal+=amount
        return self

    def withdrawal(self, amount):
        if self.is_enough_bal(amount):
            self.acct_bal-=amount
        else:
            print("Not enough balance")
        return self

    def display_user_balance(self):
        print(f"{self.name}'s current balance is {self.acct_bal}")

    def transfer_money(self,other_user,amount):
        if self.is_enough_bal(amount):
            self.withdrawal(amount)
            other_user.make_deposit(amount)
    
    def is_enough_bal(self, amount):
        if self.acct_bal > amount:
            return True
        else:
            return False


summer = User('Summer Lee', 's@l', 3000)
john = User('John Garklic', 'ewe@ga', 20000)
peter = User('Peter Lamb', 'je@w', 1000000)

summer.make_deposit(20000).make_deposit(400).make_deposit(2342).withdrawal(21000).display_user_balance()
john.make_deposit(3000).make_deposit(3230).withdrawal(200).withdrawal(100).display_user_balance()
peter.make_deposit(3000).withdrawal(200).withdrawal(100).withdrawal(100).display_user_balance()

summer.transfer_money(peter, 2000)

summer.display_user_balance()
peter.display_user_balance()