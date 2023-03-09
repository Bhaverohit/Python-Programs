# def keyword is used to declare a fn

# Function 1 : Without return
def greet(name):
    print("Nice to meet you!, " + name)


greet("Rohit")


# Function 2 : With return
def percent(marks):
    p = ((marks[0] + marks[1] + marks[2] + marks[3])/400)*100
    return p


marks1 = [43, 15, 48, 85]
marks2 = [31, 95, 44, 53]

per1 = percent(marks1)
per2 = percent(marks2)

print(per1, per2)


# Function 3 : With default argument
def greet(name="Stranger"):
    print("Nice to meet you!, " + name)


greet()


# Function Iterative
def factorial(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product


print(factorial(3))

# Recursion


def fact_recur(n):
    if n == 1 or n == 0:
        return 1
    return (n * fact_recur(n-1))


print(fact_recur(5))


# Nesting of function is allowed
def Rohit():
    def A():
        # First this is executed because it is inside outest fn
        print("Inside A")

    print("Inside Rohit")
    A()  # Second this is executed
    print("After calling A()")  # Third is it executed


Rohit()
