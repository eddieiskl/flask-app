# Part M
# Step 1: Method to get a number from the user
def getNumberFromUser():
    number = int(input("Please enter a number: "))
    return number

# Step 2: Method to compute the sum of the digits of the integer
def sumOfDigits(number):
    total = 0
    while number > 0:
        total += number % 10
        number //= 10
    return total

# Calling the methods
user_number = getNumberFromUser()
sum_digits = sumOfDigits(user_number)
print("Sum of the digits:", sum_digits)