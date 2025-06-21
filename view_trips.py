from utils import getDate

def viewTrip(selectedTrip, trips):
    viewTripMode = True
    while viewTripMode:
        for key in trips.keys():
            if key.casefold() == selectedTrip.casefold():
                print(f"-*-*-*-*- Here are the details for your {key} -*-*-*-*-\n")
                for subkey, subvalue in trips[key].items():
                    if type(subvalue) == str:
                        print(subkey + ": " + subvalue)
                    # This will collect both arrival and departure for the trip
                    elif subkey == "Arrival":
                        print(subkey + ": " + getDate(trips[key]))
                    # If the subvalue is a dictionary (flight details or hotel info), traverse the key and value of that dictionary
                    elif type(subvalue) == dict:
                        print(subkey + ":")
                        for embeddedsubkey, embeddedsubvalue in subvalue.items():
                            print(f"~ {embeddedsubkey}: {embeddedsubvalue}")
        print("\n-*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*-\n")
        viewTripMode = False