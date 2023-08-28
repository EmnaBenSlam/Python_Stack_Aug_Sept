class BankAccount:
    all_accounts = []
    def __init__ (self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance +=amount
        return self
    
    def withdraw(self, amount):
        if (self.balance-amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds: Charging a $5 fee")
            self.balance -=  5
        return self
        
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    
    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.interest_rate)
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            account.display_account_info()

class User:

    def __init__ (self,name):
        self.name = name
        self.account = {
            "Account1" : BankAccount(0.2, 1000),
            "Account2" : BankAccount (0.3 , 500)
        }

    def display_user_balance(self):
        print(f"user: {self.name}, Account1 Balance: {self.account['Account1'].display_account_info()}")
        print(f"user: {self.name}, Account2 Balance: {self.account['Account2'].display_account_info()}")
        return self
    
    def transfer_money (self,amount,user):
        self.amount -=amount
        user.amount +=amount
        self.display_user_balance()
        user.display_user_balance()
        return self

Mohamed= User("Mohamed")

Mohamed.account['Account1'].deposit(1000)
Mohamed.display_user_balance()


