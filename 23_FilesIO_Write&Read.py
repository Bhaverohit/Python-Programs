# The 'w' mode overwrites the previous text
# No matter how many times you run a single write() fn, the file's data will be overwritten
# If file doesn't exit then it'll be created

f = open('FirstWrite.txt', 'w')
f.write("This is the first time writing... ")  # This will write first line
f.close()


print("-----------------------------")

# The 'a' mode for appending without losing previous data
# Everytime you run a write() fn, content will be written
# If file doesn't exit then it'll be created

f = open('SecondWrite.txt', 'a')
f.write("This is the first time writing... ")  # This will write first line
# This will append text to the first line
f.write("I'm overriting this time...")
f.close()
