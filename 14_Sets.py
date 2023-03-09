# Set is a collection of non repeatative items
# Unhashable types are not allowed (Lists, Dictonaries), only hashable (tuple)
# Sets are immutable
# Sets are unordered
# Sets are not indexed
# If the dataType of same value is different (i.e str "5" and int 5) then both will be present in the set

sets = {1, 2, 3, 4, 4, 3, 2, 1}
print(type(sets))
print(sets)

# Empty Set wrong way
s = {}  # It'll create an empty dictonary not set
print(type(s))

# Empty Set right way
se = set()
print(type(se))

se.add(5)
se.add(4)
se.add(3)
# se.add([1, 2]) # Throws an error
# se.add((1, 2))
print(se)
print(max(se))
print(min(se))
print(len(se))

# Note
s1 = set()
s1.add(20)
s1.add("20")
s1.add(20.0)  # Because 20 and 20.0 are same so considered only once
print(s1)

# Set Functions
"""
se.add() # This function adds an element to the left most side
se.clear()
se.copy()
se.difference()
se.difference_update()
se.discard()
se.intersection()
se.intersection_update()
se.isdisjoint()
se.issubset()
se.issuperset()
se.pop()
se.remove()
se.update()
se.union()
se.symmetric_difference()
se.symmetric_difference_update()
len(se)
"""
