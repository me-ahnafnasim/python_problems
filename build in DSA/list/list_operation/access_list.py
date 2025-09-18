a = [2, 4, 7, 0, 1, -4]

#access the first element
print(a[0])

#access the last element
print(a[-1])


#Note: access through the loop
list = [4, 6, 0, 1, 3, 6, 8, 3, 72]

#solution in a line
b =[item for item in list if item > 3]
print("b-",b)

#solution in a raw way
new_list = []
for item in list:
    if item>5:
        new_list.append(item)

print(new_list)

