from utils import setFlightDateTime, setAccommodationsCheckInOut, setPhone, setDate


def editTrip(selectedTrip, trips):
    while True:
        modifyKey = input(f"You are editing {selectedTrip}. Which detail would you like to change? (e.g. trip name, city, country/region, date, general trip notes, flight or accommodations?)\n>> ").strip()
        modifyKey = modifyKey.title()

        # If the user enters either "country" or "region" it should correlate to name 'Country/Region'
        if "Name" in modifyKey:
            modifyKey = selectedTrip
        elif modifyKey == "Country" or modifyKey == "Region":
            modifyKey = "Country/Region"
        elif modifyKey == "Date":
            modifyKey = input("Which date would you like to update? arrival or departure?\n>> ").title()
        # If the user enters a string with something like 'arrival date', 'departure date':
        elif "Date" in modifyKey:
            modifyKey = modifyKey[0:-4].strip()
        elif "Trip Notes" in modifyKey:
            modifyKey = "Notes"

        for trip_name in trips.keys():
            # Grabbing original trip name -- due to unique casing reasons
            if trip_name.upper() == selectedTrip.upper():
                # Validating if the user is trying to edit the trip name
                if modifyKey == selectedTrip:
                   newTripName = input("What would you like to call this trip?\n>> ")
                   # Saving the details for the trip associated with old trip name
                   temp = trips[trip_name]
                   # Adding new trip name to the database and transferring details from original trip name in
                   trips[newTripName] = temp

                   # Deleting trip associated with old name
                   del trips[trip_name]

                   print(f"Your trip name has been updated from {trip_name} to {newTripName}!")
                   return
               # Validating if the user is trying to edit a subkey within the trip and whether that subkey exists (the label being edited within the trip)
                elif modifyKey in trips[trip_name].keys():
                   # Validating whether desired key (modifyKey) is the Flight subdict. If so, traverse the subdict and add the subdict value.
                   if modifyKey == "Flight":
                       while True:
                           # Collecting subkey (option) the user would like to edit
                           modifySubKey = input(f"""Which flight detail would you like to edit? Options:
    Airline
    Departure Date/Time
    Departure Confirmation Number
    Arrival Date/Time
    Arrival Confirmation Number
>> """).strip().title()

                           # Validating that the subkey (modifySubKey) exists within the Flight subdict
                           if modifySubKey in trips[trip_name]["Flight"].keys():

                               # Checking to see if subkey is a special value that requires unique error handling flow (departure/arrival date/time)
                               if modifySubKey == "Departure Date/Time":
                                   modifyValue = setFlightDateTime("departing", "vacation", "back home")
                               elif modifySubKey == "Arrival Date/Time":
                                   modifyValue = setFlightDateTime("arriving", "home", "to your destination")
                              # If subkey does not require special handling, simply prompt for it directly:
                               else:
                                   modifyValue = input(f"What new value would you like for {modifySubKey}?\n>> ").strip()
                               break

                           # If subkey (modifySubKey) does not exist within the Flight subdict, throw an error to the user and loop back to collecting a new subkey
                           else:
                               print("\n*** Error: Invalid data type, please check your spelling and pick from one of the data type options displayed!")
                               continue

                   # Validating whether desired key (modifyKey) is the subdict Accommodations. If so, traverse the Accommodations subdict and add the subdict value.
                   elif modifyKey == "Accommodations":
                       # Collecting subdict key with accommodations subdict options
                       modifySubKey = input(f"""Which flight detail would you like to edit? Options:
    Name 
    Address
    Phone
    Check In
    Check Out
    Cost
    Notes
>> """).strip().title()
                       while True:
                           # Checking if user input is a valid subkey (modifySubKey) within the Accommodations subdict
                           if modifySubKey in trips[trip_name]["Accommodations"].keys():
                               # Checking to see if subkey is a special value "Phone" that requires unique error handling flow
                               if modifySubKey == "Phone":
                                   modifyValue = setPhone()
                               # Checking to see if subkey is a special value "Check In" or "Check Out" which require a unique error handling flow
                               elif ("Check In" == modifySubKey and "Check In" in trips[trip_name]["Accommodations"].keys()) or ("Check Out" in trips[trip_name]["Accommodations"].keys() and "Check Out" == modifySubKey):
                                   try:
                                       modifyValue = setAccommodationsCheckInOut(modifySubKey)
                                   except:
                                       print("*** Error: Something went wrong! Please enter a valid entry! Did you mean you wanted to Check In or Check Out?")
                                       continue

                               # If subkey does not require special handling, simply prompt for it directly
                               else:
                                   modifyValue = input(
                                       f"What new value would you like for {modifySubKey}?\n>> ").strip()
                               break
                           # Error handling if user enters a non-existent subkey (modifySubKey) from subdict
                           else:
                                print("\n*** Error: Invalid data type, please check your spelling and pick from one of the data type options displayed!")
                                continue


                   # If modifyKey is not a subdict, treat it like a normal string value:
                   else:
                       # Validating if the key selected is arrival or departure which go through special date validation flow
                       if modifyKey == "Arrival" or modifyKey == "Departure":
                           modifyValue = setDate(modifyKey)
                       # If the key selected does not require special validation, collect the input directly as a string
                       else:
                           modifyValue = input(f"What new value would you like for {modifyKey.lower()}?\n>> ").strip()

                       # Update the key's value and then return to the home screen
                       trips[trip_name][modifyKey] = modifyValue
                       print(f"\n{modifyKey.lower()} updated to {modifyValue}.")
                       return

                   # Adding subdict values from either Flight or Accommodations here
                   trips[trip_name][modifyKey][modifySubKey] = modifyValue
                   print(f"\nYour {modifyKey.lower()}'s {modifySubKey.lower()} was updated to {modifyValue}.")
                   return
               # Error handling if user input is not a valid key (modifyKey) (the label being edited within the trip)
                else:
                   print("""\n*** Error: Invalid input! Please double-check your spelling or double-check that the data type is one of the following:
                                 Trip Name, City, Country/region, Date, General Trip Notes, Flight, Accommodations\n""")
                   continue
