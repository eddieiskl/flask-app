day = input("Enter the day of the week: ").capitalize()

if day in ["Saturday", "Sunday"]:
    print(f"{day} is a weekend.")
elif day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    print(f"{day} is a weekday.")
else:
    print("That's not a valid day of the week.")
