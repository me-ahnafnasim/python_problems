def factorial(n):
#the factorial of 1 and 0 is 1
    if n == 0 or n == 1
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))