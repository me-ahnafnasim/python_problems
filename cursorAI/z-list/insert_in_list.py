myList = [1,4,6,9,7,3]
myList.append(0)


myList.insert(1, 70)

myLi = [100, 200, 300]
myList.extend(myLi)
print(myList)




my_list = [1, 2]

# append adds the whole object as a single element
my_list.append([3, 4])
print(my_list)  # [1, 2, [3, 4]]

# reset
my_list = [1, 2]

# extend adds each element from the iterable
my_list.extend([3, 4])
print(my_list)  # [1, 2, 3, 4]


