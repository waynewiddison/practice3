""""
Get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt
Task 1: count number of words in the document,
then count the number of characters in the file
"""
from urllib.request import urlopen

def fetch_words(filename):
    """for the next iteration of this function, insert filename into the brackets of fetch_words"""
    count = 0
    data = []

    with urlopen(filename) as story:
        for line in story:
            words = line.decode('utf-8').split()
    # split with space as the default which needs to be place in quotes
    # print(words); words is now a list
            for word in words:
                data.append(word)

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
    file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"
    words = fetch_words(file)
    print (words)
    

if __name__ == '__main__':
    main()




