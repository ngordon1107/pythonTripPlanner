from Data.data import createDB
from new_trip import new_trip

running = True
print("Welcome to the Trip Planner App!")

while running:
    # Initializing Trip Database
    try:
        # If Trip Planner has already been used, loading existing data
        tripDB = loadDB()
    except:
        # If Trip Planner has never been used or if the user never saved any data, create a new file to store the data
        tripDB = createDB()

    userInput = input("""
What would you like to do? Please enter the appropriate keyword to proceed.
    
A = Add a new trip
V = View more trip details 
E = Edit an existing trip/add more details to an existing trip
D = Delete an existing trip
Exit = Exit Program
>>> """)
    if userInput.upper() == "A":
        new_trip(tripDB)
    elif userInput.upper() == "E":
        while editTripMode:
            pass
    elif userInput.upper() == "V":
        while viewTripMode:
            pass
    elif userInput.upper() == "D":
        while deleteTripMode:
            pass
    elif userInput.lower() == "exit":
        running = False
    else:
        print("\n**Error: Invalid input, please try again!\n")


