"""
"Ordered" means that the elements in a data structure have a defined sequence or position , and this order:

Is maintained (preserved) when you create or iterate over the structure.
Allows you to access elements by their position (like index).
Means that two collections with the same elements in different order are considered different (if order matters).
"""
list1 = [1, 2, 3]
list2 = [3, 2, 1]

print(list1 == list2)  # False — because order matters!

#order matters in the tuple
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(t1 == t2)  # True — order matters!

t1 = (1, 2, 3)
t2 = (1, 3, 2)
print(t1 == t2)  # False — order matters!


# order in dictionary
dict1 = {'a': 1, 'b': 2}
dict2 = { 'a': 1,'b': 2}
print("dictionary:",dict1 == dict2)  # True in Python 3.7+ only if order matches? Wait...

#Even though order is preserved, two dicts are equal if they have the same key-value pairs , regardless of insertion order
dict1 = {'a': 1, 'b': 2}
dict2 = { 'b': 2,'a': 1}

print("dictionary:",dict1 == dict2)  # True in Python 3.7+ only if order matches? Wait...


# set is unordered
dict1 = {1,4,7,6}
dict2 = {1,4,7,8}
print("set:",dict1 == dict2) 