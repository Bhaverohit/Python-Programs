try:
    a = int(input("Enter a number : "))
    c = 1/a
    print(c)

except Exception as e:
    print(e)
# Else block will only execute if there is no errors
else:
    print("Program Executed")
