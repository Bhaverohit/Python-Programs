def increment(num):
    try:
        return int(num) + 1

    except:
        raise ValueError("Wrong Input")


a = increment('^')
print(a)
