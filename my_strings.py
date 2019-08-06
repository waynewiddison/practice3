"""
Learn about strings
"""


def main():
    """
    Test Function
    :return: 
    """
    s1 = "This is super cool"
    print (s1)
    print("Size of s1", len(s1))
    # Concatenation "+"
    s2 = "Weber" + "State" + "University"
    print(s2)
    # If you need to join large strings, use the join() method instead of the + operator
    teams = ["Real Madrid", "Barcelona", "Manchester United"]
    record = ":".join(teams)
    print(record)
    # record = "\n".join(teams)
    # print (record)
    # split record
    print("Split rec", record.split(":"))

    # Partioning Strings
    # You can use the "dummy" object: _     which is the underscore
    departure, _, arrival = "London.Edinburgh".partition(":")
    print(departure, arrival)

    # String formatting using the format ()
    print("The age of {0} is {1}".format("Mario", 34))
    print("The age of {0} is {1}, and the birthday of {0} is {2}".format("Mario", 34, "August 12th"))
# omit the index
    print('The best numbers are {} and {}'.format(4, 22))

    # By field name
    print("Current position {latitude} {longitude}".format(latitude="60 N", longitude="5E"))

    # print elements of list
    print("Galactic position x={pos[0]}, y={pos[1]}, z={pos[2]}".format(pos=(85.6, 23.3, 99.0)))

    # Second version of "format": print(f"{var}) python 3.7 or greater
    # fname = "Waldo"
    # lname = "Weber"
    # print(f"The WSU mascon is {fname} {lname}")

if __name__ == '__main__':
    main()
    exit(1)