#In Python, you can check the type of a variable using the type() function. Here's an example:

x = 10
print(type(x))  # Output: <class 'int'>

y = "Hello"
print(type(y))  # Output: <class 'str'>

z = [1, 2, 3]
print(type(z))  # Output: <class 'list'>



#If you need to check if a variable belongs to a specific type, you can use isinstance():

x = 10
print(isinstance(x, int))  # Output: True
print(isinstance(x, float))  # Output: False
