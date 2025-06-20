def deleteTrip(selectedTrip, trips):
    deleteTripMode = True
    while deleteTripMode:
        for key in trips.keys():
            if key.casefold() == selectedTrip.casefold():
                break
        del trips[key]
        print(f"\n-*-*-*-*- {key} has been deleted. -*-*-*-*-\n")
        deleteTripMode = False