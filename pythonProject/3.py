def main():
    print("Hello! Let's get to know each other.")

    # Collecting user information
    name = input("What is your name? ")
    age = input("How old are you? ")
    location = input("Where are you from? ")
    favorite_color = input("What is your favorite color? ")

    # Displaying a personalized message
    print("\nNice to meet you, {}!".format(name))
    print("It's amazing that you are {} years old and from {}.".format(age, location))
    print("I love {} too, it's a great color!".format(favorite_color))
    print("\nThank you for sharing this information with me. Have a great day!")


if __name__ == "__main__":
    main()