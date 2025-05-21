def getUserInfo (usersData:list)->None:
    for user in usersData:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów')