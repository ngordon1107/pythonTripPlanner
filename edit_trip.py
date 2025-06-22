from utils import setDate, setFlightDateTime, setAccommodationsCheckInOut, setPhone


def editTrip(selectedTrip, trips):
    while True:
        modifyKey = input(f"You are editing {selectedTrip}. Which detail would you like to change? (e.g. city, country/region, date, flight or accommodations?)\n>> ").strip()
        modifyKey = modifyKey.title()
        # If the user enters either "country" or "region" it should correlate to key 'Country/Region'
        if modifyKey == "Country" or modifyKey == "Region":
            modifyKey = "Country/Region"
        elif modifyKey == "Date":
            modifyKey = input("Which date would you like to update? Arrival or Departure?\n>> ")
        # If the user enters a string with something like 'arrival date', 'departure date':
        elif "Date" in modifyKey:
            modifyKey = modifyKey[0:-4].strip()

        for key in trips.keys():
            # Grabbing original key value for trip name -- due to unique casing reasons
            if key.upper() == selectedTrip.upper():
               # Validating if the subkey exists (the label being edited within the trip)
               if modifyKey in trips[key].keys():
                   # Validating whether desired key (option) is the Flight subdict. If so, traverse the subdict and add the subdict value.
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

                           # Validating that the subkey (option) exists within the Flight subdict
                           if modifySubKey in trips[key]["Flight"].keys():

                               # Checking to see if subkey is a special value that requires unique error handling flow (departure/arrival date/time)
                               if modifySubKey == "Departure Date/Time":
                                   modifyValue = setFlightDateTime("departing", "vacation", "back home")
                               elif modifySubKey == "Arrival Date/Time":
                                   modifyValue = setFlightDateTime("arriving", "home", "to your destination")
                              # If subkey does not require special handling, simply prompt for it directly:
                               else:
                                   modifyValue = input(f"What new value would you like for {modifySubKey}?\n>> ").strip()

                               # Trying to see if I can combine this with Accommodations update as well
                               # # Update the Accommodations subdic with the new value and confirm the update with the user before existing the loop
                               # trips[key][modifyKey][modifySubKey] = modifyValue
                               # print(f"\nYour {modifyKey}'s {modifySubKey} was updated to {modifyValue}.")
                               break

                           # If subkey (option) does not exist within the Flight subdict, throw an error to the user and loop back to collecting a new subkey
                           else:
                               print("\n*** Error: Invalid data type, please check your spelling and pick from one of the data type options displayed!")
                               continue


                   # Validating whether desired key (option) is the subdict Accommodations. If so, traverse the Accommodations subdict and add the subdict value.
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
                           # Checking if user input is a valid key (option) in the Accommodations subdict
                           if modifySubKey in trips[key]["Accommodations"].keys():
                               # Checking to see if subkey is a special value "Phone" that requires unique error handling flow
                               if modifySubKey == "Phone":
                                   modifyValue = setPhone()
                               # Checking to see if subkey is a special value "Check In" or "Check Out" which require a unique error handling flow
                               elif ("Check In" == modifySubKey and "Check In" in trips[key]["Accommodations"].keys()) or ("Check Out" in trips[key]["Accommodations"].keys() and "Check Out" == modifySubKey):
                                   in_out = modifySubKey[5:]
                                   try:
                                       modifyValue = setAccommodationsCheckInOut(in_out)
                                   except:
                                       print("*** Error: Something went wrong! Please enter a valid entry! Did you mean you wanted to Check In or Check Out?")
                                       continue
                                   # Trying to see if I can add this to the bottom
                                   # else:
                                   #      trips[key][modifyKey][modifySubKey] = modifyValue
                                        # print(f"\nYour {modifyKey}'s {modifySubKey} was updated to {modifyValue}.")
                                        # break
                               # If subkey does not require special handling, simply prompt for it directly
                               else:
                                   modifyValue = input(
                                       f"What new value would you like for {modifySubKey}?\n>> ").strip()
                                   # trips[key][modifyKey][modifySubKey] = modifyValue
                                   # print(f"\nYour {modifyKey}'s {modifySubKey} was updated to {modifyValue}.")
                                   # break
                               # Trying to see if I can add this to flight updates as well
                               # Adding new string to accommodations subdict as a subvalue
                               # trips[key][modifyKey][modifySubKey] = modifyValue
                               # print(f"\nYour {modifyKey}'s {modifySubKey} was updated to {modifyValue}.")
                               break
                           # Error handling if user enters a non-existent key (option) in subdict
                           else:
                                print("\n*** Error: Invalid data type, please check your spelling and pick from one of the data type options displayed!")
                                continue


                   # If modifyKey is not a subdict, treat it like a normal string value:
                   else:
                       modifyValue = input(f"What new value would you like for {modifyKey}?\n>> ").strip()
                       trips[key][modifyKey] = modifyValue
                       print(f"\n{modifyKey} updated to {modifyValue}.")
                       return

                   # Adding subdict values from either Flight or Accommodations here
                   trips[key][modifyKey][modifySubKey] = modifyValue
                   print(f"\nYour {modifyKey}'s {modifySubKey} was updated to {modifyValue}.")
                   return
               # Error handling if user input is not a valid subkey (option) (the label being edited within the trip)
               else:
                   print("""\n*** Error: Invalid input! Please double-check your spelling or double-check that the data type is one of the following:
                                 City, Country/region, Date, Flight, Accommodations\n""")
                   continue

