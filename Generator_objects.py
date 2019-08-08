"""
Learn about Generator objects are a cross between comprehensions and generator functions
Syntax: Similar to list comprehension"
    (expr(item) for item in iterable)
"""
# also discussed inporting functions from a previous program (see usage of this)

from list_comprehensions import is_prime

def main():
    """
    Test function
    :return:
    list with first 1 million square numbers
    """
    m_sq = (x*x for x in range(1, 1000001))
    print(m_sq, type(m_sq))
    print('The sum of the first 1M square numbers is', sum(m_sq))
    print('The sum of the first 1M square numbers is',
          sum(x*x for x in range(1, 1000001)))
    # The sum of the prime numbers between 1 to 10K; add a filter which is prime
    print('The sum of the prime numbers between 1 to 10K;',
          sum(x for x in range(1, 10001) if is_prime(x)))



if __name__ == '__main__':
    main()
    exit(1)