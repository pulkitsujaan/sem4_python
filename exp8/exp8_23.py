class Account:
    def __init__(self, owner, balance):
        self.owner   = owner
        self.balance = balance

    def display(self):
        print(f"{self.owner}: Rs.{self.balance:.2f}")

class SavingsAccount(Account):
    interest_rate = 0.04

    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        print("Interest added.")

class CurrentAccount(Account):
    overdraft_limit = 10000

    def withdraw(self, amt):
        if amt <= self.balance + self.overdraft_limit:
            self.balance -= amt
            print(f"Withdrew Rs.{amt}")
        else:
            print("Overdraft limit exceeded.")

s = SavingsAccount("Raj", 50000)
s.add_interest()
s.display()

c = CurrentAccount("Priya", 1000)
c.withdraw(5000)
c.display()