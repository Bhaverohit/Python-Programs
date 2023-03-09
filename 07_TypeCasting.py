# Type Casting tries to typecase the given dataType into another dataType althogh it doesn't take gaurentee because you can't convert "Rohit" into Integer Right? and some other cases as well

a = "520"
# b = a + 5  # Will throw an error

b = int(a) + 5
print(b)

# Conversion Methods

# str(35) => 35
# int("35") => 35
# float(35) => 35.0

# Advanced typeCasting 
# Syntax :- int(a, base)

bin = '110'
print(int(bin, 2)) # This statement treating '110' as binary number and converting it into decimal number

# Integer to Hexadecimal, Octal and Complex number

n = 10
print(hex(n))
print(oct(n))
print(complex(n))
print(complex(2, 3))