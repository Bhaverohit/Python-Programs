# It is a composite data type
# It is a collection of objects in Key-Value pair
# Left side is Key and Right side is value corresponding to the Key
# All the keys must be unique otherwise value gonna overwritten
# Dictonaries are Mutable
# Dictonaries are indexed
# Dictonaries are unodered
# Dictonaries are dynamic
# Dictonaries can be nested
# Keys are written in small letters only generally
# Dictonary keys can be typeCast into a list
# If you try to access not present value via key using [] then you'll get an error but is you're doing same thing using get() function then it'll return None which is great as errors are bad

myDict = {
    "Name": "Rohit",
    "Age": 20,
    "Hobbies": ["Cricket", "Games"],
    "DictInsideDict": {"Surname": "Bhave", "ContactNo": 123456},
    52: 10
}

# To access whole dict
print(myDict)

# To access individual dict elements
print(myDict['Name'])
print(myDict['Hobbies'])
print(myDict['DictInsideDict'])

# To access dict inside dict value
print(myDict['DictInsideDict']['Surname'])

# OverWriting
myDict["Age"] = [21]
print(myDict["Age"])

# A list of 2 object tuples can also be used to define a dictonary using fict function
d = dict([("Apple", "Red"), ("Guava", "Green")])
print("Type of d : ", type(d))
print(d)

# To add new data
d["chocolate"] = "Brown"
print(d)

# Deleting key-value pair
del d["chocolate"]
print(d)

# Dictonary Functions

# myDict.clear()
# myDict.copy()
# myDict.fromkeys()
# myDict.get()
# myDict.items()
# myDict.keys()
# myDict.pop()
# myDict.popitem()
# myDict.update()
# myDict.values()
