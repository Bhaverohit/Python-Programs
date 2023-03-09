# The else statement after loops is only executed if loop is narturally terminated
# else can be used with while loop as well

for i in range(10):
    print(i)
    if(i == 5):
        break
else:
    # Else statement won't execute
    print("Loop successfully terminated with breakStatement")


# for i in range(10):
#     print(i)
# else:
#     print("Loop successfully terminated without breakStatement") # Else statement will execute
