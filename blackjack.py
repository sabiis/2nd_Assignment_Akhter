"""
Blackjack / Twenty-one

Blackjack is a popular card game. The objective of the game is to draw cards and
 obtain the highest total not exceeding 21.

Simplified game requirements

* The possible card values range from 1 to 10 and, unlike a real deck, the
  probability of drawing a card is equal
* The game begins by dealing two visible cards to the player (face up), and two
  cards to the dealer. However, in the case of the dealer, one card is visible
  to other players while the other is hidden.
* The player decides whether to "hit" (draw another card), or "stand" which ends
  their turn.
* The player may hit any number of times. Should the total of the cards exceed
  21, the player "busts" and loses the game to the dealer.
* If the player reaches 21, the player stands
* The dealer's turn begins by revealing the hidden card
* The dealer must hit if the total is 16 or less, and must stand if the value is
  17 or more
* The dealer wins all ties (i.e. if both the dealer and the player reach 21,
  the dealer wins)
* The program indicates who the winner is and asks to play again
"""
# Declaring modules and objects

import os
from random import shuffle


# print('Hello there! To use this program, you need to give the end value. \
# For better results, provide the start and end values too')

CARD_NAMES = [2, 3, 4, 5, 6, 7, 8, 9, 10] + ['JACK', 'QUEEN', 'KING', 'ACE']
#Includes Face cards to get bonus/Extra marks
SUITS = ['\u2660', '\u2666', '\u2663', '\u2665']


def card_deck():
    """
    Return a new deck of cards.
    """
    return [[CARD_NAME, SUIT] for CARD_NAME in CARD_NAMES for SUIT in SUITS]

def decor():
    """
    This function is used to clear the screen and create a decorative top
    """

    os.system('cls')
    print(f'{"*":*^100}')
    print(f'*{"WELCOME TO BACKJACK/TWENTY-ONE":^98}*')
    print(f'{"*":*^100}')
    print()

def card_int(card):
    """This function is used to return the integer value of the card.
    """

    CARD_NAME = card[0]
    if CARD_NAME in CARD_NAMES[0:9]: #Checks if cards are number cards
        return int(CARD_NAME) #returns the card value as integer
    elif CARD_NAME is 'ACE': #Checks if card name is 'ACE'
        return 11 #returns the value 11 for the ACE card by default (Bonus part!)
    else: #Checks if card is 'Jack', 'Queen' or 'King'
        return 10 #Card values for them are 10

def total_value(hand):
    """Returns the integer value of a set of cards.
    There are many things happening here. The total number of cards in hand are
    calculated. The total number of Ace cards are counted. The Bonus part of the
    question about the Ace card of when the value wil be taken as 1 or 11 is also
    being calculated"""
    card_value = sum(card_int(_) for _ in hand) #This will add up the values of the cards in hand
    total_aces = len([_ for _ in hand if _[0] is 'ACE']) #This will count the number of Aces in hand

# By default, the values of aces are taken as 11. This is the bonus part of the
# question, which will calculate to check if the card values 21, then the value
# of Ace will be taken as 1
    while total_aces > 0:
        if card_value > 21 and 'ACE' in CARD_NAMES:
            card_value -= 10
            total_aces -= 1
        else:
            break

# After calculating the total value of the cards and the value of the aces in hand,
# the following if function will give you the value of the current cards if it is
# not a Blackjack or Bust. If the total value of the cards is equal to 21, it will
# let the player know that he has a Blackjack. If the value exceeds 21, the message
# displayed will be bust.
    if card_value < 21:
        return [str(card_value), card_value]
    elif card_value == 21:
        return ['Blackjack!', 21] #The label will be printed on the screen. The score
# is used in internal calculation.
    else:
        return ['Bust!', 50] #The label will be printed on the screen. The score
# is used in internal calculation.

def play_game():
    # get a deck of cards, and randomly shuffle it
    DECK = card_deck()
    shuffle(DECK)

    #Game play begins and the screen is cleared to get a decorative title. The cards
    # are dealt to the player and the dealer (Computer)

    PLAY = True
    decor()
    PLAYER_CARDS = [DECK.pop(), DECK.pop()]
    # print(PLAYER_CARDS)
    DEALER_CARDS = [DECK.pop(), DECK.pop()]
    # print(DEALER_CARDS)
    # Printing the dealer's first card that he drew.
    print()
    print(f"The first card that the dealer drew is {DEALER_CARDS[0]}")
