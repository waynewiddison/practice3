"""
Learn about Python return semantics and how Python functions handle arguments
"""

def egg(var):
    """ returns a variable back to the user
    :param var: input object
    :return: input object
        """
    return var


def sum_two(num1, num2=8):
    """ sum two input objects
    :param num1: object 1
    :param num2: object 2 (optional parameter), default value is "8"
    :return: sum of objects
    required parameters must come first
    optional parameters after required parameters
    """

    total = num1 + num2
    print(num1, " + ", num2, " = ", total)
    return total
    # return num1 + num2


def banner(message, border='*'):
    """
    print message in banner form
    :param message:
    :param border:
    :return:
    """
    print(border + len(message))
    print (message)
    print(border + len(message))

def add_spam(menu=None): # None is the same as the null in C++; it means empty (I think)
    """Add spam to the menu list
    :param menu:
    :return: menu_list
    """
    if menu is None:
        menu = []
    menu.append ('spam')
    return menu


def main():
    """
    Test Function
    :return:
    """
    c = [6, 10, 20]
    e = egg(c)
    print (c is e)

    n1 = 3
    n2 = 9
    sum_two(n1, n2)
    sum_two(n1)
    banner("Weber State")
    banner("Weber State University", "$")

    breakfast = ['eggs', 'bacon']
    print("before", breakfast)
    add_spam(breakfast)
    print("After", breakfast)

    print(n1 , " + ", n2, " = ", sum_two(n1, n2))
    print("Only one input", sum_two(n1))



if __name__ == '__main__':
    main()
    exit(1)


    """ Next part of this exercise: def border (message, border = * """

# def border ():
    # b = *
    # c = *
    # how to calculate how long the border string is going to be; such as s=3 then print the string 3 times
    # ask for a word to include within the border then determine border strength
    # len (string length)
    # use 3 print statements: print upper border, then print the WORD, then print the lower border


