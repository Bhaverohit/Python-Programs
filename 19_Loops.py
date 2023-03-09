from re import L


i = 1

l = ["Rohit", "Kumar", "Bhave"]

while i <= 10:
    print(i)
    i = i + 1

for items in l:
    print(items)

# Range Function
# Iterations = PassedArgument - 1

# for k in range(10):
#     print(k)


# range(Start, Stop, SkipSize)
for k in range(5, 10, 2):
    print(k)

# Pass is a null statement in python , it instruct to do nothing, we use it in case we need to insert some code later

for i in l:
    if i == "Kumar":
        pass
