import json
stations = open("stations.json", "r")
stations_data = json.load(stations)
starting_node = input("Enter the starting node: ")
taxi_nodes_available=stations_data[starting_node]["taxi"]
bus_nodes_available=stations_data[starting_node]["bus"]
underground_nodes_available=stations_data[starting_node]["underground"]
print(f"TAXI NODES AVAILABLE: {taxi_nodes_available}")
print(f"BUS NODES AVAILABLE: {bus_nodes_available}")
print(f"UNDERGROUND NODES AVAILABLE: {underground_nodes_available}")
current_node=input("Enter the next node: ")