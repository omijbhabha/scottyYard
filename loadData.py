import json

def loadStationsData():
    with open("stations.json", "r") as file:
        stations_data = json.load(file)
    return stations_data