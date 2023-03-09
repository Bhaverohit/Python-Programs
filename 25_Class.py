class Number:
    def sum(self):
        return (self.a + self.b)


# object instantiation
num = Number()
num.a = 10
num.b = 20

add = num.sum()
print(add)


class RailwayDetails:
    formType = "Railway Form"

    def printData(self):
        print("Name is " + self.name)
        print("Railname is " + self.rail)


rohitApplicationForm = RailwayDetails()
rohitApplicationForm.name = "Rohit Kumar Bhave"
rohitApplicationForm.rail = "Rajdhani Express"

rohitApplicationForm.printData()
print(rohitApplicationForm.formType)

# Overwriting formType for an object
rohitApplicationForm.formType = "New Form Type"
print(rohitApplicationForm.formType)


MohitForm = RailwayDetails()
print(MohitForm.formType)

print("-----------------------")

# Overwriting formType for whole class
RailwayDetails.formType = "Something Form"
# Because instance attributes are present that's why they'll be printed for rohitApplicationForm.formType
print(rohitApplicationForm.formType)
print(MohitForm.formType)
