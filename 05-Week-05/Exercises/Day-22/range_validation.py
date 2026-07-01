# range_validation
# accept integer input within the range 18 and 65

def read_age(prompt : str) -> int:
    while True:
        try:
            age = int(input(prompt).strip())
            if age in range(18,66):
                return age
            else:
                print("Age must be between 18 and 65.")
        except ValueError:
            print("Please enter a whole number.")

age = read_age("Enter Age: ")
print(f"Accepted Age: {age}")