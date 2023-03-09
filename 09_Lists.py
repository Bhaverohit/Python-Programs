# List elements are present in order
# Elements can be accessed using index which starts from zero
# OverWriting an element is possible (Mutable)
# Lists are dynamic
# If you access element more than available indexes then there's error
# A list can contain different types of data (arbitary objects)
# List inside list is possible
# Slicing can also be done same as strings
# To get list in reverse order [::-1]
# Never take less than -1 in skip section of lists

sample = ["Rohit", 50, 1.1, True]

List = [1, 2, 3, 10, 20, 50, 11]
print(List)

# Return List in reverse order
print(List[::-1])

# OverWriting
List[2] = 99
print(List)

# List Methods
numbers = [2, 5, 4, 7, 9, 3, 64, 12, 35, 45]
print(numbers)

numbers.sort()  # Sorts the actual list
print(numbers)

numbers.reverse()  # Reverse the actual list

numbers.append(48)  # Adds only one element at last of the list

# Syntax => numbers.insert(indexWhereToInsert, valueToBeInserted)
numbers.insert(0, 999)  # Used in inserting element at desired index
print(numbers)

numbers.pop(2)  # Removes element at index 2

numbers.remove(9)  # Removes element which has value 9

numbers.extend([9999, 9999, 9999])  # Adds every object at last individually
print(numbers)

numbers.clear()
numbers.copy()
numbers.index()
numbers.count()
numbers.reverse()
print(max(numbers))
print(min(numbers))


# The list() function will create a list of passed string object
print(list('Number'))

# Multiple updates
lis = [1, 2, 3, 4]
lis[0:2] = ['Rohit', 'Kumar', 'Bhave']
print(lis)

# List in list

LL = [1, 2, 3]
LL[1] = ['Rohit', 'Bhave']
print(LL)
