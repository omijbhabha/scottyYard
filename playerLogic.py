from loadData import loadStationsData
stations_data = loadStationsData()

class Player:    
    def __init__(self, id=None, mr_x=None):
        self.id = id
        self.mr_x = mr_x
        self.current_node = None
        self.taxi_tickets = 0
        self.bus_tickets = 0
        self.underground_tickets = 0
    
    def getAvailableNodes(self):
        self.taxi_nodes_available = stations_data[self.current_node]["taxi"]
        self.bus_nodes_available = stations_data[self.current_node]["bus"]
        self.underground_nodes_available = stations_data[self.current_node]["underground"]
    
    def printAvailableNodes(self):
        print()
        print(f"TAXI NODES AVAILABLE: {self.taxi_nodes_available}")
        print(f"BUS NODES AVAILABLE: {self.bus_nodes_available}")
        print(f"UNDERGROUND NODES AVAILABLE: {self.underground_nodes_available}")
    
    def printAvailableTickets(self):
        print()
        print(f"YOU HAVE {self.taxi_tickets} TAXI TICKETS")
        print(f"YOU HAVE {self.bus_tickets} BUS TICKETS")
        print(f"YOU HAVE {self.underground_tickets} UNDERGROUND TICKETS")
        print()


    def setNewNode(self):
        while True:
            self.printAvailableTickets()
            self.printAvailableNodes()
            new_node = input(f"\nENTER THE NEXT NODE FOR {'MR. X' if self.id is None else f'DETECTIVE {self.id}'}: ")

            is_taxi = new_node in self.taxi_nodes_available
            is_bus = new_node in self.bus_nodes_available
            is_underground = new_node in self.underground_nodes_available

            transport_methods = sum([is_taxi, is_bus, is_underground])

            if transport_methods > 1:
                transport_type = input("Choose the type of transportation (taxi, bus, underground): ").strip().lower()

                if transport_type not in {'taxi', 'bus', 'underground'}:
                    print("INVALID TRANSPORTATION TYPE! Please choose from 'taxi', 'bus', or 'underground'.")
                    continue

                if transport_type == 'taxi' and is_taxi:
                    chosen_transport = 'taxi'
                elif transport_type == 'bus' and is_bus:
                    chosen_transport = 'bus'
                elif transport_type == 'underground' and is_underground:
                    chosen_transport = 'underground'
                else:
                    print(f"INVALID ARGUMENT CAN NOT ACCESS THAT NODE WITH {transport_type.upper()}!")
                    continue
            else:
                if is_taxi:
                    chosen_transport = 'taxi'
                elif is_bus:
                    chosen_transport = 'bus'
                elif is_underground:
                    chosen_transport = 'underground'
                else:
                    print("INVALID NODE! PLEASE ENTER A VALID NODE.")
                    continue

            if chosen_transport == 'taxi':
                if self.taxi_tickets > 0:
                    self.current_node = new_node
                    self.getAvailableNodes()
                    self.taxi_tickets -= 1
                    if self.mr_x:
                        self.mr_x.taxi_tickets += 1
                    break
                else:
                    print("NO TAXI TICKETS LEFT! Please choose another mode of transportation.")
                    continue

            elif chosen_transport == 'bus':
                if self.bus_tickets > 0:
                    self.current_node = new_node
                    self.getAvailableNodes()
                    self.bus_tickets -= 1
                    if self.mr_x:
                        self.mr_x.bus_tickets += 1
                    break
                else:
                    print("NO BUS TICKETS LEFT! Please choose another mode of transportation.")
                    continue

            elif chosen_transport == 'underground':
                if self.underground_tickets > 0:
                    self.current_node = new_node
                    self.getAvailableNodes()
                    self.underground_tickets -= 1
                    if self.mr_x:
                        self.mr_x.underground_tickets += 1
                    break
                else:
                    print("NO UNDERGROUND TICKETS LEFT! Please choose another mode of transportation.")
                    continue
        self.printAvailableTickets()


class Detective(Player):
    def __init__(self, id, mr_x):
        super().__init__(id, mr_x)
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
        if 'y' in ask_double_move:
            self.double_move_tickets -= 1
            print(f"\nYOU HAVE USED DOUBLE FARE, YOU WILL MOVE TWICE")
            self.setNewNode()
            print(f"\nMOVE 1 COMPLETE PLEASE MOVE AGAIN")