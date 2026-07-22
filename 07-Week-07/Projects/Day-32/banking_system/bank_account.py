# bank_account.py
# implements the class BankAccount
# let's not raise an Exception for a negative opening or initial balance
# to keep it simple. Let's default to zero if initial_balance was negative


class BankAccount:
    def __init__(
        self, 
        account_number: str, 
        account_owner: str,
        initial_balance: float = 0.0,
    ):
        self.account_number = account_number
        self.account_owner = account_owner
        if initial_balance < 0:
            print("Invalid initial balance. Balance defaulted to $0.00.")
            self._balance = 0.0
        else:
            self._balance = initial_balance

    def deposit(self, amount: float) -> bool:
        print(f"Depositing ${amount:,.2f} into account {self.account_number}...")
        if amount <= 0.0:
            print("Deposit rejected. Amount must be greater than zero.")
            return False
        
        self._balance += amount
        print("Deposit successful")
        print(f"New balance: ${self._balance:,.2f}")
        return True

    def withdraw(self, amount: float) -> bool:
        print(f"Withdrawing ${amount:,.2f} from account {self.account_number}...")
        if amount <= 0.0:
            print("Withdrawal rejected. Amount must be greater than zero.")
            return False
        if amount > self._balance:
            print("Withdrawal rejected. Insufficient funds.")
            print(f"Available balance: ${self._balance:,.2f}")
            return False
        
        self._balance -= amount
        print("Withdrawal successful.")
        print(f"Remaining balance: ${self._balance:,.2f}")
        return True


    def get_balance(self) -> float:
        return self._balance

    def display_account(self) -> None:
        print("----------------------------------------")
        print(f"{"Account Number":<15}: {self.account_number}")
        print(f"{"Account Owner":<15}: {self.account_owner}")
        print(f"{"Current Balance":<15}: ${self._balance:,.2f}")
        print("----------------------------------------")



if __name__ == "__main__":
    my_bank_account = BankAccount("ABC-XYZ", "Glenn", 1200)

    # let's deposit an invalid amount
    my_bank_account.deposit(-1)
    # let's display the information
    my_bank_account.display_account()
    # let's deposit a valid amount
    my_bank_account.deposit(5)
    # display account
    my_bank_account.display_account()

    #let's withdraw zero
    my_bank_account.withdraw(0)
    # let's withdraw 200
    my_bank_account.withdraw(200)
    # let's withdraw 20
    my_bank_account.withdraw(20)
    # display account
    my_bank_account.display_account()

    #let's inquire our current balance
    balance = my_bank_account.get_balance()
    print(f"Current balance: ${balance:,.2f}")