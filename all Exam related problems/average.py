
def ds_ave(xlist):
    average = []
    for sublist in xlist:
        total = 0
        count = 0
        for item in sublist:
            print("hi:",item)
            total = total + item
            count = count +1
        avg =total/count
        average.append(avg)
    return average





"""def ds_ave(xlist):
    averages = []
    for sublist in xlist:
        total = 0
        count = 0
        for item in sublist:
            total += item
            count += 1
        avg = total / count
        averages.append(avg)
    return averages


xlist = [[1, 7, 12], [4, 2, 10, 14], [15, 3, 2, 11, 20]]
print(ds_ave(xlist))  
"""




def ds_ave(xlist):
    averages = []
    for sublist in xlist:
        avg = sum(sublist) / len(sublist)
        averages.append(avg)  # this line must be inside the loop
    return averages  # also remember to return the result


xlist = [[1, 7, 12], [4, 2, 10, 14], [15, 3, 2, 11, 20]]
print(ds_ave(xlist))  # Output: [6.666..., 7.5, 10.2]
