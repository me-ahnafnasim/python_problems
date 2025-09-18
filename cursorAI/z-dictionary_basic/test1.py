

"""
for i in range(1, 20, 3):
    print(i)
"""
"""
x = "50"
print(type(x))
x = 50.50
y = int(x)
print(y)
print(type(y))
x = 50
print(type(x))

value = 3.14159
rounded = round(value, 2)
print(rounded)

print(round(3.5))


print(isinstance([2,4], tuple))
print(isinstance(34, int))

print(round(2.5069, 3))
"""



#sort a dictionary ascending based on the value
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
new_dict = dict(sorted(d.items(), key = lambda item:item[1], reverse = False))
print(new_dict)































































