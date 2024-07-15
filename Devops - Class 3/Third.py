from Second import get_user_data
print("hello world")
user_data = get_user_data()
if user_data["gender"] == "Female":
    print("hey there groovy chick")
if user_data["gender"] == "Male":
    print("whats going on dude?")