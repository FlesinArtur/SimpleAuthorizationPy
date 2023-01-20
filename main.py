import os
import json
import pwinput
import hashlib

SECURITY = 'database.json'
SALT = b'mystaticsalt'


def password_validate():

    while True:
        password = input('Введіть пароль, який ви хочете використовувати: ')
        if len(password) < 5:
            print('Маленький пароль, легко взламати...')
        else:
            return password


def hash_password(password):
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), SALT, 10000)
    key = key.hex()
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


def create_new_user(login, password):
    database = get_data_from_storage()
    database.update({login: password})
    file_writing(database)


def file_writing(database):

    with open(SECURITY, 'w') as file:
        json.dump(database, file)


def registration():

    login = input('Введіть логін, який ви хочете використовувати: ')
    password = password_validate()
    while True:
        repeat_password = input('Повторіть пароль: ')
        if password == repeat_password:
            password = hash_password(password)
            print('Успішно!')
            break
        print('Ви ввели щось не так!')
    create_new_user(login, password)


def authorization():

    database = get_data_from_storage()

    while True:
        login = input('Введіть свій логін: ')
        password = pwinput.pwinput(prompt='Введіть свій пароль: ', mask='*')
        password = hash_password(password)
        if database.get(login) == password:
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
