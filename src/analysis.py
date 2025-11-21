import pandas as pd
import matplotlib.pyplot as plt


def main():
    # data frame read from the csv file of logged rounds
    df = pd.read_csv("data/blackjack_history.csv")

    print(df['player_won'].value_counts(dropna=False))
    print(df.head())


    # win rates true or false -> convert to numeric percentage mean
    win_rate = df['player_won'].mean()
    print(f"Win rate: {win_rate:.2%}")

    # cumulative sum of wins divided by round number (cumulative win rate up to that round)
    df['cumulative_win_rate'] = df['player_won'].cumsum() / df['round_id']

    # negates player bust df and keeps only true instances
    non_bust_df = df[~df['player_bust']]
    non_bust_totals = non_bust_df['player_total']


    # creates window with multiple subplots
    # axis[0] is cumulative, axis[1] is histogram
    # figure size is in inches
    fig, axes = plt.subplots(2, 1, figsize=(8, 9))

    # Cumulative win rate plot
    axes[0].plot(df['round_id'], df['cumulative_win_rate'])
    axes[0].set_xlabel("Round")
    axes[0].set_ylabel("Cumulative Win Rate")
    axes[0].set_title("Blackjack win rate over time")

    # Histogram plot
    # splits histogram into integer bins 12-22
    axes[1].hist(non_bust_totals, bins=range(12, 23))
    axes[1].set_xlabel("Final Player Total")
    axes[1].set_ylabel("Frequency")
    axes[1].set_title("Distribution of Final Player Totals (non-bust)")

    # auto adjusts spacing and labels
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

