#In Python, a list is a built-in data structure that allows user to store multiple items in a single variable.
#  Lists are ordered, mutable (can be changed), and can contain elements of different data types
#  (e.g., integers, strings, other lists, etc.).
# Its very similar to javaScript Array
'''
FACTS:
1) indexing starting from zero;
2) it is similar of array in javascript;
3) contain elements of different data types, not like C-array;
4)
5) last element (n-1) or -1;
NOTE:
-1 refers to the last element.
-2 refers to the second-to-last element.
-3 refers to the third-to-last element, and so on.

6) count the number of elements in a list in Python, you can use the built-in len() function.
7) If you want to count how many times a specific element appears in a list, you can use the count() method.
8) In Python, the range() function can be used to generate a sequence of numbers. The loop would look
'''



#Example for 3

# A list of numbers
numbers = [1, 2, 3, 4, 5]

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A mixed list
mixed = [1, "hello", 3.14, True]

# An empty list
empty_list = []




#Example for 5
fruits = ["apple", "banana", "cherry", "date"]

# Counting the number of elements in the list
count = len(fruits)

print(count)  # Output: 4





#Example for 6
EXAMPLE:
fruits = ["apple", "banana", "cherry", "banana"]

# Counting occurrences of "banana"
banana_count = fruits.count("banana")

print(banana_count)  # Output: 2




#Example for 7
#1| NOTE: Syntax
#for i in range(n):
    # Do something

li=[1, "dhaka", 7, 4, 0, 45]
liLen= len(li)

#n=10
for i in range(liLen):
    #print i values which starts from zero
    print(i)
    #print elements inside the list
    print(li[i])


2| NOTE: Syntax
#Customizing the range:
#You can also customize the starting point, stopping point, and step size using range(start, stop, step):
# Range from 2 to 10 with a step of 2
for i in range(2, 11, 2):
    print(i)