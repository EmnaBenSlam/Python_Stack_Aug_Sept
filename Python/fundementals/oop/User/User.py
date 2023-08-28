class User:
    def __init__(self,name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawal(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

        
    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
            

Ali = User("Ali")
Olfa = User("Olfa")
Edam=User("Edam")

Ali.make_deposit(100)
Ali.make_deposit(300)
Ali.make_deposit(500)
Ali.make_withdrawal(400)
Ali.display_user_balance()

Olfa.make_deposit(1000)
Olfa.make_deposit(1500)
Olfa.make_withdrawal (1200)
Olfa.display_user_balance()
        
Edam.make_deposit(15000)
Edam.make_withdrawal(5000)
Edam.make_withdrawal(4000)
Edam.make_withdrawal(10000)
Edam.display_user_balance()

Ali.transfer_money(150,Edam)