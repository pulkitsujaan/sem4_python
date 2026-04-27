class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amt):
        if amt <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amt

    def withdraw(self, amt):
        if amt > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amt

acc = Account(500)
try:
    acc.withdraw(1000)
except ValueError as e:
    print("Error:", e)

acc.deposit(200)
print("Balance:", acc.balance)