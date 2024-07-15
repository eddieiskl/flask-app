try:
    a = 1 / 0
except ZeroDivisionError as e:
    print(f"An error occurred: {e}")

#This code will catch the ZeroDivisionError and print an error message instead of crashing.