#find average of a list

"""a=[5, 10, 0]
total = 0
length_list = len(a)
for i in range(len(a)):
    total += a[i]
average = total / length_list
print(average)


alternative,
a= [2, 4, 1, 3, 5, 6,]
average = sum(a)/len(a)
print(average)
"""


"""#find the common element of two list and return the list of the common element

1st type:

def find_common(a,b):
    result = []
    for element in a:
        if element not in result and element in b:
            result.append(element)
    return result
    
    
a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

print(find_common(a,b))


#first convert the list into set and get the intersectin

#print(a.intersection(b))  # {2, 3}
#print(a & b)

common_in_list = list(set(a) & set(b))
print(common_in_list)



common = [x for x in a if x in b]
print(common)"""





#remove duplicate from a list 

a = [2, 3, 4, 5, 6, 7, 8, 3, 4, 5]
transform =set(a)
new_list =list(transform)
print(new_list) 



a = [1, 2, 2, 3, 4, 4, 5]  # example list
result = []
for i in range(len(a) - 1):  # notice the -1 to prevent index error
    if a[i] != a[i + 1]:
        result.append(a[i])
print(result)  # prints [2, 4]


