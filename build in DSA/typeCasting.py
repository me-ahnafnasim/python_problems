while True:
    try:
        # Get input from the user
        user_input = input("Enter a value: ")

        # Try to convert the input to a float first
        float_value = float(user_input)

        # Convert the float to an integer (truncate the decimal part)
        int_value = int(float_value)

        # Print the result
        print(f"The integer part of the input is: {int_value}")
        break  # Exit the loop if conversion is successful

    except ValueError:
        # Handle the case where the input cannot be converted to a float
        print("Invalid input! Please enter a numeric value.")







try:
  print(x)
except:
  print('An exception occurred')