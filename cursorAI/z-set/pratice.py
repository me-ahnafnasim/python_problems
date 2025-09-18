"""
#empty set 
set3 = set()
#empty dictionary
myDict ={}
"""



set1={1,3,4,6,2,3}
set2={4,6,2,7,2,3, 9}
newSet =set1.intersection(set2)
if len(newSet)>=1:
    print("true")
print(newSet)


print(set2>=set1)


print(set1-set2)
print(set1.difference(set2))




#union(common uncommon sob niye ase)
print(set1|set2)
print(set2.union(set1))
#intersection(common gula asbe just)
print(set1 & set2)
print(set1.intersection(set2))



