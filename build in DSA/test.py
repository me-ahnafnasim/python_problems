"""dll = {
    'head': {'prev': None, 'next': 10},
    10: {'prev': 'head', 'next': 'tail'},
    'tail': {'prev': 10, 'next': None}
}
current = dll["head"]["next"]
current = dll[current]['next']
print(current)"""

#get the key of the dictionary

from os import name


person = {
    "Name":"Nasim",
    "Age":25,
    "Course":"Data Science",
}
"""
Note: get the key only
for key in person:
    print(key)
"""



"""
Note: get the value only
for value in person.values():
    print(value)
"""



"""
Note: get the kry, value pairs togather
for key, value in person.items():
 print(key, value)
"""



"""
Note: get the kry, value and index alltogather

for index, (key, value) in enumerate(person.items()):
    print(index, key, value)
"""



"""
Note: modify a dictionary through loop
--->for value in list(my_dict.values()):  # Loop over a copy of keys
--->my_dict.keys() gives us only the keys (e.g., "a", "b", "c", etc.).
--->my_dict[key] looks up the value for that key.
--->The condition if my_dict[key] % 2 == 0: checks if the value is even.

my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
    if my_dict[value] % 2 == 0:  # Check if the value is even
        del my_dict[value]  # Delete the key-value pair
print(my_dict)  # Final dictionary after deletion
"""






my_tuples = ("nasim", "wasim", "titu", "nayem")
#convert truples to list
my_list = list(my_tuples)
my_list.append("nayma")
print(my_list)
new_tuples = tuple(my_list)
print(new_tuples)


#tuples unpaking
choto, middle1, middle2, boro = my_tuples

"""
print(choto)
print(middle1)
print(middle2)
print(boro)"""
