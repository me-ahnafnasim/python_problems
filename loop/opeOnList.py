#find the sum of all number of a list through loop
myList = [2, 5, 7, 4, 8, 3, 9, 11, 12, 24]
total_sum=0

for number in myList:
    total_sum=total_sum+number
print("totalSum by loop=",total_sum)



#find the sum of all number of a list through building function
total=sum(myList)
print("totalSum by build in function =",total)

#find the sum of all even numbers in a list
total=0
for number in myList:
    if number%2==0:
        total+=number
print("sum of all even",total)



#find the sum of all odd number
odd_sum=0
for number in myList:
    if number%2 != 0:
        odd_sum=odd_sum+number
print("sum of all odd num =",odd_sum)


#iterating by length and reverse the array
length = len(myList)  # Calculate list length

# Reverse the list using a loop
for i in range(length // 2):
    # Swap elements
    myList[i], myList[length - i - 1] = myList[length - i - 1], myList[i]
# Print reversed list
print("Reversed list:", myList)


#push elements that obey a condition
even_list = []
for number in myList:
    if number%2 == 0:
        even_list.append(number)
    #print(number)
print("number of elements that are even",even_list)






def insert_ele(pos, ele, myList):
    if not (0 <= pos <= len(myList)):
        print("pos is invalid")
    else:
        myList.insert(pos, ele)  # Insert element at position
        print(myList)
insert_ele(0, 7, [1, 3, 5])
