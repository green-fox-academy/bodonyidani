class Bank_account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        self.balance -= amount

    def receive(self, amount):
        self.balance += amount

    def print_balance(self):
        print(self.name)
        print(self.balance)

    def transfer(self, recipient, amount):
        self.pay(amount)
        recipient.pay(amount)

account1 = Bank_account("Jozsi szamlaja", 1000)

account1.pay(500)
account1.receive(1000)
account1.print_balance()

account2 = Bank_account("Malacka szamlaja", 100)

account2.transfer(account1, 100)

account1.print_balance()
account2.print_balance()