# Printing the player’s current hand, as well as its value.
    print()
    while PLAY:
# The following print command gives the total value of the cards
        print(f"The total value of your cards is '{total_value(PLAYER_CARDS)[0]}'")
        print(f"The cards in your hand are {PLAYER_CARDS}") #Shows the cards in your hand
# The total value function is used to get the sum value of the cards. If the value
# is greater than 21 (its a bust), the function returns the value 50. No question
# of hit or stay will be asked
        if total_value(PLAYER_CARDS)[1] == 50:
            break
# If the value of the cards is equal to 21, the player stands automatically and wins
        if total_value(PLAYER_CARDS)[1] == 21:
            break
# If the total value of the cards is less than 21, the player has the option to hit or stay
        if PLAY:
            ANSWER = int(input('Hit or stand? (Hit = 1, Stand = 0): '))

# If the player asks to be hit, take the first card from the top of
# deck and add it to their hand. If they ask to stay, change
# player_in to false, and move on to the dealer’s hand.
# If the player chooses HIT, the first card from the shuffled deck will be placed
# in his hand. The player will be shown the new card. If the player chooses to stand
# the players turn will be over and the play will be false, hence ending the
# players turn
        if ANSWER:
            PLAY = True
            NEW_PLAYER_CARD = DECK.pop()
            PLAYER_CARDS.append(NEW_PLAYER_CARD)
            print()
            print(f"The card you drew is {NEW_PLAYER_CARD}")
            print(f"The total value of your cards is '{total_value(PLAYER_CARDS)[0]}'")
            print()
            if total_value(PLAYER_CARDS)[1] == 50:
                break
            if total_value(PLAYER_CARDS)[1] == 21:
                break
        else:
            PLAY = False

# Defining Card labels for player and dealer. It will give messages from the function
# if the hand is a bust or a blackjack.

    PLAYER_LABEL, PLAYER_TOTAL = total_value(PLAYER_CARDS)
    DEALER_LABEL, DEALER_TOTAL = total_value(DEALER_CARDS)

    if PLAYER_TOTAL <= 21:
    # Display the dealer's current hand, as well as its value.
        print()
    # The following print command gives the total value of the dealer's cards
        print(f"The total value of dealers cards is '{DEALER_LABEL}'")
        print(f"The cards in his hand are {DEALER_CARDS}") #Shows the cards in his hand
    # dealer_hand_string = "'\nDealer is at %s\nwith the hand %s\n'"
    # print (dealer_hand_string % (dealer_score_label, DEALER_CARDS))
    else:
        print("Dealer wins. Better luck next time!")
# The dealer only draws cards if the player's hand is not a blackjack or a bust
    if PLAYER_TOTAL != 21 and PLAYER_TOTAL < 21:
        while total_value(DEALER_CARDS)[1] < 17:
            NEW_DEALER_CARD = DECK.pop()
            DEALER_CARDS.append(NEW_DEALER_CARD)
            print()
            print(f"The card the dealer drew is {NEW_DEALER_CARD}")
            print()

    DEALER_LABEL, DEALER_TOTAL = total_value(DEALER_CARDS)

# The folowing if condition messages will be decide who the winner of the game is
    if PLAYER_TOTAL == 50:
        print("How many times do I need to tell you!!!! You lose")
    elif PLAYER_TOTAL < 50 and DEALER_TOTAL == 50:
        print('You win. Dealer busts!')
    elif PLAYER_TOTAL > DEALER_TOTAL:
        print('Good Job! You win')
    elif PLAYER_TOTAL == DEALER_TOTAL:
        print('You are tied with the dealer, and in this case dealer wins.')
    elif PLAYER_TOTAL < DEALER_TOTAL:
        print("And so is life! Dealer wins!")

# The option is given to the player to play the game again
    PLAY_AGAIN = input("Do you want to play again? (Type 'Y' for 'Yes' or 'N' \
for 'No': )").upper()
    if PLAY_AGAIN == 'Y':
        play_game()
    else:
        exit()

if __name__ == "__main__":
    play_game()
