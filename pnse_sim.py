import numpy as np
import pandas as pd
import statistics

def simulate_toy_game(k):
    """
    Simulate the toy game for a given number of dice sides k.
    """
    results = []

    s1=k
    # for s1 in range(1, k + 1):
        # for s2 in range(1, k + 1):
        #     # Common value is the sum of the signals
        #     common_value = s1 + s2
            
    # Probabilities of s1 > s2 and s1 = s2
    prob_win_outright = (s1 - 1) / k
    prob_tie = 1 / k
    
    # Winning probability
    prob_win = prob_win_outright + 0.5 * prob_tie
    
    # Expected values conditional on winning
    # Expected value of s2 given s1 > s2
    if s1 > 1:
        expected_s2_given_win = statistics.mean(range(1,s1))   # Average of {1, 2, ..., s1 - 1}
    else:
        expected_s2_given_win = 1      
    print(expected_s2_given_win)
    
    expected_common_value_given_win = (
        prob_win_outright * (s1 + expected_s2_given_win) +
        0.5 * prob_tie * (s1 + s1)
    ) / prob_win
    
    # Add the results to the dataframe
    results.append({
        'k': k,
        's1': s1,
        # 's2': s2,
        # 'Common_Value': common_value,
        'Prob_Win': prob_win,
        'Posterior_Expectation': expected_common_value_given_win
    })
    
    return pd.DataFrame(results)

# Simulate for k = 2 to k = 100
all_results = pd.concat([simulate_toy_game(k) for k in range(2, 100)], ignore_index=True)
all_results.to_csv("pnse_sim.csv")

# Display the results
# import ace_tools as tools; tools.display_dataframe_to_user(name="Toy Game Simulation Results (k=2 to k=100)", dataframe=all_results)
