"""
Learn about random
Simulate 6000 rolls of a die (1-6)
fix the number of iterations to 6000

idea: while counter <= 6000
counter = 0
cast = randomnum
counter = counter +1
this program prompts the user for the number of rolls.
"""

import random
import statistics

def roll_die(num):
    """
        Test function
        :param num: number of rolls
        :return: a list of frequencies
        Index 0 maps to 1
        Index 1 maps to 2
        """
    freq = [0] * 6  # initial value is zero
    for roll in range(num):
        n = random.randrange(1, 7)
        freq[n - 1] += 1
        # print(random.randrange(1,7))
    return freq



def main():
    """
    Test function
    :return:
    """
    num = int(input("How many times you need to roll: "))
    result = roll_die(num)
    for roll, total in enumerate(result):
        print("Total rolls of {} = {}".format(roll + 1, total))
    print("Average = {}".format(sum(result)/len(result)))
    print("Mean = {}".format(statistics.median(result)))



if __name__ == '__main__':
    main()
    exit(1)