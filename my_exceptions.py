"""
Learn about exceptions
"""

import sys

def convert(s):
    """converts a string to integer
    :return:
    """

    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error ()" \
              .format(str(e)), file=sys.stderr)
    return -1


def sqrt(x):
    """
    Compute the sqrt using the method of Heron of Alexandrea
    :param x: Number to compute the sqrt
    :return: The sqrt of x
    """
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x / guess) / 2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()
    return guess


def main():
    """
    Test function
    :return:
    """
    # print(convert("11"))
    # print(convert("Hello"))
    # print(convert([1, 4, 8]))
    # I was expecting to see an conversion error invalid literal for int() with base 10: "Hello"
    # I didn't see that ... or the 'argument must be a string' error.  Didn't see that either.

    try:
        print(sqrt(9))
        print(sqrt(11))
        print(sqrt(-1))
    except ValueError:
        print("Cannot compute the value of negative numbers")

    print("Done")

if __name__ == '__main__':
    main()
    exit(1)
