# There are two types of files
# 1. Text Files (.txt, .py, .c etc) => Combination of characters
# 2. Binary Files (.jpg, .dat etc) => Not readable by humans (can't be opened in notepad)


# Opening file syntax : open('Filename.txt' , 'Mode')
# By default mode is r (read)

# Modes:
# 1. r = open for read
# 2. w = open for write
# 3. a = open for appending
# 4. + = open for updating (read & write both)
# 5. x = creates a file if it doesn't exit
# 6. rb = open for read in binary mode
# 7. rt = open for read in text mode ('t' of rt by default adds up but not 'b' of rb)

# Reading file syntax : read()
# The function can be given parameter to read limited number of characters
# The read function by default reads whole file
# A file can only be read once (can't use more than one read() fn)
# # Closing a file is necessary


# Read data from a file "First.txt" and print it
f = open('First.txt', 'r')
# data = f.read() # Reads whole file
# print(data)
dataTwo = f.read(5)  # Reads only first 5 characters
print(dataTwo)
f.close()
print("------------------------")


# Other Reading functions performed on a file "Second.txt" and print it
f = open('Second.txt', 'r')
data = f.readline()  # Reads only one line from the file
print(data)

data = f.readline()  # Reads second line of the file
print(data)

# Returns a list made of each unread yet lines present in the file as elements
data2 = f.readlines()
print("-----------------------------")
print(data2)
f.close()
