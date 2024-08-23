def updateGameDetectives(detectives):
    for detective in detectives:
        detective.setNewNode()
        detective.printAvailableTickets()

def updateGameMrX(mr_x):
    if mr_x.double_move_tickets>1:
        mr_x.askForDoubleMove()
    mr_x.setNewNode()
    mr_x.printAvailableTickets()