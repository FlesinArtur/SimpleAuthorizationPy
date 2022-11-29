
import pwinput
SECURITY = 'security.txt'


def file_writing(user_login, user_password):

    file = open(SECURITY, 'w', encoding='utf-8')
    file.write(user_login)
    file.write(f'\n{user_password}')
    file.close()


def registration():

    user_login = input('Введіть логін, який ви хочете використовувати: ')
    user_password = input('Введіть пароль, який ви хочете використовувати: ')

    while True:
        repeat_password = input('Повторіть пароль: ')
        if user_password == repeat_password:
            print('Успішно!')
            break
        print('Ви ввели щось не так!')
    file_writing(user_login=user_login, user_password=user_password)


def authorization():

    file = open(SECURITY, 'r', encoding='utf-8')
    ls = file.readlines()
    ls[0] = ls[0].strip('\n')

    while True:
        user_login = input('Введіть свій логін: ')
        user_password = pwinput.pwinput(prompt='Введіть свій пароль: ', mask='*')
        if ls[0] == user_login and ls[1] == user_password:
            print('Вітаю козаче, ти не забув хто ти!')
            break
        else:
            print('Козаче, схоже ти забув хто ти, повтори спробу:(')

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
