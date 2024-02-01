from helpers import draw_board, check_turn, check_for_win
import os

spots = {1: '1', 2: '2', 3: '3',
        4: '4', 5: '5', 6: '6',
        7: '7', 8: '8', 9: '9'}

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    #reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    #if an invalid turn occured, let the player know
    if prev_turn == turn:
        print("Invalid spot selected, please try again")
    prev_turn = turn
    print("Player " + str((turn % 2) + 1 ) + "'s turn: Pick your spot or type q to quit")

    #get input from the player
    choice = input()
    if choice == 'q':
        playing = False

    #check if the player gave a number from 1-9
    elif str.isdigit(choice) and int(choice) in spots:

        #Check if the spot has already been taken
        if not spots[int(choice)] in {"X", "O"}:

            #valid input, update a board
            turn += 1
            spots[int(choice)] = check_turn(turn)

    #check if the game has ended(and if someone win)
    if check_for_win(spots):
        playing, complete = False, True
    if turn > 8:
        playing = False

#out of the loop, print the result
#draw the board on the last time
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

#if there was a winner, say who won:
if complete:
    if check_turn(turn) == "X":
        print("Player 1 WON")
    else:
        print("Player 2 WON")
else:
    #Tie
    print("Tie")

print("Thanks for playing")