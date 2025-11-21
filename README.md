# Blackjack Data Project

A simple Blackjack simulation project that collects game data using pandas and visualises results with matplotlib.

# What This Project Does
- Simulates Blackjack rounds (player vs dealer)
- Logs each round into a pandas DataFrame
- Saves data to data/blackjack_history.csv
- Provides analysis scripts to plot:
    - Win rate over time
    - Distribution of final totals


# Install dependencies:

pip install -r requirements.txt


# Run simulations:

python -m src.simulate_strategies


# Run analysis/plots:

python -m src.analysis