xlist = [[1, 7, 12], [4, 2, 10, 14], [15, 3, 2, 11, 20]]

"""average = []
for list in xlist:
    total = sum(list)/len(list)
    average.append(total)
    print(total)
print(average)"""

"""average = []

for sub_list in xlist:
    total = 0
    count = 0
    for element in sub_list:
        count +=1
        print(count)
        total +=element

    aveg = total/count
    average.append(aveg)
print(average)"""
    







list = [[1, 7, 12], [4, 2, 10, 14], [15, 3, 2, 11, 20]]

average =[]
for sub_list in list:
    count = 0
    total = 0
    for element in sub_list:
        count +=1
        total+= element
    ebar = total/count
    average.append(ebar)
print(average)