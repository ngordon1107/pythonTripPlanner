from types import NoneType


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
    # If there is both an arrival date and a departure date, add them to 'date' connected by a dash
    if arrival != None and departure != None:
        date = arrival + "-" + departure
    elif departure != None:
        date = arrival
    elif arrival != None:
        date = departure
    else:
        date = "TBD"
    return date

def getDestination(value):
    # Setting default destination if left empty
    destination = "Coming Soon"
    city = value["City"]
    region = value["Country/Region"]
    # If there is both a city and Country/Region add both to 'destination' separated by a  comma
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
        # Collecting the date
        date = getDate(value)
        print(f"Name: {key} | Destination: {destination} | Date: {date}")
    print("\n-*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*-\n")

# Use for modifyTrip data comparisons
def getCleanedTripList(trips):
    cleaned_list = []
    for key in trips.keys():
            cleaned_list.append(key.upper())
    return cleaned_list

def modifyTrip(action, mode, trips):
    selectedTrip = input(f"Which trip would you like to {action}? \n>> ")
    if selectedTrip.upper() not in getCleanedTripList(trips):
        print("\n**Error: Invalid trip name, please try again! (Please be sure to double-check spelling and/or title)\n")
        return
    mode(selectedTrip, trips)