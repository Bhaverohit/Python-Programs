import math

# First you need to import math


# Constants of Math Module

print(math.pi)
print(math.tau)
print(math.nan)  # NaN = Not a Number
print(math.inf)
print(-math.inf)
print(math.e)  # Eular's number

print("Type of pi:", type(math.pi))
print("Type of tau :", type(math.tau))
print("Type of nan :", type(math.nan))
print("Type of inf :", type(math.inf))
print("Type of e :", type(math.e))

# Arithmetic Functions
print("------------------------")
print(math.factorial(5))
print(math.ceil(5.7))
print(math.floor(5.012))
print(math.trunc(5.156))
print(math.perm(5))
print(math.gcd(5, 10, 20))
print(math.lcm(5, 10, 20))
print(math.comb(5, 10))

# Power & Logarithmic Functions
# All of these are float types

print("-------------------------------")
print(math.pow(2, 3))
print(math.exp(3))
print(math.log(5))
print(math.log10(10))
print(math.log2(10))
print(math.log1p(2))
print(math.sqrt(36))
print(type(math.sqrt(36)))

# Trigonometry Functions
print("--------------------------")
print(math.sin(10))
print(math.cos(10))
print(math.tan(10))
print(math.asin(1))
print(math.acos(1))
print(math.atan(1))
