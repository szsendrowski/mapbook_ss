from utils.model import users
from utils.controller import get_user_info, add_user, delete_user, update_user,get_map, get_coordinates

def main():
    print(f'Witaj {users[0]['name']}')
    while True:
        print("===============MENU===============")
        print('0 - Zakończ program')
        print('1 - Wyświetl znajomych')
        print('2 - Dodaj znajomych')
        print('3 - Usuń znajomego')
        print('4 - Zaaktualizuj dane o znajomym')
        print('5 - Przygotuj mapę')
        print('==================================')

        choice = input('Wybierz opcje Menu')
        if choice == '0': break
        if choice == '1' : get_user_info(users[1:])
        if choice == '2': add_user(users)
        if choice == '3': delete_user(users)
        if choice == '4': update_user(users)
        if choice == '5': get_map(users)

if __name__ == '__main__':
    main()