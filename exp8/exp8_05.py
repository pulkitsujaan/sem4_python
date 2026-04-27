class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance    # private

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited {amount}. Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal must be positive.")
        elif amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount
            print(f"Withdrew {amount}. Balance: {self.__balance}")

acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(200)
acc.withdraw(2000)