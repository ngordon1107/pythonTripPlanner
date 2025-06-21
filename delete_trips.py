def deleteTrip(selectedTrip, trips):
    while True:
        for key in trips.keys():
            if key.casefold() == selectedTrip.casefold():
                del trips[key]
                print(f"\n-*-*-*-*- {key} has been deleted. -*-*-*-*-\n")
                return