import json

with open("stations.json", "r") as file:
    stations_data = json.load(file)

class Detective:
    def __init__(self, id):
        self.id = id
        self.bus_tickets = 8
        self.underground_tickets = 4
        self.taxi_tickets = 10
        self.current_node = None
    def getAvailableNodes(self):
        self.taxi_nodes_available = stations_data[self.current_node]["taxi"]
        self.bus_nodes_available = stations_data[self.current_node]["bus"]
        self.underground_nodes_available = stations_data[self.current_node]["underground"]
    def setNewNode(self):
        flag=0
        while flag==0:
            print(f"TAXI NODES AVAILABLE: {self.taxi_nodes_available}")
            print(f"BUS NODES AVAILABLE: {self.bus_nodes_available}")
            print(f"UNDERGROUND NODES AVAILABLE: {self.underground_nodes_available}")
            new_node=input(f"ENTER THE NEXT NODE FOR DETECTIVE {self.id}: ")
            if new_node in self.taxi_nodes_available or new_node in self.bus_nodes_available or new_node in self.underground_nodes_available:
                self.current_node = new_node
                self.getAvailableNodes()
                flag=1
            else:
                print(f"INVALID ARGUMENT CAN NOT ACCESS THAT NODE!")

def updateGame(detectives):
    for detective in detectives:
        detective.setNewNode()
        print(f"DETECTIVE {detective.id} - STARTING NODE: {detective.current_node}")
        print(f"AVAILABLE TAXI NODES: {detective.taxi_nodes_available}")
        print(f"AVAILABLE BUS NODES: {detective.bus_nodes_available}")
        print(f"AVAILABLE UNDERGROUND NODES: {detective.underground_nodes_available}")

def main():
    detective_count = int(input("HOW MANY DETECTIVES ARE PLAYING?: "))
    detectives = []

    for id in range(1, detective_count + 1):
        detectives.append(Detective(id))

    for detective in detectives:
        detective.current_node = input(f"ENTER THE STARTING NODE FOR DETECTIVE {detective.id}: ")
        detective.getAvailableNodes()

    updateGame(detectives)

if __name__ == "__main__":
    main()
