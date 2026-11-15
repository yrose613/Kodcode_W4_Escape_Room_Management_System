import json
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(name)s - %(message)s"
)

EXISTING_BOOKINGS_DATA = Path(__file__).resolve().parent / "bookings.json"
EXISTING_ROOMS_DATA = Path(__file__).resolve().parent / "rooms.json"


# This function 'shoves' the json file into a variable
# Ultimately the function returns that variable
#   and when the function is called at a point in the program, it is assigned to a variable
#   and basically that variable stores the existing data, and can then manipulate it

def load_existing_bookings():
    try:
        with open(EXISTING_BOOKINGS_DATA, "r", encoding="utf-8") as file:
            existing_booking_data = json.load(file)
            logging.info("I guess this means it was loaded correctly")
    except FileNotFoundError:
        logging.error("Apparently the file wasn't foung")
        return []
    
    # Note: apparently this needs to be dealt with, i.e. it's not supposed to be caught here
    try:
        if isinstance(existing_booking_data, list):
            logging.info("I guess this means it's about to return")
            return existing_booking_data
        elif not isinstance(existing_booking_data, list):
            raise ValueError("\nThe JSON file's file 'outer shell' isn't a list, i.e. it's not formatted properly")
    except ValueError as e:
        print(e)


# Obviously the function below is redundant, and needs to be merged into the one above and made generic

def load_existing_rooms():
    try:
        with open(EXISTING_ROOMS_DATA, "r", encoding="utf-8") as file:
            existing_rooms_data = json.load(file)
            logging.info("I guess this means it was loaded correctly")
    except FileNotFoundError:
        logging.error("Apparently the file wasn't foung")
        return []
    
    # Note: apparently this needs to be dealt with, i.e. it's not supposed to be caught here
    try:
        if isinstance(existing_rooms_data, list):
            logging.info("I guess this means it's about to return")
            return existing_rooms_data
        elif not isinstance(existing_rooms_data, list):
            raise ValueError("\nThe JSON file's file 'outer shell' isn't a list, i.e. it's not formatted properly")
    except ValueError as e:
        print(e)

# existing_bookings = load_existing_bookings()



# For writing to JSON files you need the following 3 things

# 1. Load the file into the local variable
# 2. Deal with the local variable as if it's a regular variable
# 3. With the 'embelished' local variable, i.e. you've added, subtracted done stuff to the local list
#   you now take that variable and overwrite the entire original JSON file with it
#   in effect you overwrite everything but it's fine as the 'new' material
#   includes both the original and new

def make_json_adjustments(existing_bookings):
    pass

def test_duplicate_json():
    try:
        existing_bookings = load_existing_bookings()
        new_list_test = []
        for sub_dict in existing_bookings: # type: ignore
            new_list_test.append(sub_dict)
        
        for sub_dict in existing_bookings: # type: ignore
            new_list_test.append(sub_dict)
        
        # Now that we've finished doing the local manipulation on the code,
        #   we rewrite/overwrite it back to the file
        with open(EXISTING_BOOKINGS_DATA, "w", encoding="utf-8") as file:
            json.dump(new_list_test, file, indent=4, ensure_ascii=False)
            logging.info("Apparently it worked")
    except ValueError as error:
        # Report the problem and let the menu continue without claiming success.
        print(f"The following error was recorded: {error}")
        return False
    return True

test_duplicate_json()
