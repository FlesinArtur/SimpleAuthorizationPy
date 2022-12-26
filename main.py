
import os.path
import json
import pwinput
SECURITY = 'database.json'


def password_validate():
    while True:
        user_password = input('Введіть пароль, який ви хочете використовувати: ')
        if len(user_password) < 5:
            print('Маленький пароль, легко взламати...')
        else:
            return user_password


def create_storage(user_login, user_password):

    if not os.path.exists(SECURITY):
        file = open(SECURITY, 'w')
        database = [{
            "login": user_login,
            "password": user_password
        }]
        json.dump(database, file)
        file.close()

    else:
        database = get_data_from_storage()
        add_user(database, user_login, user_password)


def get_data_from_storage():

    file = open(SECURITY, 'r')
    database = json.load(file)
    file.close()
    return database


def add_user(database, user_login, user_password):

    database.append({
            "login": user_login,
            "password": user_password
        })
    file_writing(database)


def file_writing(database):

    file = open(SECURITY, 'w')
    json.dump(database, file)
    file.close()


def registration():

    user_login = input('Введіть логін, який ви хочете використовувати: ')
    user_password = password_validate()
    while True:
        repeat_password = input('Повторіть пароль: ')
        if user_password == repeat_password:
            print('Успішно!')
            break
        print('Ви ввели щось не так!')
    create_storage(user_login=user_login, user_password=user_password)


def authorization():

    database = get_data_from_storage()
    temp = False

    while True:
        user_login = input('Введіть свій логін: ')
        user_password = pwinput.pwinput(prompt='Введіть свій пароль: ', mask='*')

        for user in database:

            if user["login"] == user_login and user["password"] == user_password:
                temp = True
                print('Вітаю козаче, ти не забув хто ти!')
                break
            else:
                temp = False
        if not temp:
            print('Козаче, схоже ти забув хто ти, повтори спробу:(')
        else:
            break


def main():

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
