from new_trip import newTrip
from edit_trip import editTrip
from delete_trips import deleteTrip
from view_trips import viewTrip
from utils import getDestination, getDate, getCurrentTrips

trips = {}
running = True
print("Welcome to the Trip Planner App!")

while running:
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
    elif userInput.upper() == "E":
        editTrip(trips)
    elif userInput.upper() == "V":
        if len(trips.keys()) == 0:
            print("*** Error: No trips to display, please add a trip first!")
        else:
            selectedTrip = input("Which trip would you like to view in more details? \n>> ")
            viewTrip(selectedTrip)
    elif userInput.upper() == "D":
        if len(trips.keys()) == 0:
            print("*** Error: No trips to delete, please add a trip first!")
        else:
            deleteTrip(trips)
    elif userInput.upper() == "EXIT":
        running = False
    else:
        print("\n**Error: Invalid input, please try again!\n")


