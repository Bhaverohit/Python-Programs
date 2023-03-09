try:
    a = int(input("Enter a number : "))
    c = 1/a
    print(c)

except ValueError as e:
    print("Please Enter Number Only!")

except ZeroDivisionError as e:
    print("Please Enter Non-Zero Number Only!")
