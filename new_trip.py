from utils import setDate

def new_trip(trips):
    newTripMode = True
    while newTripMode:
        trip_name = input("Awesome! Let’s start planning! To start off, what would you like to call this trip? ")
        if trip_name == "":
            print("\n**Error: You must enter a trip name!\n")
            continue
        # Checking for duplicate keys(trip names)
        elif trip_name in trips.keys():
            print("\n**Error: It looks like we already have a trip with this name. Please rename your trip, or go to edit mode to edit the existing trip.\n")
            newTripMode = False
            return
        else:
            country = input(f"Great! Which country/region will your {trip_name} be taking place? ")
            city = input(f"(Optional, press enter to skip) Is there a particular city you’re visiting? ")

            # Collecting and Validating date input
            arrival = setDate("arrival")
            departure = setDate("departure")

            # Adding trip details to list
            trips[trip_name] = {
                "City": city,
                "Country": country,
                "Arrival": arrival,
                "Departure": departure,
                # "Hotel":
                #     {
                #       "Name": name,
                #       "Address": address,
                #       "Phone": phone,
                #       "Check in": hotel_check_in,
                #       "Check out": hotel_check_out,
                #       "Total Cost": cost,
                #       "Notes": notes
                #     }
                # "Flight":
                #     {
                #         "Airline": airline,
                #         "Departure": flight_departure,
                #         "Arrival": flight_arrival
                #     }
            }
            print("\nYour trip has been added! Returning to homepage...")
            newTripMode = False