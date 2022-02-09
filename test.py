import pickle
from tkinter import messagebox


def login_yes():
    user_name = 'admin'
    user_password = 'admin'
    try:
        with open('user_info.pickle', 'rb') as user_file:
            user_info = pickle.load(user_file)
    except FileNotFoundError:
        with open('user_info.pickle', 'wb') as user_file:
            user_info = {'admin': 'admin'}
            pickle.dump(user_info, user_file)

    if user_name in user_info:
        if user_password == user_info[user_name]:
            print('yes')
    else:
        print('no')


login_yes()