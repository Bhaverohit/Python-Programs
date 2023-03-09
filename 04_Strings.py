a = ''' STRING '''
b = ' Also A String '
c = " Also A String "

print(a)
print(b)
print(c)

# String Concatenate

n1 = "Rohit"
n2 = "Bhave"

print(n1 + " " + n2)


# String Slicing
# Syntax => [firstValue : secondValue : thirdValue]
# Where firstValue, secondValue and thirdValues are opitional

# Index starts from zero (Left to Right) and -1 (Right to Left)
# firstValue index represents the starting of sliced string
# secondValue index represents the ending of sliced string but it's excluded
# thirdValue is the value which represents number of characters you want to skip in sequence in sliced string
# If you try to access elements more than available indexes then there's an error
# In skip section of slicing you can put any number there won't ne an error
# Strings are immutable
# Never take less than -1 in skip section of strings

sample = "I Like Ice Cream"
print(sample[5])

print(sample[2:5])  # at 2->L, 3->i, 4->k and 5->excluded

print(sample[11::2])  # It'll skip every second character from "Cream"

print(sample[:10])  # It'll print the string from minimum index to 10

print(sample[6:])  # It'll print the string from 6th index to maximum index

print(sample[:])  # It'll print whole string

# It'll print whole string because by default skip section is considered to be 1
print(sample[::])

print(sample[-1])  # Will return right most letter of string

print(sample[-1: -5])

print(sample[::-1])  # It'll return string in reverse order


# String Methods

story = "once upon a time there was a king and an queen, they married and lived nicely"

print(len(story))
print(story.count("a"))
print(story.endswith("nicely"))
# Capitalizes first letter of string and takes no argument
print(story.capitalize())
# Returns the index of first occurance of passed argument and -1 if not found
print(story.find("king"))
# It replace all the occurance and actual string is not changed (To change actual string you need to initialize the string)
print(story.replace("a", "AND"))
print(story.isalnum())  # Alpha Numeric String :- String without spaces

# Other Methods and many more
"""
story.upper()
story.rstrip()
story.split()
story.casefold()
story.center(4)
story.encode()
story.expandtabs()
story.format()
story.format_map(4)
story.index()
story.isascii()
story.isalpha()
story.isdigit()
story.isalnum()
story.isdecimal()
story.isidentifier()
story.islower()
story.isprintable()
story.isnumeric()
story.zfill()
story.strip()
story.title()
story.isspace()
story.istitle()
story.lower()
story.isupper()
story.lstrip()
story.join()
story.maketrans()
story.startswith()
story.strip()
story.partition()
story.isalpha()
story.removesuffix()
story.removeprefix()
"""
