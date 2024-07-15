from First import get_user_age, get_user_gender
def get_user_data():
    user = {}
    user['age'] = get_user_age()
    user['gender'] = get_user_gender()
    return user