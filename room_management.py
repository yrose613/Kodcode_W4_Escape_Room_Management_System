from data_json_management import load_existing_rooms

def display_rooms():
    try:
        existing_rooms = load_existing_rooms()
        for sub_dict in existing_rooms: # type: ignore
            print (sub_dict, end="\n")

    except ValueError as error:
        print(f"The following error was recorded: {error}")