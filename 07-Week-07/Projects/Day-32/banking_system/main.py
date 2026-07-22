# main.py
# application that uses the BankAccount class
from bank_account import BankAccount

print("========================================")
print("ENCAPSULATED BANKING SYSTEM")
print("========================================")

# Scenario 1
account1 = BankAccount("1001", "Glenn Ogapong", 1200.00) 
account2 = BankAccount("1002", "Lea Rodriguez", 900.00)
account3 = BankAccount("1003", "Invalid Balance Test", -300.00)
print("\nINITIAL ACCOUNT INFORMATION\n")
account1.display_account()
account2.display_account()
account3.display_account()


print("\nTRANSACTION TESTS\n")
# Scenario 2. Successful Deposit
account1.deposit(150)
account2.deposit(200)
account1_balance = account1.get_balance()
account2_balance = account2.get_balance()

# verify that operation succeeds and account balance update on account1
# did not affect balance on account2
print(f"Account 1 balance: ${account1_balance:,.2f}")
print(f"Account 2 balance: ${account2_balance:,.2f}")

# Scenario 3. Invalid deposit
account1.deposit(0)
account1.deposit(-200)
account2.deposit(-100)
#verify account 1 balance is unchanged
print(f"Account 1 balance: ${account1.get_balance():,.2f}")
#verify account 2 balance is unchanged
print(f"Account 2 balance: ${account2.get_balance():,.2f}")

# Scenario 4. Successful withdrawal
account1.withdraw(200.00)
account2.withdraw(50)

#verify account 1 balance is updated
print(f"Account 1 balance: ${account1.get_balance():,.2f}")
#verify account 2 balance is updated
print(f"Account 2 balance: ${account2.get_balance():,.2f}")

# Scenario 5. Withdrawal exceeding balance
account1.withdraw(3000)
account2.withdraw(2000)
#verify account 1 balance is unchanged
print(f"Account 1 balance: ${account1.get_balance():,.2f}")
#verify account 2 balance is unchanged
print(f"Account 2 balance: ${account2.get_balance():,.2f}")

# Scenario 6. Invalid Withdrawal amount
account1.withdraw(-200)
account2.withdraw(-50)
#verify account 1 balance is unchanged
print(f"Account 1 balance: ${account1.get_balance():,.2f}")
#verify account 2 balance is unchanged
print(f"Account 2 balance: ${account2.get_balance():,.2f}")

# Scenario 7. Final Account Summary

print("\nFINAL ACCOUNT INFORMATION\n")
account1.display_account()
account2.display_account()
account3.display_account()
