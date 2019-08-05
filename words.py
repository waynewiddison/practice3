""""
Get a file from the web
http://icarus.cs.weber.edu/~hvalle/hafb/words.txt
Task 1: count number of words in the document
"""
from urllib.request import urlopen
file = "http://icarus.cs.weber.edu/~hvalle/hafb/words.txt"

with urlopen(file) as story:
    for line in story:
        words = line.decode('utf-8').split()
        # split with space as the default which needs to be place in quotes
        # print(words); words is now a list
        for word in words:
            count += 1
print("Total number of words")
        print(line)
# assignment: count how many words are in this STORY
# waynes idea: identify individual words ... and count them.
# notice the file is 'bytes' not strings, so decode them first.
# the instructor wants strings, so a second loop is needed.
# task two: count the number of times each word appears in the file.
print("Total number of words")



