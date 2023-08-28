class User:
    def __init__(self,name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount
        return self

    def make_withdrawal(self,amount):
        self.amount -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self

        
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self
            

Ali = User("Ali")
Olfa = User("Olfa")
Edam=User("Edam")

Ali.make_deposit(100).make_deposit(300).make_deposit(500).make_withdrawal(400).display_user_balance()

Olfa.make_deposit(1000).make_deposit(1500).make_withdrawal (1200).display_user_balance()
        
Edam.make_deposit(15000).make_withdrawal(5000).make_withdrawal(4000).make_withdrawal(10000).display_user_balance()

Ali.transfer_money(150,Edam)