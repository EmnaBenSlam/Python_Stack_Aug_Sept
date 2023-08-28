class BankAccount:
    all_accounts = []
    def __init__ (self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        print(type(self.balance))
        print(type(amount))
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

    
Mohamed = BankAccount(0.2, 1000)
Ali = BankAccount (0.3 , 500)



Mohamed.deposit(5000).deposit(3000).deposit(6000).withdraw(10000).yeild_interest().display_account_info()
Ali.deposit(15000).withdraw(5000).withdraw(14000).yeild_interest().display_account_info()

BankAccount.print_all_accounts()