# Will return to this in a bit.
# def loadDB():
#     with open("trips.json", "r") as data:
#         i = 0
#         obj = data.read()
#         for (key, value) in obj.items():
#             print(f"---- Trip{i}: {key} ----")
#             for (subkey, subvalue) in value.items():
#                 if type(subvalue) == dict:
#                     pass

def createDB():
    with open("trips.json", "w+") as new:
        file = new.readlines()
        trips = {}
        file.append(trips)
        return file