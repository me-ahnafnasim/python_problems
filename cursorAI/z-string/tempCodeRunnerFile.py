lst =[1,3, 7, 4,6, 8]
if len(lst)% 2 !=0:
    print(lst[len(lst)//2])
if len(lst)% 2 ==0:
    avg = lst[len(lst)//2]+lst[len(lst)//2-1]
    print(avg/2) 