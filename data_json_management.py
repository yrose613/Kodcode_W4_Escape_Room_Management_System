"""
import json
from pathlib import Path

# Keep the file beside the program, even when launched from another folder.
# __file__ is this module's path; .parent gets its folder and / adds a filename.
HISTORY_FILE = Path(__file__).parent / "game_history.json"


def load_game_history():
    # Return history, or raise a useful error if an existing file is damaged.
    try:
        # with closes the file automatically, including when reading fails.
        # json.load converts the file's JSON text into Python lists/dictionaries.
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            history = json.load(file)
    except FileNotFoundError:
        # A missing file is normal before the first game has been saved.
        return []

    # Make sure the loaded data has the fields needed by the interface.
    validate_history(history)
    return history

"""

# 

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

"""
 
# THE FUNCTION BELOW WRITES DATA TO THE FILE

def save_game(game):
    # Add a completed game and write the updated list directly to the JSON file.
    try:
        # Load first, then append, so earlier games stay in the updated list.
        history = load_game_history()
        history.append(game)
        # Write the full updated list directly to the history file.
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            # Indentation makes the JSON readable; ensure_ascii=False keeps
            # non-English names readable instead of writing escape sequences.
            json.dump(history, file, indent=4, ensure_ascii=False)
            file.write("\n")
    except (OSError, ValueError) as error:
        # Report the problem and let the menu continue without claiming success.
        print(f"Could not save the game: {error}")
        return False
    return True



"""



    


"""



def validate_history(history):
    # Check the basic structure needed to display history and statistics.
    # Valid JSON can still have the wrong structure, such as {} instead of [].
    if not isinstance(history, list):
        raise ValueError("Game history must contain a JSON list.")

    # Cycles through the list in the json file
    for game in history:
        if not isinstance(game, dict):
            raise ValueError("Each saved game must be a dictionary.")
        # Check keys before using them to avoid an unexpected KeyError later.
        required_keys = (
            "player_name", "rounds", "player_score", "computer_score",
            "winner", "results",
        )
        for key in required_keys:
            if key not in game:
                raise ValueError(f"A saved game is missing '{key}'.")
        if not isinstance(game["player_name"], str) or not game["player_name"].strip():
            raise ValueError("A saved player name is invalid.")
        for key in ("rounds", "player_score", "computer_score"):
            # An exact int check also rejects JSON booleans, which Python treats
            # as a kind of integer when using isinstance(value, int).
            if type(game[key]) is not int or game[key] < 0:
                raise ValueError(f"A saved game's '{key}' must be a non-negative integer.")


"""