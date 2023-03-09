# Syntax -> def AbcFunction(normalParameter, thenArgs, thenKwargs)
# if parameters are swapped then error though args and kwargs are opitional
# These are used in case you don't know how many parameters will be passed in the function


def funargs(normal, *args, **kwargs):
    print(normal)

    for item in args:
        print(item)

    for key, value in kwargs.items():
        print(f"{key} is the {value}")


tup = ["Rohit", "Rohan", "Sohan", "Mohan"]
normal = "This is a normal variable"

dict = {"Rohit": "Manager", "Raman": "Cook", "Someone": "Something"}

funargs(normal, *tup, **dict)
