# # ---- Helper -----
# Use for modifyTrip data comparisons
def getCleanedTripList(trips):
    cleaned_list = []
    for key in trips.keys():
            cleaned_list.append(key.upper())
    return cleaned_list

# Prompt the user for the trip name, validate that the trip name exists, then pass the trip_name to the appropriate mode (edit, view, delete)
def modifyTrip(action, mode, trips):
    selected_trip = input(f"Which trip would you like to {action}? \n>> ")
    if selected_trip.upper() not in getCleanedTripList(trips):
        print(
            "\n**Error: Invalid trip name, please try again! (Please be sure to double-check spelling and/or title)\n")
        return
    mode(selected_trip, trips)

#  # ---- Variable -----
optional_message = "(Optional, press enter to skip)"
y_n_error = "*** Error: Please input either Y for yes or N for no!"

# # ---- Setters -----
def setDate(name, optional=True):
    while True:
        # Checking if the date is skippable/optional, if so, use the optional message in the data_input prompt
        if optional:
            date_input = input(f"{optional_message} Do you have a date for your {name.lower()}? (MM/DD/YYYY)\n>> ")
        # If the date is not skippable/optional do not use the optional message in the data_input prompt
        else:
            date_input = input(f"Do you have a date for your {name.lower()}? (MM/DD/YYYY)\n>> ")
        # Checking to see if user attempted to enter a date.
        if date_input != "":
            # Validating that length of string is correct -- 10 characters (8 integers and 2 delimiters)
            if len(date_input) == 10:
                date_month = date_input[0:2]
                date_day = date_input[3:5]
                date_year = date_input[6:10]
                # Validating int values were entered for MM, DD or YYYY inputs.
                try:
                    int(date_month)
                    int(date_day)
                    int(date_year)
                except:
                    print("You must enter a valid date!")
                    continue
                else:
                    date = date_month + "/" + date_day + "/" + date_year
                    return date
            else:
                print("You must enter a valid date!")
                continue
        # Ending loop if user did not enter anything
        return

def setTime(time_type):
    while True:
        time = input(f"What time will your {time_type.lower()} be? Must be 00:00 AM/PM format. e.g. 12:00 AM\n>> ")
        hour = time[0:2]
        mins = time[3:5]
        am_pm = time[6:8]
        try:
            int(hour)
            int(mins)
            am_pm = am_pm.upper()
        except:
            print("*** Error: Invalid date/time. Please ensure it is in the format: HH:MM AM or HH:MM PM! For example: 05:00 AM\n")
        else:
            if am_pm == "AM" or am_pm == "PM":
                return f"{hour}:{mins} {am_pm}"
            else:
                print("*** Error: Please be sure to use the format HH:MM AM or HH:MM PM (the space is required)!\n")

def setAccommodationsCheckInOut(in_out):
    while True:
        check_in_out_protocol = input(f"Does your accommodations have a specific {in_out} time? Y/N\n>> ")
        if check_in_out_protocol.upper() == "Y":
            accommodations_check_in_out = setTime(in_out)
        elif check_in_out_protocol.upper() == "N":
            accommodations_check_in_out = None
        else:
            print(y_n_error)
            continue
        return accommodations_check_in_out

def setPhone():
    while True:
        country_code = input(
            f"Does your accommodations phone number have a country code? {optional_message}\n>> ")
        phone = input(
            f"Please enter the remaining phone number without the country code for your accommodations {optional_message}:\n>> ")
        # If user does not enter a phone number, set the phone number to "N/A" as a default
        if phone == "":
            phone = "N/A"
        # Validate phone number has correct number of digits. 12 if only including area code and dashes, 10 if only including area code without dashes
        elif len(phone.strip()) == 12 or len(phone.strip()) == 10:
            phone = country_code + " " + phone
        else:
            print(
                "*** Error: Invalid phone number! If you are adding a country code, please do so in the next question when prompted for country code. Otherwise, please ensure your number is formatted as: 123-123-1234 or 1231231234!")
            continue
        return phone.strip()

