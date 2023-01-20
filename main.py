import os
import json
import pwinput
import hashlib

SECURITY = 'database.json'
SALT = b'mystaticsalt'


def password_validate():

    while True:
        user_password = input('Введіть пароль, який ви хочете використовувати: ')
        if len(user_password) < 5:
            print('Маленький пароль, легко взламати...')
        else:
            return user_password


def hash_password(password):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), SALT, 10000)
    key = key.hex()
    print(key)
    print(type(key))
    return key


def create_storage():

    if not os.path.exists(SECURITY):
        with open(SECURITY, 'w') as file:
            database = {}
            json.dump(database, file)


def get_data_from_storage():

    with open(SECURITY, 'r') as file:
        database = json.load(file)
        return database


def create_new_user(user_login, user_password):
    database = get_data_from_storage()
    database.update({user_login: user_password})
    file_writing(database)


def file_writing(database):

    with open(SECURITY, 'w') as file:
        json.dump(database, file)


def registration():

    user_login = input('Введіть логін, який ви хочете використовувати: ')
    user_password = password_validate()
    while True:
        repeat_password = input('Повторіть пароль: ')
        if user_password == repeat_password:
            user_password = hash_password(user_password)
            print('Успішно!')
            break
        print('Ви ввели щось не так!')
    create_new_user(user_login, user_password)


def authorization():

    database = get_data_from_storage()

    while True:
        user_login = input('Введіть свій логін: ')
        user_password = pwinput.pwinput(prompt='Введіть свій пароль: ', mask='*')
        user_password = hash_password(user_password)
        if database.get(user_login) == user_password:
            print('Вітаю козаче, ти не забув хто ти!')
            break
        else:
            print('Козаче, схоже ти забув хто ти, повтори спробу:(')


def main():

    create_storage()

    while True:
        variant = input('Введіть 1, якщо ви хочете зареєструватись, введіть 2, якщо ви хочете авторизуватись: ')

        if variant == '1':
            registration()
            break
        elif variant == '2':
            authorization()
            break
        else:
            print('Вельми шановне панство, буль даска перевірте введені данні!')


if __name__ == "__main__":
    main()
