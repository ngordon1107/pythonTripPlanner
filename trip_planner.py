import datetime as date

running = True
trips = {}
print("Welcome to the Trip Planner App!")

while running:
    newTripMode = False
    viewTripMode = False
    editTripMode = False
    deleteTripMode = False
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
            # Checking for duplicate keys(trip names)
            elif trip_name in trips:
                print("\n**Error: It looks like we already have a trip with this name. Please rename your trip, or go to edit mode to edit the existing trip.\n")
                newTripMode = False
                break
            else:
                country = input(f"Great! Which country/region will your {trip_name} be taking place? ")
                city = input(f"(Optional, press enter to skip) Is there a particular city you’re visiting? ")

                # Collecting and Validating date input
                validDate = False
                while not validDate:
                    arrival = input(f"(Optional, press enter to skip) Do you have an arrival date? (MM/DD/YYYY) ")
                    # Checking to see if user attempted to enter a date.
                    if arrival != "":
                        # Validating that length of string is correct -- 10 characters (8 integers and 2 delimiters)
                        if len(arrival) == 10:
                            # Validating int values were entered for MM, DD or YYYY inputs.
                            try:
                                arrival_month = int(arrival[0:2])
                                arrival_day = int(arrival[3:5])
                                arrival_year = int(arrival[6:10])
                                arrival = date.date(arrival_year, arrival_month, arrival_day)
                            except:
                                print("You must enter a valid date!")
                                continue
                        else:
                            print("You must enter a valid date!")
                            continue
                    departure = input(f"(Optional, press enter to skip) Do you have a departure date? (MM/DD/YYYY) ")
                    # Checking to see if user attempted to enter a date.
                    if departure != "":
                        # Validating that length of string is correct
                        if len(departure) == 10:
                            # Validating int values were entered for MM, DD or YYYY inputs.
                            try:
                                departure_month = int(departure[0:2])
                                departure_day = int(departure[3:5])
                                departure_year = int(departure[6:10])
                                departure = date.date(departure_year, departure_month, departure_day)
                            except:
                                print("You must enter a valid date!")
                                continue
                        else:
                            print("You must enter a valid date!")
                            continue
                    validDate = True

                # Adding trip details to list
                trips[trip_name] = {
                            "City": city,
                            "Country": country,
                            "Arrival": arrival,
                            "Departure": departure,
                            #"Hotel":
                            #     {
                            #       "Name": name,
                            #       "Address": address,
                            #       "Phone": phone,
                            #       "Check In": hotel_check_in,
                            #       "Check out": hotel_check_out,
                            #       "Total Cost": cost,
                            #     }
                        }
                print("Your trip has been added!")


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


