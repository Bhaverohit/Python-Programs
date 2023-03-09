file = open("First.txt", 'r')

file.read()  # To read file's content
file.tell()  # To print current file reading pointer location
file.detach()
file.fileno()
file.flush()
file.readable()
file.seek('enter_index')  # reset pointer to 0 or to 'enter_index'
file.isatty()
file.reconfigure()
file.seekable()
file.truncate()
file.write()
file.writable()
file.writelines()
