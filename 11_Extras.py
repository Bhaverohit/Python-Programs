# Variables are pointers or references to the objects that are actually present in the memory (Variables themselves do not have a memory location in the memory)

# Identity :- Can be considered to be the address in the memory where the object is stored. An object's identity never changes once it has been created 
# id() function returns an integer representing its identity
# is operator compares the identity of two objects
x = 45
y = 45
z = 65

print(id(x), id(y), id(z)) # ID of x and y are same because they're pointing to the same value in the memory

print(id(x) is id(y))

# Python don't have char data type

# Indentations can be a tab or four spaces