"""
Learn about lists



"""

def main():
    """

    :return:
    """
    s = "show how to do it".split()
    print(s, type(s))

    # Accsss by index
    print("s[3]", s[3])
    print ("last member:", s[len(s) - 1])  # very unpythonic
    print () # print a blank line

    # use negative index
    print("s[-1]:", s[-1])

    # slicing
    print("From 1 to one before the last member", s[1:-1])
    print("From l to three members", s[1:3])
    print("From l to the end", s[1:])
    print("From beg to the 3", s[:3])
    print("From beg to the end", s[:])
    print ()

    # Make a copy of list
    t = s   # shallow copy
    print ("s:", s)
    print ("t:", t)
    t = s[:]    # deep copy
    # or this: t = s.copy()
    # or this: t = list(s)
    print("t is s:", t is s)
    print("t==s:", t == s)
    print()

    # shallow copies
    # A list of list
    a = [[1,2], [3, 4]]
    print(a, type(a))
    print()
    print("a[0]:", a[0])
    print("a[0][1]:", a[0][1])

    # copy the list of list
    b = a[:]
    print("b is a: ", b is a)
    print("b[0]", b[0])
    print("a[0] is b[0]", a[0] is b[0])
    # change on element
    # assignment: change a[0] to something different
    a[0] = [8, 9]
    print("change a[0] to [8,9]")
    print("a[0]:", a[0])
    print("b[0]:", b[0])
    print("a[0] is b[0]", a[0] is b[0])
    print("a[1] is b[1]", a[1] is b[1])

    # modify a[1]
    print("a[1]:", a[1])
    print("b[1]:", b[1])
    print("a[1] is b[1]", a[1] is b[1])
    print("a:", a)
    print("b:", b)

    # Repetition
    c = [21, 37]
    d = c * 4
    print("c", c)
    print("d", d)
    s= [[-1, 1]] * 5
    print(s)
    s[1].append(7)
    print(s)

    # index
    w = "the quick brown fox jumps over the lazy dog".split()
    i = w.index('fox')
    print("The index of 'fox' entry is:", i)
    # i = w.index('cat')
    # print("The index of 'cat' entry is:", i)
    # If no index is found, it will throw a ValueError

    print("'the' value is ", w.count("the"))
    # Membership testing with: count()
    # Also test membership with: in, not in
    print(37 in [12, 22, 37, 99])
    print(78 not in [12, 22, 37, 99])
    print()

    # Removing elements from list: index and del
    w = "the quick brown fox jumps over the lazy dog".split()
    print(w)
    print(len(w), w)
    del w[3]    # delete using index
    print(len(w), w)
    # remove using: remove()
    w.remove("over")
    print(len(w), w)
    # same as
    del w[w.index('dog')]
    print(len(w), w)

    # Rearranging the list of elements
    g = [1,11,21,1211,112111]
    print ("g:", g)
    g.reverse() # permanent change in order
    print ("reverse g:", g)
    g.reverse()   # restore order

    # Sorting method accepts two arguments, key and reverse
    d = [21, 33, 11, 77, 88, 33, 101, 1]
    print ("d:    ", d)
    d.sort()
    print("sort d:", d)
    d = [21, 33, 11, 77, 88, 33, 101, 1]
    d.sort(reverse=True)
    print("sort.reverse d: ", d)

    # Sort by key
    w = "the quick brown fox jumps over the lazy dog".split()
    print("the orig list is:", w)
    w.sort(key=len)
    print("reverse order:", w)

    # consider studying list on my own using help list

    print()
    print ("Wayne declares end of program")


if __name__ == '__main__':
    main()
    exit(1)