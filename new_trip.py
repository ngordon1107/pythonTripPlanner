from utils import setDate, setAccommodations, setFlight, optional_message


def newTrip(trips):
    while True:
        trip_name = input("Awesome! Let’s start planning! To start off, what would you like to call this trip? \n>> ")
        if trip_name == "":
            print("\n**Error: You must enter a trip name!\n")
            continue
        # Checking for duplicate keys(trip names)
        elif trip_name in trips.keys():
            print("\n**Error: It looks like we already have a trip with this name. Please rename your trip, or go to edit mode to edit the existing trip.\n")
            return
        else:
            country_region = input(f"Great! Which country/region will your {trip_name} be taking place? {optional_message} \n>> ")
            city = input(f"Is there a particular city you’re visiting? {optional_message}\n>> ")

            # Collecting and Validating date input
            arrival = setDate("arrival")
            departure = setDate("departure")

            general_notes = input(f"{optional_message} Any notes you would like to add to this trip?\n>> ")

            # Adding base trip details to list
            trips[trip_name] = {
                "City": city,
                "Country/Region": country_region,
                "Arrival": arrival,
                "Departure": departure,
                "Notes": general_notes
            }

            # Prompt for Hotel and Flight information. If not skipped, add to the dictionary
            setAccommodations(trips, trip_name)
            setFlight(trips, trip_name)

            #
            print("\nYour trip has been added! Returning to homepage...")
            return