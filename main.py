from utils.model import users
from utils.controller import getUserInfo

def main():
    print(f'Witaj {users[0]['name']}')
    getUserInfo(users[1:])

if __name__ == '__main__':
    main()