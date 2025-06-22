import json
from new_trip import newTrip
from edit_trip import editTrip
from delete_trips import deleteTrip
from view_trips import viewTrip
from utils import getCurrentTrips, modifyTrip

db_file = "trips.json"

# Initializing Database
try:
    db = open(db_file, "r")
    trips = json.load(db)

# If there is no existing database file, create one
except:
    with open(db_file, "w") as db:
        trips = {}
        json.dump(trips, db)

print("Welcome to the Trip Planner App!")

while True:
    # If there were any previously added trips, display them here
    if len(trips.keys()) > 0:
        getCurrentTrips(trips)

    # Initiating Option Menu
    userInput = input("""
What would you like to do next? Please enter the appropriate keyword to proceed.

A = Add a new trip
V = View more details about a specific trip
E = Edit an existing trip/add more details to an existing trip
D = Delete an existing trip
Exit = Exit Program
>>> """)
    if userInput.upper() == "A":
        newTrip(trips)
    elif userInput.upper() == "EXIT":
        break
    else:
        # Error handling if user is attempting to enter a modifying trip mode when there are no trips saved
        if len(trips.keys()) == 0:
            print("*** Error: Please add a trip first!")
        elif userInput.upper() == "E":
            modifyTrip("edit", editTrip, trips)
        elif userInput.upper() == "V":
            modifyTrip("view in more detail", viewTrip, trips)
        elif userInput.upper() == "D":
            modifyTrip("delete", deleteTrip, trips)
        else:
            print("\n**Error: Invalid input, please try again!\n")
    # Saving trips to the database
    with open(db_file, "w") as db:
        json.dump(trips, db)