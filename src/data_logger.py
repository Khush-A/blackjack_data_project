import pandas as pd 

class GameLogger:
    def __init__(self):

        # Sets column headers
        self.history = pd.DataFrame(columns=[
            'round_id',
            'player_total',
            'dealer_total',
            'player_bust',
            'dealer_bust',
            'player_won',
            'push',
            'num_player_cards',
            'num_dealer_cards',
            'player_actions',
            'strategy_name',
        ])
    
    # logs the round under the headers
    def log_round(self, **kwargs):
        self.history.loc[len(self.history)] = kwargs
    
    # Save the history of the round to the csv
    def save(self, path="data/blackjack_history.csv"):
        self.history.to_csv(path, index=False)

