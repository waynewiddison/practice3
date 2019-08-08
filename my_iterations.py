"""
Learn about When working with iterators, generators, etc.
look at the documentation for the itertools module
"""

from itertools import islice, count, chain
# islice(iterable, stop)

from list_comprehensions import is_prime

def main():
    """
    Test function
    :return:
    """
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print(thousand_primes, type(thousand_primes))
    print("List of first 1K prime numbers:", list(thousand_primes))
    # Note: If you need to use the object again, you need to re-generate it
    thousand_primes = islice((x for x in count() if is_prime(x)), 1000)
    print("Sum of first 1K prime numbers:", sum(thousand_primes))

    # Other built-ins to use with itertools: any (think "or"), all (think "and")
    print(any([False, False, True]))
    print(all([False, False, True]))
    print()

# Assignment: Do I have any prime numbers in the range of 1328, 1361?
# my guess: use the range command
# this should return a TRUE
    print("Are there prime numbers between 1328 and 1361?",
          any(is_prime(x) for x in range(1328, 1362)),
          list(x for x in range(1328, 1362) if is_prime(x)))


    # Check if all names in an iterable are in title form: First letter capitalized
    names = ["London", "New York", "Ogden"]
    print(all(name == name.title() for name in names)) # name == name.title will yield true or false
    print()

    # Another built-in: zip
    sunday = [2, 2, 5, 7, 9, 10, 9, 6, 4, 4]
    monday = [12, 14, 14, 15, 15, 16, 15, 13, 10, 9]
    tuesday = [13, 14, 15, 15, 16, 17, 16, 16, 12, 12]
    # Calculate the min, max, and average of all points
    # (:6.1f) => 6 chars width, 1 decimal precision floating point
    for temps in zip(sunday, monday, tuesday):
        # print("Average =", (mon + tue/2)   We moditied this from what we did earlier
        print("min={:4.1f}, max={:4.1f}, ave={:6.1f}".format(
            min(temps), max(temps), sum(temps)/len(temps)))

    # chain from intertools
    all_temps = chain(sunday, monday, tuesday)
    print("All temperatures > 0", all(t > 0 for t in all_temps))
        # This returns a true/false statement.  For this example: true


if __name__ == '__main__':
    main()
    exit(1)