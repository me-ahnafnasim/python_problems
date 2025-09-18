#-----------------------------------------------------------------Defination-----------------------------------------------------------------

'''
NOTE:
In Python, a dictionary is a built-in data structure that stores data in key-value pairs.
 It is defined using curly braces {} or the dict() function
'''

#-------------------------------------------------------------structure of dictionary--------------------------------------------------------
 
# Using curly braces
student = {
    "name": "Alice",
    "age": 22,
    "course": "Data Science"
}


 
# Using the dict() function

person = dict(name="John", age=30, city="New York")

print(student)
print(person)

#--------------------------------------------------------accessing the value and key-----------------------------------------------------
"""
student ={
  "name":"Nasim",
  "age": 22,
  "subject":"Data science"
}
make a dictionary by using dict constructor
student = dict(name:"nasim", age=30, location="kishoreganj")
1. access using square brackets ([])
print(student["name"])
print(student.get("name", "not found any name"))
"""
# 1. Access Using Square Brackets ([])
print(student["name"])   # Output: Alice
print(student["age"])    # Output: 22
print(student["course"]) # Output: Data Science
# ⚠️ Note: If the key does not exist, this method will raise a KeyError.


# 2. Access Using .get()Method(Safer Way)
print(student.get("name"))  # Output: Alice
print(student.get("age"))   # Output: 22
print(student.get("course"))# Output: Data Science

# ⚠️ Note: If key is not found, return a default value instead of an error
print(student.get("grade", "Not Available"))  # Output: Not Available



#-------------------------------------------------------------looping through dictionary---------------------------------------------------

person ={
    "name":"nasim",
    "age": 23,
    "location":"Messina, Italy"
}


print("NOTE: get the key value pairs through loop: ")
#NOTE: get the key value pairs through loop

for key in person:
    print(key, ":", person[key])

print()
print("note: get the key only through for loop: ")
#note: get the key only through for loop
for key in person:
    print("key:",key)

print()
print("NOTE: GET THE VALUE ONLY: ")
#NOTE: GET THE VALUE ONLY 

for value in person:
    print("value:",person[value])



#-----------------------------------------------------Python Dictionary Built-in Methods----------------------------------------------------
student ={
    "name":"nasim",
    "age": 23,
    "location":"Messina, Italy"
}

print()
print("copy the dictionary: ")
new_dict=student.copy()
print(new_dict)


print()
print("update the existing dictionary : ")
student.update({"age":35,"course":"information technology", "university":"unime"})
print(student)

print()
print("get the keys of the dictionary : ")
result=student.keys()
print(result)
#output: dict_keys(['name', 'age', 'location', 'course', 'university'])


print()
print("get the values of the dictionary : ")
val=student.values()
print(val)
#output: dict_values(['nasim', 35, 'Messina, Italy', 'information technology', 'unime'])


print()
print("get the items of the dictionary : ")
val=student.items()
print(val)
#output: dict_items([('name', 'nasim'), ('age', 35), ('location', 'Messina, Italy'), ('course', 'information technology'), ('university', 'unime')])


print()
print("remove an item from the dictionary : ")
poped=student.pop('location')
print(val)
#output: dict_items([('name', 'nasim'), ('age', 35), ('location', 'Messina, Italy'), ('course', 'information technology'), ('university', 'unime')])

# Using a default value if the key is missing
result = my_dict.pop('country', 'Not Found')
print(result)     # Output: Not Found


# Remove last inserted item
item = student.popitem()
print(item)      
print(my_dict)    


print()
print("clear the new_dict: ")
student.clear()
print("clear done",new_dict)

