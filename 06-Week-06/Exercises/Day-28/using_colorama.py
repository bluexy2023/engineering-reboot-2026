# a python script that uses the installed colorama package

from colorama import init, Fore, Back, Style

init()

# Changing text color
print(Fore.RED + "This is red text!")
print(Fore.GREEN + "This is green text!")

# Changing background color
print(Back.WHITE+ "This text has a white background!")

# Changing styles
print(Style.BRIGHT + "This is bright/bold text!")

# CRITICAL: Always reset back to default!
print(Style.RESET_ALL)
print("Back to normal terminal colors.")
