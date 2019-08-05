# This program is called list
"""
Learn about lists
Unlike strings, lists are mutable.
you can update, and append elements to it.
"""
# use [] for define a list
l = []
print("List ", l, type(l))
# a list of objects ... any type
a=["apple", "orange", "pear"]
# access by index notation   Index starts at zero
print (a, a[1])
print (a, a[2])
# replace an element
a[0]="tomatoes"
print (a, a[1])
a[1] = 3.14159
print(a, a[1])

# begin with an empty list
# ask user to enter 3 names, add them to the list
names = []
        # name = input("Enter your name")
total = 0
while total < 3:
    name = input ("Enter a name")
    names.append(name)
    total = total+1
# display list
print(names)

 # wayne's attempt - didn't wok   response = input()  # take user input
# if input % 0 == 0:  # take user input
       # exit loop
   # append names
