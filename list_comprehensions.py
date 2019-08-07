"""
List Comprehensions
"A lazy evaluation of the object"
Readable, expressive, and effective

"""
from math import factorial, sqrt
from pprint import pprint as pp



def is_prime(num):
    """
    Determine if the number is prime
    :param num: num to test
    :return: True for prime numbers
            False for non-prime numbers
    """

    if num < 3:
       return False
    for i in range(2, int(sqrt(num)) + 1):
       if num % i == 0:
           return False
    return True


def main():
    """
    Test function
    :return:
    """

    words = "Today I am very happy to learn about list comprehensions".split()
    print(words)
    data = []   # empty list for now
    for word in words:   # some analysis...
        data.append(word)


    # "Filter" data
    print(data)

    # another example...
    # task: sum? length of first 20 factorial numbers

    # Wayne's recommendation: create a list of the individual results then count all the digits in the list
    # instructor: catch the values in an array or actually and empty list
    info = []  # empty list
    for x in range(20):
        # print(factorial(x))
        info.append(len(str(factorial(x))))
    print(info, type(info))
    # Use a list comprehension: []
    info2 = [len(str(factorial(x))) for x in range(20)]
    print(info2, type(info2))

    # Set comprehensions: ()
    info3 = (len(str(factorial(x))) for x in range(20))
    print(info3, type(info3))

    # Dictionary Comprehensions
    nba_teams = {'jazz': 'SLC', 'warriors': 'OAKLAND', 'clippers': 'LA'}
    print(nba_teams)
    teams_nba = {city: mascot for mascot, city in nba_teams.items()}
    print(teams_nba)

    primes = [x for x in range(101) if is_prime(x)]  # instead of 101, we could use a larger number like 10001
    print(len(primes), primes)




if __name__ == '__main__':
    main()
    exit(1)