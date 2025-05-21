def getUserInfo (usersData:list)->None:
    for user in usersData:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów')

def add_user(users_data:list)->None:

    new_name:str = input("Podaj imie nowego znajomego: ")
    new_location:str = input("Podaj jego miejsce zamieszkania: ")
    new_posts:int = int(input("Podaj jego liczbę postów "))

    users_data.append({"name":new_name,"location":new_location,"posts":new_posts})