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
        newTripMode = True
        while newTripMode:
            trip_name = input("Awesome! Let’s start planning! To start off, what would you like to call this trip? ")
            if trip_name == "":
                print("\n**Error: You must enter a trip name!\n")
                continue
            elif trip_name in trips:
                print("\n**Error: It looks like we already have a trip with this name. Please rename your trip, or go to edit mode to edit the existing trip.\n")
                newTripMode = False
                break
            else:
                trips.append({trip_name: {}})
            country = input(f"Great! Which country/region will your {trip_name} be taking place? ")
            city = input(f"(Optional, press enter to skip) Is there a particular city you’re visiting? ")
            validDate = False
            while not validDate:
                arrival = input(f"(Optional, press enter to skip) Do you have an arrival date? (MM/DD/YYYY) ")
                # Checking to see if user attempted to enter a date.
                if arrival != "":
                    # Validating that length of string is correct
                    if len(arrival) == 10:
                        try:
                            month = int(arrival[0:2])
                            day = int(arrival[3:5])
                            year = int(arrival[6:10])
                        except:
                            print("You must enter a valid date!")
                            continue
                    else:
                        print("You must enter a valid date!")
                        continue
                departure = input(f"(Optional, press enter to skip) Do you have a departure date? (MM/DD/YYYY) ")
                if departure != "":
                    # Validating that length of string is correct
                    if len(departure) == 10:
                        try:
                            month = int(departure[0:2])
                            day = int(departure[3:5])
                            year = int(departure[6:10])
                        except:
                            print("You must enter a valid date!")
                            continue
                    else:
                        print("You must enter a valid date!")
                        continue
                validDate = True
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


