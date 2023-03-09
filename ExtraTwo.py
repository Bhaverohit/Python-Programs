# It can be used for set and dictonary as well

a = [20, 1, 55, 48, 4]
b = []

# for item in a:
#     if item % 2 == 0:
#         b.append(item)

b = [item for item in a if item % 2 == 0]
print(b)
