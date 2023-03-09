# Tuples Syntax => tuple = (1,2,3)
# Tuples can be accessed using indexes
# Tuple elements can not be overWritten (Immutable) if you try then get error
# To get tuple in reverse order (::-1)
# Program execution faster than than Lists
# More efficient than Lists for creating non-modifiable ordered list
# Never take less than -1 in skip section of tuples

t = (1, 2, 3, 4, 5)
t1 = ()  # Empty Tuple
t2 = (5)  # Wrong way to initialize a tuple of single element
t3 = (6,)  # Right way to initialize a tuple of single element

# Print tuple in reverse order
print(t[::-1])

# The tuple() function will make tuple of passed String object
print(tuple('123456'))

# Packing
tup = (1, 2, 3, 4)
# UnPacking
# Here in other words we're assigning 1 to a, 2 to b, 3 to c and 4 to d {Which can be accessed using a,b,c,d}
(a, b, c, d) = tup
print(a, d)

# Another ways for Packing and Unpacking
(g, i, f) = (10, 20, 30)
x, y, z = 9, 99, 999

print(g, i, f)
print(x, y, z)


# Tuple Functions
tupl = (1, 2, 3, 4, 5)

tupl.count()
tupl.index()
