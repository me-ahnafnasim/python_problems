"""#-------------------------------------------------#list Constructor-----------------------------------------------------------------
empty_list = list()
print(empty_list)  # Output: []

#2. From a String
chars = list("hello")
print(chars)  # Output: ['h', 'e', 'l', 'l', 'o']

# from a tuple
tup = (1, 2, 3)
lst = list(tup)
print(lst)  # Output: [1, 2, 3]

#from a set
s = {3, 1, 2}
lst = list(s)
print(lst)  # Output: [1, 2, 3] (order may vary since sets are unordered)


d = {'a': 1, 'b': 2}
lst = list(d)
print(lst)  # Output: ['a', 'b'] (only keys are added to the list)
#Note:
print(list(d.values()))   # Output: [1, 2]
print(list(d.items()))    # Output: [('a', 1), ('b', 2)]
"""
"""
x = 1234
listx = list(x)
#output: TypeError: 'int' object is not iterable
"""





"""
What Does It Mean That a List Is Mutable in Python?
In Python, "mutable" means that the contents of an object can be changed after it's created.

Since lists are mutable , you can:

Add, remove, or change elements
Modify elements in place
Sort, reverse, or otherwise alter the list without creating a new object

example:
# Original list
numbers = [1, 2, 3]
print("Original:", numbers)  # [1, 2, 3]

# Change an element
numbers[0] = 10
print("After change:", numbers)  # [10, 2, 3]

# Add an element
numbers.append(4)
print("After append:", numbers)  # [10, 2, 3, 4]

# Remove an element
numbers.remove(2)
print("After remove:", numbers)  # [10, 3, 4]
"""

"""
my_set = [1,4,6,7]
my_set[2]=3
print("modified",my_set) #output modified [1, 4, 3, 7]



#append only add a single element in the end of the list
lst = [1, 2]
lst.append(3)
print(lst) 

#
lst = [1, 2]
lst.extend([3, 4, 1])
print(lst)  # [1, 2, 3, 4]
"""


"""s = {1, 2, 3, 8,0}
s2 = s.copy()
s2.add(9)

print(s2)
print(s)

s4 ={2,9, 0, 3}
print(s4)"""




  
from traceback import print_tb


lst1 =[2,5,7,4]
lst4 =[2,5,7,4]
lst2 =[0,4,8,1,3]
lst3=lst2
"""
if(lst1 == lst4):
    print(True)
else:
    print(False)"""


"""d = {'a': 1, 'b': 2}
print(list(d.values()))  
# dict_values([1, 2])"""


""" """

"""
count = 0
while count <=5:
    count +=2
    print("2nd",count)


count = 0
while count <=5:
    print(count)
    count +=2"""



"""
count = 0
while count <=5:
    print("1st",count)
    count = count+1

count = 0
while count <=5:
    count = count+1
    print(count)
#in the pre incriment initial value start 1 to end value greater that of 5 """


#reverse loop

"""i =5
while i>0:
    print(i)
    i-=1"""

"""count = -5
while count <0:
    count +=1
    print(count)
"""
"""
numbers = [1, 3, 5, 2]
print(len(numbers))
index = 0
while index < len(numbers):
    if numbers[index] == 2:
        print("Found!")
        break
    index += 1
else:  # Triggered if 2 not found
    print("Not found!")  # Output: "Not found!"""




x=0
while x==3:
    x += 1
else:
    print("done")



"""
count = 0
while count <=5:
    count = count + 1
    print("post increment", count)"""



"""my_dict ={"a":1, "b":2}
send_dict ={"e":5}
my_dict["c"]=3
my_dict["a"]=0
print(my_dict)

my_dict.update(send_dict)
print(my_dict)
"""





"""kes = ["name", "age", "roll"]

new_dict = dict.fromkeys(kes)
print(new_dict)"""


my_dict = {'a': 1, 'b': 2, 'c': 3}
remove_item = my_dict.popitem()
print(remove_item)
print(my_dict)
print(my_dict.values())
#output dict_keys(["a", "b", "c"])
#dict_values[1, 2, 3]