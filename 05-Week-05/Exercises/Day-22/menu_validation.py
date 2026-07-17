# menu validation

VALID_CHOICES = {"1","2","3","4"}

def read_menu_choice(prompt : str) -> str:
    while True:
        choice = input(prompt).strip()
        if choice in VALID_CHOICES:
            return choice
        else:
            print("Invalid menu selection.")


print(f"Available choices: {sorted(VALID_CHOICES)}")
choice = read_menu_choice("Enter Menu Selection:")
print(f"Option Accepted: {choice}")

