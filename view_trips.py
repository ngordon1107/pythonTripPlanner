from utils import getDestination, getDate, getCurrentTrips
import datetime

def viewTrip(selectedTrip, trips):
    viewTripMode = True
    while viewTripMode:
        for key in trips.keys():
            if key.upper() == selectedTrip.upper():
                print(f"-*-*-*-*-Here are the details for your {key} Trip-*-*-*-*-\n")
                for subkey, subvalue in trips[selectedTrip].items():
                    if type(subvalue) == str:
                        print(subkey + ": " + subvalue)
                    elif subkey == "Arrival":
                        print(subkey + getDate(key))
        print("\n-*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*-\n")
        viewTripMode = False