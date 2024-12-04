import numpy as np
import pandas as pd
import statistics
import matplotlib.pyplot as plt

def simulate_toy_game_with_interim_and_posterior(k_values):
    """
    Simulate the toy game for given values of k, calculating both interim and posterior expectations.
    """
    results = []

    for k in k_values:
        s1 = k  # Consider the maximum signal for Player 1
        # Probabilities of s1 > s2 and s1 = s2
        prob_win_outright = (s1 - 1) / k
        prob_tie = 1 / k
        
        # Winning probability
        prob_win = prob_win_outright + 0.5 * prob_tie
        
        # Expected value of s2 given s1 > s2
        if s1 > 1:
            expected_s2_given_win = statistics.mean(range(1, s1))  # Average of {1, 2, ..., s1 - 1}
        else:
            expected_s2_given_win = 1  # Default to 1 for edge case
        
        # Posterior expectation
        expected_common_value_given_win = (
            prob_win_outright * (s1 + expected_s2_given_win) +
            0.5 * prob_tie * (s1 + s1)
        ) / prob_win

        # Interim expectation
        interim_expectation = s1 + (k + 1) / 2  # Expected value of s2 is the mean of {1, ..., k}

        # Add results
        results.append({
            'k': k,
            'Interim_Expectation': interim_expectation,
            'Posterior_Expectation': expected_common_value_given_win
        })
    
    return pd.DataFrame(results)

# Define the range of k values
k_values = range(2, 101)

# Simulate for k = 2 to k = 100
results = simulate_toy_game_with_interim_and_posterior(k_values)
results.to_csv("another.csv")

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(results['k'], results['Interim_Expectation'], label='Interim Expectation', marker='o')
plt.plot(results['k'], results['Posterior_Expectation'], label='Posterior Expectation', marker='x')
plt.xlabel('k (Number of Sides on Dice)')
plt.ylabel('Expectations')
plt.title('Interim vs Posterior Expectations as k Increases')
plt.legend()
plt.grid()
plt.savefig("inter_post_exp.png")
plt.show()
