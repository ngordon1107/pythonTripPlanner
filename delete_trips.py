from utils import getDestination, getDate, getCurrentTrips

def deleteTrip(trips):
    deleteTripMode = True
    while deleteTripMode:
        selectedTrip = input(f""" Which trip would you like to delete? 
{getCurrentTrips(trips)}""")

        deleteTripMode = False