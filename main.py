from loadData import loadStationsData
stations_data = loadStationsData()

from playerLogic import *

def print_separator(message):
    print("\n" + "=" * 50)
    print(message.center(50))
    print("=" * 50 + "\n")

def print_player_positions(mr_x, detectives):
    print("\nCurrent Positions:")
    for detective in detectives:
        print(f"Detective {detective.id}: {detective.current_node}")
    print()

def main():
    print_separator("GAME STARTED")
    print("MR. X HAS BEEN INITIALISED\n")
    mr_x = MrX()

    while True:
        mr_x.current_node = input("ENTER THE STARTING NODE FOR MR. X: ")
        try:
            mr_x.getAvailableNodes()
            break
        except:
            print("VALUE SEEMS TO BE WRONG PLEASE CHECK THE VALUE AND TRY AGAIN!\n")

    while True:
        detective_count = int(input("\nHOW MANY DETECTIVES ARE PLAYING?: "))
        if (detective_count < 6 and detective_count > 1):
            break
        else:
            print("MINIMUM 2 DETECTIVES AND MAXIMUM DETECTIVES CAN BE 5")

    detectives = []

    for id in range(1, detective_count + 1):
        detectives.append(Detective(id, mr_x))

    print("\n")

    all_players = [mr_x] + detectives

    for detective in detectives:
        while True:
            detective.current_node = input(f"ENTER THE STARTING NODE FOR DETECTIVE {detective.id}: ")
            if any(player.current_node == detective.current_node for player in all_players if player != detective):
                print("This node is already occupied. Please choose a different node.")
                continue
            try:
                detective.getAvailableNodes()
                break
            except:
                print("VALUE SEEMS TO BE WRONG PLEASE CHECK THE VALUE AND TRY AGAIN!\n")
        print("\n")

    def updateGameDetectives(detectives):
        for detective in detectives:
            print_separator(f"DETECTIVE {detective.id}'S TURN")
            print(f"Current position: {detective.current_node}")
            result = detective.setNewNode(all_players)
            if result == "GAME_OVER":
                return "GAME_OVER"
            print(f"\nDetective {detective.id} moved to node {detective.current_node}")
            input("\nPress Enter to continue...")
        return "CONTINUE"

    def updateGameMrX(mr_x):
        print_separator("MR X'S TURN")
        print(f"Current position: {mr_x.current_node}")
        if mr_x.double_move_tickets > 0:
            result = mr_x.askForDoubleMove(all_players)
            if result == "GAME_OVER":
                return "GAME_OVER"
        else:
            result = mr_x.setNewNode(all_players)
            if result == "GAME_OVER":
                return "GAME_OVER"
        print("\nMr. X has completed their move.")
        input("\nPress Enter to continue...")
        return "CONTINUE"

    turn_count = 1
    while True:
        print_separator(f"TURN {turn_count}")
        print_player_positions(mr_x, detectives)
        
        if updateGameDetectives(detectives) == "GAME_OVER":
            print_separator("GAME OVER")
            print("Mr. X has been caught! Detectives win!")
            break
        
        if updateGameMrX(mr_x) == "GAME_OVER":
            print_separator("GAME OVER")
            print("A detective has caught Mr. X! Detectives win!")
            break
        
        turn_count += 1

if __name__ == "__main__":
    main()