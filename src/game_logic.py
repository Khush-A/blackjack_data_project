import random

RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

CARD_VALUES = {
    'A': 11, 
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
    '10': 10, 'J': 10, 'Q': 10, 'K': 10
}

def new_deck():
    deck = []
    for rank in RANKS:
        for suit in SUITS:
            deck.append((rank, suit))

    random.shuffle(deck)
    return deck

# works out hand values
def hand_value(hand):
    total = sum(CARD_VALUES[rank] for rank, x in hand)
    aces = sum(1 for rank, x in hand if rank == 'A')

    while total > 21 and aces >0:
        total = total - 10
        aces = aces - 1

    return total


def deal_initial_hands(deck):
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand

def is_bust(hand):
    return hand_value(hand) > 21