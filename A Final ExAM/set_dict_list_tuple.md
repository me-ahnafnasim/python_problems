You're right! In Markdown, especially for **tables to render cleanly in VS Code**, we must follow these rules:

* Use consistent spacing and alignment in table columns.
* Avoid code formatting (backticks) inside tables unless necessary.
* Ensure text like `list` or `dict` appears **plain** for table cells to render cleanly.
* Keep lines **unbroken** within table cells.

---

### ✅ Here's the **corrected and perfectly aligned version** of your `.md` file content:

````markdown
# 🐍 Python Built-in Methods Reference Chart

Below is a list of commonly used built-in methods for Python's major data structures:

- list
- set
- dict (dictionary)
- tuple

---

## 📘 List (list)

| Method                          | Description                                          |
|--------------------------------|------------------------------------------------------|
| append(x)                      | Adds an item to the end of the list                 |
| extend(iterable)               | Extends the list by adding all items from iterable  |
| insert(i, x)                   | Inserts an item at a given index                    |
| remove(x)                      | Removes the first occurrence of value x             |
| pop([i])                       | Removes and returns the item at index i             |
| clear()                        | Removes all items from the list                     |
| index(x[, start[, end]])       | Returns the index of the first occurrence of x      |
| count(x)                       | Returns the number of times x appears               |
| sort(key=None, reverse=False)  | Sorts the list in place                             |
| reverse()                      | Reverses the elements in place                      |
| copy()                         | Returns a shallow copy of the list                  |
| del list[i]                    | Deletes the item at index i                         |
| len(list)                      | Returns number of items                             |
| min(list) / max(list)          | Returns smallest/largest item                       |
| sum(list)                      | Returns sum of numeric items                        |

---

## 🔁 Set (set)

| Method                          | Description                                             |
|--------------------------------|---------------------------------------------------------|
| add(x)                          | Adds an element to the set                              |
| remove(x)                       | Removes an element; raises KeyError if not present      |
| discard(x)                      | Removes an element if present; no error if not          |
| pop()                           | Removes and returns an arbitrary element                |
| clear()                         | Removes all elements                                    |
| copy()                          | Returns a shallow copy                                  |
| union(*others) or `|`           | Returns a new set with all elements                     |
| intersection(*others) or `&`    | Returns common elements                                 |
| difference(*others) or `-`      | Elements in set but not in others                       |
| symmetric_difference(other) or `^` | Elements in either set but not both                 |
| issubset(other) or `<=`         | Checks if set is subset                                 |
| issuperset(other) or `>=`       | Checks if set is superset                               |
| isdisjoint(other)               | Checks if sets have no common elements                  |

---

## 🗂 Dictionary (dict)

| Method                          | Description                                             |
|--------------------------------|---------------------------------------------------------|
| clear()                         | Removes all key-value pairs                             |
| copy()                          | Returns a shallow copy                                  |
| get(key[, default])            | Returns value for key, else default                     |
| items()                         | Returns view of (key, value) pairs                      |
| keys()                          | Returns view of dictionary keys                         |
| values()                        | Returns view of dictionary values                       |
| pop(key[, default])            | Removes and returns value for key                       |
| popitem()                       | Removes and returns last inserted (key, value) pair     |
| setdefault(key[, default])     | Returns value for key; inserts default if missing       |
| update([other])                | Updates dictionary with key-value pairs                 |
| len(dict)                       | Returns number of items                                 |
| in                              | Checks if key exists: `key in dict`                     |

---

## 📦 Tuple (tuple)

Note: Tuples are immutable, so they have no modifying methods.

| Method              | Description                                  |
|---------------------|----------------------------------------------|
| count(x)            | Returns number of times x appears            |
| index(x)            | Returns index of first occurrence of x       |
| len(tuple)          | Returns number of items                      |
| min(tuple) / max(tuple) | Returns smallest/largest item           |
| sum(tuple)          | Returns sum of numeric items                 |
| in                  | Checks if value exists: `x in tuple`         |

---

## 🧪 See All Methods with dir()

```python
print(dir(list))
print(dir(set))
print(dir(dict))
print(dir(tuple))
````


