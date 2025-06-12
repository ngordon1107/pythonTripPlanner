import datetime as date

def setDate(name):
    validDate = False
    while not validDate:
        dateInput = input(f"(Optional, press enter to skip) Do you have a date for your {name}? (MM/DD/YYYY) ")
        # Checking to see if user attempted to enter a date.
        if dateInput != "":
            # Validating that length of string is correct -- 10 characters (8 integers and 2 delimiters)
            if len(dateInput) == 10:
                # Validating int values were entered for MM, DD or YYYY inputs.
                try:
                    date_month = int(dateInput[0:2])
                    date_day = int(dateInput[3:5])
                    date_year = int(dateInput[6:10])
                    return date.date(date_year, date_month, date_day)
                except:
                    print("You must enter a valid date!")
                    continue
            else:
                print("You must enter a valid date!")
                continue
        # Ending loop if user did not enter anything
        validDate = True
    return