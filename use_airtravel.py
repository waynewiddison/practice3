"""
Learn about creating our own "class"
Use in conjunction with program airtravel

"""

from airtravel import Flight, Aircraft


def main():
    """
    Test function
    :return:
    """
    f1 = Flight("SN066")
    print(f1.number(), f1.airline())
    # print(f, type(f))
    # print(f.number())
    # f2 = Flight("ab345")
    f2 = Flight("AB352")
    print(f2.number(), f2.airline())
    # could use: Flight.number(f)
    a1 = Aircraft("G-EUP", "Airbus A319", num_rows = 22, num_seats_per_row = 6)
    print(a1.registration(), a1.model())



if __name__ == '__main__':
    main()
    exit(1)