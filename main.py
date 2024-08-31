from loadData import loadStationsData
stations_data = loadStationsData()

from playerLogic import *

def updateGameDetectives(detectives, active_nodes):
    for detective in detectives:
        detective.setNewNode()
        active_nodes[detective.id] = detective.current_node
        printSeparator()

def updateGameMrX(mr_x, active_nodes):
    print("MR X'S TURN!!!")
    if mr_x.double_move_tickets > 1:
        mr_x.askForDoubleMove()
    mr_x.setNewNode()
    active_nodes[0] = mr_x.current_node

def printSeparator():
    print()
    print("*" * 50)
    print()

def main():
    print(f"GAME STARTED \nMR.X HAS BEEN INITIALISED")

    active_nodes = []

    mr_x = MrX()

    while True:
        detective_count = int(input("HOW MANY DETECTIVES ARE PLAYING?:"))
        if 1 < detective_count < 6:
            break
        else:
            print(f"MINIMUM 2 DETECTIVES AND MAXIMUM DETECTIVES CAN BE 5")

    while True:
        mr_x.current_node = input(f"ENTER THE STARTING NODE FOR MR. X: ")
        try:
            mr_x.getAvailableNodes()
            active_nodes.append(mr_x.current_node)
            break
        except KeyError:
            print(f"VALUE SEEMS TO BE WRONG PLEASE CHECK THE VALUE AND TRY AGAIN!")

    detectives = []

    for id in range(1, detective_count + 1):
        detectives.append(Detective(id, mr_x))

    for detective in detectives:
        while True:
            flag = 0
            detective.current_node = input(f"ENTER THE STARTING NODE FOR DETECTIVE {detective.id}: ")
            if detective.current_node in active_nodes:
                print(f"THIS NODE IS ALREADY OCCUPIED!, PLEASE TRY ANOTHER NODE!")
                printSeparator()
                flag = 1
                detective.current_node = None
            else:
                active_nodes.append(detective.current_node)
            try:
                detective.getAvailableNodes()
                break
            except KeyError:
                if flag == 0:
                    print(f"VALUE SEEMS TO BE WRONG PLEASE CHECK THE VALUE AND TRY AGAIN!")
                else:
                    continue
            printSeparator()

    while active_nodes[0] not in active_nodes[1:len(active_nodes)]:
        printSeparator()
        updateGameMrX(mr_x, active_nodes)
        printSeparator()
        updateGameDetectives(detectives, active_nodes)

    print("GAME FINISHED, MR-X IS CAUGHT")

if __name__ == "__main__":
    main()
