"""
basic syntax

[expression for item in iterable]
"""

#create a list of 10 integer range 10 and print it.
integerx =list(range(10))
print(integerx)



# Even numbers between 0 and 20
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


# Create a list of squares from 0 to 9
squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



# Replace negative numbers with 0 and keep positives
numbers = [-2, -1, 0, 1, 2]
processed = [x if x >= 0 else 0 for x in numbers]
print(processed)  # Output: [0, 0, 0, 1, 2]



