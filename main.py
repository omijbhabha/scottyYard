import json

with open("stations.json", "r") as file:
    stations_data = json.load(file)

class Detective:
    def __init__(self, id):
        self.id = id
        self.taxi_tickets = 10
        self.bus_tickets = 8
        self.underground_tickets = 4
        self.current_node = None
    def getAvailableNodes(self):
        self.taxi_nodes_available = stations_data[self.current_node]["taxi"]
        self.bus_nodes_available = stations_data[self.current_node]["bus"]
        self.underground_nodes_available = stations_data[self.current_node]["underground"]
    def setNewNode(self):
        flag=0
        while flag==0:
            print()
            print(f"TAXI NODES AVAILABLE: {self.taxi_nodes_available}")
            print(f"BUS NODES AVAILABLE: {self.bus_nodes_available}")
            print(f"UNDERGROUND NODES AVAILABLE: {self.underground_nodes_available}")
            new_node=input(f"ENTER THE NEXT NODE FOR DETECTIVE {self.id}: ")
            if new_node in self.taxi_nodes_available:
                self.current_node = new_node
                self.getAvailableNodes()
                self.taxi_tickets-=1
                flag=1
            elif new_node in self.bus_nodes_available:
                self.current_node = new_node
                self.getAvailableNodes()
                self.bus_tickets-=1
                flag=1
            elif new_node in self.underground_nodes_available:
                self.current_node = new_node
                self.getAvailableNodes()
                self.underground_tickets-=1
                flag=1
            else:
                print(f"INVALID ARGUMENT CAN NOT ACCESS THAT NODE!")

def updateGame(detectives):
    for detective in detectives:
        detective.setNewNode()
        print(f"YOU HAVE {detective.taxi_tickets} TAXI TICKETS")
        print(f"YOU HAVE {detective.bus_tickets} BUS TICKETS")
        print(f"YOU HAVE {detective.underground_tickets} UNDERGROUND TICKETS")

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
