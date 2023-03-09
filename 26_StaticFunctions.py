class Employee:
    company = "Google"

# Will Throw an error
    # def greet():
    #     print("Hello Sir")

# # Will Run
#     def greet(self):
#         print("Hello Sir")

# Will Run
    @staticmethod
    def greet():
        print("Hello Sir")

# Will Not Run
    # @staticmethod
    # def greet(self):
    #     print("Hello Sir")


rohit = Employee()
rohit.greet()
