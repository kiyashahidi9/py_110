'''
RULES:
Deck: standard 52-card deck with 4 suits of 13 values each.
    - 2 - 10 are all worth their face value
    - J, K, Q are all worth 10
    - A can be worth 1 or 11
        - if A is worth 11 and the sum of the hand is > 21, A is worth 1
        - otherwise, A is worth 11

Setup: the game has a dealer and a player
    - both are initially dealt a hand of two cards.
    - the player can see both their cards
    - can see only one of the dealers cards

Player turn: the player alwasy goes first
    - can decide to either hit or stay
    - the turn is over until the player stays or busts

hit: the player wants to be dealt another card
    - if the total exceeds 21, he will bust and lose the game.

dealer turn: the dealer must hit until the total is at least 17.
    - if the dealer busts, the player wins

comparing cards: when both the player and the dealer stay
    - the cards are compared, and whoever has the highest value wins.

IMPLEMENTATION STEPS
### 1. deal two random cards to both the player and the dealer
### 2.5: calculate the total_card_value of both
### 2. display both cards of the player and one random card of the dealer
### 3. ask the player if they want to hit or stay
### 4. if they hit, deal another card to the player
### 5. calculate the total value of the player
### 6. if the total value is above 21, the player busts, dealer wins
### 7. if not, repeat 3
### 8. if they stay, it is computer's turn
### 9. deal random cards to the computer's hand until the total is at least 17
### 10. if the total is over 21, the computer busts and player wins
### 11. if no bust, the cards are revealed and total is compared
### 12. whoever has the highest total wins the game

DATA STRUCTURE
to contain the deck card/value: dictionary
to contain the players cards: dictinoary
to contain the dealers cards: dictionary
'''

import random
import time
import os

## Constants and magic numbers

SUITS = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]]
INITIAL_CARD_AMOUNT = 2
LIMIT = 21
player_wins = 0
dealer_wins = 0

## Aesthetic and Introduction Functions ##

def display_header_box(message):
    ''' Formats a message within a large box '''

    width = 50
    edge = f'+{'-' * width}+'
    mid = f'|{' ' * width}|'
    message_line = f'|{message.center(width).title()}|'

    order = [edge, mid, message_line, mid, edge]

    for line in order:
        print(line)

def star_center_line(message):
    ''' Formats a message in a centered line between *** '''

    width = 50
    print(f'*** {message.center(width)} ***')

def clear_screen():
    os.system('clear')

def short_pause():
    time.sleep(2)

def long_pause():
    time.sleep(5)

def display_card_values():

    star_center_line('CARD VALUES')
    print(
f'''
- Number cards: Have the same value as their face number

- Jack, Queen, King: Have the value 10

- Ace: Has a value of 11 if total sum of the hand is less than {LIMIT}
    Otherwise, it's value is 1
'''

    )

    star_center_line('BEST OUT OF FIVE')

def display_further_rules():
    star_center_line('You are going against the dealer (Computer)')
    print(
f'''
- You both will start off with two random cards
- You will go first

- You can 'hit' to draw another card
- Or 'stay' to switch to the dealer's turn

- Your goal is to get as close to {LIMIT} as possible
'''
    )

def ready_to_start():
    ''' Prompts the user if they are ready to start the game '''

    valid_choices = ['yes', 'no', 'y', 'n']
    ready = ask_question('\nAre you ready to start? y)es n)o',
                         valid_choices)
    if ready in ['y', 'yes']:
        play_twenty_one()
    else:
        print('Take your time!')
        ready_to_start()

## Game mechanic functions ##

def initialize_deck():
    ''' Returns a full deck '''

    return {f'{card} of {suit}': value for suit in SUITS
            for card, value in zip(CARDS, VALUES)}

def initial_hand_deal(deck):
    ''' Returns two intial hands with two random cards '''

    player_hand = deal_x_random_cards(deck, INITIAL_CARD_AMOUNT)
    dealer_hand = deal_x_random_cards(deck, INITIAL_CARD_AMOUNT)
    return player_hand, dealer_hand

