# personal_notes_manager python program
# Day 16 Project/Implementation Assignment

# Requirements:
# - Be able to Add Notes
# - Be able to View Notes
# - Be able to Exit
### Acceptance Criteria
# - Notes are succesfully written to disk
# - Notes remain available after program restart
# - Program Exits without errors

# hard-coded filename for notes
personal_notes_text_file="personal_notes.txt"

# let's create our menu
def display_menu():
    print("1. Add Note")
    print("2. View Notes")
    print("3. Exit")

# let's add the notes just inputted to our notes file
def add_notes(note_text):
    with open(personal_notes_text_file, "a") as file:
        file.write(note_text + "\n")

# let's define view notes routine
def view_notes():
    with open(personal_notes_text_file,"r") as file:
        # read the file one line at a time 
        # treat the file as an iterator. this opens the file
        # from the disk as a stream, pauses when it sees
        # a newline character
        for line in file:
            # rstrip() removes trailing new lines
            print(line.rstrip())

# main routine

while True:
    display_menu()
    selection = int(input("Enter selection:"))
    if selection == 1:
        new_note=input("Enter note:")
        add_notes(new_note)
    elif selection == 2:
        view_notes()
    elif selection == 3:
        print("Exit")
        break
    else:
        continue
#### Note: This is not a try, except exercise to 
#          catch errors in input for the menus
#          Also,file that does not exist when viewing
#          notes is also not considered as this is not 
#          a part of the success criteria
