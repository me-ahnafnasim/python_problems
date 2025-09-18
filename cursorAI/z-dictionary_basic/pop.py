#note: "Take out any one item from the(set, dict, list), remove it, and give it back to us." 

myList = [1,4,6,9,0,12]
print(myList.pop(1))
print(myList)
#in the list pop() take the index and remove this number and 
#return the number as well as
#by default pop() remove and return the last element of a list


#pop() with dictionary
myDict ={"a":"nasim", "b":"wasim", "c":"titu"}
print(myDict.pop("a"))
print(myDict)
#in the dictionary pop() delete the key-value pair
#based on key and return the value

#pop() also work with set and in set it removes item randomly and return it
my_set = {10, 20, 30, 40}
removed_element = my_set.pop()
print(removed_element)  # e.g., 10 (or any element — arbitrary)
print(my_set)           # e.g., {20, 30, 40}



