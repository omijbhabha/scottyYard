from loadData import loadStationsData
stations_data = loadStationsData()

class Player:    
    def __init__(self, id=None):
        self.id = id
        self.current_node = None
        self.taxi_tickets = 0
        self.bus_tickets = 0
        self.underground_tickets = 0
    
    def getAvailableNodes(self):
        self.taxi_nodes_available = stations_data[self.current_node]["taxi"]
        self.bus_nodes_available = stations_data[self.current_node]["bus"]
        self.underground_nodes_available = stations_data[self.current_node]["underground"]
    
    def printAvailableNodes(self):
        print("\n")
        print(f"TAXI NODES AVAILABLE: {self.taxi_nodes_available}")
        print(f"BUS NODES AVAILABLE: {self.bus_nodes_available}")
        print(f"UNDERGROUND NODES AVAILABLE: {self.underground_nodes_available}")

    def setNewNode(self):
        flag = 0
        while flag == 0:
            self.printAvailableNodes()
            new_node = input(f"\nENTER THE NEXT NODE FOR {'MR. X' if self.id is None else f'DETECTIVE {self.id}'}: ")
            if new_node in self.taxi_nodes_available:
                self.current_node = new_node
                self.getAvailableNodes()
                self.taxi_tickets -= 1
                flag = 1
            elif new_node in self.bus_nodes_available:
                self.current_node = new_node
                self.getAvailableNodes()
                self.bus_tickets -= 1
                flag = 1
            elif new_node in self.underground_nodes_available:
                self.current_node = new_node
                self.getAvailableNodes()
                self.underground_tickets -= 1
                flag = 1
            else:
                print(f"INVALID ARGUMENT CAN NOT ACCESS THAT NODE!")

    def printAvailableTickets(self):
        print()
        print(f"YOU HAVE {self.taxi_tickets} TAXI TICKETS")
        print(f"YOU HAVE {self.bus_tickets} BUS TICKETS")
        print(f"YOU HAVE {self.underground_tickets} UNDERGROUND TICKETS")
        print()

class Detective(Player):
    def __init__(self, id):
        super().__init__(id)
        self.taxi_tickets = 10
        self.bus_tickets = 8
        self.underground_tickets = 4

class MrX(Player):
    def __init__(self):
        super().__init__()
        self.taxi_tickets = 4
        self.bus_tickets = 3
        self.underground_tickets = 3
        self.black_fare_tickets = 5
        self.double_move_tickets = 2
    
    def getAvailableNodes(self):
        super().getAvailableNodes()
        self.black_nodes_available = stations_data[self.current_node]["black"]
    
    def printAvailableNodes(self):
        super().printAvailableNodes()
        print(f"BLACK FARE NODES AVAILABLE: {self.black_nodes_available}")

    def askForDoubleMove(self):
        ask_double_move = input("DO YOU WANT TO USE DOUBLE FARE? (y/n): ")
        if ask_double_move.lower() == 'y':
            self.double_move_tickets -= 1
            self.setNewNode()