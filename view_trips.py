from utils import getDate

def viewTrip(selectedTrip, trips):
    while True:
        # Grabbing original trip name -- accommodates instances where user utilizes unpredictable casing
        for trip_name in trips.keys():
            # If the original trip name is found, traverse the trip's details within the dictionary's key, value pairs.
            if trip_name.upper() == selectedTrip.upper():
                print(f"-*-*-*-*- Here are the details for your {trip_name} -*-*-*-*-\n")
                for subkey, subvalue in trips[trip_name].items():
                    # If the detail value is a simple string, display it directly
                    if type(subvalue) == str:
                        print(subkey + ": " + subvalue)
                    # If the subkey is "Arrival" collect both arrival and departure date for the trip
                    elif subkey == "Arrival":
                        print(subkey + ": " + getDate(trips[trip_name]))
                    # If the subvalue is a dictionary (flight details or accommodations info), traverse the key and value of that embedded dictionary
                    elif type(subvalue) == dict:
                        # Print the subkey (flight or accommodations) first
                        print(subkey + ":")
                        # Under the subkey, list each of the embedded subkeys and values
                        for embeddedsubkey, embeddedsubvalue in subvalue.items():
                            print(f"~ {embeddedsubkey}: {embeddedsubvalue}")
        print("\n-*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*-\n")
        return