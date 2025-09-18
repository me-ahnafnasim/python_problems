
### 1. **Creating Sets**
- Using curly braces:  
  ```python
  s = {1, 2, 3}
  ```
- Using the `set()` constructor:  
  ```python
  s = set([1, 2, 3])
  ```
- Empty set must use `set()`, empty `{}` creates an empty dictionary.

### 2. **Basic Set Operations**
- **Union:** Elements in either set  
  - Using operator `|` or method `.union()`  
  ```python
  a | b
  a.union(b)
  ```
- **Intersection:** Elements common to both sets  
  - Using operator `&` or method `.intersection()`  
  ```python
  a & b
  a.intersection(b)
  ```
- **Difference:** Elements in one set but not the other  
  - Using operator `-` or method `.difference()`  
  ```python
  a - b
  a.difference(b)
  ```
- **Symmetric Difference:** Elements in either set but not in both  
  - Using operator `^` or method `.symmetric_difference()`  
  ```python
  a ^ b
  a.symmetric_difference(b)
  ```

### 3. **Set Comparison Operations**
- **Subset:** `a` is subset of `b`  
  - Using `=` or `.issuperset()`  
  ```python
  a >= b
  a.issuperset(b)
  ```
- **Proper Superset:** `a` is superset but not equal to `b`  
  - Using `>`  
  ```python
  a > b
  ```

### 4. **Set Modification Methods**
- **Add an element:**  
  ```python
  a.add(4)
  ```
- **Remove an element (raises error if not present):**  
  ```python
  a.remove(3)
  ```
- **Discard an element (does not raise error if not present):**  
  ```python
  a.discard(3)
  ```
- **Pop an arbitrary element:**  
  ```python
  a.pop()
  ```
- **Clear all elements:**  
  ```python
  a.clear()
  ```

### 5. **In-place Set Operations**
- **Union update:**  
  ```python
  a.update(b)  # a = a union b
  ```
- **Intersection update:**  
  ```python
  a.intersection_update(b)  # a = a intersection b
  ```
- **Difference update:**  
  ```python
  a.difference_update(b)  # a = a - b
  ```
- **Symmetric difference update:**  
  ```python
  a.symmetric_difference_update(b)  # a = a ^ b
  ```

### 6. **Other Useful Methods**
- **Copy a set:**  
  ```python
  c = a.copy()
  ```
- **Check membership:**  
  ```python
  3 in a
  4 not in a
  ```

### Summary Table of Operators and Methods:

| Operation               | Operator | Method                   | Description                         |
|-------------------------|----------|--------------------------|-----------------------------------|
| Union                   | `|`      | `.union()`               | Elements in either set             |
| Intersection            | `&`      | `.intersection()`        | Elements present in both sets      |
| Difference              | `-`      | `.difference()`          | Elements in first, not second     |
| Symmetric Difference    | `^`      | `.symmetric_difference()`| Elements in exactly one set        |
| Subset                  | `=`     | `.issuperset()`          | Checks if superset                 |
| Proper Superset         | `>`      | -                        | Checks if proper superset          |
| Add element             | -        | `.add()`                 | Add an element                    |
| Remove element          | -        | `.remove()`              | Remove element (error if absent)  |
| Discard element         | -        | `.discard()`             | Remove element (no error if absent)|
| Pop element             | -        | `.pop()`                 | Remove and return arbitrary element|
| Clear all elements      | -        | `.clear()`               | Remove all elements               |
| Copy set                | -        | `.copy()`                | Return a shallow copy              |
| Update (union) in-place | `|=`     | `.update()`              | In-place union                    |
| Intersection in-place   | `&=`     | `.intersection_update()` | In-place intersection             |
| Difference in-place     | `-=`     | `.difference_update()`   | In-place difference               |
| Symmetric difference in-place | `^=`    | `.symmetric_difference_update()` | In-place symmetric difference |

