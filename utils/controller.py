def get_user_info (usersData:list)->None:
    for user in usersData:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów')

def add_user(users_data:list)->None:
    new_name:str = input("Podaj imie nowego znajomego: ")
    new_location:str = input("Podaj jego miejsce zamieszkania: ")
    new_posts:int = int(input("Podaj jego liczbę postów "))
    users_data.append({"name":new_name,"location":new_location,"posts":new_posts})

def delete_user(users_data:list)->None:
    username:str = input("Podaj imie znajomego którego chcesz usunąć: ")
    for user in users_data:
        if user["name"] == username:
            users_data.remove(user)

def update_user(users_data: list) -> None:
    user_name: str = input('Wpisz kogo chcesz zmodyfikować: ')
    for user in users_data:
        if user['name'] == user_name:
            user['name'] = input('Podaj nowe imie: ')
            user['location'] = input('Podaj nowa lokalizację: ')
            user['posts'] = input('Podaj liczbę postów: ')

def get_coordinates(location_name: str) -> list:
    import requests
    from bs4 import BeautifulSoup
    adres_url: str = f'https://pl.wikipedia.org/wiki/{location_name}'
    response_html = BeautifulSoup(requests.get(adres_url).text, 'html.parser')
    return [
        float(response_html.select('.latitude')[1].text.replace(',', '.')),
        float(response_html.select('.longitude')[1].text.replace(',', '.')),
    ]

def get_map(users_data: list[dict]) -> None:
    import folium
    map = folium.Map(location=[52.3, 21.0], zoom_start=6, tiles='OpenStreetMap')
    for user in users_data:
        # print(get_coordinates(user['location'])) debug
        folium.Marker(
            location=get_coordinates(user['location']),
            popup=f'<h5>{user['location']}</h5><br/>{user['name']}<br/>{user['posts']}'
        ).add_to(map)
    map.save('mapa.html')
