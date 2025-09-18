d1 =['a', 'b', 'c', 'd', 'e', 'f']
d2 =[1, 2, 3, 4, 5]

merged ={}
min_len = min(len(d1), len(d2))
print(min_len)

for i in range(min_len):
    merged[d1[i]] = d2[i]
print(merged)