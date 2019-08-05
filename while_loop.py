""""""
# Learn conditional repetition
# two loops for-loops and while loops
""""""

counter = 5
while counter !=0:
    print (counter)
    # augmented operator
    counter -= 1

counter = 5
while counter:
        print(counter)
        # augmented operator
        counter -= 1

print ("outside while loop")

# Run forever
while True:
    print ("Enter a number")
    response = input() # take user input
    if int(response) %7 == 0:   # take user input
        break                   # number dividible by 7
                                # exit loop
