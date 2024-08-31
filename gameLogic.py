def updateGameDetectives(detectives):
    for detective in detectives:
        detective.setNewNode()
        printSeparator()

def updateGameMrX(mr_x):
    print("MR X'S TURN!!!")
    if mr_x.double_move_tickets>1:
        mr_x.askForDoubleMove()
    mr_x.setNewNode()

def printSeparator():
    print()
    print("*"*50)
    print()