from room_management import display_rooms


def main_menu_display():
    pass

def room_management_display():
    user_input = ""

    while user_input != "6":
        print(
"""
========================
Room Adjustment Menu
========================
1. Display all the rooms
2. Display the full details of a specific room
3. Add a new room
4. Update an existing room
5. Activate or deactivate a room
6. Go back to the main menu
"""
        )
        
        user_input = input("Please select an option from 1→5: ").strip()

        if user_input == "1":
            display_rooms()
        elif user_input == "2":
            print("You've selected option 2")
        elif user_input == "3":
            print("You've selected option 3")
        elif user_input == "4":
            print("You've selected option 4")
        elif user_input == "5":
            print("You've selected option 5")
        elif user_input == "6":
            print("You're being returned to the main menu.")
        else:
            print("You're option wasn't recognised. Please try again")


room_management_display()

    
# Let's say that I'm printing a menu in python, and then afterwards, I have an input().strip function, how do I ensure that if the user 
# and I want to have this 'validating' function 


# 2. Escape Room Management
# The system must support:
# 1. Displaying all rooms.
# 2. Displaying full details of a specific room.
# 3. Adding a new room.
# 4. Updating an existing room's details.
# 5. Activating or deactivating a room.
# Do not allow two rooms to be created with the same ID. An inactive room must not accept new bookings.
# Deactivating a room must not automatically cancel existing bookings.