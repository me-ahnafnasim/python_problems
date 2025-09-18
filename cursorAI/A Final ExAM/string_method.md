# Python String Methods Reference

| Method | Description | Example |
|--------|-------------|---------|
| `capitalize()` | Returns string with first character capitalized and rest lowercase | `"hello world".capitalize()` → `"Hello world"` |
| `casefold()` | Returns lowercase string, more aggressive than lower() | `"HELLO".casefold()` → `"hello"` |
| `center(width, fillchar)` | Centers string in field of given width | `"hello".center(10, '*')` → `"**hello***"` |
| `count(substring, start, end)` | Counts non-overlapping occurrences of substring | `"hello".count('l')` → `2` |
| `encode(encoding, errors)` | Encodes string using specified encoding | `"hello".encode('utf-8')` → `b'hello'` |
| `endswith(suffix, start, end)` | Returns True if string ends with suffix | `"hello.txt".endswith('.txt')` → `True` |
| `expandtabs(tabsize)` | Replaces tabs with spaces | `"hello\tworld".expandtabs(4)` → `"hello    world"` |
| `find(substring, start, end)` | Returns lowest index of substring, -1 if not found | `"hello".find('l')` → `2` |
| `format(*args, **kwargs)` | Formats string using positional and keyword arguments | `"Hello {}".format("world")` → `"Hello world"` |
| `format_map(mapping)` | Formats string using mapping object | `"Hello {name}".format_map({'name': 'John'})` → `"Hello John"` |
| `index(substring, start, end)` | Like find() but raises ValueError if not found | `"hello".index('l')` → `2` |
| `isalnum()` | Returns True if all characters are alphanumeric | `"hello123".isalnum()` → `True` |
| `isalpha()` | Returns True if all characters are alphabetic | `"hello".isalpha()` → `True` |
| `isascii()` | Returns True if all characters are ASCII | `"hello".isascii()` → `True` |
| `isdecimal()` | Returns True if all characters are decimal numbers | `"123".isdecimal()` → `True` |
| `isdigit()` | Returns True if all characters are digits | `"123".isdigit()` → `True` |
| `isidentifier()` | Returns True if string is valid Python identifier | `"var_name".isidentifier()` → `True` |
| `islower()` | Returns True if all characters are lowercase | `"hello".islower()` → `True` |
| `isnumeric()` | Returns True if all characters are numeric | `"123".isnumeric()` → `True` |
| `isprintable()` | Returns True if all characters are printable | `"hello".isprintable()` → `True` |
| `isspace()` | Returns True if all characters are whitespace | `"   ".isspace()` → `True` |
| `istitle()` | Returns True if string is titlecased | `"Hello World".istitle()` → `True` |
| `isupper()` | Returns True if all characters are uppercase | `"HELLO".isupper()` → `True` |
| `join(iterable)` | Joins elements of iterable with string as separator | `"-".join(['a', 'b', 'c'])` → `"a-b-c"` |
| `ljust(width, fillchar)` | Left-justifies string in field of given width | `"hello".ljust(10, '*')` → `"hello*****"` |
| `lower()` | Returns string in lowercase | `"HELLO".lower()` → `"hello"` |
| `lstrip(chars)` | Removes leading characters (whitespace by default) | `"  hello".lstrip()` → `"hello"` |
| `maketrans(x, y, z)` | Creates translation table for translate() method | `str.maketrans('abc', '123')` → `{97: 49, 98: 50, 99: 51}` |
| `partition(separator)` | Splits string into 3 parts: before, separator, after | `"hello-world".partition('-')` → `('hello', '-', 'world')` |
| `removeprefix(prefix)` | Removes prefix from string if present | `"HelloWorld".removeprefix("Hello")` → `"World"` |
| `removesuffix(suffix)` | Removes suffix from string if present | `"HelloWorld".removesuffix("World")` → `"Hello"` |
| `replace(old, new, count)` | Replaces occurrences of old with new | `"hello".replace('l', 'x')` → `"hexxo"` |
| `rfind(substring, start, end)` | Returns highest index of substring, -1 if not found | `"hello".rfind('l')` → `3` |
| `rindex(substring, start, end)` | Like rfind() but raises ValueError if not found | `"hello".rindex('l')` → `3` |
| `rjust(width, fillchar)` | Right-justifies string in field of given width | `"hello".rjust(10, '*')` → `"*****hello"` |
| `rpartition(separator)` | Splits string into 3 parts from the right | `"hello-world-test".rpartition('-')` → `('hello-world', '-', 'test')` |
| `rsplit(separator, maxsplit)` | Splits string from the right | `"a.b.c".rsplit('.', 1)` → `['a.b', 'c']` |
| `rstrip(chars)` | Removes trailing characters (whitespace by default) | `"hello  ".rstrip()` → `"hello"` |
| `split(separator, maxsplit)` | Splits string into list | `"a,b,c".split(',')` → `['a', 'b', 'c']` |
| `splitlines(keepends)` | Splits string at line breaks | `"hello\nworld".splitlines()` → `['hello', 'world']` |
| `startswith(prefix, start, end)` | Returns True if string starts with prefix | `"hello.txt".startswith('hello')` → `True` |
| `strip(chars)` | Removes leading and trailing characters | `"  hello  ".strip()` → `"hello"` |
| `swapcase()` | Swaps case of all characters | `"Hello".swapcase()` → `"hELLO"` |
| `title()` | Returns titlecased string | `"hello world".title()` → `"Hello World"` |
| `translate(table)` | Translates characters using translation table | `"hello".translate(str.maketrans('l', 'x'))` → `"hexxo"` |
| `upper()` | Returns string in uppercase | `"hello".upper()` → `"HELLO"` |
| `zfill(width)` | Pads string with zeros on the left | `"42".zfill(5)` → `"00042"` |

## Notes:
- All string methods return new strings (strings are immutable in Python)
- Optional parameters are shown in parentheses
- Some methods have additional optional parameters not shown for brevity
- Python 3.9+ added `removeprefix()` and `removesuffix()` methods