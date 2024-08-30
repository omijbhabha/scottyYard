from loadData import loadStationsData
stations_data = loadStationsData()

from playerLogic import *
from gameLogic import *

def main():
    print(f"GAME STARTED\n\nMR.X HAS BEEN INITIALISED\n\n")
    mr_x = MrX()

    while True:
        mr_x.current_node = input(f"ENTER THE STARTING NODE FOR MR. X: ")
        try:
            mr_x.getAvailableNodes()
            break
        except:
            print(f"VALUE SEEMS TO BE WRONG PLEASE CHECK THE VALUE AND TRY AGAIN!\n")

    while True:
        detective_count = int(input("\n\nHOW MANY DETECTIVES ARE PLAYING?:"))
        if (detective_count < 6 and detective_count > 1):
            break
        else:
            print(f"MINIMUM 2 DETECTIVES AND MAXIMUM DETECTIVES CAN BE 5")

    detectives = []

    for id in range(1, detective_count + 1):
        detectives.append(Detective(id, mr_x))

    print("\n")

    for detective in detectives:
        while True:
            detective.current_node = input(f"ENTER THE STARTING NODE FOR DETECTIVE {detective.id}: ")
            try:
                detective.getAvailableNodes()
                break
            except:
                print(f"VALUE SEEMS TO BE WRONG PLEASE CHECK THE VALUE AND TRY AGAIN!\n")
        print("\n")

    updateGameDetectives(detectives)
    updateGameMrX(mr_x)

if __name__ == "__main__":
    main()