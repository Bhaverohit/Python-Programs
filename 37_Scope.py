# There are two scopes :- Global And Local

a = 1  # Global Variable
b = 2  # Global Variable


def AddMe():
    # a = 10  # Local Variable
    b = 5  # Local Variable

    # Can access global variable but can't overwrite it
    # To overwrite global variable from local scope we use global keyword
    # global keyword will access only global variable, in case there is no global variable then nothing happens. it won't change the local variable

    # a = a + 10 # throws an error
    global a  # Can't initialize it, only declare first
    a = a + 100
    print("Inside Add Me : ", a+b)


AddMe()
print(a)  # Can't Access Local Variable
