
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


def file_writing(user_login, user_password):
    database = {
        "password": user_password,
        "login": user_login
    }
    file = open(SECURITY, 'r+', encoding='utf-8')
    line = file.readline()
    if line != '':
        file.write("\n")
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
    file_writing(user_login=user_login, user_password=user_password)


def authorization():
    file = open(SECURITY, 'r', encoding='utf-8')
    temp = False
    while True:
        user_login = input('Введіть свій логін: ')
        user_password = pwinput.pwinput(prompt='Введіть свій пароль: ', mask='*')

        while True:
            line = file.readline()
            if not line:
                break
            database = json.loads(line)
            if database["login"] == user_login and database["password"] == user_password:
                temp = True
                print('Вітаю козаче, ти не забув хто ти!')
                break
            else:
                temp = False
        if not temp:
            print('Козаче, схоже ти забув хто ти, повтори спробу:(')
        else:
            break

    file.close()


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
