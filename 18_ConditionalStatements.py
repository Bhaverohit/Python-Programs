a = 10

if a > 100:
    print("A greater than 100")
elif a > 5:                      # Whichever statement get true first, gets executed
    print("A > 5")
elif a > 7:
    print("A > 7")
else:
    print("Dunno")


# If for searching in other dataTypes
lis = [1, 2, 3, 4, 5, 6]

if 6 in lis:
    print("Yes! it is there")
    if 7 not in lis:
        print("No! it is not there")


# Short-Hand if else block
X = 100
Y = 12

print("X greater than Y") if X > Y else print("Y greater than X")
