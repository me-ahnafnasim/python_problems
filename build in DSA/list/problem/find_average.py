xlist =[2,4, 5,0,2,8,9,1]
avg_list =[]
total =0
count =0
for i in range(len(xlist)):
    total +=xlist[i]
    count +=1
avg_list.append(total/count)
print(avg_list)




