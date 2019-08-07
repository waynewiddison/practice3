"""
Learn about recursions
iterable, iterator objects
Use the built-in iter(): create an iterable object,
and next(): fetch the next element in the iterable object
"""

def first(iterable):
    """Return the next member of the list IF available
    :param iterable: iterable object
    :return: Next member or
    :except: ValueError for StopIteration"""

    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")


def main():
    """
    Test function
    :return:
    """
    iterable = ["Spring", "Summer", "Fall", "Winter"]
    iterator = iter(iterable) # give me an iterator
    print(type(iterator), iterator)
    print(next(iterator))   # Actually only need one of these statements, not 6 or more.
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))


# need code here to call "first"


if __name__ == '__main__':
    main()
    exit(1)