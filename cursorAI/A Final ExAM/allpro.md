
## 1. Group Words by First Letter

```python
def group_words(words):
    grouped = {}
    for word in words:
        first_letter = word[0].lower()  # convert to lowercase for consistent keys
        if first_letter not in grouped:
            grouped[first_letter] = []
        grouped[first_letter].append(word)
    return grouped

words = ["apple", "banana", "cherry", "date", "elderberry"]
print(group_words(words))
```

## 2. Merge Two Dictionaries of Lists

```python
def merged_dict(d1, d2):
    merged = {}
    for key in d1:
        # Copy the list to avoid modifying original d1
        merged[key] = d1[key].copy()
    
    for key in d2:
        if key in merged:
            merged[key].extend(d2[key])  # Append values for matching keys
        else:
            merged[key] = d2[key].copy()
    return merged

dict1 = {'a': [1, 2], 'b': [3, 4]}
dict2 = {'a': [5, 6], 'c': [7, 8]}

result = merged_dict(dict1, dict2)
print(result)
```

## 3. Count Uppercase and Lowercase Characters in a String

```python
def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return (upper, lower)

s = "Hello"
called = count_case(s)
print(called)
```

## 4. Find Common Elements of Two Lists Without Duplicates, Preserving Order

```python
def common_elements(a, b):
    result = []
    for item in a:
        # Append if item is in b and not already in result
        if item not in result and item in b:
            result.append(item)
    return result
```

## 5. Check for Strictly Increasing or Decreasing Consecutive Triplets

```python
def has_consecutive_triplet(lst):
    if len(lst)  b > c):
            return True
    return False

lst = [1, 2, 3, 6, 7, 8]
print(has_consecutive_triplet(lst))
```

*Note:* `range(len(lst) - 2)` ensures no index out of range error when accessing `lst[i+2]`.

## 6. Sum Values of Dictionary Lists

```python
def sum_dict_values(d):
    result = {}
    for key in d:
        result[key] = sum(d[key])
    return result

d = {
    "a": [2, 4, 4],
    "b": [3, 2],
    "c": [2]
}
call = sum_dict_values(d)
print(call)
```

## 7. Recursively Flatten a Nested List

```python
def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

print(flatten([1, [2, [3, [4]], 5]]))
# Output: [1, 2, 3, 4, 5]
```

## 8. Count Vowels in a String

```python
def count_vowels(s):
    s_conv = s.lower()
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    for char in s_conv:
        if char in vowels:
            vowel_count += 1
    return vowel_count

print(count_vowels("Hello World"))
```

## 9. Calculate Factorial of a Non-negative Integer

```python
def factorial(n):
    # The factorial of 0 and 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
```

## 10. Convert List of Tuples to Dictionary

```python
def tuples_to_dict(tuples):
    result = {}
    for key, value in tuples:
        result[key] = value
    return result

tuple_list = [("name", "Alice"), ("age", 25), ("job", "Engineer")]
dictionary = tuples_to_dict(tuple_list)
print(dictionary)
```

## 11. Alternate Case Letters in a String Starting with Uppercase

```python
def alternate_case(s):
    result = []
    for i, c in enumerate(s):
        if i % 2 == 0:
            result.append(c.upper())
        else:
            result.append(c.lower())
    return ''.join(result)

print(alternate_case("hello world"))
```

## 12. Calculate Averages of Sublists in a Nested List

```python
a = [[2, 3, 4], [2, 7, 9, 3], [2, 8]]

newl = []
for xlist in a:
    suma = sum(xlist)
    length = len(xlist)
    newl.append(suma / length)
print(newl)
```

### Alternative approach (with corrections):

```python
def ds_ave(xlist):
    average = []
    for sublist in xlist:
        total = 0
        count = 0
        for item in sublist:
            total += item
            count += 1
        avg = total / count
        average.append(avg)
    return average

a = [[2, 3, 4], [2, 7, 9, 3], [2, 8]]
print(ds_ave(a))
```

This Markdown file can be saved as `python_snippets.md` and opened in VS Code for convenient browsing and editing.

If you want me to generate the actual `.md` file content for download or any other format, just let me know!