# "is" and "is not" are two identity operators in python

a = 1001
b = 1000 + 1

print(id(a))
print(id(b))

print((a == b))  # True because both variables have same value
print(a is b)  # False because id's of both variables are different
