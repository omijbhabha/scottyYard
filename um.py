import json

stations = open("stations.json", "r")
stations_data = json.load(stations)

class Detective:
    def __init__(self, id):
        self.id = id
        self.bus_tickets = 8
        self.underground_tickets = 4
        self.taxi_tickets = 10
        self.current_node = -1

class MrX:
    def __init__(self):
        self.bus_tickets = 3
        self.underground_tickets = 3
        self.taxi_tickets = 4
        self.current_node = -1

def getPlayerCount():
    detective_count = int(input("HOW MANY DETECTIVES ARE PLAYING?: "))
    print("AUTOMATICALLY CREATING MrX")
    return detective_count

detectives = []

mr_x = MrX()

for player_id in range(1, getPlayerCount() + 1):
    detectives.append(Detective(player_id))

print(f"MrX created with tickets: Bus {mr_x.bus_tickets}, Underground {mr_x.underground_tickets}, Taxi {mr_x.taxi_tickets}")

detective_1=Detective(1)
print(detective_1.id)