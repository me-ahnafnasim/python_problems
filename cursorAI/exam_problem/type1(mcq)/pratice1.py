#the think you need to remember that
"""
#work and its normal
i = 0
while i < 10:
    print(i)
    i += 1
"""


"""
# its not work and it abnormal 
i = 0
while i < range(10):
    print(i)
    i += 1
"""

"""
#its work perfectly
i = 0
while i in range(6):
    print(i)
    i = i+1
"""

# lear how to use break and continue
# break = programm will work till the condition 
# continue = program will skipp the exucation of the condition's 
# 
#  #

"""
# when we use break, print() function position after the while loop 
i = 0
while i < 10:
    print(i)
    i +=1
    if i==6:
        break
"""

"""
# the print() function is positioned at the end of the program
i = 0
while i < 10:
    i +=1
    if i==6:
        continue
    print(i)
"""
   
    

"""
#this program skip the even number only print the odd number
i = 0
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
"""


"""
#Falsy Values in Python
False (the boolean False)

None (represents "nothing" or "no value")

Zero (numeric types)

0 (integer)

0.0 (float)

0j (complex number)

Empty sequences/containers

"" (empty string)

[] (empty list)

() (empty tuple)

{} (empty dictionary)

set() (empty set)

#Truthy Values
Everything else is considered truthy (evaluates to True), including:

Non-zero numbers (1, -5, 3.14)

Non-empty strings ("hello", " " (space), "0")

Non-empty containers ([1, 2], {"key": "value"})




a = []
b = 0
c = ""
d = "False"
print(a)
print(b)
print(c)
print(d)

#Here in option d is a string which is not null that is why it is true, except this everything is false
"""

"""
x = 3
while x :
    print(x)
    x -=1
#same same
i = 5
while i>0:
    print(i)
    i -= 1
"""

