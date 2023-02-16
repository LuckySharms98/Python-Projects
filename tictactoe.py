import random

# define board and list
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# print board (yes i know i can use f-strings im just lazy)
def display_board(board):
    print('   |   |   ')
    print(' {} | {} | {} '.format(board[6], board[7], board[8]))
    print('---|---|---')
    print(' {} | {} | {} '.format(board[3], board[4], board[5]))
    print('---|---|---')
    print(' {} | {} | {} '.format(board[0], board[1], board[2]))
    print('   |   |   ')

# define function to choose what player goes first
def choose_first():
    num = random.randint(1, 2)
    print(f'Player {num} goes first!')
    return num

# define player input function
def player_input(num):
    mark = 0
    while mark not in ('X', 'O'):
        mark = input(f"Player {num}: choose either 'X' or 'O': ")
    return mark

# define player2 input function
def player2_input(mark):
    if mark == 'X':
        mark2 = 'O'
    else:
        mark2 = 'X'
    return mark2

# define place marker function
def place_marker(board, mark, position):
    board[position - 1] = mark
    display_board(board)

# define win check function
def win_check(board, mark):
    # middle row
    if len(set(board[3:6])) == 1 and board[4] == mark:
        print(f'{mark} has won in the middle row!')
        return True
    # middle vert
    elif len(set(board[1:9:3])) == 1 and board[4] == mark:
        print(f'{mark} has won in the middle column!')
        return True
    # left diag
    elif len(set(board[0:9:4])) == 1 and board[4] == mark:
        print(f'{mark} has won in the left diag!')
        return True
    # right diag
    elif len(set(board[0:7:2])) == 1 and board[4] == mark:
        print(f'{mark} has won in the right diag!')
        return True
    # left wall
    elif len(set(board[0:7:3])) == 1 and board[3] == mark:
        print(f'{mark} has won in the left column!')
        return True
    # top wall
    elif len(set(board[6:9])) == 1 and board[7] == mark:
        print(f'{mark} has won in the top row!')
        return True
    # right wall
    elif len(set(board[2:9:3])) == 1 and board[5] == mark:
        print(f'{mark} has won in the right column!')
        return True
    # bottom wall
    elif len(set(board[0:3])) == 1 and board[2] == mark:
        print(f'{mark} has won in the bottom row!')
        return True
    else:
        return False

# define if space is filled
def space_check(board, position):
    return board[position-1] == ' '

# define function to check if board is completely filled
def full_board_check(board):
    # check each value in list
    if len(set(board)) == 2 and ' ' not in set(board): #case where board is filled
        print('Tie.')
        return True
    else: #will have 'X', 'O', and ' ' in set
        return False

# take next position and check if it's filled or not
def player_choice(board):
    position = -1
    while int(position) not in range(1, len(board)+1):
        position = int(float(input('Choose a new space (1-9): ')))
    empty = space_check(board, position)
    while empty != True:
        print('This position is filled. Pick another: ')
        position = int(input('Choose a new space (1-9): '))
        empty = space_check(board, position)
    else:
        return position


# define a replay function
def replay():
    outcome = ' '
    while outcome not in ('Yes', 'No'):
        outcome = input('Would you like to play again? Yes or No: ')
    if outcome == 'Yes':
        return True
    else:
        return False

# play the game!

# preset win condition
win = False
outcome = True

while outcome == True:
    # start up game
    print('Welcome to Tic Tac Toe!')

    # pick what player goes first
    num = choose_first()

    # have players choose a marker
    mark = player_input(num)

    mark2 = player2_input(mark)

    display_board(board)

    while not win:

        # have first player pick a position
        position = player_choice(board)

        # place first player mark and check if board full
        place_marker(board, mark, position)

        full = full_board_check(board)
        if not full:
            pass
        else:
            break

        # check if p1 wins
        win = win_check(board, mark)
        #print(win)

        if not win:
            pass
        else:
            break

        # have second player pick a position
        position = player_choice(board)

        # player second player mark and check if board full
        place_marker(board, mark2, position)

        full = full_board_check(board)
        if not full:
            pass
        else:
            break

        # check if second wins
        win = win_check(board, mark2)
        #print(win)

        if not win:
            pass
        else:
            break

    # ask to replay if win
    outcome = replay()

    #reset variables
    win = False
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    #clear screen
    print('\n' * 100)