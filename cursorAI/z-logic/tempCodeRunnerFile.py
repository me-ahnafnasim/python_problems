def is_armstrong(number):
    digits = [int(d) for d in str(number)]  # Convert number to list of digits
    num_digits = len(digits)  # Count of digits
    sum_powered_digits = sum(d ** num_digits for d in digits)  # Sum of each digit powered to num_digits
    return sum_powered_digits == number

# Example usage
print(is_armstrong(153))  # True, since 1^3 + 5^3 + 3^3 = 153
print(is_armstrong(123))  # False