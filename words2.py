""""
Get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt
Task 1: count number of words in the document,
then count the number of characters in the file

Day 2: We started with this program today.
Function driven
"dunder = double underscore

"""
from urllib.request import urlopen

def fetch_words(filename):
    """for the next iteration of this function, insert filename into the brackets of fetch_words
    :param filename: url address to file
    :return: a list with the items
    """
    count = 0  # this defines a counter
    data = [] # this begins as an empty list

    with urlopen(filename) as story:
        for line in story: # line is a "record".
            words = line.decode('utf-8').split() # uses the space as a separator
    # split with space as the default which needs to be placed in quotes
    # print(words); words is now a list
            for word in words:
                data.append(word) #data.append is now a list of words
    return data


"""
def print_words: # created a new function
later...
def print_items (items):
Print elements of the collection
:param items: A collection of objects
:return: nothing
"""

"""
for item in items:
    print(item
"""

def main():
    """
    Test function for words library
    :returns nothing
    :return:
    """
    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    words = fetch_words(file) # this is a list of items ... in this case they are words
    print (words)
    

if __name__ == '__main__':
    main()
    exit(0)






