# a = 24
# b = 15

# # Booleans
# print(a > b)
# print(a == b)

# Strings - can use both single or double quotes

# c = "double quotes\n"
# d = 'single quotes\n'
# e = 'Printing "double quotes" within single quotes'
#
# print(c, d, e)

# # Slicing strings
# hi = "Hello World!"
# print(hi)
#
# # Indexing in Python begins at position 0
# # Python slicing includes the first number in the slice but excludes the second number in the slice
# print(hi[0:12])
# print(hi[0:5])
# # Ie [0:5] returns a slice up to index 0, 1, 2, 3, 4
#
# print(hi[:8])
# print(hi[::-1])
#
#
# print(hi.upper())
# print(hi.capitalize())
# print(hi.count("l"))

# # Booleans
# hi = "Hello World"
# a = True
# b = False
#
# print(a == b)
#
# # This comes back false because it contains a 'space' and an exclamation pt !.
# # would return true if hi = "helloworld"
# print(hi.isalpha())
#
# # another one
# print(hi.endswith("d"))

# In python zero represents false, any number which is not zero will return true
x = 10
y = 0

print(bool(x))
print(bool(y))

# None keyword is equivalent to Null is SQL
z = None

print(bool(z))
print(bool(z == False))
# Even though the boolean of z is None, None does not equal None as None is a non existent value, not zero

