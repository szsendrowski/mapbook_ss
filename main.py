users:list =[
    {"name":"Julia","location":"Ząbki","posts":10},
    {"name":"Julia","location":"Sokółka","posts":20},
    {"name":"Klaudia","location":"Warszawa","posts":7},
    {"name":"Marcin","location":"Grudziądz","posts":1000},
    {"name":"Mateusz","location":"Lublin","posts":1}
]





def getUserInfo (usersData:list)->None:
    for user in usersData:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów')

print(f'Witaj {users[0]["name"]}')
getUserInfo(users[1:])