def get_integer_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input: Please enter a valid integer")


try:
    # Get valid integer inputs from the user
    number1 = get_integer_input("Enter a number: ")
    number2 = get_integer_input("Enter another number: ")

    # Calculate the result
    result = number1 + number2

    # Print the result with proper type conversion
    print("result is " + str(result))
except TypeError:
    # Handle TypeError which might occur during concatenation or type conversion
    print("could not cast")
except BaseException as e:
    # General exception handler to catch other exceptions and print their messages
    print(f"Error: {e.args}")

# This statement will always execute
print("Moshe")
