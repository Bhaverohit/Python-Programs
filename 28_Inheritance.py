# Types of Inheritance Allowed
# 1. Single
# 2. Multiple
# 3. Multi-level

# Parent Base or SuperClass
class Employee:

    def getData(self):
        print("Good Morning!")

# Child Drived or SubClass


class Child(Employee):

    language = "Python And C++"


e = Employee()
e.getData()

c = Child()
c.getData()
