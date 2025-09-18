"""
max():--max with (string, list, tuple, etc.)
      What it does: Returns the largest item in an iterable
        (string, list, tuple, etc.) or the largest of two+ arguments.

      Default behavior for strings: Uses lexicographical 
      order (like dictionary order, based on Unicode values)

example:
     print(max([2, 8, 5]))      # 8
     print(max("python"))       # 'y' (because 'y' > all other chars in Unicode)
 
     
👉 You can also use a key function:
words = ["cat", "elephant", "dog"]
print(max(words, key=len))   # 'elephant' (longest word)

"""




"""
max()--wirh dictionary

1) When max() is applied directly to a dictionary, it compares the keys 
(not the values) and returns the largest key based on lexicographical 
(alphabetical) order(if string).

d = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(max(d)) #Charlie


2) return the largest value
d = {"a": 10, "b": 25, "c": 5}
print(max(d.values()))   # 25


3)return the key whose value is max
d = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(max(d, key=d.get))   # 'Bob' (because 92 is max value)


4) return the key,value whose value is max
d = {"Alice": 85, "Bob": 92, "Charlie": 78}
print(max(d.items(), key=lambda x: x[1]))   # ('Bob', 92)


"""





"""
min() --with list, tuople, string

What it does: Opposite of max(). Returns the smallest item.

example:
print(min([2, 8, 5]))    # 2
print(min("python"))     # 'h'

👉 With key:
words = ["cat", "elephant", "dog"]
print(min(words, key=len))   # 'cat' (shortest word)

"""



"""
1. What is sorted()?

It takes an iterable (list, tuple, string, dict, etc.).
Returns a new sorted list (original data is unchanged).

example:
nums = [4, 1, 7, 3]
print(sorted(nums))    # [1, 3, 4, 7]
print(nums)            # [4, 1, 7, 3] (unchanged)


2. Works on Different Iterables
print(sorted("python"))     # ['h', 'n', 'o', 'p', 't', 'y']
print(sorted((9, 2, 5)))    # [2, 5, 9]
print(sorted({3, 1, 4}))    # [1, 3, 4]


3. Important Parameters
(a) reverse
-----Default is False.
-----If True, sorts in descending order.

nums = [4, 1, 7, 3]
print(sorted(nums, reverse=True))   # [7, 4, 3, 1]
(b) key
----Allows custom sorting logic.
----key takes a function that is applied to each element before comparison.
"""




#this sorted() function sort the dictionary based on key(asc->desc)
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict =dict(sorted(my_dict.items(), key = lambda item:item[1]))
#item = item[1], means each set er second value
print(sorted_dict)


#this sorted() function sort the dictionary based on key(desc->asc)
my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
sorted_dict =dict(sorted(my_dict.items(), key = lambda item:item[1], reverse=True))
print(sorted_dict)





#Get the second (key, value) pair from a dictionary.
second_pair = list(my_dict.items())[1]  # index 1 = second item
print(second_pair)

# Get only the second key
second_key = list(my_dict.keys())[1]
print(second_key)  # 'banana'

# Get only the second value
second_value = list(my_dict.values())[1]
print(second_value)  # 1







vowels ="aeiou"
str1 ="nasim"
result=""
for char in str1:
    if char in vowels:
        result +=char
print(result, len(result))



def non_repeating(str2):
    result ={}
    for char in str2:
        result[char] = result.get(char, 0)+1
    for char in str2:
        if result[char] ==1:
            return char
    return None
print(non_repeating("abcda"))



s="naassiimm"


def remDuplicate(str3):
    result ={}
    for char in str3:
        result[char] = 0
    return "".join(result)
print(remDuplicate("naassmm"))
    