import json
stations = open("stations.json", "r")
stations_data = json.load(stations)

class Detective:
    id
    bus_tickets=8
    underground_tickets=4
    taxi_tickets=10
    current_node=-1
class Mrx:
    bus_tickets=3
    underground_tickets=3
    taxi_tickets=4
    current_node=-1

def getPlayerCount():
    detective_count=int(input("HOW MANY DETECTIVES ARE PLAYING?: "))
    print("AUTOMATICALLY CREATING MrX")
    return detective_count

for i in range(1,getPlayerCount()):
    #dynamically create a different variable for each player
