from typing import Callable, Any, Optional, Dict, NamedTuple


def read_input(
    prompt: str,
    converter: Callable[[str], Any] = str,
    predicate: Optional[Callable[[Any], bool]] = None,
    error_message: str = "Invalid input. Please try again."
) -> Any:
    """
    Prompts the user for input until it passes conversion and an optional predicate check.
    
    :param prompt: The text displayed to the user.
    :param converter: A function to convert the string input (e.g., int, float).
    :param predicate: A function that takes the converted input and returns a boolean.
    :param error_message: Message displayed when validation fails.
    """
    while True:
        user_raw = input(prompt).strip()
        
        # 1. Try to convert the type
        try:
            converted_value = converter(user_raw)
        except (ValueError, TypeError):
            print(error_message)
            continue
            
        # 2. Check the predicate (if one is provided)
        if predicate is not None and not predicate(converted_value):
            print(error_message)
            continue
            
        return converted_value
    


# A simple data structure to hold the label and the function together
class MenuItem(NamedTuple):
    label: str
    action: Callable[[], None]

class ConsoleMenu:
    def __init__(self, title: str):
        self.title = title
        self._registry: Dict[str, MenuItem] = {}
        
    def add_option(self, key: str, label: str, action: Callable[[], None]) -> None:
        """Registers a new menu option and its corresponding function."""
        self._registry[key] = MenuItem(label, action)
        
    def _display(self) -> None:
        """Prints the menu UI dynamically based on registered items."""
        print(f"\n=== {self.title} ===")
        for key, item in self._registry.items():
            print(f"[{key}] {item.label}")
        print("====================")

    def run(self) -> None:
        """Starts the menu loop using your generic read_input logic."""
        while True:
            self._display()
            
            # Use a predicate to ensure the user only picks a valid registered key
            choice = read_input(
                prompt="Select an option: ",
                converter=lambda s: s.strip(),
                predicate=lambda s: s in self._registry,
                error_message="Invalid selection. Please try again."
            )
            
            # Dispatch! Execute the function associated with the choice
            action_to_run = self._registry[choice].action
            
            # If the function returns True (or a specific signal), break the loop to exit
            if action_to_run() == "EXIT":
                break


"""
read_input samples:
1. getting a simple integer

age = read_input("Enter your age: ", converter=int)

2. Getting an Integer within a Specific Range
rating = read_input(
    prompt="Rate your experience (1-10): ",
    converter=int,
    predicate=lambda x: 1 <= x <= 10,
    error_message="Please enter a whole number between 1 and 10."
)

3. Getting a Non-Empty String
name = read_input(
    prompt="Enter your username: ",
    predicate=lambda s: len(s) > 0,
    error_message="Username cannot be blank!"
)

4. Getting a Float Greater Than Zero

price = read_input(
    prompt="Enter the item price: ",
    converter=float,
    predicate=lambda x: x > 0.0,
    error_message="Price must be a positive number."
)

5. Matching a Specific Set of Choices

choice = read_input(
    prompt="Choose (yes/no/maybe): ",
    converter=lambda s: s.lower(),
    predicate=lambda s: s in ['yes', 'no', 'maybe'],
    error_message="Invalid choice. Choose 'yes', 'no', or 'maybe'."
)
"""


"""
Console Menu Sample

# 1. Define your menu actions (the functions)
def do_something():
    print("\n -> Doing something awesome right now!")

def do_something_else():
    print("\n -> Doing something else entirely!")

def exit_program():
    print("\nGoodbye!")
    return "EXIT"  # Signal to the menu loop to stop

# 2. Build and run the menu
if __name__ == "__main__":
    # Create the menu instance
    main_menu = ConsoleMenu("Main Utility Menu")
    
    # Register options into the dispatch table
    main_menu.add_option("1", "Run Awesome Task", do_something)
    main_menu.add_option("2", "Run Secondary Task", do_something_else)
    main_menu.add_option("q", "Quit", exit_program)
    
    # Run it!
    main_menu.run()
"""