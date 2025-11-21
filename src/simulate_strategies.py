from src.game_logic import (
    new_deck, hand_value, deal_initial_hands, is_bust
)
from src.data_logger import GameLogger

# Always hit until you get a score of 17 or more
def easy_strategy(deck, player_hand):
    actions = []
    while hand_value(player_hand) < 17:
        # hit
        actions.append('H')
        player_hand.append(deck.pop())
        if is_bust(player_hand):
            break
    if not is_bust(player_hand):
        # stay
        actions.append("S")
    return actions


# Same as easy strategy, hit until 17
def dealer_strategy(deck, dealer_hand):
    while hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())


def simulate_round(round_id, strategy_name, logger):
    deck = new_deck()
    player_hand, dealer_hand = deal_initial_hands(deck)


    actions = easy_strategy(deck, player_hand)
    dealer_strategy(deck, dealer_hand)

    p_total = hand_value(player_hand)
    d_total = hand_value(dealer_hand)

    player_bust = p_total > 21
    dealer_bust = d_total > 21

    if player_bust and dealer_bust:
        player_won = False
        push = True
    elif player_bust:
        player_won = False
        push = False
    elif dealer_bust:
        player_won = True
        push = False
    else:
        player_won = p_total > d_total
        push = (p_total == d_total)

# Adds data to row under the data frame
    logger.log_round(
        round_id = round_id,
        player_total = p_total,
        dealer_total = d_total,
        player_bust = player_bust,
        dealer_bust = dealer_bust,
        player_won = player_won,
        push = push,
        num_player_cards = len(player_hand),
        num_dealer_cards = len(dealer_hand),
        player_actions = ','.join(actions),
        strategy_name = strategy_name,
    )



if __name__ == "__main__":
    logger = GameLogger()
    strategy_name = "hit_till_17"

    # simulate round 1000 times and log to csv
    for round_id in range(1, 1001):
        simulate_round(round_id, strategy_name, logger)

    logger.save()
