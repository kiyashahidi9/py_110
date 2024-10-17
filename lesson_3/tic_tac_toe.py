'''
Tic-Tac-Toe game with a computer with defensive/offensive abilities
'''

import random
import os
import time

INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
WIN_AMOUNT = 5
player_wins = 0
computer_wins = 0

# Welcome's the user and displays the guidelines
def welcome_display():
    os.system('clear')
    pretty_display('Welcome to Tic Tac Toe!')
    print('- You are "X" and the computer is "Y"')
    print('- First to 5 wins, wins!\n')

# Prompts the user who goes first, validates reponse
def who_goes_first():
    choice = prompt('Who goes first? (p)layer or (c)omputer?')
    while True:
        match choice.casefold():
            case 'player':
                return 'player'
            case 'p':
                return 'player'
            case 'c':
                return 'computer'
            case 'computer':
                return 'computer'
            case _:
                choice = prompt('Please choose: (p)layer or (c)omputer.')

# takes a yes or no question, validates response and returns a boolean
def answer_yes_no(message):
    answer = prompt(f'{message} y)es or n)o')
    while True:
        if answer.casefold() in ['y', 'yes']:
            return True
        if answer.casefold() in ['n', 'no']:
            return False

        answer = prompt(f'{message}\nPlease enter a y)es or a n)o')

# displays the tic-tac-toe board
def display_board(board):
    os.system('clear')
    print('')
    print('     |     |')
    print(f'  {board[1]}  |  {board[2]}  |  {board[3]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[4]}  |  {board[5]}  |  {board[6]}')
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f'  {board[7]}  |  {board[8]}  |  {board[9]}')
    print('     |     |')
    print('')

# returns an empty board
def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

# gathers input from the user and formats it with ==>
def prompt(message):
    return input(f'==> {message}\n').strip()

# returns a list of squares on the board that are empty
def empty_squares(board):
    return [key for key, value in board.items()
                    if value == INITIAL_MARKER]

# selects the appropriate turn for who is choosing
def choose_square(board, current_player):
    if current_player.casefold() == 'player':
        player_chooses_square(board)
    else:
        computer_chooses_square(board)

# alternates the player choosing, for taking turns
def alternate_player(current_player):
    if current_player == 'player':
        return 'computer'
    elif current_player == 'computer':
        return 'player'

# prompts the player to choose a square, validates input
def player_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        square = prompt(f'Choose a square {join_or(valid_choices)}:')
        if square in valid_choices:
            break
        display_board(board)
        print('* Sorry, that\'s not a valid choice.')

    board[int(square)] = HUMAN_MARKER

# joins elements of a list with an 'or' separator for the last element
def join_or(elements, sep=', ', last_word='or'):
    elements = [str(element) for element in elements]
    if len(elements) > 1:
        return f'{sep.join(elements[0:-1])} {last_word} {elements[-1]}'
    elif len(elements) == 1:
        return elements[0]
    else:
        return ""

# creates an offensive/defensive computer strategy
def find_risk_square(board):
    threat_positions = [[1, 2, 3], [2, 3, 1], [1, 3, 2],
                        [4, 5, 6], [6, 5, 4], [4, 6, 5],
                        [7, 8, 9], [8, 9, 7], [7, 9, 8],
                        [1, 4, 7], [4, 7, 1], [1, 7, 4],
                        [2, 5, 8], [2, 8, 5], [5, 8, 2],
                        [3, 6, 9], [6, 9, 3], [3, 9, 6],
                        [1, 5, 9], [5, 9, 1], [1, 9, 5],
                        [3, 5, 7], [5, 7, 3], [3, 7, 5],]

    for threat in threat_positions:
        if (board[threat[0]] == COMPUTER_MARKER
                and board[threat[1]] == COMPUTER_MARKER
                and board[threat[2]] != HUMAN_MARKER):
            return threat[2]
        elif (board[threat[0]] == HUMAN_MARKER
                and board[threat[1]] == HUMAN_MARKER
                and board[threat[2]] != COMPUTER_MARKER):
            return threat[2]

    return False

# prompts the computer to choose a square.
# if an offensive/defensive/square 5 is not available,
# a random sqare is chosen.
def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    if find_risk_square(board):
        square = find_risk_square(board)
    elif board[5] == INITIAL_MARKER:
        square = 5
    else:
        square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

# returns True if the board is full
def board_full(board):
    return len(empty_squares(board)) == 0

# returns True if someone won
def someone_won(board):
    return bool(detect_winner(board))

# returns who won the round
def detect_winner(board):
    winner_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]
    for line in winner_lines:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER and
                board[sq2] == HUMAN_MARKER and
                board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER and
                board[sq2] == COMPUTER_MARKER and
                board[sq3] == COMPUTER_MARKER):
            return 'Computer'
    return None

# returns who won the match
def detect_total_winner():
    if player_wins == WIN_AMOUNT:
        return 'Player'
    if computer_wins == WIN_AMOUNT:
        return 'Computer'
    return False

# increments appropriate scores as rounds are won
def track_score(winner):
    match winner:
        case 'Player':
            global player_wins
            player_wins += 1
        case 'Computer':
            global computer_wins
            computer_wins += 1

# resets the round scores both to 0
def reset_score():
    global player_wins, computer_wins
    player_wins, computer_wins = (0, 0)

# displays a message in a formatted box
def pretty_display(message):
    width = 50
    print(f'{'*' * width}*')
    print(f'*{' ' * (width - 1)}*')
    print(f'*{message.center(width - 1)}*')
    print(f'*{' ' * (width - 1)}*')
    print(f'{'*' * width}*')

# displays the total number of rounds won
def display_total_wins():
    print(f'Player: {player_wins} wins.')
    print(f'Computer: {computer_wins} wins.')

# the main loop
def play_tic_tac_toe():

    welcome_display()

    # allows you to choose to play another mtach
    while True:

        reset_score()
        first_player = who_goes_first()
    

        # allows you to choose to play another round
        while True:

            board = initialize_board()
            current_player = first_player

            # choosing squares until someone wins the round
            while True:
                display_board(board)

                choose_square(board, current_player)
                current_player = alternate_player(current_player)
                if someone_won(board) or board_full(board):
                    break

            display_board(board)

            if someone_won(board):
                winner = detect_winner(board)
                pretty_display(f'{winner} won the round!')
                track_score(winner)
            else:
                pretty_display('It\'s a tie!')

            display_total_wins()

            # if someone won 5 rounds
            if detect_total_winner():
                break

            play_again = answer_yes_no('Play another round?')
            if not play_again:
                break


        if detect_total_winner():
            os.system('clear')
            pretty_display(f'{winner} won the game!')
            display_total_wins()
            play_again = answer_yes_no('Play another match?')
        else:
            break
        if not play_again:
            break

    os.system('clear')
    pretty_display('Thank you for playing :)')
    time.sleep(3)
    os.system('clear')

play_tic_tac_toe()