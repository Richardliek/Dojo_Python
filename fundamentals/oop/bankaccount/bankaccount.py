class bankaccount:
    accounts = []
    def __init__(self,int_rate,balance): 
        self.int_rate = int_rate
        self.balance = balance
        bankaccount.accounts.append(self)

    def deposit(self,amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

Richard = bankaccount(.06,3000)
Joanna = bankaccount(.5,8000)

Richard.deposit(100).deposit(500).deposit(100).withdraw(200).yield_interest().display_account_info()
Joanna.deposit(400).deposit(500).deposit(111).withdraw(300).yield_interest().display_account_info()

bankaccount.print_all_accounts()