def deal_x_random_cards(deck, x):
    ''' Returns a hand with a specified random cards
        removes the cards from the deck '''

    random_choices = list(deck.items())
    chosen_cards = dict([random.choice(random_choices) for _ in range(x)])
    remove_cards_from_deck(chosen_cards, deck)
    return chosen_cards

def remove_cards_from_deck(cards, deck):
    ''' Removes chosen cards from the deck '''

    for card in cards:
        if card in deck:
            deck.pop(card)

def calc_total_card_value(cards):
    ''' Returns the total card value '''

    return sum(list(cards.values()))

def return_total_card_value(cards):
    ''' Scans through cards for ace values 
        Calculates accordingly, returns the
        True total '''

    determine_ace_value(cards)
    return calc_total_card_value(cards)

def determine_ace_value(cards):
    ''' Determines the value of an ace '''

    ace_cards = [card for card in cards if card.startswith('Ace')]
    if ace_cards:
        calc_ace_value(ace_cards, cards)

def calc_ace_value(ace_cards, cards):
    ''' Helper function for `determine_ace_value` '''

    for ace_card in ace_cards:
        cards[ace_card] = 11
    for ace_card in ace_cards:
        if calc_total_card_value(cards) > LIMIT:
            cards[ace_card] = 1

def card_display(cards):
    ''' Returns a formatted display of the cards 
        Helper function for display_cards '''

    return ' and '.join([card.split()[0] for card in cards])

def display_cards(player_hand, dealer_hand):
    ''' Displays the current cards in each player hand '''

    plural = 's' if len(dealer_hand) > 2 else ''

    print(f'Dealer has: {card_display(dealer_hand).split()[0]}'
          f' and unknown card{plural}')

    print(f'You have: {card_display(player_hand)}')

def ask_question(question, valid_choices):
    ''' Takes a question and returns a user answer
        once a valid response is given. '''

    while True:
        prompt = input(f'{question}\n')
        if prompt.casefold() in valid_choices:
            return prompt.casefold()

        print('Please enter a valid response!')

def prompt_player_hit_stay():
    ''' Prompts the user if they would like to hit or stay. '''

    valid_choices = ['hit', 'stay', 'h', 's']
    player_hit_or_stay = ask_question(
            '\nWould you like to hit or stay? h)it or s)tay', 
             valid_choices)

    return player_hit_or_stay

def deal_another_card(deck, hand):
    ''' Adds a random card to the given hand '''

    random_card = deal_x_random_cards(deck, 1)
    hand.update(random_card)

def busted(hand):
    ''' Returns a boolean value if the player has busted '''

    return return_total_card_value(hand) > LIMIT

def display_final_cards(player_hand, dealer_hand):
    ''' Prints both hands without the 'Unknowns' '''

    star_center_line('FINAL CARDS')
    print(f'Dealer had: {card_display(dealer_hand)} |'
          f' {return_total_card_value(dealer_hand)}')

    print(f'You had: {card_display(player_hand)} |'
          f' {return_total_card_value(player_hand)}')

def who_won(player_hand, dealer_hand):
    ''' Calculates and returns the winner, increments score '''

    global player_wins, dealer_wins
    player_score = return_total_card_value(player_hand)
    dealer_score = return_total_card_value(dealer_hand)

    if player_score > dealer_score:
        winner = 'player'
        increment_player_scores(winner)
        return winner
    elif dealer_score > player_score:
        winner = 'dealer'
        increment_player_scores(winner)
        return winner
    return 'tie'

def win_display(winner, player_hand, dealer_hand):
    ''' Displays the winner and final hands '''

    if winner == 'tie':
        result = ''
    else:
        result = ' won'
    display_header_box(f'{winner.capitalize()}{result} this round!')
    short_pause()
    
    display_final_cards(player_hand, dealer_hand)
    display_scoreboard()

def busted_display(player_busted):
    ''' Displays a message if someone busts '''

    if player_busted:
        star_center_line('You Busted!')
    else:
        star_center_line('Dealer Busted!')

