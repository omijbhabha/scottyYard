from loadData import loadStationsData
stations_data = loadStationsData()

from playerLogic import *

from gameLogic import *


def main():
    print(f"GAME STARTED \nMR.X HAS BEEN INITIALISED")
    
    active_nodes=[]

    mr_x=MrX()

    while True:
        detective_count = int(input("HOW MANY DETECTIVES ARE PLAYING?:"))
        if (detective_count<6 and detective_count>1):
            break
        else:
            print(f"MINIMUM 2 DETECTIVES AND MAXIMUM DETECTIVES CAN BE 5")

    while True:
        mr_x.current_node = input(f"ENTER THE STARTING NODE FOR MR. X: ")
        try:
            mr_x.getAvailableNodes()
            active_nodes.append(mr_x.current_node)
            break
        except:
            print(f"VALUE SEEMS TO BE WRONG PLEASE CHECK THE VALUE AND TRY AGAIN!")

    detectives = []

    for id in range(1, detective_count + 1):
        detectives.append(Detective(id))

    for detective in detectives:
        while True:
            flag=0
            detective.current_node = input(f"ENTER THE STARTING NODE FOR DETECTIVE {detective.id}: ")
            if detective.current_node in active_nodes:
                print(f"THIS NODE IS ALREADY OCCUPIED!, PLEASE TRY ANOTHER NODE!")
                printSeparator()
                flag=1
                detective.current_node=None
            else:
                active_nodes.append(detective.current_node)
            try:
                detective.getAvailableNodes()
                break
            except:
                if flag==0:
                    print(f"VALUE SEEMS TO BE WRONG PLEASE CHECK THE VALUE AND TRY AGAIN!")
                else:
                    continue
            printSeparator()
    
    # print(active_nodes)
    


    # printSeparator()
    # updateGameMrX(mr_x)
    # printSeparator()
    # updateGameDetectives(detectives)

if __name__ == "__main__":
    main()
