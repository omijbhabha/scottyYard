import json
stations = open("stations.json", "r")
stations_data = json.load(stations)
current_node = input("Enter the starting node: ")
taxi_nodes_available=stations_data[current_node]["taxi"]
bus_nodes_available=stations_data[current_node]["bus"]
underground_nodes_available=stations_data[current_node]["underground"]
print(f"TAXI NODES AVAILABLE: {taxi_nodes_available}")
print(f"BUS NODES AVAILABLE: {bus_nodes_available}")
print(f"UNDERGROUND NODES AVAILABLE: {underground_nodes_available}")
flag=0
while flag==0:
    change_node=input("Enter the next node: ")
    if change_node in taxi_nodes_available:
        current_node=change_node
        flag=1
    elif change_node in bus_nodes_available:
        current_node=change_node
        flag=1
    elif change_node in underground_nodes_available:
        current_node=change_node
        flag=1
    elif current_node not in taxi_nodes_available and current_node not in bus_nodes_available and current_node not in underground_nodes_available:
        print(f"INVALID ARGUMENT CAN NOT ACCESS THAT NODE!")
        print(f"TAXI NODES AVAILABLE: {taxi_nodes_available}")
        print(f"BUS NODES AVAILABLE: {bus_nodes_available}")
        print(f"UNDERGROUND NODES AVAILABLE: {underground_nodes_available}")
print(f"YOUR CURRENT NODE IS {current_node}")