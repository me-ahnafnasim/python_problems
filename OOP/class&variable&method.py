class Person:
    def __init__(self, person_name, date_of_birth, ht):
        self.name = person_name
        self.date_of_birth = date_of_birth
        self.height = ht

    def get_name(self):
        return self.name

    def get_summary(self):
        return f"Name: {self.name}, DOB: {self.date_of_birth}, Height: {self.height}"

# Example usage
a_person = Person("Zulkamine", "1990", "6 feet")
print(a_person.get_summary())




#1. What is an f-string?
#An f-string (formatted string literal) is a way to embed(establish) expressions or variables
#  inside a string. It allows you to dynamically insert values into a string without needing
# concatenation or additional formatting functions.
# formate: f"write string inside the quat"



#Class : Person
#--An object is an instance of a class. When you create an object, you are creating a specific
#  entity based on the blueprint defined by the class.

#Object : a_person
#Variables : self.name, self.date_of_birth, self.height
#Methods : __init__, get_name, get_summary

#Method ar variable class er under e thake, method ekta function er moto kaj kore