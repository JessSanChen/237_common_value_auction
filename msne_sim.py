import numpy as np

# Dice sides and bidding range
bidding_range = range(1, 7)

# Simulate the game
def play_game(strategy):
    # Player 1 always rolls a 3
    roll1 = 3

    # Player 2 rolls randomly (1, 2, or 3)
    roll2 = np.random.randint(1, 4)

    # Common value
    common_value = roll1 + roll2

    # Determine Player 2's bid
    if roll2 == 1:
        bid2 = 2
    elif roll2 == 2:
        bid2 = 2
    else:  # roll2 == 3
        bid2 = np.random.choice(bidding_range, p=strategy)

    # Player 1 bids based on their strategy
    bid1 = np.random.choice(bidding_range, p=strategy)

    # Calculate payouts
    if bid1 > bid2:
        return common_value - bid1, 0
    elif bid1 < bid2:
        return 0, common_value - bid2
    else:  # Tie case
        winner = np.random.choice([0, 1])  # Randomly decide winner
        if winner == 0:
            return common_value - bid1, 0
        else:
            return 0, common_value - bid2

# Update strategy based on expected payouts
def update_strategy(strategy, expected_payouts, learning_rate=0.01):
    new_strategy = strategy + learning_rate * (expected_payouts - strategy)
    new_strategy[new_strategy < 0] = 0  # Ensure no negative probabilities
    return new_strategy / new_strategy.sum()  # Normalize probabilities

# Main function to find Nash equilibrium
def find_nash_equilibrium(num_iterations=10000, learning_rate=0.01):
    # Initial uniform strategies
    strategy = np.ones(len(bidding_range)) / len(bidding_range)

    for _ in range(num_iterations):
        # Track expected payouts for each bid
        expected_payouts1 = np.zeros(len(bidding_range))
        expected_payouts2 = np.zeros(len(bidding_range))

        # Simulate games to calculate payouts
        for _ in range(100):  # Number of simulations per iteration
            payout1, payout2 = play_game(strategy)
            bid1_idx = np.random.choice(len(bidding_range), p=strategy)
            bid2_idx = np.random.choice(len(bidding_range), p=strategy)
            expected_payouts1[bid1_idx] += payout1
            expected_payouts2[bid2_idx] += payout2

        # Normalize expected payouts
        expected_payouts1 /= expected_payouts1.sum() if expected_payouts1.sum() > 0 else 1
        expected_payouts2 /= expected_payouts2.sum() if expected_payouts2.sum() > 0 else 1

        # Update strategies
        player1_strategy = update_strategy(player1_strategy, expected_payouts1, learning_rate)
        player2_strategy = player1_strategy  # Symmetry ensures they match

    return player1_strategy

# Find Nash equilibrium
iterations = 20000
payout1,payout2 = 0,0
for _ in range(iterations):
    # strategy = np.ones(len(bidding_range)) / len(bidding_range)
    # strategy = [0, 0, 1,0, 0, 0]
    strategy = [0, 0.5, 0.5, 0, 0, 0]
    p1,p2 = play_game(strategy)
    payout1 += p1
    payout2 += p2
payout1 /= iterations
payout2 /= iterations
print("MSNE: ", strategy)
print("Player (1, 2)'s payout: ", payout1, payout2)

