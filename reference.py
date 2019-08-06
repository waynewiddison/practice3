"""
This 'reference' file is to learn about references
"""

def modify(k):
    """ test functions
        :return nothing"""
    k.append(39)  # append to the list inside the function
    print("k=", k)


def replace(g):
    """replace input list
    :param g: input list
    :return: nothing
    """
    g = [17, 48, 89]
    print("g = ", g)


def replace_content(g):
    """
    Replace the content of the list
    :param g: input list
    :return: nothing
    """
    g[0] = 88
    g[1] = 22
    g[2] = 44
    print("g = ", g)


def main():
    """ test functions
    :return nothing"""
    m= [9, 15, 24]
    print("Before m = ", m)
    modify(m)
    print("After m = ", m)
    # list are pass by reference
    replace(m)
    print("After replace() m = ", m)

    replace(m)
    print("After replace() m = ", m)

    replace_content(m)
    print ("after replace content() m = ", m)



if __name__ == '__main__':
    main()
    exit(0)
