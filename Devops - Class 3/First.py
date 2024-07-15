# Function to get user age
def get_user_age():
    age = int(input("Enter your age: "))
    if age > 120 or age < 0:
        return -1
    return age

# Function to get user gender
def get_user_gender():
    gender = input("Enter your gender: ")
    response = requests.get("https://en.wikipedia.org/wiki/" + gender)
    if gender == "M":
        return "Male"
    if gender == "F":
        return "Female"
    if gender == "Apache":
        return "Apache"
    return "Unknown"

# Usage example
try:
    age = get_user_age()
    if age == -1:
        print("Invalid age, must be between 0 and 120")
    else:
        print(f"Your age is: {age}")

    gender = get_user_gender()
    print(f"Your gender is: {gender}")

except ValueError:
    print("Invalid input, please enter a valid number for age.")