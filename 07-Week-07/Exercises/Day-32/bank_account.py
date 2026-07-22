# bank_account.py
# exercise 2 for Day 32
# practice encapsulation

class BankAccount:
    def __init__(self, account_number, owner, opening_balance):
        self.account_number = account_number
        self.owner = owner
        self._balance = opening_balance

    def deposit(self, amount):
        if amount < 0:
            print("Cannot deposit a negative amount.")
        else:
            self._balance += amount

    def withdraw(self,amount):
        if amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance


if __name__ == "__main__":
    ba = BankAccount(123456,"Glenn", 1000)
    ba.deposit(-5)
    print(f"Account Balance: {ba.get_balance()}")
    ba.deposit(20)
    print(f"Account Balance: {ba.get_balance()}")
    ba.withdraw(2000)
    print(f"Account Balance: {ba.get_balance()}")