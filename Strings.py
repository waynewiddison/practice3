# file name Strings
"""
Strings and collections
a strng is a immutable sequence of Unicolde code-points
"""
print ('this is a string')
print ("this is a string too")
# concatenation and adjacent strings
s1 = "First "
s2 = "Second"
print (s1 + s2)

# multi-line strings and newlines
s3 = """This is
a multiline
 string"""
print (s3)
s4 = "This is\na multi-line\nstring"
print (s4)
 # support for backslash

s5 = "A\\in a string"
print (s5)

s6 = 'this is "wow'
print (s6)

# Raw Strings
raw_string = r'c:User\Documents\Books'
print (raw_string)

# capitalize the string
print (s, s.capitalize())


# String as sequence
s = "arrot"
print ("s[4]", s[4], type (s))  # index notation: 0, 1, 2, etc

