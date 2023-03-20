import random

#Board Display
def display_board(board):
    print('\n' * 100)
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[7]+'|'+board[8]+'|'+board[9])


#ASK PLAYER INPUT BETWEEN X,O

def player_input():
    marker = ''

    # KEEP ASKING PLAYER1 TO CHOOSE X or O
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player1, choose X or O: ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#PLACE THE MARKER IN A POSITION

def place_marker(board, marker, position):
    board[position] = marker

#CHECK IF SOMEONE WON

def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or #top row
            (board[4] == board[5] == board[6] == mark) or #Middle row
            (board[7] == board[8] == board[9] == mark) or #bottom row
            (board[1] == board[4] == board[7] == mark) or #first column
            (board[2] == board[5] == board[8] == mark) or #second column
            (board[3] == board[6] == board[9] == mark) or #third column
            (board[1] == board[5] == board[9] == mark) or #diagonal
            (board[3] == board[5] == board[7] == mark))  #diagonal

#WHO WILL PLAY FIRST

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

#CHECK IF A SPACE IS EMPTY

def space_check(board, position):
    return board[position] == ' '

#CHECK IF THE BOARD IS COMPLETELY FILLED

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True

#PLAYER PICK A POSITION IN THE BOARD

def player_choice(board):
    position = 0
    while position not in range(1, 10) or not space_check(board, position):
        position = int(input("pick a position between 1-9: "))

    return position

#ASK PLAYERS IF THEY WANT TO PLAY AGAIN

def replay():
    choice = input('Do you want to play again? yes or no ')
    return choice == 'yes'

#RUN THE GAME

print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n?')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    # game play

    while game_on:

        if turn == 'Player 1':

            # show the board
            display_board(the_board)
            # choose a  position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player1_marker, position)

            # check if the won
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            # show the board
            display_board(the_board)
            # choose a  position
            position = player_choice(the_board)
            # place the marker on the position
            place_marker(the_board, player2_marker, position)

            # check if the won
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('TIE GAME!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break