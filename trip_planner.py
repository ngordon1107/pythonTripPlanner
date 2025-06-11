import datetime as date

running = True
trips = []


while running:
    newTripMode = False
    viewTripMode = False
    editTripMode = False
    deleteTripMode = False
    print("Welcome to the Trip Planner App!")
    userInput = input("""
What would you like to do? Please enter the appropriate keyword to proceed.
    
A = Add a new trip
V = View more trip details 
E = Edit an existing trip/add more details to an existing trip
D = Delete an existing trip
Exit = Exit Program
>>> """)
    if userInput.upper() == "A":
        new_Trip_mode = True
        while new_Trip_mode:
            title = input("What would you like for this trip to be called? ")
            if title not in trips:
                    trips.append({title:{}})
            else:
                print("\n**Error: It looks like we already have a trip with this name. Please rename your trip, or go to edit mode to edit the existing trip.\n")
                new_Trip_mode = False
                break
            city = input()
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