def setAccommodations(trips, trip_name):
        while True:
            accommodations = input("Do you have any information for your accommodations yet? Y/N\n>> ").strip()
            # If user has information for their accommodations and enters "Y", begin the setAccommodations logic
            if accommodations.upper() == "Y":
                accommodations_name = input(f"Does your accommodations have a name? {optional_message}\n>> ")
                accommodations_address = input(f"What's the address of your accommodations? {optional_message}\n>> ")

                phone = setPhone()

                accommodations_check_in = setAccommodationsCheckInOut("check in")
                accommodations_check_out = setAccommodationsCheckInOut("check out")

                cost = input(f"How much is your accommodations? {optional_message}\n>> ")
                accommodations_notes = input("Any additional notes you'd like to add for your accommodations?\n>> ")

                # Adding accommodations information if it exists
                trips[trip_name]["Accommodations"] = {
                    "Name": accommodations_name,
                    "Address": accommodations_address,
                    "Phone": phone,
                    "Check In": accommodations_check_in,
                    "Check Out": accommodations_check_out,
                    "Cost": cost,
                    "Notes": accommodations_notes
                }
                break
            # If the user enters a non-valid value (neither "N" nor "Y") to the accommodations prompt, throw the yes no error (prompting them to enter either y or n) and restart the accommodations flow)
            elif accommodations.upper() != "N":
                print(y_n_error)
                continue
            # If user entered "N", break the while loop and end the function
            else:
                break

def setFlightDateTime(type, origin, destination):
    while True:
        # Prompt the user for the date of their flight. Customize the set Date message based on the type (arrival/departure), origin/destination (destination or home)
        flight_date = setDate(
            f"{type} flight (the date you will leave your {origin} to begin your travel {destination})", False)
        # Prompt the user for the time of their flight using the setTime function, customize the prompt based on arriving/departing flight
        flight_time = setTime(f"{type} flight")
        # Validating that a date and time were entered -- both are required fields
        if flight_date and flight_time:
            # Add the date and time to a string and return the value
            flight_datetime = flight_date + " " + flight_time
            return flight_datetime
        # If either the date or time is missing, throw and error to the user and restart the flight date/time flow
        else:
            print("\n*** Error: Please enter a valid date and time!")
            continue

def setFlight(trips, trip_name):
    while True:
        # Checking for Flight information
        flight = input("Do you have any flight information yet? Y/N\n>> ")
        # Validating whether user pressed "Y" to proceed
        if flight.upper() == "Y":
            airline = input("What airline are you flying with?\n>> ")
            # Getting departure and arrival date and time and confirmation

            flight_arrival = setFlightDateTime("arriving", "home","to your destination")
            arrival_confirmation = input("What is your arrival confirmation number?\n>> ")

            flight_departure = setFlightDateTime("departing", "vacation", "back home")
            depart_confirmation = input("What is your departure confirmation number?\n>> ")

            # Adding flight details to trip
            trips[trip_name]["Flight"] = {
                "Airline": airline,
                "Departure Date/Time": flight_departure,
                "Departure Confirmation Number": depart_confirmation,
                "Arrival Date/Time": flight_arrival,
                "Arrival Confirmation Number": arrival_confirmation,
            }
            return
        # If user pressed "N" to skip, then break the while loop and end the function
        elif flight.upper() == "N":
            break
        # If user entered an invalid input, throw the yes/no error (y/n error) and  restart the setFLight flow
        else:
            print(y_n_error)
            continue

# # ---- Getters -----
def getDate(value):
    date = ""
    arrival = value["Arrival"]
    departure = value["Departure"]
    # If there is both an arrival date and a departure date, add them to 'date' connected by a dash
    if arrival is not None and departure is not None:
        date = arrival + "-" + departure
    elif departure is not None:
        date = arrival
    elif arrival is not None:
        date = departure
    else:
        date = "TBD"
    return date

def getCurrentTrips(trips):
    print("-*-*-*-*-Here are your current trips-*-*-*-*-\n")
    for key, value in trips.items():
        # Collecting the destination
        # # Setting default destination if left empty
        destination = "Coming Soon"
        city = value["City"]
        country_region = value["Country/Region"]
        # If there is both a city and Country/Region add both to 'destination' separated by a  comma
        if city and country_region:
            destination = city + ", " + country_region
        # If there is only a city, the destination displayed is just the city
        elif city:
            destination = city
        # If there is only a country/region, the destination displayed is just the country/region
        elif country_region:
            destination = country_region

        # Collecting the date
        date = getDate(value)
        print(f"Name: {key} | Destination: {destination} | Date: {date}")
    print("\n-*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*--*-*-*-*-\n")
