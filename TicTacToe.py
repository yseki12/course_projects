from IPython.display import clear_output
import random

#Display game board, 3x3 representation of numpad 1-9 on keyboard
def display_board(board):
    clear_output()
    print('      ' + '|' + '       ' + '|' + '          ')
    print('  ' + board[7]+ '   |   ' + board[8] + '   |   ' + board[9])
    print('      ' + '|' + '       ' + '|' + '          ')
    print('------------------------')
    print('      ' + '|' + '       ' + '|' + '          ')
    print('  ' + board[4]+ '   |   ' + board[5] + '   |   ' + board[6])
    print('      ' + '|' + '       ' + '|' + '          ')
    print('------------------------')
    print('      ' + '|' + '       ' + '|' + '          ')
    print('  ' + board[1]+ '   |   ' + board[2] + '   |   ' + board[3])
    print('      ' + '|' + '       ' + '|' + '          ')

#take in a player input and assign their marker as 'X' or 'O'.
def player_input():
    
    clear_output()
    marker = ' '
     
    while marker != "X" and marker != "O":
        marker = input("Player 1: Please Choose X or O: ").upper()
        
    player1 = marker
    
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"
        
    print(f"Player 1 is {player1}")
    print(f"Player 2 is {player2}")
        
    return (player1, player2)

#takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board
def place_marker(board, marker, position):
    
    board[position] = marker

#takes in a board and a mark (X or O) and then checks to see if that mark has won
def win_check(board, mark):
    
    if (mark == board[1] == board[5] == board[9] or 
    mark == board[1] == board[2] == board[3]or 
    mark == board[4] == board[5] == board[6]or
    mark == board[7] == board[8] == board[9]or
    mark == board[1] == board[4] == board[7]or 
    mark == board[2] == board[5] == board[8]or
    mark == board[3] == board[6] == board[9]or
    mark == board[3] == board[5] == board[7]):
        return True

#randomly decide which player goes first
def choose_first():
    first = random.randint(1,2)
    
    if first == 1:
        return "Player1"
    else:
        return "Player2"


#returns a boolean indicating whether a space on the board is freely available
def space_check(board, position):
    
    if board[position] == ' ':
        return True

#checks if the board is full and returns a boolean value.  True if full
def full_board_check(board):
    
    for i in range(1,10):
        if space_check(board,i):
            return False
    
    return True


#asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. 
#if it is, then return the position for later use.

def player_choice(board):
    
    while True:

        try:
            position = 0
            
            while position not in range(1,10) or not space_check(board,position):
                position = int(input("Enter next position (1-9): "))

        except:
            print("please enter a number 1-9")

        else:
            break
    return position

#asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    
    replay = ' '
    
    while replay[0] != 'y' and replay[0] != 'n': #and replay != 'y' and replay != 'n':
        replay = input("Play Again? (y/n)").lower()
    
    if replay[0] == "y": #or replay == "yes":
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')

###SETUP###
while True:
    # Reset the board
    board = [' '] * 10

    player1_marker, player2_marker = player_input()

    choose_first()

    turn = choose_first()

    print(turn + " will go first")

    play_game = input("Ready? (y/n)").lower()

    if play_game[0] == "y":
        game_on = True
    else:
        game_on = False
    
    while game_on == True:

        # Player1's turn.

        if turn == "Player1":
            
            display_board(board)

            position = player_choice(board)

            place_marker(board,player1_marker,position)
        
            if win_check(board, player1_marker) == True:
                display_board(board)
                print("Player 1 has WON")
                game_on = False
        
            else:
                if full_board_check(board) == True:
                    display_board(board)
                    print("Tie")
                    game_on = False
                else:
                    turn = "Player2"
        
        else:

            # Player2's turn

            display_board(board)

            position = player_choice(board)

            place_marker(board,player2_marker,position)
        
            if win_check(board, player2_marker) == True:
                display_board(board)
                print("Player 2 has WON")
                game_on = False
        
            else:
                if full_board_check(board) == True:  
                    display_board(board)
                    print("Tie")
                    game_on = False
                else:
                    turn = "Player1"

    if not replay():
        break