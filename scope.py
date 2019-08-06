"""
Learn about scoping in Python
define a global variable
"""

count = 0 # global variable


def show_count():
    """display the current count
    :return: nothing
    """
    print(count)

def set_count(num):
    """set global to input
    :param num: input number
    :return: nothing
    """
    global count
    count = num


def main():
    """
    Test Function
    :return: 
    """
    show_count()
    set_count(9)
    show_count()



if __name__ == '__main__':
    main()
    exit(0)