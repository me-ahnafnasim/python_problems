"""xlist =[2,6,3,0,-4,1,7,3,-10]
print(min(xlist))


smallest = 0
for item in xlist:
    if item<smallest:
        smallest = item

print(smallest)"""

xlist =[2,6,3,0,-4,1,7,3,-10]
print(max(xlist))


largest = xlist[0]
for item in xlist:
    if item>largest:
        largest = item

print(largest)
