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
                    elif subkey == "Arrival":
                        print(subkey + getDate(key))
        print("\n-*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*-\n")
        viewTripMode = False