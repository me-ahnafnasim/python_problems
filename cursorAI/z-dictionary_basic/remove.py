#The remove() method removes the first occurrence of a specified value from a list.

# remove(value) value ta, list er jei element er sathe
#match korbe oi ta kei delet kore dibe
#same element more than two ta hole wo, ekdom first ta delet kore dibe

myList = [10, 30, 10, 40, 60]
myList.remove(10) #first 10 will be remove
print(myList)

mySet = {10, 30, 10, 40, 60}
mySet.remove(30) #first 30 will be remove
print(mySet)