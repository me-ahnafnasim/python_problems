xlist =[2,6,3,-4,1,7,3,-10]
even_list =[]
total=0
for item in xlist:
    if item%2==0:
        even_list.append(item)
print(even_list)

for element in even_list:
    total += element
print(total)


 
        
