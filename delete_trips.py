def deleteTrip(selectedTrip, trips):
    while True:
        # Grabbing original trip name -- accommodates instances where user utilizes unpredictable casing
        for trip_name in trips.keys():
            if trip_name.upper() == selectedTrip.upper():
                # Once found, delete the trip name from the dictionary and display a success message
                del trips[trip_name]
                print(f"\n-*-*-*-*- {trip_name} has been deleted. -*-*-*-*-\n")
                return