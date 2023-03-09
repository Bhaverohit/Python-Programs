class Name:
    # It's name must be __init__
    def __init__(self, name, salary, address):
        self.name = name
        self.salary = salary
        self.address = address
        print("Constructor runs automatically as soon as Object is created")

    def getData(self):
        print(f"The name of Employee {self.name}")
        print(f"The salary of Employee {self.salary}")
        print(f"The address of Employee {self.address}")


Rohit = Name("Rohit", 1000, "GGC")
Rohit.getData()
