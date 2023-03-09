# Whenever there's a text longer than a single line in print statement then you need to write that string in triple quotes

''' Will throw error

print("Jonny 
Deep ")

'''

print('''Jonny
Deep''')


print("The value of 4 + 5 is : ", 4 + 5)

# You can print multiple things
print(5, "Rohit")

# Using comma for multiple strings to print
print("Hello", "World")  # There will be a space between both strings by default

# end function :- It is used to tell how will the print statement will end (You can put anything inside end function)
print("Rohit", end=" ")
print("Bhave")

# We can use arithematic * operator for printing same thing multiple times in a print statement
var = "Variable \n"
print(var * 10)
