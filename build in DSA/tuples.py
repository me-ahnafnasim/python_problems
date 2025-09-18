#NOTE: Tuple items are ordered(the position of elements is fixed), unchangeable, and allow duplicate values.
#Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

learnTuple=("water", "suger", "oil", "rice")
#NOTE: 0=First elements and 3 is the last elements. Moreover, you can get the access through negative valu
#like, -1 means last elements from the last.

#print(learnTuple[-2])

#NOTE: looping through tuple
for x in learnTuple:
    print(x)

for i in range(len(learnTuple)):
    print(i,learnTuple[i])

#NOTE: WHILE LOOP
    thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i=i+1

#NOTE: join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#NOTE: Method in tuple
# count() --Returns the number of times a specified value occurs in a tuple
# index() --Searches the tuple for a specified value and returns the position of where it was found

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

#return the nearest number index
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)


my_tuples = ("nasim", "wasim", "titu", "nayem")
#convert truples to list
my_list = list(my_tuples)
#normally truples is unchangeable means you can not add a new element and even you cant delet one
#you can operate add and remove by translating truples to list
my_list.append("nayma")
print(my_list)
#convert tuples to list
new_tuples = tuple(my_list)
print(new_tuples)