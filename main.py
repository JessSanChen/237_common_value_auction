import random
import statistics
import matplotlib.pyplot as plt


def main():
    curse_mags = list()
    for side in range(2,100):
        for s1 in range(2, side+1):
            # interim expectation
            interim_s2 = statistics.mean(range(1,side+1))
            interim_val = s1 + interim_s2 

            # posterior expectation
            post_s2 = statistics.mean(range(1,s1)) 
            post_val = s1 + post_s2

            # magnitude of winner's curse
            curse_mag = post_val-interim_val
            curse_mags.append((side,curse_mag))
    return curse_mags


if __name__ == "__main__":
    curses = main()

    # Extract x and y values
    x_values = [x for x, y in curses]
    y_values = [y for x, y in curses]

    # Create the plot
    plt.plot(x_values, y_values)
    plt.xlabel('Sides of Dice')
    plt.ylabel("Magnitude of Winner's Curse (Posterior - Interim Value Expectation)")
    plt.title("Winner's Curse Magnitude by Sides of Dice")
    plt.savefig('initial_sim.png')
    plt.show()