def current_draw_display(hand, player_drawing=True):
    ''' Displays the card that was drawn '''

    if player_drawing:
        star_center_line(f'You drew a {list(hand)[-1]}')
    else:
        star_center_line(f'Dealer drew a card')

def final_busted_display(winner, player_hand, dealer_hand, player_busted):
    ''' If a player busts, it displays:
        - Who busted
        - The final scoreboard '''

    increment_player_scores(winner)
    clear_screen()
    busted_display(player_busted)
    short_pause()
    win_display(winner, player_hand, dealer_hand)
    short_pause()

def final_compare_display(player_hand, dealer_hand):
    ''' If nobody busts, the two hands are compared
        and a winner is displayed '''

    clear_screen()
    winner = who_won(player_hand, dealer_hand)
    win_display(winner, player_hand, dealer_hand)
    short_pause()

def play_again():
    ''' Prompts the user if they want to play again '''

    valid_choices = ['yes', 'no', 'y', 'n']
    yes_or_no = ask_question('Would you like to start a new round? y)es or n)o',
                              valid_choices)
    if yes_or_no in ['yes', 'y']:
        play_twenty_one()

def increment_player_scores(winner):
    ''' Increments the score of the winner '''

    global player_wins, dealer_wins
    if winner == 'player':
        player_wins += 1
    else:
        dealer_wins += 1

def prompt_next_round():
    ''' Prompts the user to continue to the next round '''

    input("\nHit enter to continue to the next round: ")

def display_scoreboard():

    star_center_line('SCOREBOARD')
    print(f'Player Wins: {player_wins}')
    print(f'Dealer Wins: {dealer_wins}')

def game_win_display(winner, player_hand, dealer_hand):
    ''' Displays the winner after best out of 5 is won '''

    clear_screen()
    display_header_box(f'{winner} won the game!!')
    short_pause()
    display_final_cards(player_hand, dealer_hand)
    display_scoreboard()
    short_pause()


## Main game functions ##

def play_twenty_one():
    ''' The main game function '''

    global player_wins, dealer_wins
    player_wins = 0
    dealer_wins = 0

    while True:

        while True:

            # intializing the round
            clear_screen()
            deck = initialize_deck()
            player_hand, dealer_hand = initial_hand_deal(deck)

            # The player's turn
            while True:
                display_cards(player_hand, dealer_hand)

                if busted(player_hand) or prompt_player_hit_stay() in ['s', 'stay']:
                    break

                deal_another_card(deck, player_hand)

                current_draw_display(player_hand)
                short_pause()

                clear_screen()

            # If the player busted
            if busted(player_hand):
                winner = 'dealer'
                final_busted_display(winner, player_hand, dealer_hand, True)
                break

            clear_screen()
            star_center_line('The dealer will now play')
            short_pause()

            # Dealer's turn
            while True:
                display_cards(player_hand, dealer_hand)
                short_pause()

                if return_total_card_value(dealer_hand) > (LIMIT - 4) or busted(dealer_hand):
                    break

                deal_another_card(deck, dealer_hand)

                current_draw_display(dealer_hand, False)
                short_pause()

                clear_screen()

            # If the dealer busted
            if busted(dealer_hand):
                winner = 'player'
                final_busted_display(winner, player_hand, dealer_hand, False)
                break

            # If no one busted, the cards are compared
            final_compare_display(player_hand, dealer_hand)
            break

        if player_wins == 3:
            game_winner = 'player'
            game_win_display(game_winner, player_hand, dealer_hand)
            break
        elif dealer_wins == 3:
            game_winner = 'dealer'
            game_win_display(game_winner, player_hand, dealer_hand)
            break
        prompt_next_round()

        


    play_again()

def introduction():
    ''' An intro sequence with game rules '''

    clear_screen()
    display_header_box(f'welcome to {LIMIT}!')
    short_pause()
    clear_screen()
    star_center_line('RULES AND GUIDELINES')
    short_pause()
    clear_screen()
    display_further_rules()
    display_card_values()
    ready_to_start()

def goodbye():
    ''' Outro '''

    clear_screen()
    display_header_box('Thank you for playing!')

introduction()
goodbye()