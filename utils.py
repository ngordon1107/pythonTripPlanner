def setDate(name):
    validDate = False
    while not validDate:
        dateInput = input(f"(Optional, press enter to skip) Do you have a date for your {name}? (MM/DD/YYYY)\n>> ")
        # Checking to see if user attempted to enter a date.
        if dateInput != "":
            # Validating that length of string is correct -- 10 characters (8 integers and 2 delimiters)
            if len(dateInput) == 10:
                # Validating int values were entered for MM, DD or YYYY inputs.
                try:
                    date_month = dateInput[0:2]
                    date_day = dateInput[3:5]
                    date_year = dateInput[6:10]
                    date = date_month + "/" + date_day + "/" + date_year
                    return date
                except:
                    print("You must enter a valid date!")
                    continue
            else:
                print("You must enter a valid date!")
                continue
        # Ending loop if user did not enter anything
        validDate = True
    return

def getDate(value):
    date = ""
    arrival = value["Arrival"]
    departure = value["Departure"]
    if arrival != "" and departure != "":
        date = arrival + "-" + departure
    elif departure != "":
        date = arrival
    elif arrival != "":
        date = departure
    return date

def getDestination(value):
    destination = "Coming Soon"
    city = value["City"]
    region = value["Country/Region"]
    if city != "" and region != "":
        destination = city + ", " + region
    elif city != "":
        destination = city
    elif region != "":
        destination = region
    return destination

def getCurrentTrips(trips):
    print("-*-*-*-*-Here are your current trips-*-*-*-*-\n")
    for key, value in trips.items():
        # Collecting the destination
        destination = getDestination(value)
        date = getDate(value)
        print(f"Name: {key} | Destination: {destination} | Date: {date}")
    print("\n-*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*-\n")

def getCleanedTripList(trips):
    cleaned_list = []
    for key in trips.keys():
            cleaned_list.append(key.upper())
    return cleaned_list



def modifyTrip(action, mode, trips):
    selectedTrip = input(f"Which trip would you like to {action}? \n>> ")
    if selectedTrip.upper() not in getCleanedTripList(trips):
        print("\n**Error: Invalid input, please try again! (Please be sure to double-check spelling and/or title)\n")
        return
    mode(selectedTrip, trips)