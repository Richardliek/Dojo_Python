
class user:

    def __init__(self, name):
        self.name = name
        self.amount = 0 

    def make_deposit(self, amount):
        self.amount += amount


    def make_withdrawal(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"user: {self.name}, Balance: {self.amount}")

richie = user("richie")
joanna = user("joanna")
Josh = user("josh")

richie.make_deposit(250)
richie.make_deposit(100)
richie.make_deposit(500)
richie.make_withdrawal(175)
richie.display_user_balance()

joanna.make_deposit(1000)
joanna.make_deposit(1200)
joanna.make_withdrawal(400)
joanna.make_withdrawal(500)
joanna.display_user_balance()

Josh.make_deposit(6000)
Josh.make_withdrawal(450)
Josh.make_withdrawal(33)
Josh.make_withdrawal(200)
Josh.display_user_balance()