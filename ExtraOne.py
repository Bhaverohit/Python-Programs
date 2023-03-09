a = 10
b = 20
# c = sum(a, b)  # Will throw an error because sum() fn doesn't work on int objects
c = sum((a, b))
print(c)
