from utils.model import users
from utils.controller import getUserInfo, add_user

def main():
    print(f'Witaj {users[0]['name']}')
    while True:
        print("===============MENU===============")
        print('0 - Zakończ program')
        print('1 - Wyświetl znajomych')
        print('2 - Dodaj znajomych')
        print('==================================')

        choice = input('Wybierz opcje Menu')
        if choice == '0': break
        if choice == '1' : getUserInfo(users[1:])
        if choice == '2': add_user(users)

if __name__ == '__main__':
    main()