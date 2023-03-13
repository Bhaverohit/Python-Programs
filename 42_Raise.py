# raise keyword is used in order to throw an error

# It should containt only alphabets
yourName = input("Enter your name : ") 

if yourName.isnumeric():
    raise Exception("Name can't be numbers")

print("This print statement and below code is executed only if yourName is not numeric")


# Raising built-in errors 

# Enter 0 as your salary
yourSalary = int(input("Enter your Salary : "))

if yourSalary == 0:
    raise ZeroDivisionError("Salary can't be zero")