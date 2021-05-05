class BankAccount:
    _allBankAccounts = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate = 0.01, balance = 0):
        self._allBankAccounts.append(self)
        self.int_rate = int_rate
        self.account_balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class 

    def deposit(self, amount):
        self.account_balance += amount
        return self
        # your code here

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        else:
            self.account_balance -= amount
        return self

    def display_account_info(self):
        # your code here
        print(f"Balance:{self.account_balance}")
        return self

    def yield_interest(self):
        # your code here
        if self.account_balance > 0:
            self.account_balance = self.account_balance * (1+self.int_rate)
        return self

    @classmethod
    def print_all_bank_accounts(self):
        for instance in BankAccount._allBankAccounts:
            print(instance.int_rate, instance.account_balance)



# checking = BankAccount(0.01, 200)
# checking.deposit(900).deposit(100).deposit(300).withdraw(400).yield_interest().display_account_info()

# savings = BankAccount(0.04, 1500)
# savings.deposit(400).deposit(100).withdraw(50).withdraw(20).withdraw(20).withdraw(700).yield_interest().display_account_info()

# # checking instances
# checking.print_all_bank_accounts()

class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def deposit(self, amount):
        self.account.deposit(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

bob = User("Bob", "bob@python.com")
bob.deposit(30).withdraw(25).display_user_balance()