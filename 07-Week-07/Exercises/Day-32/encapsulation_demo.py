# encapsulation_demo.py
# exercise 3 for Day 32
# continue practice encapsulation

class BankAccount:
    def __init__(self, account_number, owner, opening_balance):
        self.account_number = account_number
        self.owner = owner
        # use double undescore for the balance attribute
        self.__balance = opening_balance

    def deposit(self, amount):
        if amount < 0:
            print("Cannot deposit a negative amount.")
        else:
            self.__balance += amount

    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


if __name__ == "__main__":
    ba = BankAccount(123456,"Glenn", 1000)
    ba.deposit(-5)
    print(f"Account Balance: {ba.get_balance()}")
    ba.deposit(20)
    print(f"Account Balance: {ba.get_balance()}")
    ba.withdraw(2000)
    print(f"Account Balance: {ba.get_balance()}")

    # let's try to access the __balance variable
    ba.__balance = 120000
    ba.__balance += 7000
    print(f"Account Balance: {ba.get_balance()}")