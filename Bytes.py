"""
Learn about bytes.
Bytes are similar to str type, but they are a sequence of bytes instead of Unicode coode points.

Use for raw bianary data, fixded-width, single-byte encloding: ASCII

Use the byte() constructor
"""

d-b'data'
print (d, type(d))  # the type is a byte ... not a string

info - b'some bytes here' \
# split the bytes using split() method for bytes
print (info split())

#Encoding: Alt+162 =
message = "Vamos al zoologico"
data = (message)
data = message.encode ("utf-8")
print (data)
# Decoding the string
new-message = data.decode("utf-8")
print(new_message)



