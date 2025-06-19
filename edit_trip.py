def editTrip(selectedTrip, trips):
    editTripMode = True
    while editTripMode:
        modifyKey = input(f"You are editing {selectedTrip}. Which detail would you like to change? (e.g. city, country/region, date etc.)\n>> ").strip()
        modifyKey = modifyKey[0:1].upper() + modifyKey[1:].lower()
        if modifyKey == "Country" or modifyKey == "Region":
            modifyKey = "Country/Region"
        if modifyKey == "Date":
            modifyKey = input("Which date would you like to update? Arrival or Departure?\n>> ")
        elif "date" in modifyKey:
            modifyKey = modifyKey[0:-4].strip()

        for key in trips.keys():
            if key.upper() == selectedTrip.upper():
               if modifyKey in trips[key].keys():
                   modifyValue = input(f"What new value would you like for {modifyKey}?\n>> ").strip()
                   trips[key][modifyKey] = modifyValue
                   print(f"{modifyKey} updated to {modifyValue}.")
                   editTripMode = False
                   return
        print("\n*** Error: Invalid input! Please double-check your spelling or double-check that the data type is associated with your trip!\n")
        editTripMode = False

