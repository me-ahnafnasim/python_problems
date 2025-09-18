"""print("hello".upper())
name = input("Enter your name: ").strip()"""
"""print(name)
 upper()
lower()
capitalize()
title()


islower()
isupper()
"""

"""print("md nasim".endswith("n"))
print("md nasim".find("n"))
"""



"""text = "this is my beautiful village"
new_text = text.split()
new_text[-1] = "country"
modify_text = " ".join(new_text)
print(modify_text)"""



"""sample1 = 'The lyrics is not that poor!'
sample = sample1.split()

for word in sample:
    if word.find("not") and word.find("poor"):

"""


#Convert String to List & Back

s ="bangla"
lst = list(s)
st ="".join(lst)
print(lst, st)



myStr = "the quick browns fox jumps over the lazy dog."
newStr = myStr.split()
lw = max(newStr, key =len)
print(lw)

max_len = 0
min_len = 0
for word in newStr:
    if max_len is None or len(word) > max_len:
        max_len = word
        
    if min_len is None or len(word) < min_len:
        min_len = word

print(max_len, min_len)




str1 ="bangla"
str2 ="dhakabangladesh"
result =[]
for char in str1:
    if char in str2:
        result.append(char)
print("".join(result))



s ="bangladeshhgl"
result =[]
for char in s:
    if char not in result:
        result.append(char)
print("".join(result))




s ="programming"
unique_element = list(dict.fromkeys(s))
print("".join(unique_element))



def remDuplicate(str3):
    result ={}
    for char in str3:
        print(char)
        result[char] = 0
    return "".join(result)
print(remDuplicate("nasimmmm"))




myStr ="red 12 black 45 green"
new_str = myStr.split()
result = []
for item in new_str:
    if item.isnumeric():
        result.append(item)
print(result)





name ="Nasim 12"
n =name.split()
for char in n:
    if char.isnumeric():
        print("yes")
    else:
        print("no")



#pangram --- containing every letter of the english alphabet
#pangram ---containing every letter of the english alphaber
#pangram --- containing every letter of the english ap


def is_pangram(str1):
    inputStr = str1.replace(" ","").lower().strip()
    pangram ="qwertyuiopasdfghjklzxcvbnm"
    for char in pangram:
        if char not in inputStr:
            return False
    return True
print(is_pangram("the quick brown fox jumps over the lazy dog"))





lst =[1,3, 7, 4,6, 8]
if len(lst)% 2 !=0:
    print(lst[len(lst)//2])
if len(lst)% 2 ==0:
    avg = lst[len(lst)//2]+lst[len(lst)//2-1]
    print(avg/2)   